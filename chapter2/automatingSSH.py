import pexpect 

PROMPT = ['# ' , '>>> ' ,'\$ ', '> ']

def send_command(child, cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	print (child.before) # The before property will contain all text up to the expected string pattern.

def connect(user, host, password):
	ssh_newK = 'Are you sure you want to continue connecting'
	ssh_command = 'ssh ' + user + '@' + host
	child = pexpect.spawn(ssh_command) # spawn class take an input that is the command we want to automate
	ret = child.expect([pexpect.TIMEOUT, ssh_newK, '[P|p]assword: '])
	if ret == 0: # the numbers corresponds to the index that expect returns 
		print ("Error in connecting")
		return 0
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT,'[P|p]assword: '])
		if ret == 0:
			print ("Error in connecting")
			return 0
	
	child.sendline(password)
	child.expect(PROMPT)
	return child


def main():
	child = connect('osboxes','127.0.0.1','Omar12345')
	send_command(child, 'ls -l')


if __name__ == '__main__':
	main()