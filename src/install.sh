#!/bin/bash

bold="\e[1m"
uline="\e[4m"
reset="\e[0m"
green="\e[0;92m"
blue="\e[0;94m"

echo -e "${blue}${bold}${uline}[Dionysus-Bartender]${reset}"
echo " "

echo -e "${blue}${bold}${uline}[Phase 1 of 6]${reset}"
echo -e "${green}${bold}[Installing system dependencies]${reset}"
echo -e "${green}Updating package list...${reset}"
sudo apt update
echo " "

echo -e "${green}Installing window provider...${reset}"
sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   libgstreamer1.0-dev \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} libmtdev-dev \
   xclip xsel libjpeg-dev
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
echo " "

echo -e "${green}Installing unclutter...${reset}"
sudo apt-get install unclutter
echo " "

echo -e "${blue}${bold}${uline}[Phase 2 of 6]${reset}"
echo -e "${green}${bold}[Setting up virtual environment]${reset}"
echo -e "${green}Installing virtual environment...${reset}"
cd kivymd
python3 -m venv virt
echo -e "${green}Starting virtual environment...${reset}"
source virt/bin/activate
echo " "

echo -e "${blue}${bold}${uline}[Phase 3 of 6]${reset}"
echo -e "${green}${bold}[Installing KivyMD dependencies]${reset}"
pip install Pillow
pip install kivy
echo " "

echo -e "${blue}${bold}${uline}[Phase 4 of 6]${reset}"
echo -e "${green}${bold}[Installing KivyMD]${reset}"
echo -e "${green}Cloning repository...${reset}"
git clone https://github.com/kivymd/KivyMD.git --depth 1
echo " "
echo -e "${green}Building framework...${reset}"
cd KivyMD
pip install .
echo " "

echo -e "${blue}${bold}${uline}[Phase 5 of 6]${reset}"
echo -e "${green}${bold}[Copying config]${reset}"
sudo cp ../../config/kivy/config.ini ~/.kivy/config.ini 
sudo cp ~/.kivy/config.ini /root/.kivy/config.ini
echo " "

echo -e "${blue}${bold}${uline}[Phase 6 of 6]${reset}"
echo -e "${green}${bold}[Setting up miscellaneous]${reset}"
echo -e "${green}Setting hostname...${reset}"
sudo hostnamectl set-hostname dionysus
echo -e "${green}Setting cursor settings...${reset}"
echo "@unclutter -idle 0" >> ~/.config/lxsession/LXDE-pi/autostart

read -n 1 -s -r -p "Press any key to reboot"

sudo reboot
