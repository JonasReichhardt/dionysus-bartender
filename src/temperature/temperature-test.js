const fs = require("fs")
const path = require("path")

const base_dir = "/sys/bus/w1/devices/"
const filename = "w1_slave"

const isTempsensor = fileName => {
    return !fs.lstatSync(path.join(base_dir,fileName)).isFile() && fileName.startsWith("28")
}

function read_temps(){
    let dirs = fs.readdirSync(base_dir).filter(isTempsensor).map(fileName => {
        return path.join(base_dir, fileName);
    });

    console.log("INF| Found "+ dirs.length + " temperature sensor(s)")

    temps = []
    dirs.forEach(dir=>{
        let content = fs.readFileSync(path.join(dir,filename),'utf-8')
        let startIndex = content.indexOf("t=")+2
        temps.push(parseFloat(content.substring(startIndex,startIndex+5))/1000)
    })
    
    return temps
}

console.log(read_temps())
