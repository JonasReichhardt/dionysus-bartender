const express = require('express')
const fs = require("fs")
const { SerialPort } = require('serialport')
var serialEnabled = true

main()

async function main() {
    var serial = await open_serial_port()
    var settings = load_app_settings()
    var cocktails = load_cocktails()
    var pumps = load_ingredients()

    var app = express()
    app.use(express.json())

    app.post('/cocktails', (req, res) => {
        // check if cocktails exists
        index = req.body.cocktail - 1
        if (index < 0 || index > cocktails.length) {
            res.status(404).send('no cocktail with given id')
            return
        }

        makeCocktail(index, cocktails, pumps, serial)

        res.status(200).send('preparing cocktail')
    })

    app.get('/cocktails', (req, res) => {
        res.status(200).send(cocktails)
    })

    app.get('/pumps', (req, res) => {
        res.status(200).send(pumps)
    })

    var server = app.listen(settings.port, function () {
        var host = require('ip').address()
        var port = server.address().port
        console.info("INF| Server listening at http://%s:%s", host, port)
    })
}

async function open_serial_port() {
    let portList = await SerialPort.list()
    if (portList != undefined && portList.length > 0) {
        return new SerialPort({ path: portList[0].path, baudRate: 115200 }, function (err) {
            if (err) {
                return console.error('ERR| could not open port |', err.message)
            }
        })
    } else {
        console.error("ERR| no serial port found")
        serialEnabled = false
    }
}

function load_app_settings() {
    try {
        return JSON.parse(fs.readFileSync('appsettings.json', 'utf8'))
    } catch (err) {
        console.error("ERR| could not load app settings")
        console.error(err)
    }
}

function load_cocktails() {
    try {
        return JSON.parse(fs.readFileSync('..\\res\\cocktails.json', 'utf8')).cocktails
    } catch (err) {
        console.error("ERR| could not load cocktail config")
        console.error(err)
    }
}

function load_ingredients() {
    try {
        return JSON.parse(fs.readFileSync('..\\res\\pump-config.json', 'utf8')).pumps
    } catch (err) {
        console.error("ERR| could not load pump config")
        console.error(err)
    }
}

function makeCocktail(index, cocktails, pumps, serial) {
    let cocktail = cocktails[index]
    let command = [0, 0, 0, 0, 0, 0,]

    for (let i = 0; i < cocktail.ingredients.length; i++) {
        for (let j = 0; j < pumps.length; j++) {
            if (pumps[j].ingredient == cocktail.ingredients[i].name) {
                let pumpTime = cocktail.ingredients[i].amount / pumps[j].flowrate
                // convert to milliseconds
                command[j] = pumpTime * 1000
            }
        }
    }

    sendCommand(command, serial)
}

function sendCommand(command, serial) {
    if (command.length > 6) {
        console.error("ERR| command too large")
        return
    }
    msg = command.join('|').concat('|')
    console.info("INF| writing command <%s>", msg)

    // only send if serial is enabled
    if(serialEnabled){
        serial.write(msg,
            function (err) {
                if (err) {
                    return console.error('ERR| could not write to port |', err.message)
                }
            }
        )
    }
}