import pyfiglet
from skpy import Skype
import os 
from skpy import SkypeEventLoop, SkypeNewMessageEvent

banner = pyfiglet.figlet_format("SKYTOOL")
print(banner)


sk = Skype('youremail', 'yourpassword')

choice = int(input("1.Message Sender\n2.File Sender\n3.Spammer (may lag)\n4.Help\n\n>"))
if choice == 1:
	person = input("Enter the skype id of the contact you want to send a message: ")
	
	for i in range(10000000000000):
		text = input("Enter the message: ")
		contact = sk.contacts[(person)]
		contact.chat.sendMsg(text)
 
	
if choice == 2:
	person = ("Enter the skype id of the contact you want to send a file: ")
	for k in range(100000000):
		name_of_file = input("Enter the name of the file you want to send: ")
		ch.sendFile(open(name_of_file), "rb"), (name_of_file)

if choice == 3:
	person = input("Enter the skype id of the contact you want to spam: ")
	text = input("Enter the message you want to spam: ")
	times = input("Enter how many times you want to spam it: ")
	for i in range(times):
		contact = sk.contacts[(person)]
		contact.chat.sendMsg(text)


if choice == 4:
	print("Message Sender = it sends messages\n User info = it shows some info about a user\nFile Sender = it sends files\nSpammer = it spams a user\nHelp = it shows this message")
