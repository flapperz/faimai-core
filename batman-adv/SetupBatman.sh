#!/bin/bash
wlan_ip = "112.116.44.1/28"
bat_ip = "112.116.44.2/28"
port = 28795

echo "Copy bat0"
chmod 744 bat0
sudo cp $(pwd)/bat0 /etc/network/interfaces.d/bat0
echo "Done"
echo "Copy wlan0"
chmod 744 wlan0
sudo cp $(pwd)/wlan0 /etc/network/interfaces.d/wlan0
echo "Done"
echo "Installing batctl"
sudo apt-get install -y batctl
echo 'batman-adv' | sudo tee --append /etc/modules
echo 'denyinterfaces wlan0' | sudo tee --append /etc/dhcpcd.conf
echo "$(pwd)/start-batman-adv.sh" >> ~/.bashrc
sudo ifconfig wlan0 $wlan_ip
sudo ifconfig bat0 $bat_ip
echo "Reboot to complete installation."