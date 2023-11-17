## About

Overlay for StarCraft II which shows build order  

## Dependencies:
```keyboard Pillow requests beautifulsoup4```

## Quick guide  
### Installation
#### Windows
download and install python  
https://www.python.org/downloads/windows/  
open cmd and write there  
```pip install keyboard Pillow requests beautifulsoup4```  
download build helper  
```git clone https://github.com/Prepodobnuy/sc_build_helper.git```  
run the main.py file.
#### Linux
install python  
install dependencies  
```python3 -m pip install keyboard Pillow requests beautifulsoup4```   
download build helper  
```git clone https://github.com/Prepodobnuy/sc_build_helper.git```  
and run app with sudo
```sudo python main.py```  
sudo is needed because of keyboard module which is needed for hotkeys in the app.
### Keybinds
```ctrl + a``` -> starts build execution  
```ctrl + p``` -> pause build execution  
```ctrl + b``` -> opens the builds menu  
```ctrl + [``` -> previous build order  
```ctrl + ]``` -> next build order
in builds menu you can install and delete builds
### Builds installation
#### Local installation
To install build you need to copy it from spawningtool.com and paste to the .txt file with any name.  
after this run the build helper, press ctrl + b and push the **Add Build** button
#### Online installation
Press "Browse for builds" button in build selecter, select matchup and push "Find builds" button.  
Programm will show to you builds from spawningtool.com which you can download.
