# Python BMS Viewer  

## Download Python for Windows:
Download Python from <https://www.python.org/downloads/>
Then run the installer. 
**Important**: Check the box that says "Add Python to PATH" during installation.
To verify the installation, open a terminal and run
`python --version`

## Download Python for Mac:
Option 1: Install homebrew if you don't already have it
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
Then type `brew install python`
Option 2: Similar to Windows, download from the link.
Then verify with `python3 --version`

## Download Python for Linux:
Ubuntu/Debian:
`sudo apt update`
`sudo apt install python3 python3-pip`
Fedora:
`sudo dnf install python3`
Arch Linux:
`sudo pacman -S python`
Then verify with `python3 --version`

## For CAN: 
1.2.2 PCAN
Download and install the latest driver for your interface from PEAK-System’s download page
Link: https://www.peak-system.com/Support.55.0.html?&L=1

## PyQt For Windows:
1. Make sure Python is installed
2. Open a terminal
3. `python -m pip install --upgrade pip`
4. `pip install PyQt5`

## PyQt For Mac:
1. Make sure Python is installed
2. Open a terminal
3. `python3 -m pip install --upgrade pip`
4. `pip3 install PyQt5`

## PyQt For Linux:
1. Make sure Python is installed
2. Open a terminal
3. `sudo apt update`
4. `sudo apt install python3-pyqt5`

## Installing Mac
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip3 install -r requirements.txt`

## Installing Windows
1. `python -m venv venv`
2. CMD: `venv\Scripts\activate` PowerShell: `venv\Scripts\Activate`
3. `pip install -r requirements.txt` 

## Running
Mac: 
1. `source venv/bin/activate`
2. `python3 main.py`  

Windows:
1. CMD: `venv\Scripts\activate` PowerShell: `venv\Scripts\Activate`
2. `python main.py`


## Button Message Functions
- Normal current 0x0037 5.5A
- Lower current 0x000A 1A
- Charger Voltage 0x1770 600
- Slow Charge Threshhold 32700 3.27V
- Stop Charge 41500 4.15V
- Charge Out ID 405
