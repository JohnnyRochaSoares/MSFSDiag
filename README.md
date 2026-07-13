# **MSFSDiag**



**A diagnostic tool for Microsoft Flight Simulator 2020 and Microsoft Flight Simulator 2024.**

**Scans your Community folder, validates add-on manifests, detects broken symlinks and reads Windows Event Logs - all from a clean Flet GUI.**





\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





### **Features:**



* **Detects MSFS2020 and 2024 installations automatically;**



* **Reads "UserCfg.opt" to find your Community folder (even on a different drive);**



* **Validates "manifest.json" and "layout.json" for each add-on;**



* **Detects broken symlinks in the Community folder**;



* Reads Windows Event Logs for MSFS-related errors;



* Supports 14 languages (Arabic, Chinese, Dutch, English, French, German, Hindi, Italian, Japanese, Korean, Portuguese, Russian, Spanish and Turkish);



* Light and Dark theme.





\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





### **Requirements:**



* Windows 10/11 (64-bit);



* Microsoft Flight Simulator 2020/2024 with loading problems;



* Python 3.11+ (only if you choose to use the .py files instead of the .exe.)



* Administrator permissions (for Event Log access).



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





### **Installation:**



###### **From github.com:**





1. Go to https://github.com/JohnnyRochaSoares/MSFSDiag/releases;
2. Download the latest .exe;
3. Run it.





###### **From Git:**



1. Open CMD on your PC;
2. Type the following commands:



```bash
git clone https://github.com/JohnnyRochaSoares/MSFSDiag.git
cd MSFSDiag
pip install -r requirements.txt
cd src
python main.py
```



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





### **Project Structure:**



```
MSFSDiag/

├── LICENSE

├── README.md

├── requirements.txt

├── assets/

│   ├── MSFSDiag.ico

│   └── MSFSDiag.png

├── src/

│   ├── config.py

│   ├── main.py

│   ├── core/

│   │   ├── analyzer.py

│   │   ├── json_validator.py

│   │   ├── manifest_parser.py

│   │   └── scanner.py

│   ├── os_services/

│   │   ├── event_logs.py

│   │   └── symlinks.py

│   └── ui/

│       └── app.py

└── tests/

         ├── conftest.py

         ├── test_analyzer.py

         └── test_manifest_parser.py
```

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





### **License:**



##### **Copyright (c) 2026 João Rocha Soares**



##### **All rights reserved.**



This code and all its contents are the intellectual property of João Rocha Soares.

Users may run, use and modify this code exclusively for personal purposes.

It is strictly prohibited to distribute, sell or publish this code, or any modified

version, without prior written permission from the author.



To request permission, contact the author via Email, GitHub or Instagram.



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





### **Contacts:**

######  		│

######           	├─ Email: \[joao.rocha.soares.13.pt@gmail.com]

######  	  	│

######         	├─ GitHub: \[JohnnyRochaSoares]

######  		│

######         	├─ Instagram: \[@johnny\_rocha\_soares]

######  	  	│

