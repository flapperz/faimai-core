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
```
sudo cp $(pwd)/start-batman-adv.sh ~/start-batman-adv.sh
```
3. make start-batman-adv.sh executable
```
chmod +x ~/start-batman-adv.sh
```
4. create/copy wlan0 file
```
sudo nano /etc/network/interfaces.d/wlan0
```
```
sudo cp $(pwd)/wlan0 /etc/network/interfaces.d/wlan0
```
5. create/copy bat0 file
```
sudo nano /etc/network/interfaces.d/bat0
```
```
sudo cp $(pwd)/wlan0 /etc/network/interfaces.d/bat0
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
echo "~/start-batman-adv.sh" >> ~/.bashrc
```
8. config static IP for your pi: 

- range : 112.116.44.0-15/28 

but we will use only fibonacci sequence just for fun 
```
sudo ifconfig wlan0 112.116.44.1/28
sudo ifconfig bat0 112.116.44.2/28
```
8. reboot & test
    
    1. check status >> wlan0: active
    ```
    sudo batctl if 
    ```
    2. check table (Are there other Pi(s)?)
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

---------------
## IP configuration

|hostname|Interface|IP|
|--------|---------|--|
|rpi1    |wlan0    |112.116.44.1|
|        |bat0     |112.116.44.2|
|rpi2    |wlan0    |112.116.44.3|
|        |bat0     |112.116.44.5|
|rpi3    |wlan0    |112.116.44.8|
|        |bat0     |112.116.44.13|