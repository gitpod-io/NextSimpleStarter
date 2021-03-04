import os
from telethon import TelegramClient
import asyncio
import re
import shutil


print("----------------SESSION CONTROLLER -------------")
print("Enter your command")
print("Session Checker:- 1")
print("Cancel menu command:- 2")
print("Exit:- 3")

user = input("Enter your command:\n")

if user == '1':
	# Get your own values from my.telegram.org
	api_id = 800812
	api_hash = 'db55ad67a98df35667ca788b97f771f5'
	async def main():
		# with open(r"C:\\Users\\PRASHANT\Desktop\\New folder\\OTHER\\CRYPTO\\HACKS FOR EARNING\\session checker\\list.txt","r") as f:
		#     # print(f.readlines()) #it read all lines which is the reason other functions can't print anything
		#     # print(f.readline())
		#     a = f.readlines()
		#     b = []
		# for i in range(len(a)):
		#     b.append(a[i].strip('\n'))
		# print(b)
		# change directory according to file
		# os.chdir(os.path.dirname(__file__))
		# make folder session
		if not os.path.exists("session"):
			os.mkdir("session")
		# get filtered list only .session files
		relevant_path = "session//"
		included_extensions = ['session']
		file_names = [fn for fn in os.listdir(relevant_path)
					  if any(fn.endswith(ext) for ext in included_extensions)]
		# remove .session from numbers
		stop = ['.session']
		b = [(lambda x: re.sub(r'|'.join(stop), '', x))(x)
			 for x in file_names]
		print(b)
		# collect one by one numbers to process
		for i in range(len(b)):
			phone_number = str(b[i])
			# fd = (str(b[i]))
			# Connect to client
			client = TelegramClient("session//"+phone_number, api_id, api_hash)
			# await client.start(phone_number)
			#     break
			# else:
			#     me = await client.get_me()
			#     print(me.first_name, me.last_name)
			try:
				await client.connect()
				await client.sign_in(phone_number)
				await client.is_user_authorized()
				# await client.start(phone_number)
				if await client.get_me():
					me = await client.get_me()
					print(i+1, str(b[i]), "--",
						  me.first_name, me.last_name)
					if not os.path.exists("correct"):
						os.mkdir("correct")
					shutil.move("session//"+phone_number +".session", "correct//")
				else:
					# os.close(fd)
					print(i+1, str(b[i]), "--",
						  "code required to login again")
					if not os.path.exists("invalid"):
						os.mkdir("invalid")
					# os.chdir("session")
					shutil.move("session//"+phone_number +".session", "invalid//")
			except:
				print(i+1, str(b[i]), "--", "banned")
				if not os.path.exists("banned"):
					os.mkdir("banned")
				# os.chdir("session")
				shutil.move("session//"+phone_number +".session", "banned//")
				continue
			# await client.run_until_disconnected()
	asyncio.get_event_loop().run_until_complete(main())
	print("RESULTS ------------")
	# COUNT SESSION FILES IN FOLDER
	def counter(path):
		# get filtered list only .session files
		relevant_path = path
		included_extensions = ['session']
		file_names = [fn for fn in os.listdir(relevant_path)
					  if any(fn.endswith(ext) for ext in included_extensions)]
		return file_names
	# ACTIVE SESSIONS ONLY
	if os.path.exists("correct"):
		no_active_sessions = len(counter("correct//"))
		print("ACTIVE SESSIONS - ", no_active_sessions)
	else:
		no_active_sessions = 0
		print("ACTIVE SESSIONS - ", no_active_sessions)
	# INVALID SESSIONS ONLY
	if os.path.exists("invalid"):
		no_invalid_sessions = len(counter("invalid//"))
		print("INVALID SESSIONS - ", no_invalid_sessions)
	else:
		no_invalid_sessions = 0
		print("INVALID SESSIONS - ", no_invalid_sessions)
	# BANNED SESSIONS ONLY
	if os.path.exists("banned"):
		no_banned_sessions = len(counter("banned//"))
		print("BANNED SESSIONS - ", no_banned_sessions)
	else:
		no_banned_sessions = 0
		print("BANNED SESSIONS - ", no_banned_sessions)
	# TOTAL SESSIONS
	print("TOTAL SESSIONS - ", no_active_sessions +
		  no_invalid_sessions + no_banned_sessions)
