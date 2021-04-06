#####################################
##         Needs improved!         ##
#####################################
import discord
import requests
from discord.ext import commands
import colorama
from discordwebhook import Discord
from colorama import Fore
import datetime
import os
import random
import asyncio
from cfonts import render, say                


#vars / ascii
client = discord.Client()
output = render('discolog', colors=['yellow', 'red'])
os.system('cls')
prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)

data = {
    "content" : "",
    "username" : "DiscoLog",
}
def ascii():
	print(output)
	print(f"""

				{Fore.RED}w{Fore.RESET}{Fore.GREEN}w{Fore.RESET}{Fore.CYAN}w{Fore.RESET}{Fore.YELLOW}.{Fore.RESET}{Fore.LIGHTGREEN_EX}9{Fore.RESET}{Fore.LIGHTBLUE_EX}s{Fore.RESET}{Fore.RED}p{Fore.RESET}{Fore.MAGENTA}y{Fore.RESET}{Fore.GREEN}.{Fore.RESET}{Fore.LIGHTRED_EX}m{Fore.RESET}{Fore.YELLOW}l{Fore.RESET}

	""")

ascii()
token = input(f"Input your {Fore.RED}Token{Fore.RESET}: ")
print(" ")


option = input(str(f"Would you like to log DMs or DMs + Server Texts? {Fore.RED}dm/all{Fore.RESET}: "))
if option == "dm":
	print(" ")
	print(f"	[{Fore.RED}>{Fore.RESET}] Alright! all {Fore.YELLOW}DMs{Fore.RESET} will be logged")
	print(" ")
else:
	print(" ")
	print(f"	[{Fore.RED}>{Fore.RESET}] Alright! all {Fore.YELLOW}Messages{Fore.RESET} will be logged")
	print(" ")


logyn = input(str(f"Do you want the messages to be sent to your webhook? {Fore.RED}y/n{Fore.RESET}: "))
print(" ")


#webhook shit
if logyn == "y":
	url = input(f"	[{Fore.RED}>{Fore.RESET}] Alright! please enter your {Fore.YELLOW}webhook link{Fore.RESET}: ")
	print(" ")
	print(f"	[{Fore.RED}>{Fore.RESET}] Thanks! all messages logged will be sent to your {Fore.YELLOW}webhook{Fore.RESET}")
	print(" ")
else:
	print(f"	[{Fore.RED}>{Fore.RESET}] Alright! all messages logged will {Fore.YELLOW}not{Fore.RESET} be sent")
	print(" ")

current_time = datetime.datetime.now()
os.system('cls')

ascii()
#start logging
print(f'[{Fore.RED}>{Fore.RESET}] {Fore.CYAN}Monitoring Started{Fore.RESET}:')
print(" ")
print(f"Log @ {Fore.RED}" + str(current_time.year) + "/" + str(current_time.month) + "/" + str(current_time.day) + f" {Fore.RESET}")
print(" ")

