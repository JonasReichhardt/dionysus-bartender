const express = require('express')
const cors = require('cors')
const fs = require("fs")
const { SerialPort } = require('serialport')
var serialEnabled = true

main()

async function main() {
    var serial = await open_serial_port()
    var settings = load_app_settings()
    var pumps = load_pumps()
    var ingredients = extract_ingredients(pumps)
    var cocktails = load_cocktails(pumps)

    if (cocktails == undefined || pumps == undefined) {
        console.error("ERR| could not load config")
    }

    var app = express()
    app.use(express.json())
    app.use(cors())
    app.use(express.static('../webapp/dist'))

    /*
    * Request a cocktail with custom ingredients
    */
    app.post('/cocktails/custom', (req, res) => {
        cocktail = req.body

        if(!check_ingredients(cocktail,ingredients)){
            res.status(409).send('not all ingredients are available')
            return
        }
        
        // check drink size
        amounts = []
        cocktail.ingredients.forEach(ing => {
            amounts.push(ing.amount)
        });

        if(amounts.reduce((a, b) => a + b)>500){
            res.status(409).send('cocktail cannot be bigger than 500ml')
            return
        }

        makeCocktail(cocktail,pumps,serial)
        res.status(200).send('making custom cocktail')
    })

    /*
    * Request that a standard cocktail shall be made
    */
    app.post('/cocktails/standard/:cocktailName', (req, res) => {
        cocktailName = req.params.cocktailName
        if (cocktailName == "cancel") {
            sendCommand("x")
            res.status(200).send('cocktail cancelled')
            return
        }

        index = -1
        for (let i = 0; i < cocktails.length; i++) {
            if (cocktails[i].name.replace(/\s+/g, '').toLowerCase() == cocktailName) {
                index = i
                break
            }
        }

        if (index == -1) {
            res.status(404).send('no cocktail with given id')
            return
        }

        if (makeCocktail(cocktails[index],pumps, serial)) {
            res.status(200).send('preparing cocktail ' + cocktails[index].name)
        } else {
            res.status(409).send('not all ingredients are available')
        }


    })

    app.post('/cocktail', (req, res) => {
        cocktail = req.body

        // check necessary parameter
        if (cocktail.name == undefined) {
            res.status(400).send("name list required")
            return
        }
        if (cocktail.ingredients == undefined) {
            res.status(400).send("ingredient list required")
            return
        }

        if (!check_ingredients(cocktail, ingredients)) {
            res.status(400).send("not all ingredients are available")
            return
        }

        exists = false
        for (let i = 0; i < cocktails.length; i++) {
            if (cocktails[i].name == cocktail.name) {
                cocktails[i] = cocktail
                exists = true
            }
        }
        if (!exists) {
            cocktails.push(cocktail)
        }

        res.status(201).send(cocktail)
    })

    app.post('/ingredients', (req, res) => {
        ingList = req.body

        ingredients = ingList
        cocktails = sanitize_cocktails(cocktails, ingredients)

        res.status(201).send(cocktails.length + " cocktails can be made")
    })

    app.get('/cocktails', (req, res) => {
        res.status(200).send(cocktails)
    })

    app.get('/ingredients', (req, res) => {
        res.status(200).send(ingredients)
    })

    var server = app.listen(settings.port, function () {
        var host = require('ip').address()
        var port = server.address().port
        console.info("INF| Server listening at http://%s:%s", host, port)
    })
}

async function open_serial_port() {
    port = get_serial_port(await SerialPort.list())
    if (port != undefined) {
        console.log("INF| using serial port with path " + port.path)
        return new SerialPort({ path: port.path, baudRate: 115200 }, function (err) {
            if (err) {
                return console.error('ERR| could not open port |', err.message)
            }
        })
    } else {
        console.error("ERR| no serial port found")
        serialEnabled = false
    }
}

function get_serial_port(portList){
    for(let i=0; i<portList.length; i++){
        if(portList[i].path != undefined && portList[i].serialNumber != undefined && portList[i].serialNumber != ""){
            return portList[i]
        }
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
        ingredients = []

        pumps.forEach(p => {
            ingredients.push(p.ingredient)
        });

        let cocktails = JSON.parse(fs.readFileSync('../res/cocktails.json', 'utf8')).cocktails

        return sanitize_cocktails(cocktails, ingredients)

    } catch (err) {
        console.error("ERR| could not load cocktail config")
        console.error(err)
    }
}

// removes cocktails which cannot be made with current ingredients
function sanitize_cocktails(cocktails, ingredients) {
    let sanitized = []
    for (let i = 0; i < cocktails.length; i++) {
        if (check_ingredients(cocktails[i], ingredients)) {
            sanitized.push(cocktails[i])
        }
    }
    return sanitized
}

// checks if all ingredients of a cocktail are in the specified ingredient list
function check_ingredients(cocktail, ingredients) {
    let cocktailIng = []
    cocktail.ingredients.forEach(p => {
        cocktailIng.push(p.name)
    });
    if (cocktailIng.every(r => ingredients.includes(r))) {
        return true
    }
}

function load_pumps() {
    try {
        return JSON.parse(fs.readFileSync('../res/pump-config.json', 'utf8')).pumps
    } catch (err) {
        console.error("ERR| could not load pump config")
        console.error(err)
    }
}

function makeCocktail(cocktail, pumps, serial) {
    let command = [0, 0, 0, 0, 0, 0,]

    for (let i = 0; i < cocktail.ingredients.length; i++) {
        for (let j = 0; j < pumps.length; j++) {
            if (pumps[j].ingredient == cocktail.ingredients[i].name) {
                let pumpTime = cocktail.ingredients[i].amount / pumps[j].flowrate
                // convert to milliseconds and round to nearest integer
                pumpTime = pumpTime * 1000
                command[j] = Math.round(pumpTime)
            }
        }
    }

    if (command.filter(x => x != 0).length < cocktail.ingredients.length) {
        console.error("ERR| not all ingredients are available. No command sent")
        return false
    }

    sendCommand(command, serial)
    return true
}

function sendCommand(command, serial) {
    msg = ""
    if (typeof command != "string") {
        if (command.length > 6) {
            console.error("ERR| command too large")
            return
        }
        msg = command.join('|').concat('|')
    } else {
        msg = command
    }

    console.info("INF| writing command <%s>", msg)

    // only send if serial is enabled
    if (serialEnabled) {
        serial.write(msg,
            function (err) {
                if (err) {
                    return console.error('ERR| could not write to port |', err.message)
                }
            }
        )
    }
}

function extract_ingredients(pumps) {
    ingredients = []

    pumps.forEach(p => {
        ingredients.push(p.ingredient)
    });

    return ingredients
}