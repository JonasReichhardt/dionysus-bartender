#!/bin/bash

bold="\e[1m"
uline="\e[4m"
reset="\e[0m"
green="\e[0;92m"
blue="\e[0;94m"

echo -e "${blue}${bold}${uline}[Dionysus-Bartender | Run KivyMD client]${reset}"
echo " "

echo -e "${blue}${bold}${uline}[Phase 1 of 4]${reset}"
echo -e "${green}Pulling latest changes...${reset}"
git pull
echo " "

echo -e "${blue}${bold}${uline}[Phase 2 of 4]${reset}"
echo -e "${green}${bold}[Copying config]${reset}"
sudo cp ../../config/kivy/config.ini ~/.kivy/config.ini 
sudo cp ~/.kivy/config.ini /root/.kivy/config.ini
echo " "

echo -e "${blue}${bold}${uline}[Phase 3 of 4]${reset}"
echo -e "${green}Starting virtual environment...${reset}"
cd kivymd
source ./virt/bin/activate
echo " "

echo -e "${blue}${bold}${uline}[Phase 4 of 4]${reset}"
echo -e "${green}Starting application...${reset}"

python3 main.py

read -n 1 -s -r -p "Press any key to continue"