elif user == '2':
	# Get your own values from my.telegram.org
	api_id = 800812
	api_hash = 'db55ad67a98df35667ca788b97f771f5'
	async def main():
		# with open(r"C:\\Users\\PRASHANT\Desktop\\New folder\\OTHER\\CRYPTO\\HACKS FOR EARNING\\session checker\\list.txt","r") as f:
		#     # print(f.readlines()) #it read all lines which is the reason other functions can't print anything
		#     # print(f.readline())
		#     a = f.readlines()
		#     b = []
		# for i in range(len(a)):
		#     b.append(a[i].strip('\n'))
		# print(b)
		# change directory according to file
		# os.chdir(os.path.dirname(__file__))
		# make folder session
		if not os.path.exists("correct"):
			os.mkdir("correct")
		# get filtered list only .session files
		relevant_path = "correct//"
		included_extensions = ['session']
		file_names = [fn for fn in os.listdir(relevant_path)
					  if any(fn.endswith(ext) for ext in included_extensions)]
		# remove .session from numbers
		stop = ['.session']
		b = [(lambda x: re.sub(r'|'.join(stop), '', x))(x) for x in file_names]
		print(b)
		# collect one by one numbers to process
		for i in range(len(b)):
			try:
				phone_number = str(b[i])
				# fd = (str(b[i]))
				# Connect to client
				client = TelegramClient("correct//"+phone_number, api_id, api_hash)
				await client.start(phone_number)
				me = await client.get_me()
				print(i+1, str(b[i]), "--", me.first_name, me.last_name)
				await client.send_message('@Dogecoin_click_bot', '/cancel')
				# message = await client.get_messages('@Dogecoin_click_bot')
				# print(message)
				# message_1337 = await client.get_messages(chat, ids=24363)
				# print(message_1337)
				# async for message in client.iter_messages(chat, from_user='me'):
				# 	print(message.text)
				await client.send_message('@Dogecoin_click_bot', '/menu')
			except Exception as e:
				print(i+1, str(b[i]), "--", e)
				if not os.path.exists("BLOCKED_ON_COMMAND"):
					os.mkdir("BLOCKED_ON_COMMAND")
				# os.chdir("session")
				shutil.move("correct//"+phone_number +".session", "BLOCKED_ON_COMMAND//")
				continue
		print("Complete")
	asyncio.get_event_loop().run_until_complete(main())
	def counter(path):
		# get filtered list only .session files
		relevant_path = path
		included_extensions = ['session']
		file_names = [fn for fn in os.listdir(relevant_path)
					  if any(fn.endswith(ext) for ext in included_extensions)]
		return file_names
	# ACTIVE SESSIONS ONLY
	if os.path.exists("correct"):
		no_active_sessions = len(counter("correct//"))
		print("ACTIVE SESSIONS - ", no_active_sessions)
	else:
		no_active_sessions = 0
		print("ACTIVE SESSIONS - ", no_active_sessions)
	# BLOCKED ON COMMAND ONLY
	if os.path.exists("BLOCKED_ON_COMMAND"):
		no_blocked_on_command_sessions = len(
			counter("BLOCKED_ON_COMMAND//"))
		print("BLOCKED_ON_COMMAND - ", no_blocked_on_command_sessions)
	else:
		no_blocked_on_command_sessions = 0
		print("BLOCKED_ON_COMMAND - ", no_blocked_on_command_sessions)
	# TOTAL SESSIONS
	print("TOTAL SESSIONS - ", no_active_sessions +
		  no_blocked_on_command_sessions)