if option == "dm":
	@bot.event
	async def on_message(message):
		current_time = datetime.datetime.now()
		if logyn == "y":
			if message.channel.type is discord.ChannelType.private or message.channel.type is discord.ChannelType.group:
				if bot.user.id == message.author.id:
					print(str(current_time.hour) + f"{Fore.RESET}:" + str(current_time.minute) + ":" + str(current_time.second) + f" [{Fore.GREEN}" + "You" + f"{Fore.RESET}] @ [{Fore.CYAN}" + str(message.channel) + f"{Fore.RESET}] : " + str(message.content))
					print(" ")
					data["embeds"] = [
						{
							"description" : f"`{message.content}`",
							"title" : f"{message.author}  ~ :  {message.channel}",
							"color" : 0xff0000
						}
					]
					result = requests.post(url, json = data)

				else:
					print(str(current_time.hour) + f"{Fore.RESET}:" + str(current_time.minute) + ":" + str(current_time.second) + f" [{Fore.RED}" + str(message.author) + f"{Fore.RESET}] @ [{Fore.CYAN}" + str(message.channel) + f"{Fore.RESET}] : " + str(message.content))
					print(" ")
					data["embeds"] = [
						{
							"description" : f"`{message.content}`",
							"title" : f"{message.author}  ~ :  {message.channel}",
							"color" : 0xff0000
						}
					]
					result = requests.post(url, json = data)
			else:
				pass
		else:
			if message.channel.type is discord.ChannelType.private or message.channel.type is discord.ChannelType.group or message.channel.type is discord.ChannelType.text:
				if bot.user.id == message.author.id:
					print(str(current_time.hour) + f"{Fore.RESET}:" + str(current_time.minute) + ":" + str(current_time.second) + f" [{Fore.GREEN}" + "You" + f"{Fore.RESET}] @ [{Fore.CYAN}" + str(message.channel) + f"{Fore.RESET}] : " + str(message.content))
					print(" ")
				else:
					print(str(current_time.hour) + f"{Fore.RESET}:" + str(current_time.minute) + ":" + str(current_time.second) + f" [{Fore.RED}" + str(message.author) + f"{Fore.RESET}] @ [{Fore.CYAN}" + str(message.channel) + f"{Fore.RESET}] : " + str(message.content))
					print(" ")
			else:
				pass
else: # aka if user wants to monitor all messages.
	@bot.event
	async def on_message(message):
		current_time = datetime.datetime.now()
#if webhook option = yes, when we get a message send it to a webhook and log it.
		if logyn == "y":
			if message.channel.type is discord.ChannelType.private or message.channel.type is discord.ChannelType.group or message.channel.type is discord.ChannelType.text:
				if bot.user.id == message.author.id:
					if message.content == "": #this stops the logging of the webhooks own messages (creates an endless loop), due to the embeds having '' message content
						pass
					else:
						print(str(current_time.hour) + f"{Fore.RESET}:" + str(current_time.minute) + ":" + str(current_time.second) + f" [{Fore.GREEN}" + "You" + f"{Fore.RESET}] @ [{Fore.CYAN}" + str(message.channel) + f"{Fore.RESET}] : " + str(message.content))
						print(" ")
						data["embeds"] = [
							{
								"description" : f"`{message.content}`",
								"title" : f"{message.author}  ~ :  {message.channel}",
								"color" : 0xff0000
							}
						]
						result = requests.post(url, json = data)
					
				else:
					if message.content == "":
						pass
					else:
						print(str(current_time.hour) + f"{Fore.RESET}:" + str(current_time.minute) + ":" + str(current_time.second) + f" [{Fore.RED}" + str(message.author) + f"{Fore.RESET}] @ [{Fore.CYAN}" + str(message.channel) + f"{Fore.RESET}] : " + str(message.content))
						print(" ")
						data["embeds"] = [
							{
								"description" : f"`{message.content}`",
								"title" : f"{message.author}  ~ :  {message.channel}",
								"color" : 0xff0000
							}
						]
						result = requests.post(url, json = data)
			else:
				pass
		else:
			if message.channel.type is discord.ChannelType.private or message.channel.type is discord.ChannelType.group or message.channel.type is discord.ChannelType.text:
				if bot.user.id == message.author.id:
					print(str(current_time.hour) + f"{Fore.RESET}:" + str(current_time.minute) + ":" + str(current_time.second) + f" [{Fore.GREEN}" + "You" + f"{Fore.RESET}] @ [{Fore.CYAN}" + str(message.channel) + f"{Fore.RESET}] : " + str(message.content))
					print(" ")
				else:
					print(str(current_time.hour) + f"{Fore.RESET}:" + str(current_time.minute) + ":" + str(current_time.second) + f" [{Fore.RED}" + str(message.author) + f"{Fore.RESET}] @ [{Fore.CYAN}" + str(message.channel) + f"{Fore.RESET}] : " + str(message.content))
					print(" ")
			else:
				pass

		
        

bot.run(token, bot=False)
