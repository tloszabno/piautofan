# piautofan

## Description

This is a simple script that turns on cooling fan when raspberry cpu gets hot. It provides silence in any other cases :)

## How to install

### Prerequirements

On the raspbian os / ubuntu:
```bash
sudo apt install python3 -y
sudo apt install git -y
sudo apt install python3-rpi.gpio -y
```

### Installing

Just clone repo to some folder on your raspberry pi. Let's assume its home foler:

```bash
cd ~
git clone https://github.com/tloszabno/piautofan.git
```

edit file `app.py`

```bash
nano piautofan/app.py
```

and adjust variable `FAN_CONTROL_PIN_NUMBER` to point to pin where you connected the base of the fan transistor.

Please also make sure the file is executable:
```bash
chmod +x piautofan/app.py
```


then add this script to run on start up:

```bash
sudo nano /etc/rc.local
```

and add on the end of file  (before `exit 0`)

```
/home/pi/piautofan/app.py &
```
(please adjust path to actual script location)
