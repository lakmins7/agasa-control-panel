# AGASA Control Panel
This repository is for the front-end UI and the back-end software needed to configure AGASA using a WebUI.

## How to install in a AlmaLinux (or a related linux distribution)

First install Apache, and then clone the repository, and then setup the necessary files, before finally running Uvicorn.

### Step 1: Installing Apache2
The below steps are only needed if you don't have Apache2 in your machine. 

1. Install Apache2: `sudo dnf install httpd -y`
2. Then run it: `sudo systemctl start httpd` and then do `sudo systemctl enable httpd`
3. Verify Apache2 is running by going to the browser and checking `http://<ip-of-your-machine>/`

This should be enough. However, there maybe additional settings needed in some machines. 
For that, you will have to create a file under `/etc/httpd/conf.d`.

4. Run `sudo emacs -nw /etc/httpd/conf.d/agasa-ctrl.conf`
5. Then in this file copy paste the below,
```
Alias /AGASACtrlPanel /var/www/html/AGASACtrlPanel

<Directory /var/www/html/AGASACtrlPanel>
    AllowOverride All
    Require all granted

    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^ index.html [L]
</Directory>

# Reverse proxy to FastAPI
ProxyPreserveHost On
ProxyPass        /api http://127.0.0.1:8000/api
ProxyPassReverse /api http://127.0.0.1:8000/api
```

### Step 2: Clone and setup the frontend WebUI
1. First clone the AGASA control panel repository: `git clone https://github.com/lakmins7/agasa-control-panel.git`

2. Change directory: `cd agasa-control-panel`

3. Copy the Webpage under `/var/www/html`: `sudo cp -r AGASACtrlPanel /var/www/html`

4. Check if you can access the webpage using `http://<ip-of-your-machine>/AGASACtrlPanel`

### Step 3: Setup the backend FastAPI

1. Change directory and open the change the lines in `main.py`
```
cd Backend
emacs -nw main.py
```

and change lines
+ `<path-to-asagi-controller>` --> Real path to the ASAGI Controller binary `AsagiController-main/bin/set_asic_register`
+ `<HUL-IP-address>` --> IP Address of the HUL board.

2. Then go the Backend and create a Python virtual environment: 
```
cd Backend
python3 -m venv Venv
source Venv/bin/activate
```

3. Then install FastAPI and Uvicorn: `pip install fastapi uvicorn`

4. Open a screen (or Tmux session) and run the app: 
```
screen -S S1
uvicorn main:app --host 127.0.0.1 --port 8000
```

+ To leave the screen you can do `Ctrl+A` and `Ctrl+D`

Now you should be able to run the WebUI and use it to configure the AGASA chips. \
If the config is successfully done, there will be a `STATUS: Successfully saved config to <path-to-config-files>`