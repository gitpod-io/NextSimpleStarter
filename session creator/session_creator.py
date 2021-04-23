import os
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
import telethon
import asyncio
import re
import shutil


# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'


async def main():
	# change directory according to file
	os.chdir(os.path.dirname(__file__))

	# make folder session
	if not os.path.exists("session"):
		os.mkdir("session")

	# ASK FOR PHONE NO.
	phone_number = input("Enter your number: ")

	# Connect to client
	client = TelegramClient(phone_number, api_id, api_hash)
	await client.start(phone_number)
	# await client.connect()
	# await client.send_code_request(phone_number)
	# code = input('enter code: ')
	# try:
	# 	first_name = input('Enter first name: ')
	# 	last_name = input('Enter last name: ')
	# 	await client.sign_up(code, first_name, last_name)
	# except:
	# 	print("no signup needed")

asyncio.get_event_loop().run_until_complete(main())
