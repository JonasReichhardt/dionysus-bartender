#!/bin/bash

bold="\e[1m"
uline="\e[4m"
reset="\e[0m"
green="\e[0;92m"
blue="\e[0;94m"

echo -e "${blue}${bold}${uline}[Dionysus-Bartender | Install webserver and web application]${reset}"
echo " "

echo -e "${blue}${bold}${uline}[Phase 1 of 4]${reset}"
echo -e "${green}${bold}[Installing system dependencies]${reset}"
echo -e "${green}Updating package list...${reset}"
sudo apt update
echo " "

echo -e "${green}Installing nodejs/npm...${reset}"
sudo apt install npm nodejs
echo " "

echo -e "${green}Pulling latest changes...${reset}"
git pull
echo " "

echo -e "${blue}${bold}${uline}[Phase 2 of 4]${reset}"
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

echo -e "${blue}${bold}${uline}[Phase 3 of 4]${reset}"
echo -e "${green}${bold}[Building webserver]${reset}"
echo -e "${green}Installing dependencies...${reset}"
cd webserver
npm install
echo " "

echo -e "${blue}${bold}${uline}[Phase 4 of 4]${reset}"
echo -e "${green}${bold}[Run webserver]${reset}"
echo -e "${green}Starting webserver...${reset}"
npm run start
echo " "