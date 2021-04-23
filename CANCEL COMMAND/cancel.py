import os
from telethon import TelegramClient
import asyncio
import re
import shutil


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
	os.chdir(os.path.dirname(__file__))

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
			shutil.move("session//"+phone_number+".session", "BLOCKED_ON_COMMAND//")
			continue
	print("Complete")
asyncio.get_event_loop().run_until_complete(main())
