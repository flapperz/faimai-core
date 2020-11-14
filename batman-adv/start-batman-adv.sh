#!/bin/bash
# batman-adv interface to use
sudo batctl if add wlan0

# Activates batman-adv interfaces
sudo ifconfig wlan0 up
sudo ifconfig bat0 up