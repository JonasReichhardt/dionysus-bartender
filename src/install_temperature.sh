#!/bin/bash

bold="\e[1m"
uline="\e[4m"
reset="\e[0m"
green="\e[0;92m"
blue="\e[0;94m"

echo -e "${blue}${bold}${uline}[Dionysus-Bartender | Install one wire temperature sensor]${reset}"
echo " "

sudo modprobe w1-gpio
sudo modprobe w1-therm

sudo sed -i "w1_gpio\nw1_therm" /etc/modules

ls /sys/bus/w1/devices/