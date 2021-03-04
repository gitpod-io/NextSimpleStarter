import pexpect
import sys
while True:
		child = pexpect.spawn('python3.8 bot.py', encoding='utf-8')
		child.logfile = sys.stdout
		child.expect('[1/2] ?')
		child.sendline('2')
		child.expect('Input your choice:')
		child.sendline('2')
		child.expect('[1/2] ?')
		child.sendline('1')
		child.expect('Your Clickbot Refferal Link :')
		child.sendline('n')
		child.expect('Input your number')
		number = str(input("Enter your number here:"))
		if number == 'q':
			exit()
		else:
			child.sendline("+1"+number)
		t = child.expect(['Enter Your Code', '[•°•]'])
		if t == 0:
			code = str(input("Enter your code here:"))
			child.sendline(code)
		else:
			pass
		child.expect("00")
		child.sendline('\n')
		continue
		child.expect(pexpect.EOF, timeout=None)
