## Reference
-  https://github.com/binnes/WiFiMeshRaspberryPi/blob/master/README.md
- https://medium.com/@tdoll/how-to-setup-a-raspberry-pi-ad-hoc-network-using-batman-adv-on-raspbian-stretch-lite-dce6eb896687

*follow above instruction may be better and understandable*

## Setup batman-adv
1. install batctl
```
sudo apt-get install -y batctl
```
2. copy/create start-batman-adv.sh
3. make start-batman-adv.sh executable
```
chmod +x ~/start-batman-adv.sh
```
4. create interface & copy wlan0 file
```
sudo nano /etc/network/interfaces.d/wlan0
```
5. load at boot time
```
echo 'batman-adv' | sudo tee --append /etc/modules
```
6. stop dhcp
```
echo 'denyinterfaces wlan0' | sudo tee --append /etc/dhcpd.conf
```
7. make sure start script get call
```
sudo nano /etc/rc.local
```
insert before "exit 0"
```
/home/pi/start-batman-adv.sh &
```
8. reboot & test
    
    1. check status >> wlan0: active
    ```
    sudo batctl if 
    ```
    2. check table (Are ther other Pi(s)?)
    ```
    sudo batctl n
    ```

## Connect to pie
### SSH
1. Enable ssh on pi some how
    
    1. edit file through card reader
    2. pi's preference via monitor
2. Find IP of the pi through local network or connect via hostname (wireless)
```
ssh pi@hostname.local
ssh pi@IPaddress
```
2. connect via wired LAN

### VNC
1. Enable VNC on pi
2. Install VNC client on laptop
3. use same IP as pi

