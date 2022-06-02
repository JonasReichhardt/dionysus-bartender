#!/bin/bash

bold="\e[1m"
uline="\e[4m"
reset="\e[0m"
green="\e[0;92m"
blue="\e[0;94m"

echo -e "${blue}${bold}${uline}[Dionysus-Bartender | Install web application]${reset}"
echo " "

echo -e "${green}${bold}[Building frontend application]${reset}"
echo -e "${green}Installing dependencies...${reset}"
cd webapp
npm install
echo -e "${green}Building application...${reset}"
npm run build
cd ..
echo -e "${green}Copying artifacts into server directory...${reset}"
sudo cp -r ./webapp/dist/. ./webserver/dist/
echo " "