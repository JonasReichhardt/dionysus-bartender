const express = require('express')
const fs = require("fs")
const { SerialPort } = require('serialport')
var serialEnabled = true

main()

async function main() {
    var serial = await open_serial_port()
    var settings = load_app_settings()
    var pumps = load_ingredients()
    var cocktails = load_cocktails(pumps)
    
    if(cocktails == undefined || pumps == undefined){
        console.error("ERR| could not load config")
    }

    var app = express()
    app.use(express.json())

    app.post('/cocktails/:cocktailId', (req, res) => {
        index = req.params.cocktailId - 1
        if(index < 0){
            sendCommand("x")
            res.status(200).send('cocktail cancelled')
            return
        }

        if (index > cocktails.length) {
            res.status(404).send('no cocktail with given id')
            return
        }

        if(makeCocktail(index, cocktails, pumps, serial)){
            res.status(200).send('preparing cocktail '+cocktails[index].name)
        }else{
            res.status(409).send('not all ingredients are available')
        }

        
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

function load_cocktails(pumps) {
    try {
        let sanitized = []
        ingredients = []

        pumps.forEach(p => {
            ingredients.push(p.ingredient)    
        });

        let cocktails = JSON.parse(fs.readFileSync('..\\res\\cocktails.json', 'utf8')).cocktails

        for (let i = 0; i < cocktails.length; i++) {
            let cocktailIng = []
            cocktails[i].ingredients.forEach(p => {
                cocktailIng.push(p.name)    
            });
            if(cocktailIng.every(r => ingredients.includes(r))){
                sanitized.push(cocktails[i])
            }
        }
        return sanitized
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

    if(command.filter(x=>x!=0).length < cocktail.ingredients.length){
        console.error("ERR| not all ingredients are available. No command sent")
        return false
    }

    sendCommand(command, serial)
    return true
}

function sendCommand(command, serial) {
    msg = ""
    if(typeof command != "string"){
        if (command.length > 6) {
            console.error("ERR| command too large")
            return
        }
        msg = command.join('|').concat('|')
    }else{
        msg = command
    }

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

function buildEndpoints(app){
    
}