# coding=UTF-8

from array import array

from ast import excepthandler
import asyncio
import textwrap
import io
from asyncio.events import get_child_watcher
from asyncio.windows_events import INFINITE
from datetime import datetime
import sqlite3
import json
import os
from turtle import Turtle
from urllib.request import urlopen
import random
import shutil
import sys
import time
import urllib.request
from random import randint
from time import sleep
from venv import create
import aiohttp
from aiohttp.client import ClientSession
import giphy_client
from giphy_client.rest import ApiException
import lxml.html as lxml
from lxml.html import parse
from lxml.html import fromstring
import requests
import re
from requests.api import get
from selenium import webdriver
from bs4 import BeautifulSoup
import chess
import matplotlib
import chess.svg

from libs import iFunny
from libs import yandex
from libs.iFunny import User
from libs import ws_client
from libs.ws_client import Buffer
from termcolor import colored
from PIL import Image
import math

from libs import fleep


email = "email"
password = "pass"
region = "United States"  # or "Brazil"
prefix = "" #Assert a prefix, like / . # @
basicauth = "Get Your own basic auth"


bot = iFunny.Bot(email, password, region, prefix, basicauth)
bearer = bot.buff.bearer
yandex_client = yandex.Yandex(yandexuid="7718144411634207533")
bot.developer = "Your user id for ultimate control"
# scripst: bot.developer = "620c6094174118743b5bd574"
botid = "The bot's user id"


src = r"D:\iPartybot"
dest = r"D:\iPartybot_Backup"
dest2 = r"D:\iPartybot_Backup2"
files = os.listdir(src)
files2 = os.listdir(dest)
os.chdir(src)

header = {
	'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

basicheaders = {
		'Host': 'api.ifunny.mobi',
		'Applicationstate': '1',
		'Accept': 'video/mp4, image/jpeg',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Authorization': f'Basic {basicauth}',
		'Accept-Encoding': 'gzip, deflate',
		'Ifunny-Project-Id': 'iFunny',
		'User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)',
		'Content-Length': '0',
		'Accept-Language': 'en-US;q=1',
	}

bearerheaders = {
		'Host': 'api.ifunny.mobi',
		'Applicationstate': '1',
		'Accept': 'video/mp4, image/jpeg',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Authorization': f'Bearer {bearer}',
		'Accept-Encoding': 'gzip, deflate',
		'Ifunny-Project-Id': 'iFunny',
		'User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)',
		'Content-Length': '0',
		'Accept-Language': 'en-US;q=1',
	}

os.chdir("D:\\iPartyBot")


async def upload_pixel(chat_id=None, data=None,mime=None):
		with open("bearer.json", "r") as bearerfile:
				logindata = json.load(bearerfile)
				user_bearer = logindata["bearer"]
		#data = io.BytesIO(data.read())

		await bot.buff.send_ifunny_ws(json.dumps([48, bot.buff.ifunny_ws_counter, {}, "co.fun.chat.message.create_empty", [], {"chat_name": f"{chat_id}"}]))
		await asyncio.sleep(.3)
		message_id = ws_client.message_ids[0]
		await bot.buff.send_ifunny_ws(json.dumps([48, bot.buff.ifunny_ws_counter, {}, "co.fun.chat.get_chat", [], {"chat_name": f"{chat_id}"}]))
		from urllib.request import urlopen
		

		headers = {
			"Host": "api.ifunny.mobi",
			"Accept": "video/mp4, image/jpeg",
			"Accept-Encoding": "gzip, deflate",
			"Connection": "close",
			"ApplicationState": "1",
			"Authorization": "Bearer " + user_bearer,
			"iFunny-Project-Id": "iFunny",
			"User-Agent": "iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)",
			"Accept-Language": "en-US;q=1, zh-Hans-US;q=0.9"
			}

		#mime = fleep.get(data.getvalue()).mime
		if mime:
			datatype = mime
			if datatype.startswith("image/"):
				upload_type = "pic"
				if datatype.endswith("/gif"):
					upload_type = "gif"
			elif datatype.startswith("video/"):
				upload_type = "video_clip"
		else:
			#print("somethin happened here")
			return
		if upload_type == "video_clip":
			uppload = "video"
		else:
			uppload = "image"
		re = requests.post(url='https://api.ifunny.mobi/v4/content', data={'message_id':message_id, 'type':upload_type, 'tags':[], 'description':'', 'visibility':'chats'}, headers=headers, files={uppload: ("image.tmp", data.getvalue(), mime[0])}).json()
		
		if "error" in re:
			return "Error"


async def upload(chat_id=None, data=None):
		with open("bearer.json", "r") as bearerfile:
				logindata = json.load(bearerfile)
				user_bearer = logindata["bearer"]
		data = io.BytesIO(data.read())

		await bot.buff.send_ifunny_ws(json.dumps([48, bot.buff.ifunny_ws_counter, {}, "co.fun.chat.message.create_empty", [], {"chat_name": f"{chat_id}"}]))
		await asyncio.sleep(.3)
		message_id = ws_client.message_ids[0]
		await bot.buff.send_ifunny_ws(json.dumps([48, bot.buff.ifunny_ws_counter, {}, "co.fun.chat.get_chat", [], {"chat_name": f"{chat_id}"}]))
		from urllib.request import urlopen
		# url = "https://c.tenor.com/fK0qAu06Y50AAAAC/pepe-hacker.gif"
		# r = urlopen(url).read()

		headers = {
			"Host": "api.ifunny.mobi",
			"Accept": "video/mp4, image/jpeg",
			"Accept-Encoding": "gzip, deflate",
			"Connection": "close",
			"ApplicationState": "1",
			"Authorization": "Bearer " + user_bearer,
			"iFunny-Project-Id": "iFunny",
			"User-Agent": "iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)",
			"Accept-Language": "en-US;q=1, zh-Hans-US;q=0.9"
			}

		mime = fleep.get(data.getvalue()).mime
		if mime:
			datatype = mime[0]
			if datatype.startswith("image/"):
				upload_type = "pic"
				if datatype.endswith("/gif"):
					upload_type = "gif"
			elif datatype.startswith("video/"):
				upload_type = "video_clip"
		else:
			#print("somethin happened here")
			return
		if upload_type == "video_clip":
			uppload = "video"
		else:
			uppload = "image"
		re = requests.post(url='https://api.ifunny.mobi/v4/content', data={'message_id':message_id, 'type':upload_type, 'tags':[], 'description':'', 'visibility':'chats'}, headers=headers, files={uppload: ("image.tmp", data.getvalue(), mime[0])}).json()
		print(re)
		#print("made it here")


async def change_pfp(file):
	
	with open(file,"rb") as f:

		file = io.BytesIO(f.read())

	headers = {
		'Host': 'api.ifunny.mobi',
		'Accept': 'video/mp4, image/jpeg',
		'Applicationstate': '1',
		'Content-Type': 'multipart/form-data; boundary=Boundary+92D003A7-70DB-4A25-BEF2-291A92259082',
		'Accept-Language': 'en-us',
		'Ifunny-Project-Id': 'iFunny',
		'User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)',
		'Authorization': 'Bearer 7adda7c0f2fe3fda0126d382722e6c7578766647226eab74392167e4a3308951',
		'Accept-Encoding': 'gzip, deflate',
	}
	
	response = requests.put('https://api.ifunny.mobi/v4/account/photo', data={"filename":"Photo"}, headers=bearerheaders, files={"photo": ("image.tmp", file.getvalue(), "image/png")})
	
	if response.status_code == 200:
		return "done"
	else:
		print(response.text)


def cprint(*args, end_each=" ", end_all=""):
	dt = str(datetime.fromtimestamp(int(time.time())))
	print(colored(dt, "white"), end=end_each)
	for i in args:
		print(colored(str(i[0]), i[1].lower()), end=end_each)
	print(end_all)


async def check_dm(chat_id):

	file_src = f"D:\\iPartyBot\\chat_databases\\{chat_id}.json"
	try:
		with open(file_src,"r") as f:
			j = json.load(f)
		return True
	except:
		return False

async def create_dm(ctx,chat_id,user):

	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.get_or_create_chat",[1,chat_id,None,None,None,[user.id]],{}]))



@bot.command(help_category="fun")
async def hug(ctx,hugg=None,*args):
	chat = ctx.chat
	if args:
		msg = ctx.message.args
		return await chat.send(f"❤️ You wrapped {msg} in a warm snuggly embrace and held them until they felt a little happier ❤️")
	if not hugg:
		return await chat.send("You hugged a tree and everyone looked at you funny.")
	return await chat.send(f"❤️ You wrapped {hugg} in a warm snuggly embrace and held them until they felt a little happier ❤️")

@bot.command(hide_help=True,auth=True,help_category="userdata",help_message="Usage: /edit username category value\n\nAcceptable values:\n\nBoolean:\n(True, False)\n\nJson:\n(Array [\"thing1\",\"thing2\"], Dict {\"key\":\"value\"}\n\nTime:\n(Now, Epoch)\n\nInteger:\n(1,48,80085)\n\nString:\n(Any Text)")
async def edit(ctx,user=None,thing=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return await chat.send("no")
	o = user
	user = await ctx.user(user)
	if not user:
		return await chat.send("User was invalid")
	data = await get_file(ctx,user)
	try:
		d = data[thing.lower()]
	except:
		return await chat.send("That category doesnt exist (use /cat to find out what you can edit)")
	argsh = args[0]
	if argsh.isdigit():
		argsh = int(args[0])
	full = ctx.message.args.replace(o+" ","").replace(thing+" ","")
	print(full)

	if str(full):
		if full.lower() in ["true","false"]:
			if full.lower() == "true":
				argsh = True
			else:
				argsh = False

	if full.startswith("[") or full.startswith("{"):
		if full.endswith("]") or full.endswith("}"):
			try:
				argsh = json.loads(full)
			except:
				return await chat.send("Invalid json format")
	
	data[thing] = argsh
	await update_data(data,user)
	return await chat.send(f"{thing} was set to {args[0]}")



@bot.command(help_category="admin",help_message=r'Set a welcome message after the command. The "%user" parameter can be used to say the username of the person who joins.')
async def setwelcome(ctx,*args):
	chat = ctx.chat
	data = await get_file(ctx,user=None,chat=chat)
	if ctx.message.author.id not in data["admins"]:
		return await chat.send("You are not an admin!")
	if not args:
		return await chat.send(r'Set a welcome message after the command. The "%user" parameter can be used to say the username of the person who joins.')
	message = ctx.message.args
	data["welcome"] = message
	await update_chat(data,chat)
	return await chat.send("Welcome message has been set!")

@bot.command(help_category="admin",help_message="Set rules.")
async def setrules(ctx,*args):
	chat = ctx.chat
	data = await get_file(ctx,user=None,chat=chat)
	if ctx.message.author.id not in data["admins"]:
		return await chat.send("You are not an admin!")
	message = ctx.message.args
	data["rules"] = message
	await update_chat(data,chat)
	return await chat.send("Rules have been set!")

@bot.command(help_category="tools")
async def rules(ctx,*args):
	chat = ctx.chat
	data = await get_file(ctx,user=None,chat=chat)
	if data.get("rules"):
		return await chat.send(data["rules"])
	else:
		return await chat.send("No rules have been set for this chat.")

@bot.command(help_category="tools",help_message="https://ifunny.co/picture/3T5dxqUC9")
async def ranks(ctx,*args):
	chat = ctx.chat
	return await chat.send("https://ifunny.co/picture/3T5dxqUC9")


@bot.command(help_category="admin",help_message="Admin a user of your chat!\n\nAdmins cannot admin other users or set chat ownership.")
async def admin(ctx,username=None,*args):
	chat = ctx.chat
	chat_type = chat.type
	role = chat.role
	user = ctx.message.author
	message = ctx.message
	data = await get_file(ctx,user=None,chat=chat)
	for i in data["owner"]:
		ownername = data["owner"][i]["nick"]
	if chat_type == 1:
		return
	if not username:
		return await chat.send("Input the username or userid of the user you would like to admin.")
	
	if username.lower() == "rainbot":
		if role == 2:
			if not message.payload.get("local_id"):
				return await chat.send("I have detected that you are on an Android device, Follow these directions to get started:\nhttps://ifunny.co/picture/uC2ZpHVB9")
			elif "-" in message.payload["local_id"]:
				return await chat.send("I have detected that you are on an IOS device, Follow these directions to get started:\nhttps://ifunny.co/picture/4mbZdwIC9")
			else:
				return await chat.send("I could not detect what device you are using, Try these instructions: https://ifunny.co/picture/uC2ZpHVB9")
		elif role == 1:
			if not message.payload.get("local_id"):
				return await chat.send("You set me as an operator instead of the chat admin. De-op me and follow these instructions: https://ifunny.co/picture/uC2ZpHVB9")
			elif "-" in message.payload["local_id"]:
				return await chat.send("You set me as an operator instead of the chat admin. De-op me and follow these instructions: https://ifunny.co/picture/4mbZdwIC9")
			else:
				return await chat.send("You set me as an operator instead of the chat admin. De-op me and follow these instructions: https://ifunny.co/picture/uC2ZpHVB9")
		else:
			return await chat.send("I am already admin.")

	
	other_user = await ctx.user(username)
	if not other_user:
		return


	if role != 0:
		return await chat.send("I am not the admin of this chat!")
	if user.id not in data["owner"]:
		return await chat.send(f"Only {ownername} can edit the admins of this chat!")
	if other_user.id in data["admins"]:
		return await chat.send(f"{other_user.nick} is already an admin.")
	admins = data["admins"]
	admins.append(other_user.id)
	data["admins"] = admins

	if chat.type == 3:
		newoplist = data["ops"]
		newoplist.append(other_user.id)
		data["ops"] = newoplist
		# await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.register_operators",[],{"chat_name":f"{chat.id}","operator_ids":[f"{other_user.id}"]}]))
	await update_chat(data,chat)
	return await chat.send(f"{other_user.nick} was promoted to admin.")


@bot.command(hide_help=True,auth=True,help_category="chats",help_message="Use this only for making the bot leave a chat if it is the current admin. chat ownership will be passed to you, please dont use this to take over or delete group chats, instead give the ownership back to the original owner.")
async def forceleave(ctx,*args):
	user = ctx.message.author
	if not user.auth:
		return
	chat = ctx.chat
	await chat.send("ok")
	await asyncio.sleep(.2)
	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.leave_chat",[],{"admin":f"{user.id}","chat_name":f"{chat.id}"}]))

@bot.command(help_category="admin",help_message="Un-Admin a previously adminned user. Only the chat owner can un-admin a user")
async def unadmin(ctx,username=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	data = await get_file(ctx,user=None,chat=ctx.chat)
	mems = await chat.members()
	index = 0
	for i in data["owner"]:
		ownername = data["owner"][i]["nick"]

	if not username:
		return await chat.send("Input a username")
	if username.lower() == "rainbot":
		if user.id in data["owner"] or user.nick.lower() == "scripts":
			if chat.role == 0:
				unmodlist = []
				await chat.send("Giving owner status to you...")
				if chat.type == 3:
					for i in mems:
						users = mems[index]
						if users.role == 1:
							unmodlist.append(users.id)
						index += 1
						continue
				# await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.unregister_operators",[],{"chat_name":str(chat.id),"operator_ids":unmodlist}]))
				await asyncio.sleep(2)                
				await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.leave_chat",[],{"admin":f"{user.id}","chat_name":f"{chat.id}"}]))
				await chat.invite(await ctx.user("rainbot"))
				return
		else:
			return await chat.send(f"Only {ownername} can take ownership of this chat!")
	other_user = await ctx.user(username)
	if not other_user:
		return
	if user.id not in data["owner"]:
		return await chat.send(f"Only {ownername} can edit admins!")
	if str(other_user.id) not in data["admins"]:
		return await chat.send(f"{other_user.nick} Wasn't an admin to begin with!")
	
	admins = data["admins"]
	admins.remove(other_user.id)
	data["admins"] = admins
	
	if chat.type == 3:
		ops = data["ops"]
		if other_user.id in ops:
			ops.remove(other_user.id)
			# await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.unregister_operators",[],{"chat_name":str(chat.id),"operator_ids":[str(other_user.id)]}]))
		data["ops"] = ops
	await update_chat(data,chat)
	return await chat.send(f"{other_user.nick} was demoted to member.")

@bot.command(help_category="admin",help_message="Toggle whether or not known bot accounts can join your chat (yk what bots im talking about)")
async def antibot(ctx,*args):
	chat = ctx.chat
	chat_type = chat.type
	if chat_type == 1:
		return await chat.send("This is a DM, not a group chat.")
	
	data = await get_file(ctx,user=None,chat=chat)
	user = ctx.message.author
	if user.id not in data["admins"]:
		return await chat.send("You are not an admin")
	status = chat.bot_role
	if status != 0:
		return await chat.send("This feature will not work unless i am admin of the chat.")
	nopfp = data.get("antibot")
	if not nopfp:
		data["antibot"] = False
		nopfp = False
		await update_chat(data,chat)
	if nopfp == True:
		data["antibot"] = False
		await chat.send("Anti-Bot has been disabled")
		return await update_chat(data=data,chat=chat)
	if nopfp == False:
		data["antibot"] = True
		await chat.send("Anti-Bot has been enabled, anybody who is a known bot that joins the chat will be kicked.")
		return await update_chat(data,chat)


async def kick_user_by_id(ctx,chat,user):
	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.kick_member",[],{"chat_name":f"{chat.id}","user_id":f"{user}"}]))

async def kick_user(ctx,chat,user):
	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.kick_member",[],{"chat_name":f"{chat.id}","user_id":f"{user.id}"}]))

@bot.command(help_category="admin",help_message="Kick a user from the chat!")
async def kick(ctx,username=None,*args):
	chat = ctx.chat
	data = await get_file(ctx,user=None,chat=chat)
	user = ctx.message.author
	if user.id not in data["admins"]:
		if user.id not in data["mods"]:
			return await chat.send("You are not an admin or mod of this chat!")
	members = await chat.members()
	if not username:
		return
	index = 0
	user_id = None
	for i in members:
		user2 = members[index]
		name = user2.nick
		if username.lower() == name.lower():
			user_id = user2.id
			break
		index += 1
	if not user_id:
		return await chat.send("That user must be in the chat for me to kick them!")
	if user_id in data["admins"]:
		return await chat.send("You must first Un-Admin that user before i can kick them!")
	if user_id in data["mods"]:
		return await chat.send("You must first Un-Mod that user before i can kick them!")
	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.kick_member",[],{"chat_name":f"{chat.id}","user_id":f"{user_id}"}]))
	return await chat.send(f"{name} was kicked")

@bot.command(help_category="tools",help_message="See if a certain user is banned from the chat. Useful for large ban lists.",aliases=["sb"])
async def searchbans(ctx,username=None,*args):
	chat = ctx.chat
	if not username:
		return await chat.send("Input a username")
	data = await get_file(ctx,user=None,chat=chat)
	user = await ctx.user(username)
	if not user:
		return await chat.send("I couldn't find that user!")
	if user.id in data["banned"]:
		return await chat.send(f"✅ {user.nick} is banned.")
	else:
		return await chat.send(f"❌ {user.nick} is not banned")

@bot.command(help_category="admin",help_message="Ban a user out of your chat")
async def ban(ctx,*args):
	chat = ctx.chat
	data = await get_file(ctx,user=None,chat=chat)
	bans = data["banned"]
	user = ctx.message.author
	mems = await chat.members()
	if user.id not in data["admins"]:
		if user.id not in data["mods"]:
			return await chat.send("You are not an admin or a mod!")
	msg = ""
	for username in args:
		index = 0

		
		other_user = await ctx.user(username)
		if not other_user:
			for i in mems:
				other_user = i
				if i.nick.lower() != username.lower():
					continue
				if i.nick.lower() == username.lower():
					index += 1
					break
			if index == 0:
				msg += f"🔍 couldnt find {username}\n"
				continue
		if other_user.id in data["admins"]:
			msg += f"❌ I cannot ban {other_user.nick} as they are an admin.\n"
			continue
		if other_user.id in data["mods"]:
			msg += f"❌ I cannot ban {other_user.nick} as they are a mod.\n"
			continue
		if other_user.id not in bans:
			bans.append(other_user.id)
		msg += f"✅ {other_user.nick} was banned\n"
		for userobj in mems:
			if other_user.id == userobj.id:
				await kick_user(ctx,chat=chat,user=other_user)
			continue
	data["banned"] = bans
	
	await update_chat(data=data,chat=chat)
	return await chat.send(msg)


@bot.command(help_category="fun",help_message = "Make obama say stuff",developer=True)
async def obama(ctx,*args):
	import http3
	client = http3.AsyncClient()
	chat = ctx.chat
	q = ""
	count = len(args)
	index = 0
	for i in args:
		index += 1
		if index == count:
			q += f"{i}"
			break
		q += f"{i}+"
	print(q)
	q = q.replace(",","")
	q = q.replace(".","")
	q = q.replace("'","")
	q = q.replace("’","")

	cookies = {
	'_ga': 'GA1.2.827908840.1645478358',
	'_gid': 'GA1.2.1774432474.1645478358',
}
	data = f'input_text='+q

	headers = {
		'Host': 'talkobamato.me',
		'Content-Length': f'{len(data)}',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'Origin': 'http://talkobamato.me',
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'Referer': 'http://talkobamato.me/synthesize.py?speech_key=00de8216bae3778ad5c16c80df347efa',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.9',
		'Connection': 'close',
	}

	while True:

		response = requests.post('http://talkobamato.me/synthesize.py', headers=headers, cookies=cookies, data=data, verify=False)
		index = 0
		while True:
			index += 1
			print(index)
			await asyncio.sleep(1)
			if not response.text:
				print("continue")
				continue
			print(response.text)
			break

		html = fromstring(response.text)
		if "The server encountered an internal error" in response.text:
			return await chat.send("That broke obamer. good job")
		print(html.cssselect("source"))
		ele = html.cssselect("source")
		if ele == []:
			await asyncio.sleep(1)
			continue
		break
	for i in ele:
		t = lxml.tostring(i)
		print(t)
	t = t.decode('utf-8')
	t = str(t)
	t = t.replace("<source src=\"","")
	print(t)
	t = t.replace("\" type=\"video/mp4\">","")
	t = t.replace("\n        Your browser does not support the video tag.\n        </source>","")
	
	print(t)
	index = 0
	while True:
		await asyncio.sleep(1)
		url = "http://talkobamato.me/"+t
		try:
			url = urlopen(url)
		except:
			await asyncio.sleep(1)
			continue
		if not url:
			index += 1
			continue
		if index > 10:
			return await chat.send("Something went wrong")
		else:
			try:
				await chat.send("Generated!")
				await upload(chat_id=chat.id,data=url)
				break
			except:
				return await chat.send("Something went wrong")
				break

@bot.command(help_category="admin",help_message="Unbans a user from the chat")
async def unban(ctx,username=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	data = await get_file(ctx,user=None,chat=chat)
	bans = data["banned"]
	if user.id not in data["admins"]:
		if user.id not in data["mods"]:
			return await chat.send("You are not an admin or a mod.")
	if not username:
		return await chat.send("Input a user to unban")
	other_user = await ctx.user(username)
	if not other_user:
		return
	if other_user.id not in bans:
		return await chat.send("That user isnt banned to begin with.")
	bans.remove(other_user.id)
	data["banned"] = bans
	await update_chat(data=data,chat=chat)
	return await chat.send(f"{other_user.nick} has been forgiven")



@bot.command(help_category="admin",help_message="Makes the chat go into lockdown mode. To disable, run the command again.")
async def lockdown(ctx,*args):
	chat = ctx.chat
	chat_type = chat.type
	if chat_type == 1:
		return await chat.send("This is a DM, not a group chat.")
	data = await get_file(ctx,user=None,chat=chat)
	user = ctx.message.author
	status = chat.bot_role
	if status != 0:
		return await chat.send("This feature will not work unless i am admin of the chat.")
	if user.id not in data["admins"]:
		return await chat.send("You are not an admin")
	lockdown = data["lockdown"]
	if lockdown == True:
		data["lockdown"] = False
		await chat.send("Lockdown has been disabled")
		return await update_chat(data=data,chat=chat)
	if lockdown == False:
		data["lockdown"] = True
		await chat.send("Lockdown has been enabled, anybody who joins the chat will be kicked.")
		return await update_chat(data,chat)

@bot.command(help_category="admin",help_message="Toggle whether or not users with no Profile Pics can join the chat.")
async def nopfp(ctx,*args):
	chat = ctx.chat
	chat_type = chat.type
	if chat_type == 1:
		return await chat.send("This is a DM, not a group chat.")
	
	data = await get_file(ctx,user=None,chat=chat)
	user = ctx.message.author
	if user.id not in data["admins"]:
		return await chat.send("You are not an admin")
	status = chat.bot_role
	if status != 0:
		return await chat.send("This feature will not work unless i am admin of the chat.")
	nopfp = data["nopfp"]
	if nopfp == True:
		data["nopfp"] = False
		await chat.send("automatic kicking of users with no profile pic has been disabled")
		return await update_chat(data=data,chat=chat)
	if nopfp == False:
		data["nopfp"] = True
		await chat.send("NoPfp has been enabled, anybody who joins the chat without a Profile Pic will be kicked.")
		return await update_chat(data,chat)
	

@bot.command(help_category="admin",help_message="Mute the chat so only admins can talk. Only works for public chats.")
async def mute(ctx,*args):
	chat = ctx.chat
	data = await get_file(ctx,user=None,chat=chat)
	user = ctx.message.author
	admins = data["admins"]
	mods = data["mods"]
	if user.id not in data["admins"]:
		return await chat.send("This is an Admin only command")
	if chat.type != 3:
		return await chat.send("This feature only works for public chats.")
	await chat.send("Muting the chat... only admins will be able to send messages")
	if data["ops"] != []:
		await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.unregister_operators",[],{"chat_name":f"{chat.id}","operator_ids":data["ops"]}]))
	for i in mods:
		if i not in admins:
			admins.append(i)
	await asyncio.sleep(1)
	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.register_operators",[],{"chat_name":f"{chat.id}","operator_ids":admins}]))
	await asyncio.sleep(1)
	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.freeze_chat",[],{"chat_name":f"{chat.id}"}]))
	return await chat.send("Chat has been muted")

@bot.command(help_category="admin",help_message="Unmutes a chat from a previous mute. Only works for public chats.")
async def unmute(ctx,*args):
	chat = ctx.chat
	data = await get_file(ctx,user=None,chat=chat)
	mods = data["mods"]
	for i in data["owner"]:
		ownername = data["owner"][i]["id"]
	user = ctx.message.author
	if user.id not in data["admins"]:
		return await chat.send("This is an Admin only command")
	if chat.type != 3:
		return await chat.send("This feature only works for public chats.")
	admins = data["admins"]
	admins.remove(ownername)
	for i in mods:
		if i not in admins:
			admins.append(i)

	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.unfreeze_chat",[],{"chat_name":f"{chat.id}"}]))
	if admins != []:
		await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.unregister_operators",[],{"chat_name":str(chat.id),"operator_ids":admins}]))
	await chat.send("Chat has been un-muted")
	return await refresh_file(ctx,chat)

@bot.command(help_category="admin",help_message="Mod a user of your chat!\n\nMods can only kick or ban users from the chat.")
async def mod(ctx,username=None,*args):
	chat = ctx.chat
	chat_type = chat.type
	role = chat.role
	user = ctx.message.author
	message = ctx.message
	data = await get_file(ctx,user=None,chat=chat)
	for i in data["owner"]:
		ownername = data["owner"][i]["nick"]
	if chat_type == 1:
		return
	if not username:
		return await chat.send("Input the username or userid of the user you would like to admin.")
	
	if username.lower() == "rainbot":
		return await chat.send("I cannot be set as a mod.")

	
	other_user = await ctx.user(username)
	if not other_user:
		return await chat.send("I couldn't find that user.")


	if role != 0:
		return await chat.send("I am not the operator of this chat!")
	if user.id not in data["owner"]:
		return await chat.send(f"Only {ownername} can set mods of this chat!")
	if other_user.id in data["admins"]:
		return await chat.send(f"{other_user.nick} is an admin.")
	if other_user.id in data["mods"]:
		return await chat.send(f"{other_user.nick} is already a mod.")
	mods = data["mods"]
	mods.append(other_user.id)
	data["mods"] = mods

	# if chat.type == 3:
	#    newoplist = data["ops"]
	#    newoplist.append(other_user.id)
	#    data["ops"] = newoplist
		# await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.register_operators",[],{"chat_name":f"{chat.id}","operator_ids":[f"{other_user.id}"]}]))
	await update_chat(data,chat)
	return await chat.send(f"{other_user.nick} was promoted to Moderator.")

@bot.command(help_category="admin",help_message="Un-Mod a user. Only admins and the chat owner can Un-Mod a user")
async def unmod(ctx,username=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	data = await get_file(ctx,user=None,chat=ctx.chat)
	mems = await chat.members()
	index = 0
	for i in data["owner"]:
		ownername = data["owner"][i]["nick"]

	if not username:
		return await chat.send("Input a username")
	if username.lower() == "rainbot":
		return await chat.send(f"I cannot be set as a mod. Why did you try this? Silly {user.name}")
	
	
	other_user = await ctx.user(username)
	if not other_user:
		return await chat.send("I couldn't find that user!")
	if user.id not in data["admins"]:
		return await chat.send(f"Only an admin or the chat owner, ({ownername}), can remove a Mod!")
	if str(other_user.id) not in data["mods"]:
		return await chat.send(f"{other_user.nick} Wasn't a mod to begin with!")
	
	mods = data["mods"]
	mods.remove(other_user.id)
	data["mods"] = mods
	
	# if chat.type == 3:
	#    ops = data["ops"]
	#    if other_user.id in ops:
	#        ops.remove(other_user.id)
			# await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.unregister_operators",[],{"chat_name":str(chat.id),"operator_ids":[str(other_user.id)]}]))
	#    data["ops"] = ops
	await update_chat(data,chat)
	return await chat.send(f"{other_user.nick}'s status has been set to Member.")

@bot.command(aliases=["chatpfp","setcover"],help_category="admin",help_message=f"Change the Chat's Profile pic\n\nUsage: {prefix}setpfp (link to an image)\n\nSupports direct image links from the internet (If in a private chat), or ifunny post links")
async def setpfp(ctx,link=None,*args):
	chat = ctx.chat
	chat_id = chat.id
	chattitle = chat.title
	user = ctx.message.author
	
	data = await get_file(ctx,user=None,chat=chat)
	if user.id not in data["admins"]:
		return await chat.send("You are not an admin for this chat!")


	if not link: return await chat.send("I need something new to set the pfp to")
	if chat.type == 3:
		if "https://ifunny.co" not in link:
			return await chat.send("Public chats can only be set to iFunny post links!!")
	if "https://ifunny.co" in link:
		link = link.split("/")
		link = link[4]
		link = link.split("?s=")
		content_id = link[0]
		basicauth = await gen_basic()
		header = {'Host': 'api.ifunny.mobi','Applicationstate': '1','Authorization': 'Basic '+basicauth,'Ifunny-Project-Id': 'iFunny','User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)','Accept-Language': 'en-US;q=1','Accept-Encoding': 'gzip, deflate'}
		url = f"https://api.ifunny.mobi/v4/content/{content_id}"

		req = requests.get(url,headers=header)
		data = json.loads(req.text)
		if data["status"] == 404:
			return await chat.send("That content either got banned or doesnt exist.")
		link = data["data"]["url"]


	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.edit_chat",[],{"unset":[],"set":{"title":f"{chattitle}","cover":f"{link}"},
	"chat_name":f"{chat_id}"}]))
			

	return await chat.send("Cover has been set!")


async def encode_special(string):

	args_list = string.split(" ")
	chosen = args_list.pop(0)
	msg = ""
	for i in args_list:
		msg += f"{i} "
	print(args_list)
	msg = msg[:len(msg)-1]

	
	norm = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789_"
		
	fonts = [
		"𝗔𝗮𝗕𝗯𝗖𝗰𝗗𝗱𝗘𝗲𝗙𝗳𝗚𝗴𝗛𝗵𝗜𝗶𝗝𝗷𝗞𝗸𝗟𝗹𝗠𝗺𝗡𝗻𝗢𝗼𝗣𝗽𝗤𝗾𝗥𝗿𝗦𝘀𝗧𝘁𝗨𝘂𝗩𝘃𝗪𝘄𝗫𝘅𝗬𝘆𝗭𝘇𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵_",
		"𝘈𝘢𝘉𝘣𝘊𝘤𝘋𝘥𝘌𝘦𝘍𝘧𝘎𝘨𝘏𝘩𝘐𝘪𝘑𝘫𝘒𝘬𝘓𝘭𝘔𝘮𝘕𝘯𝘖𝘰𝘗𝘱𝘘𝘲𝘙𝘳𝘚𝘴𝘛𝘵𝘜𝘶𝘝𝘷𝘞𝘸𝘟𝘹𝘠𝘺𝘡𝘻123456789_",
		"𝘼𝙖𝘽𝙗𝘾𝙘𝘿𝙙𝙀𝙚𝙁𝙛𝙂𝙜𝙃𝙝𝙄𝙞𝙅𝙟𝙆𝙠𝙇𝙡𝙈𝙢𝙉𝙣𝙊𝙤𝙋𝙥𝙌𝙦𝙍𝙧𝙎𝙨𝙏𝙩𝙐𝙪𝙑𝙫𝙒𝙬𝙓𝙭𝙔𝙮𝙕𝙯123456789_",
		"𝔄𝔞𝔅𝔟ℭ𝔠𝔇𝔡𝔈𝔢𝔉𝔣𝔊𝔤ℌ𝔥ℑ𝔦𝔍𝔧𝔎𝔨𝔏𝔩𝔐𝔪𝔑𝔫𝔒𝔬𝔓𝔭𝔔𝔮ℜ𝔯𝔖𝔰𝔗𝔱𝔘𝔲𝔙𝔳𝔚𝔴𝔛𝔵𝔜𝔶ℨ𝔷123456789_",
		"𝕬𝖆𝕭𝖇𝕮𝖈𝕯𝖉𝕰𝖊𝕱𝖋𝕲𝖌𝕳𝖍𝕴𝖎𝕵𝖏𝕶𝖐𝕷𝖑𝕸𝖒𝕹𝖓𝕺𝖔𝕻𝖕𝕼𝖖𝕽𝖗𝕾𝖘𝕿𝖙𝖀𝖚𝖁𝖛𝖂𝖜𝖃𝖝𝖄𝖞𝖅𝖟123456789_",
		"𝒜𝒶𝐵𝒷𝒞𝒸𝒟𝒹𝐸𝑒𝐹𝒻𝒢𝑔𝐻𝒽𝐼𝒾𝒥𝒿𝒦𝓀𝐿𝓁𝑀𝓂𝒩𝓃𝒪𝑜𝒫𝓅𝒬𝓆𝑅𝓇𝒮𝓈𝒯𝓉𝒰𝓊𝒱𝓋𝒲𝓌𝒳𝓍𝒴𝓎𝒵𝓏𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫_",
		"𝓐𝓪𝓑𝓫𝓒𝓬𝓓𝓭𝓔𝓮𝓕𝓯𝓖𝓰𝓗𝓱𝓘𝓲𝓙𝓳𝓚𝓴𝓛𝓵𝓜𝓶𝓝𝓷𝓞𝓸𝓟𝓹𝓠𝓺𝓡𝓻𝓢𝓼𝓣𝓽𝓤𝓾𝓥𝓿𝓦𝔀𝓧𝔁𝓨𝔂𝓩𝔃123456789_",
		"𝕒α𝔟Ｂｃ𝒸ｄ𝐝𝒆ε𝓕Ƒ𝐠𝑔𝐡𝒽𝕚Ｉⓙ𝐣ķᵏĹⓛ๓Ⓜ𝐧𝓃ｏⓞƤƤ𝐐𝓠ℝⓡŜˢţ𝐓ᵘ𝓾𝓥Ｖⓦｗ𝔵᙭Ⓨ𝐲ℤℤ❶２３４➄６７➇９_",
		"🄰🄰🄱🄱🄲🄲🄳🄳🄴🄴🄵🄵🄶🄶🄷🄷🄸🄸🄹🄹🄺🄺🄻🄻🄼🄼🄽🄽🄾🄾🄿🄿🅀🅀🅁🅁🅂🅂🅃🅃🅄🅄🅅🅅🅆🅆🅇🅇🅈🅈🅉🅉123456789_",
		"🅰🅰🅱🅱🅲🅲🅳🅳🅴🅴🅵🅵🅶🅶🅷🅷🅸🅸🅹🅹🅺🅺🅻🅻🅼🅼🅽🅽🅾🅾🅿🅿🆀🆀🆁🆁🆂🆂🆃🆃🆄🆄🆅🆅🆆🆆🆇🆇🆈🆈🆉🆉123456789_",
		"ⒶⓐⒷⓑⒸⓒⒹⓓⒺⓔⒻⓕⒼⓖⒽⓗⒾⓘⒿⓙⓀⓚⓁⓛⓂⓜⓃⓝⓄⓞⓅⓟⓆⓠⓇⓡⓈⓢⓉⓣⓊⓤⓋⓥⓌⓦⓍⓧⓎⓨⓏⓩ①②③④⑤⑥⑦⑧⑨_",
		"ＡａＢｂＣｃＤｄＥｅＦｆＧｇＨｈＩｉＪｊＫｋＬｌＭｍＮｎＯｏＰｐＱｑＲｒＳｓＴｔＵｕＶｖＷｗＸｘＹｙＺｚ１２３４５６７８９_",
		"𝔸𝕒𝔹𝕓ℂ𝕔𝔻𝕕𝔼𝕖𝔽𝕗𝔾𝕘ℍ𝕙𝕀𝕚𝕁𝕛𝕂𝕜𝕃𝕝𝕄𝕞ℕ𝕟𝕆𝕠ℙ𝕡ℚ𝕢ℝ𝕣𝕊𝕤𝕋𝕥𝕌𝕦𝕍𝕧𝕎𝕨𝕏𝕩𝕐𝕪ℤ𝕫𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡_"

	]
	
	final = ""
	f = [r"%bold",r"%italic",r"%italic_bold",r"%gothic",r"%gothic_bold",r"%fancy",r"%fancy_bold",r"%funky",r"%boxed",r"%emoji",r"%bubble",r"%smooth",r"%outline"]
	if not chosen or chosen.lower() not in f:
		print("nope")
		return string
	the_font = fonts[f.index(chosen.lower())]
	
	
	for char in msg:
		if char not in norm:
			final += char
			continue
	
		encoded_char = the_font[norm.index(char)]
		final += encoded_char
		continue
	return final

@bot.command(help_category="fonts",help_message="Turns whatever you type into the selected font\n\nUsage: /font %gothic this is a test")
async def font(ctx,*args):
	chat = ctx.chat
	msg = ctx.message.args
	f = [r"%bold",r"%italic",r"%italic_bold",r"%gothic",r"%gothic_bold",r"%fancy",r"%fancy_bold",r"%funky",r"%boxed",r"%emoji",r"%bubble",r"%smooth",r"%outline"]
	title = ctx.message.args
	if args:
		if args[0].lower() in f:
			title = await encode_special(ctx.message.args)
	return await chat.send(title)

@bot.command(help_category="admin",help_message=r"Set the chat name\n\nUsage:\n/setname Chat Name Here\n\nYou can also select a font!\n\nFont usage:\n/setname %font Chat Name Here\n\nAvailable Fonts:\n%bold : 𝗛𝗲𝗹𝗹𝗼\n%italic : 𝘏𝘦𝘭𝘭𝘰\n%italic_bold : 𝙃𝙚𝙡𝙡𝙤\n%gothic : ℌ𝔢𝔩𝔩𝔬\n%gothic_bold : 𝕳𝖊𝖑𝖑𝖔\n%fancy : 𝐻𝑒𝓁𝓁𝑜\n%fancy_bold : 𝓗𝓮𝓵𝓵𝓸\n%funky : ⒽέĻŁᵒ\n%boxed : 🄷🄴🄻🄻🄾\n%emoji : 🅷🅴🅻🅻🅾\n%bubble : Ⓗⓔⓛⓛⓞ\n%smooth : Ｈｅｌｌｏ\n%outline : ℍ𝕖𝕝𝕝𝕠",aliases=["settitle"])
async def setname(ctx,*args):
	chat = ctx.chat
	chat_id = chat.id
	data = await get_file(ctx,user=None,chat=chat)
	user = ctx.message.author
	if user.id not in data["admins"]:
		return await chat.send("You are not an admin of this chat!")
	if not args:
		title = "Un-named Chat"
	f = [r"%bold",r"%italic",r"%italic_bold",r"%gothic",r"%gothic_bold",r"%fancy",r"%fancy_bold",r"%funky",r"%boxed",r"%emoji",r"%bubble",r"%smooth",r"%outline"]
	title = ctx.message.args
	if args:
		if args[0].lower() in f:
			title = await encode_special(ctx.message.args)

	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.edit_chat",[],{"unset":[],"chat_name":f"{chat_id}","set":{"title":f"{title}"}}]))
	return await chat.send("Chat name has been updated")

@bot.command(help_category="tools",help_message="Disable certain commands")
async def disable(ctx,cmd=None,*args):
	chat = ctx.chat
	if chat.type == 1:
		return
	data = await get_file(ctx,user=None,chat=chat)
	author = ctx.message.author
	if author.id not in data["owner"]:
		d = await get_file(ctx,author)
		if d["auth"] != True:
			return await chat.send("You are not the owner of this chat!")
	if not cmd:
		return await chat.send("Input a command to disable")
	cmd = cmd.lower()
	l = ["disable","admin","admins","mod","mods","unadmin","unmod","help","support","setwelcome","setrules","antibot","kick","ban","unban","lockdown","nopfp","mute","unmute","setpfp","setname","purge"]
	if cmd in l:
		return await chat.send("I am unable to disable that command")
	d = data["disabled"]
	if function := bot.commands.get(cmd):
		if cmd not in d:
			d.append(cmd)
			st = "disabled"
		else:
			d.remove(cmd)
			st = "enabled"
		data["disabled"] = d
		await update_chat(data,chat)
		return await chat.send(f"The {cmd.capitalize()} command was {st}.")
	else:
		return await chat.send("That command doesnt exist")

@bot.command(hide_help=True)
async def impend(ctx,*args):
	chat = ctx.chat
	author = ctx.message.author
	if author.name.lower() != "impend":
		return
	msg = ["Coding is hot ngl","i cooked\n\n\nfinch toafst","I'm not a liberal","I was referring to black people","One of the few times i decided to show respect lol","i dont cook i don- cook cook cook cook cookcookcookcookcookcook","*fortnite death sounds* GOD DAMMIT"]
	return await chat.send(random.choice(msg))

@bot.command(help_category="tools",help_message="View Current admins in this chat")
async def admins(ctx,*args):
	chat = ctx.chat
	data = await get_file(ctx,user=None,chat=chat)
	admins = data["admins"]
	mods = data["mods"]
	mems = await chat.members()
	ownername = []
	
	for i in data["owner"]:
		ownername = data["owner"][i]["nick"]
		
		ownerid = data['owner'][i]['id']

	if admins == []:
		if ownername == []:
			return await chat.send("This chat is not owned by a user or a bot and nothing can be done about it.")
		return await chat.send(f"{ownername} is the current owner of the chat.")

	index = 0
	names = []
	
	for i in admins:
		userid = admins[index]
		index2 = 0
		for user in mems:
			userob = mems[index2]
			if userob.id == ownerid:
				index2 += 1
				continue
			if userob.id == userid:
				names.append(userob.nick)
				admins.remove(userob.id)
			index2 += 1
			continue
		index += 1
		continue
	if admins != []:
		index = 0
		for i in admins:
			user_id = admins[index]
			if user_id == ownerid:
				index+=1
				continue
			data = requests.get(f'https://api.ifunny.mobi/v4/users/{user_id}', headers=basicheaders)
			data = data.json()
			nick = data['data']['nick']
			names.append(nick)
			index += 1
			continue
	names2 = []
	index = 0
	for i in mods:
		userid = mods[index]
		index2 = 0
		for user in mems:
			userob = mems[index2]
			if userob.id == ownerid:
				index2 += 1
				continue
			if userob.id == userid:
				names2.append(userob.nick)
				mods.remove(userob.id)
			index2 += 1
			continue
		index += 1
		continue
	if mods != []:
		index = 0
		for i in mods:
			user_id = mods[index]
			if user_id == ownerid:
				index+=1
				continue
			data = await ctx.user(user_id)
			if not data:
				nick = "<Deactivated User>"
				names2.append(nick)
				index += 1
				continue
			nick = data.nick
			names2.append(nick)
			index += 1
			continue

	msg = f"Owner:\n{ownername}\n\n"
	if names != []:
		msg += f"Admins:\n"
	elif names == []:
		msg += f"There are no admins set. Set an admin by saying {ctx.bot.prefix}admin (username)."

	

	index2 = 0

	for i in names:
		name = names[index2]
		msg += f"{name}\n"
		index2 += 1
		continue

	if names2 != []:
		msg+= f"\nMods:\n"
	elif names == []:
		msg += "There are no mods set."

	index2 = 0

	for i in names2:
		name = names2[index2]
		msg += f"{name}\n"
		index2 += 1
		continue
	
	return await chat.send(msg)



@bot.command(hide_help=True,auth=True,help_message="Grants XP to a user. Dont go overboard. Use - to take xp away.",help_category="userdata")
async def grantxp(ctx,username=None,amount = None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return
	other_user = await ctx.user(username)
	if not other_user:
		return await chat.send("User does not exist")
	data = await get_file(ctx,user=other_user)

	if not amount:
		return
	

	data["xp"] += round(int(amount))
	
	await update_data(data,other_user)
	await chat.send(f"You added {int(amount):,}XP to {other_user.name}")


@bot.command(hide_help=True,auth=True,help_category="userdata",help_message="Add or remove from someones balance. Dont go overboard.")
async def grant(ctx,username=None,amount = None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return
	other_user = await ctx.user(username)
	if not other_user:
		return await chat.send("User does not exist")
	data = await get_file(ctx,user=other_user)

	if not amount:
		return
	

	data["wallet"] += round(int(amount))
	
	await update_data(data,other_user)
	await chat.send(f"You added {int(amount):,} to {other_user.name}'s wallet")



@bot.command(help_category="general",help_message="Tell someone that you love them. or hate them. idc.",cooldown=60,aliases=["dm"])
async def tell(ctx,username=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not username:
		return
	user = await ctx.user(username)
	if not user:
		return await chat.send("That user doesnt exist")
	og_id = chat.id
	chat_id = botid+"_"+user.id
	if author.name != user.nick:
		status = await chat_invite_check(ctx,author,user)
	else:
		status = "allowed"
	if ctx.message.author.auth:
		status = "allowed"
	if status == "allowed":
		check = await check_dm(chat_id)
		if not check:
			chat_id = user.id+"_"+botid
			check = await check_dm(chat_id)
			if not check:
				await create_dm(ctx,chat_id,user)

		msg = f"{author.nick} sent you a message! it reads:\n\n"
		for i in args:
			msg += f"{i} "
		msg += "\n\nSend a message using /tell or an anonymous message by using /whisper"
		await chat.send("sent")
		# chat.id = chat_id
		chat.id = chat_id
		return await chat.send(msg)
	elif status == "subs":
		return await chat.send("That user isnt subscribed to you :(")
	else:
		return await chat.send("This user's DMs are closed.")


@bot.command(help_category="general",help_message="Tell someone that you love them. or hate them. idc.",cooldown=60)
async def whisper(ctx,username=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not username:
		return
	user = await ctx.user(username)
	if not user:
		return await chat.send("That user doesnt exist")
	og_id = chat.id
	chat_id = botid+"_"+user.id

	status = await chat_invite_check(ctx,author,user)
	if ctx.message.author.auth:
		status = "allowed"
	if status == "allowed":
		check = await check_dm(chat_id)
		if not check:
			chat_id = user.id+"_"+botid
			check = await check_dm(chat_id)
			if not check:
				await create_dm(ctx,chat_id,user)

		msg = f"An anonymous user sent you a message! it reads:\n\n"
		for i in args:
			msg += f"{i} "
		msg += "\n\nSend a message using /tell or an anonymous message by using /whisper"
		await chat.send("sent")
		chat.id = chat_id
		await chat.send(msg)
		return
	elif status == "subs":
		return await chat.send("That user isnt subscribed to you :(")
	else:
		return await chat.send("This user's DMs are closed.")

@bot.command(help_category="fun",help_message="Generates a random identity")
async def newid(ctx, *args):
	chat = ctx.chat
	json_data = requests.get("https://randomuser.me/api/").json()

	results = json_data["results"][0]
	name = results.get("name")
	namef = name.get("first")
	namel = name.get("last")
	gen = results.get("gender").capitalize()
	loc = results.get("location")
	city = loc.get("city")
	state = loc.get("state")
	countr = loc.get("country")
	zipp = loc.get("postcode")

	return await chat.send(f"-Heres your new identity-\n\nGender: {gen}\nName: {namef} {namel}\nCity: {city}\nState: {state}\nCountry: {countr}\nZip: {zipp}")


async def get_file(ctx,user=None,chat=None,mems=None):
	if user:
		file_src = f"D:\\iPartyBot\\user_databases\\{user.id}.json"
		try:
			with open(file_src,"r") as f:
				file = json.load(f)
				
				return file
		except:
			with open(file_src,"w") as file:
				data = {}
				data["nick"] = user.nick
				data["wallet"] = 1000
				data["past_users"] = []
				data["chance"] = 0
				data["garage"] = []
				data["clan"] = ""
				data["xp"] = 0
				data["pfp"] = False
				data["reason"] = []
				data["secret"] = ""




				json.dump(data,file,indent=1)
				cprint(("User File was Created","cyan"))
				return data



	if chat:
		file_src = f"D:\\iPartyBot\\chat_databases\\{chat.id}.json"
		try:
			with open(file_src,"r") as f:
				file = json.load(f)
				return file
		except:
			if not mems:
				mems = await chat.members()
			chat_type = chat.type
			with open(file_src,"w") as file:
				data = {}
				data["chat_id"] = chat.id
				index = 0
				data["owner"] = {}
				data["ops"] = []
				data["members"] = []
				data["nopfp"] = False
				data["lockdown"] = False
				data["title"] = chat.title
				data["disabled"] = []
				data["car"] = ""
				data["worth"] = ""

				
				for i in mems:
					user = mems[index]
					name = user.nick
					status = user.role
					is_bot = user.is_bot
					if status == 0:
						data["owner"][str(user.id)] = {}
						data["owner"][str(user.id)]["nick"] = user.nick
						data["owner"][str(user.id)]["id"] = user.id

					if status == 1:
						data["ops"].append(user.id)


					if status == 2:
						data["members"].append(user.id)
					
					index += 1
					continue


				
				data["admins"] = []
				data["mods"] = []
				
				data["type"] = chat_type
				data["banned"] = []

				json.dump(data,file,indent=1)
				cprint(("Created a Chat File","cyan"))
				
				return data
	print("help")

async def get_file_by_name(name=None):
	file_src = f"D:\\iPartyBot\\user_databases\\"+name
	with open(file_src,"r") as file:
		data = json.load(file)

	return data

async def get_file_by_id(name=None):
	file_src = f"D:\\iPartyBot\\user_databases\\{name}.json"
	with open(file_src,"r") as file:
		data = json.load(file)

	return data

async def get_chat_by_id(name=None):
	file_src = f"D:\\iPartyBot\\chat_databases\\{name}.json"
	with open(file_src,"r") as file:
		data = json.load(file)

	return data

async def get_chat_by_name(name=None):
	file_src = f"D:\\iPartyBot\\chat_databases\\"+name
	with open(file_src,"r") as file:
		data = json.load(file)

	return data

async def update_chat_by_name(data=None,user=None):
	file_src = f"D:\\iPartyBot\\chat_databases\\{user}.json"
	with open(file_src,"w") as chatfile:
		json.dump(data,chatfile,indent=1)

async def update_data_by_name(data=None,user=None):
	file_src = f"D:\\iPartyBot\\user_databases\\{user}"
	with open(file_src,"w") as chatfile:
		json.dump(data,chatfile,indent=1)

async def update_data(data=None,user=None):
	file_src = f"D:\\iPartyBot\\user_databases\\{user.id}.json"
	with open(file_src,"w") as chatfile:
		json.dump(data,chatfile,indent=1)

async def update_chat(data=None,chat=None):
	file_src = f"D:\\iPartyBot\\chat_databases\\{chat.id}.json"
	with open(file_src,"w") as chatfile:
		json.dump(data,chatfile,indent=1)

async def refresh_file(ctx,chat):
	file_src = f"D:\\iPartyBot\\chat_databases\\{chat.id}.json"
	mems = await chat.members()
	chat_type = chat.type
	with open(file_src,"r") as file:
		data = json.load(file)
		
		index = 0
		
		data["ops"] = []
		data["members"] = []
		
		for i in mems:
			user = mems[index]
			name = user.nick
			status = user.role
			is_bot = user.is_bot
			if status == 0:
				if user.id != botid:
					data["owner"] = {}
					data["owner"][str(user.id)] = {}
					data["owner"][str(user.id)]["nick"] = user.nick
					data["owner"][str(user.id)]["id"] = user.id
			if status == 1:
				data["ops"].append(user.id)
			if status == 2:
				data["members"].append(user.id)
				
			index += 1
			continue
		
		
		
		
		data["type"] = chat_type
	with open(file_src,"w") as fil:
		json.dump(data,fil,indent=1)
		cprint(("Renewed a chat file","yellow"))

async def set_owner(ctx,chat,user):
	file_src = f"D:\\iPartyBot\\chat_databases\\{chat.id}.json"
	data = await get_file(ctx,user=None,chat=ctx.chat)
	data["owner"][str(user.id)] = {}
	data["owner"][str(user.id)]["nick"] = user.nick
	data["owner"][str(user.id)]["id"] = user.id
	admins = data["admins"]
	if user.id not in admins:
		admins.append(user.id)
	data["admins"] = admins
	with open(file_src,"w") as file:
		json.dump(data,file,indent=1)

async def create_bearer(key=None,bearer=None):
	headers = {
	'Host': 'identitytoolkit.googleapis.com',
	'Content-Length': '848',
	'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="98"',
	'X-Client-Version': 'Chrome/JsCore/9.1.2/FirebaseCore-web',
	'Sec-Ch-Ua-Mobile': '?0',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
	'Sec-Ch-Ua-Platform': '"Windows"',
	'Accept': '*/*',
	'Origin': 'https://app.wombo.art',
	'Sec-Fetch-Site': 'cross-site',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9',
		}

	params = (
		('key', key),
	)
	
	json_data = {
		'idToken': bearer,
	}
	
	response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:lookup', headers=headers, params=params, json=json_data).json()
	print(response)
	return

rtoken = "AIwUaOmR_IKRbXIbLNBJ6cxT3HhcI5tB1FsfNrXSqyD6oLsFnJ9iwoMgOhQCuY8e1BJIaaX0Mw-i948zI8NwUoIbmNfzN9vq9ONK5GhIHtXt3K-Ma9shtdwyk7BFHeTWmxV-LyZwqhZtcUo_8vmsa26qLmsKK5BfhCCDwaF0avfWv-yMAYXiZAc"

async def refresh_token():
	headers = {
	'Host': 'securetoken.googleapis.com',
	'Content-Length': '222',
	'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="98"',
	'Content-Type': 'application/x-www-form-urlencoded',
	'X-Client-Version': 'Chrome/JsCore/9.1.2/FirebaseCore-web',
	'Sec-Ch-Ua-Mobile': '?0',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
	'Sec-Ch-Ua-Platform': '"Windows"',
	'Accept': '*/*',
	'Origin': 'https://app.wombo.art',
	'Sec-Fetch-Site': 'cross-site',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': 'https://app.wombo.art/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9',
}
	key = "AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw"
	params = (
	('key', f'{key}'),
	)

	data = f'grant_type=refresh_token&refresh_token={rtoken}'

	response = requests.post('https://securetoken.googleapis.com/v1/token?key=AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw', headers=headers, data=data)
	bearer = response["access_token"]
	data = {}
	data['bearer'] = bearer
	with open("wbearer.json","w") as f:
		json.dump(data,f,indent=1)
	print(response)


async def startup(token=None):
	headers = {
		'Host': 'identitytoolkit.googleapis.com',
		'Content-Length': '848',
		'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="98"',
		'X-Client-Version': 'Chrome/JsCore/9.1.2/FirebaseCore-web',
		'Sec-Ch-Ua-Mobile': '?0',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
		'Sec-Ch-Ua-Platform': '"Windows"',
		'Accept': '*/*',
		'Origin': 'https://app.wombo.art',
		'Sec-Fetch-Site': 'cross-site',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.9',
	}

	params = (
		('key', 'AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw'),
	)

	json_data = {
		'idToken': token }

	response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:lookup', headers=headers, params=params, json=json_data)
	print(response.json())

member_request_ids = {}
member_list_queues = {}

async def get_members(chat_id):
		request_id = int(time.time()*1000)
		member_request_ids[request_id] = chat_id
		member_list_queues[chat_id] = asyncio.Queue()
		await bot.buff.send_ifunny_ws(await bot.buff.form_ifunny_frame({"type": "list_members", "chat_id": chat_id, "request_id": request_id}))
		
		try:
			member_list = await asyncio.wait_for(member_list_queues[chat_id].get(), 3)
		except asyncio.TimeoutError:
			member_list = []
			
		del member_list_queues[chat_id]
		member_list = [User(i) for i in member_list]
		return member_list

async def other_members(chat_id):
	return await get_members(chat_id)
		

@bot.command(help_category="tools",help_message="See how long until a username gets released (Approximately)",aliases=["nr"],cooldown=15)
async def namerelease(ctx,username=None,*args):
	chat = ctx.chat
	og_id = chat.id
	user = await ctx.user(username)
	if not user:
		return await chat.send("That name is open, or it is a banned account (unsearchable)")
	
	chat_id = botid+"_"+user.id
	check = await check_dm(chat_id)
	if not check:
		chat_id = user.id+"_"+botid
		check = await check_dm(chat_id)
		if not check:
			await create_dm(ctx,chat_id,user)
	ctx.chat.id = chat_id
	mems = await chat.members()
	ctx.chat.id = og_id
	for i in mems:
		if i.id == user.id:
			timer = i.status
			timer = str(timer)
			timer = int(timer[:10])
			if timer == 0:
				return await chat.send("That user is currently online. Good luck trying to get this username")
			added = timer + 31556926
			subbed = added - round(time.time())
			sex = seconds_to_str(subbed)
			return await chat.send(f"There is {sex} until this name is released")
				





@bot.command(hide_help=True,developer=True)
async def wombo(ctx,number=None,*args):
	chat = ctx.chat
	with open("wbearer.json","r") as f:
		data = json.load(f)
	wtoken = data["bearer"]
	await startup(wtoken)
	if not number:
		return
	if not args:
		return
	q = ""
	for i in args:
		q += i
	# 3 = None, 1 = Synthwave, 2 = Ukiyoe, 4 = Steampunk, 5 = Fantasy Art, 6 = Vibrant, 7 = HD, 8 = Pastel, 9 = Psychic, 10 = Dark Fantasy, 12 = Christmas, 11 = Mystical, 18 = Rose Gold
	# 17 = Providence, 16 = Watercolor, 15 = S Dali, 14= Etching, 13 = Baroque, 20 = Blacklight, 19 = Moonwalker
	nums = ["3","1","2","4","5","6","7","8","9","10","11","12","18","17","16","15","14","13","20","19"]
	if number not in nums:
		return await chat.send("Usage: /wombo (selection[num]) (query)\n\n1: Synthwave\n2: Ukiyoe\n3: No Effect\n4: Steampunk\n5: Fantasy\n6: Vibrant\n7: HD\n8: Pastel\n9: Psychic\n10: Dark Fantasy\n11: Mystical\n12: Christmas\n13: Barogue\n14: Etching\n15: S. Dali\n16: Watercolor\n17: Providence\n18: Rose Gold\n19:Moonwalker\n20: Blacklight")
	



	# Making the initial request
	timenow = round(time.time())

	cookies = {
	'_ga': f'GA1.1.306116653.{timenow}',
	'_ga_BRH9PT4RKM': f'GS1.1.{timenow-1}.1.1.{timenow+175}.0',
	}



	headers = {
	'Host': 'app.wombo.art',
	'Content-Length': '69',
	'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="98"',
	'Authorization': f'bearer {wtoken}',
	'Content-Type': 'text/plain;charset=UTF-8',
	'Sec-Ch-Ua-Mobile': '?0',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
	'Sec-Ch-Ua-Platform': '"Windows"',
	'Accept': '*/*',
	'Origin': 'https://app.wombo.art',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': 'https://app.wombo.art/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9',
	}

	data = '{"premium":false}'
	index = 1
	while True:
		index += 1
		if index > 4:
			return await chat.send("Something went wrong.")
		try:
			response = requests.post('https://app.wombo.art/api/tasks', headers=headers, cookies=cookies, data=data).json()
			postid = response["id"]
			break
		except:
			
			await refresh_token()
			continue
	await chat.send("Please wait...")


	data = '{"input_spec":{"prompt":'+f"\"{q}\""+',"style":'+number+',"display_freq":10}}'
	
	response = requests.put('https://app.wombo.art/api/tasks/'+postid, headers=headers, cookies=cookies, data=data)

	while True:
		await asyncio.sleep(1)
		headers = {
			'Host': 'app.wombo.art',
			'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="98"',
			'Authorization': f'bearer {wtoken}',
			'Sec-Ch-Ua-Mobile': '?0',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
			'Sec-Ch-Ua-Platform': '"Windows"',
			'Accept': '*/*',
			'Sec-Fetch-Site': 'same-origin',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Dest': 'empty',
			'Referer': 'https://app.wombo.art/',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9',
		}
		try:
			r = requests.get('https://app.wombo.art/api/tasks/'+postid, headers=headers, cookies=cookies).json()
			
			state = r["state"]
		except:
			await refresh_token()
			await asyncio.sleep(1)
			with open("wbearer.json","r") as f:
				data = json.load(f)
			wtoken = data["bearer"]
			return await chat.send("Something went wrong! try it again later.")

		if state != "completed":
			continue
		url = r.get("result")
		url = url["final"]
		break
	url = urlopen(url)
	await chat.send("Generated!")
	await upload(chat_id=chat.id,data=url)


@bot.command(help_category="minecraft",help_message="Get the inv link for the minecraft server Discord.")
async def discord(ctx,username = None,*args):
	chat = ctx.chat
	if not username:
		if chat.type == 1:
			return await chat.send("https://discord.gg/Zd8PMc3Hu4")
		await chat.send("Do this in dms to get the direct link, or just copy this code:")
		return await chat.send("Zd8PMc3Hu4")
	user = await ctx.user(username)
	if not user:
		return await chat.send("That user doesnt exist!")
	data = await get_file(ctx,user=user)
	if not data.get("discord"):
		return await chat.send("This user isn't linked to discord")
	privacy = data.get("show_discord")
	if privacy == True:
		await chat.send(f"{data['discord_name']}")
	else:
		return await chat.send("This user's discord is private!")

@bot.command(help_category="discord",help_message="Sets the privacy of other users being able to see your discord tag. (e.g. iPartyBot#3829)\n\nBy default this setting is turned off")
async def privacy(ctx,*args):
	chat = ctx.chat
	user = ctx.message.author
	data = await get_file(ctx,user=user)
	if not data["discord"]:
		return await chat.send("You aren't linked to discord yet!")
	privacy = data.get("show_discord")
	if not privacy:
		data["show_discord"] = True
		p = "public"
	elif privacy:
		data["show_discord"] = False
		p = "private"
	await update_data(data,user)
	return await chat.send(f"Your privacy was updated, it is now {p}")
	

@bot.command(hide_help=True)
async def dms(ctx,username=None,username2=None,*args):
	chat = ctx.chat
	if username2:
		user1 = await ctx.user(username)
		if not user1:
			return await chat.send("The first user doesnt exist")
		user2 = await ctx.user(username2)
		if not user2:
			return await chat.send("The second user doesnt exist")
		await chat.send(f"https://ifunny.co/c/{user2.id}_{user1.id}")
		return await chat.send(f"https://ifunny.co/c/{user1.id}_{user2.id}")
	if not username:
		return await chat.send("Input a user")
	user1 = ctx.message.author
	user2 = await ctx.user(username)
	if not user2:
		return await chat.send("That user doesnt exist.")
	await chat.send(f"https://ifunny.co/c/{user1.id}_{user2.id}")
	return await chat.send(f"https://ifunny.co/c/{user2.id}_{user1.id}")

async def set_owner(ctx,chat,user):
	file_src = f"D:\\iPartyBot\\chat_databases\\{chat.id}.json"
	data = await get_file(ctx,user=None,chat=ctx.chat)
	data["owner"][str(user.id)] = {}
	data["owner"][str(user.id)]["nick"] = user.nick
	data["owner"][str(user.id)]["id"] = user.id
	admins = data["admins"]
	if user.id not in admins:
		admins.append(user.id)
	data["admins"] = admins
	with open(file_src,"w") as file:
		json.dump(data,file,indent=1)




@bot.command(hide_help=True)
async def capri(ctx,*args):
	chat = ctx.chat
	return await chat.send("Coding's good friend :)")

@bot.command(hide_help=True)
async def braxus(ctx,*args):
	chat = ctx.chat
	return await chat.send("Bots brokest homie D:")

@bot.command(aliases=["purplecrewmate","purplecrew"],hide_help=True)
async def purple(ctx,*args):
	chat = ctx.chat
	message = ctx.message
	choices = random.choice(["blue","purple","red","green","yellow"])
	await chat.send(f"The first person to say \"{choices}\" gets a kiss!")
	while message := await chat.input(type=iFunny.Message):
		if isinstance(message, iFunny.Message):
			if message.text.lower() == choices:
				return await chat.send(f"{message.author.name} gets a kiss! mwah <3")

@bot.command(hide_help=True,aliases=["fae","lilfae"])
async def sillylilfae(ctx,*args):
	chat = ctx.chat
	choice = ["💎","😽","💚","🧚‍♀️","✨"]
	emoji_list = []
	for i in range(1,4):
		count = len(choice) - 1
		index = randint(0,count)
		emoji = choice.pop(index)
		emoji_list.append(emoji)

	await chat.send(f"Guess what emoji i chose! The choices are:\n\n{emoji_list[0]},{emoji_list[1]},{emoji_list[2]}.")
	rchoice = random.choice(emoji_list)
	while message := await chat.input(type=iFunny.Message):
		if isinstance(message, iFunny.Message):
			if message.text.lower() == rchoice:
				return await chat.send(f"{message.author.name} Guessed correct! :D")

@bot.command(help_category = "cars",help_message="See the total amount of cars that are availible.")
async def countcars(ctx,*args):
	chat = ctx.chat
	cars = await get_all_cars()

	make_count = len(cars["cars"]["make"])
	makes = cars["cars"]["make"]
	model_count = 0
	for i in makes:
		models = len(i['models'])
		model_count += models
	return await chat.send(f"There are {make_count} different makes and {model_count} total cars.")
async def get_alts(ctx,user):
	

	data = 'type=installation'

	bresponse = requests.put(f'https://api.ifunny.mobi/v4/users/my/blocked/{user.id}', headers=bearerheaders, data=data).json()
	if bresponse["status"] == 200:
		response = requests.get('https://api.ifunny.mobi/v4/users/my/blocked', headers=bearerheaders).json()

		items = response["data"]["users"]["items"]
		for i in items:
			alt_count = i.get("indirectly_blocked_users_count")
			if not alt_count:
				msg = f"No alts were found for {user.nick}"
			else:
				msg = f"{alt_count} alts were found for {user.nick}, however i am unable to get their usernames"
	else:
		print(bresponse)
		msg = bresponse
	bresponse = requests.delete(f'https://api.ifunny.mobi/v4/users/my/blocked/{user.id}', headers=bearerheaders, data=data).json()
	return msg

@bot.command(hide_help=True,auth=True,help_message="Find out how many alt accounts ifunny has logged for a user. Same thing as blocking all accounts and looking at your blocked list...")
async def alts(ctx,username=None,*args):
	chat = ctx.chat
	if not ctx.message.author.auth:
		return
	if not username:
		username = ctx.message.author.nick
	user = await ctx.user(username)
	msg = await get_alts(ctx,user)
	await chat.send(msg)


@bot.command(hide_help=True)
async def urban(ctx, *args):
	chat = ctx.chat
	message = ctx.message
	search = message.args
	url = "http://api.urbandictionary.com/v0/random"

	if search:
		url = f"http://api.urbandictionary.com/v0/define?term={urllib.parse.quote(search)}"
	
	r = requests.get(url)

	if not r.ok:
		await chat.send("Urban dictionary not worky")
		return

	data = r.json()
	print(data)

	if data["list"]:

		word = data["list"][0]["word"]
		definition = data["list"][0]["definition"]
		example = data["list"][0]["example"]
		final_str = f"{word}\n\n{definition}\n\n{example}"
		final_str = final_str.replace("]", "")
		final_str = final_str.replace("[", "")
		await chat.send(final_str)
	
	else:
		await chat.send("No definitions found")



@bot.command(help_category="data",help_message="Displays your wallet amount",aliases=["balance"])
async def bal(ctx, *args):
	chat = ctx.chat
	user = ctx.message.author

	

	if args:
		user = await ctx.user(args[0])

	if not user:
		return await chat.send("That username doesn't exist.")
	data = await get_file(ctx,user)

	highest = data.get("highest")
	if not highest:
		highest = 0
	wallet_amt = data["wallet"]
	if data["wallet"] > highest:
			highest = data["wallet"]
	data["highest"] = highest
	coins = data.get("coins")
	if not coins:
		coins = "ballers"

	return await chat.send(f"{user.name}'s Balance:\n${wallet_amt:,} {coins}.")

@bot.command(cooldown=1200,help_category="fun",help_message="this command lets you sell imaginary items for money.")
async def beg(ctx, *args):
	return
	final = ["first born son", "first gen ps4", "V6 charger", "weed stash", "crack pipe","broken tv","silverware","bass guitar","second born son","22 inch rimmed cavalier","virginity"]
	chat = ctx.chat
	message = ctx.message
	author = ctx.author
	user = ctx.message.author
	data = await get_file(ctx,author)



	earnings = random.randrange(400,6000)
	highest = data.get("highest")
	if not highest:
		highest = 0
	data["wallet"] += earnings
	if data["wallet"] > highest:
		highest = data["wallet"]
	data["highest"] = highest
	await update_data(data,author)
	msg = f"{author.name} sold their {random.choice(final)} for ${earnings:,}"
	return await chat.send(msg)


@bot.command(help_category="jobs",help_message="View availible jobs YOU can apply for. These lists are different for everyone and can be refreshed daily. More jobs unlock as you level up!")
async def jobs(ctx,*args):
	chat = ctx.chat
	author = ctx.message.author
	jobs = json.load(open("jobs.json","r"))

	data = await get_file(ctx,ctx.message.author)
	time_now = round(time.time())
	
	msg = "Your Available Jobs:\n\n"
	lvl = data['level']
	if data['searched'] == 0:
		data['searched'] = time_now
	
	if data['searched'] > time_now:
		print(data['searched'])
		joblist = data['listed']
	else:
		joblist = []
		data['searched'] = time_now + 43200
		while True:
			if len(joblist) >= 4:
				break
			obj = random.choice(jobs['jobs'])
			jobdata = obj['data']
			company = random.choice(jobdata['companies'])
			position = random.choice(jobdata['positions'])
			reqlevel = position['min']
			if lvl < reqlevel:
				continue
			joblist.append({"name":position['name'],"wage":position['wage'],"company":company})
			continue
	index = 1
	for i in joblist:
		w = f"${i['wage']}/hr"
		if isinstance(i['wage'],list):
			w = f"~${round((i['wage'][0]+i['wage'][1])/2)}/hr (Max: ${i['wage'][1]})."
		msg += f"{index})\nCompany: {i['company']}\nPosition: {i['name']}\nWage: {w}\n\n"
		index += 1

	data['listed'] = joblist

	await update_data(data,author)
	msg += "Use /apply [int] to get a job!\n\n"
	msg += f"{seconds_to_str(data['searched'] - time_now)} until job postings refresh."



	await chat.send(msg)


@bot.command(hide_help=True)
async def pat(ctx,username=None,*args):
	chat = ctx.chat
	return await chat.send(f"You gave {username} headpats <3")

		


@bot.command(help_category="fun", aliases=["give"], help_message="Pay another user",cooldown=60)
async def pay(ctx, username = None, amount = None, *args):    
	chat = ctx.chat
	message = ctx.message
	author = message.author
	
	if not username:
		return await chat.send("Input a user to give coins to.")
	other_user = await ctx.user(username)
	
	if not other_user:
		return await chat.send("That user doesnt exist.")
	if other_user.id == author.id:
		return
	other_name = other_user.original_nick
	if other_name == "noonaboners":
		other_name = "reginaboners"
	data = await get_file(ctx,author)
	data2 = await get_file(ctx,other_user)

	
	author_bal = data["wallet"]
	other_bal = data2["wallet"]
	if amount == None:
		await chat.send("Enter an amount to give.")
		return
	
	if amount not in ['all', 'half','random']:
		try:
			amount = int(str(amount).replace("k", "000").replace("m","000000").replace("b","000000000").replace("t","000000000000").replace("q","000000000000000"))
		except:
			await chat.send("The amount specified is not a number.")
			return
	else:
		if amount.lower() == 'all':
			amount = author_bal
		elif amount.lower() == 'half':
			amount = int(author_bal/2)
		elif amount.lower() == 'random':
			amount = randint(1,author_bal)

	amount = int(amount)

	if amount > author_bal:
		await chat.send("You cant give more than what you have.")
		return
	elif amount <= 0:
		await chat.send("You cant send negative money :/")
		return
	author_bal -= amount
	other_bal += amount
	data["wallet"] = author_bal
	data2["wallet"] = other_bal
	
	await update_data(data,author)
	await update_data(data2,other_user)
	coins = data.get("coins")
	if not coins:
		coins = "ballers"

	return await chat.send(f"You gave {amount:,} {coins} to {other_name}.")


jayson = {}

async def clearjayson():
	jayson.clear()

async def check_results(ctx,*args):
	nickname = None
	numb = 0
	won = 0
	for user_ in jayson:
		score = jayson[str(user_)]["balance"]
		if score >= 10:
			won = 1
			nickname = jayson[str(user_)]["nickname"]
			return won
		numb += 1
	
	return won
async def check_results2(ctx,*args):
	nickname = None
	numb = 0
	for user_ in jayson:
		score = jayson[str(user_)]["balance"]
		if score >= 10:
			nickname = jayson[str(user_)]["nickname"]
			return nickname
		numb += 1

	return nickname


async def open_jayson(ctx,author,*args):
	if str(author.id) in jayson:
		return False
	else:
		jayson[str(author.id)] = {}
		jayson[str(author.id)]["balance"] = 1
		jayson[str(author.id)]["nickname"] = author.nick
		json.dumps(jayson)
		return True

async def open_jayson2(ctx,author,*args):
	if str(author.id) in jayson:
		return False
	else:
		jayson[str(author.id)] = {}
		jayson[str(author.id)]["balance"] = 0
		jayson[str(author.id)]["nickname"] = author.nick
		json.dumps(jayson)
		return True


async def postquestion(ctx,questions,*args):
	chat = ctx.chat
	
	gen = len(questions)
	gen = gen -1
	gen = randint(0,gen)
	question = questions.pop(gen)
	await chat.send(f"Never have i ever...\n\n{question}")

@bot.command(hide_help=True,auth=True,help_category="maintenance",help_message="Use this if someone complains about the Never have i Ever Game not working")
async def resetnever(ctx,*args):
	chat = ctx.chat
	user = ctx.message.author
	if not user.auth:
		return
	await clearjayson()
	return await chat.send("Reset")

@bot.command(help_category="games",aliases=["nhie","never"],help_message="How to play:\nWhen a question appears, and it applies to you, just say \"i have\"\nif it doesnt apply, just ignore it. \nWhen everyone is ready for the next question, the original command runner must say \"continue\" \nThe first person to 10 loses.")
async def neverhaveiever(ctx,*args):
	chat = ctx.chat
	user = ctx.message.author
	message = ctx.message

	acresponse = ["have","i have","yep","yes","yeah","sadly","sadly i have","sadly yes"]
	if jayson != {}:
		return await chat.send("There is a game already running in a different chat, please try again later")
	
	questions = ["cheated on a partner.","gone skinny dipping.","faked sick from work","cheated on a test","marched in a protest","overdrafted my bank account","smoked a joint","played strip poker",
	"pissed in a pool.","tried hard drugs.","fallen asleep in public.","had sex in public.","given/recieved road head.","fallen asleep at work.","had a one night stand.","lied on a resume.","drunk-dialed my ex.","dropped acid.",
	"read a partner's texts.","sang in public","played a musical instrument","sent nudes","fucked in a car","got caught having sex","had anal sex","paid for sex","had a threesome","got caught masturbating","had sex in the shower","stole someones prescription drugs",
	"been or gotten someone pregnant","sucked someones toes","got suspended","came in under a minute","came from foreplay","put on a fursuit","eaten shrooms","kill an animal","smoked from a bong","made a makeshift bong","made a makeshift bowl","fucked a teacher","bit someone","had sex while intoxicated","made someone bleed from violence",
	"took viagra","been in a fight","been mentally abused","had incestrous thoughts","did lewd actions with a relative","had interracial sex","used a sex toy","caught others having sex","had period sex","drank alcohol before turning 21","had sex with the same gender",
	"gave a rimjob","been touched by someone else","kissed someone of the same sex","had a wet dream","smoked nicotine","smoked nicotine before the age of 18","had sex before the age of 18","been robbed","stolen something from a store","fucked a MILF/DILF","smoked weed","got drunk in public",
	"performed on a stage","won a talent show","got a GED or diploma","crashed a car","been in a car crash","been legally declared dead","fainted","made a reddit account\n\n(ew)","killed someone","put your cat on the mic","dyed your hair"]



	await chat.send("Never Have I Ever has started! Find out who is the worst person in this chat! do /help never if you dont know how to play.\n\nThe first question will send in 10 seconds!")
	await asyncio.sleep(10)
	await postquestion(ctx,questions)

	index = 1
	while message := await chat.input(type=iFunny.Message):
		if isinstance(message, iFunny.Message):
			if message.author.id == user.id:
				if message.text.lower() == "continue":
					await postquestion(ctx,questions)
					index += 1
					continue
			if message.text.lower() == "stop":
				await clearjayson()
				return await chat.send("The game has been ended")
			if message.text.lower() in acresponse:
				author = message.author
				if str(author.id) not in jayson:
					await open_jayson(ctx,author)
				if jayson[str(author.id)]["balance"] >= index:
					continue
				jayson[str(author.id)]["balance"] += 1
				json.dumps(jayson)
				continue
			if message.text.lower() == "score":
				author = message.author
				if str(author.id) not in jayson:
					await open_jayson2(ctx,author)
				score = jayson[str(author.id)]["balance"]
				username = jayson[str(author.id)]["nickname"]
				await chat.send(f"{username}'s score: {score}")

		check = await check_results(ctx)
		nickname = await check_results2(ctx)
		if check == 1:
			totals = {}
			ind = 1
			for ob in jayson:
				total_balance = jayson[ob]["balance"]
				totals.update({ob:total_balance}) 
				totals_2 = {k: v for k, v in sorted(totals.items(), key=lambda item: item[1])}

			msg = f"{nickname} is the worst person here! shame on you.\n\nLeaderboard:\n"

			for index, ob in enumerate(reversed(totals_2)):
				
				name = jayson[ob]["nickname"]
				balance = totals_2[ob]

				msg += f"\n{ind}. {name}: {balance}"
				ind += 1
			
			await clearjayson()
			return await chat.send(msg)
					

					
@bot.command(help_category="tools",help_message="Sends the account name of a user ID")
async def whois(ctx,*args):
	chat = ctx.chat
	message = ctx.message
	
	user = await ctx.user(args[0])
	
	if not user:
		return await chat.send("This is not a user ID")

	return await chat.send(f"Username: {user.original_nick}\n\nhttps://ifunny.co/user/{user.original_nick}")

@bot.command(hide_help=True,aliases=["userid"])
async def id(ctx,username=None,*args):
	chat = ctx.chat
	if not username:
		username = ctx.message.author.nick
	try:
		if int(username):
			try:
				user = await ctx.user(username)
				return await chat.send(user.id)
			except:
				if int(username) > 50 or int(username) < 1:
					return await chat.send("Input a number 1-50")

				await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.list_messages",[],{"limit":51,"chat_name":chat.id}]))
				await asyncio.sleep(1)
				chats = ws_client.chat_frames
				print(len(chats[0]))
				data = chats[0][int(username)]
				user = data.get("user")
				user_id = user.get("id")
				return await chat.send(user_id)
	except:
		user = await ctx.user(username)
		if not user:
			return await chat.send("That user doesnt exist!")
		return await chat.send(user.id)


@bot.command(hide_help=True)
async def bed(ctx,*args):
	chat = ctx.chat
	return await chat.send("You went to bed! gn :3")

@bot.command(help_category="tools",help_message="Sends the cover of the user you specify")
async def cover(ctx,*args):
	chat = ctx.chat
	message = ctx.message
	author = message.author
	if not args:
		other_user = await ctx.user(author.nick)
	if args:
		other_user = await ctx.user(args[0])
	if not other_user:
		return await chat.send("That user doesnt exist.")
	
	cover = other_user.cover
	if not cover:
		return await chat.send("That user doesnt have a cover photo.")
	cover = urlopen(cover)
	try:
		await upload(chat.id,cover)
	except:
		return await chat.send("Error uploading image")


async def get_days(t):
	time_now = round(time.time())
	f = round((time_now - int(t))/86400)
	return f

@bot.command(help_category="tools",help_message="Sends basic info about a user")
async def bio(ctx,*args):
	chat = ctx.chat
	author = ctx.message.author
	if args:
		other_user = await ctx.user(args[0])
	else:
		other_user = await ctx.user(author.nick)
	if not other_user:
		return await chat.send("Put in an actual username")
	data = await get_file(ctx,user=other_user)
	num = other_user.num
	meme = other_user.meme_experience
	days = meme.get("days")
	rank = meme.get("rank")
	bio = other_user.bio
	chat_p = other_user.privacy
	bans = other_user.bans
	verified = other_user.verified
	banned = other_user.banned
	deleted = other_user.deleted
	sub_to = num.get("subscriptions")
	subs = num.get("subscribers")
	posts = num.get("total_posts")
	original = num.get("created")
	featured = num.get("featured")
	smiles = num.get("total_smiles")
	repubs = posts + featured
	original2 = original + featured
	met_me = data.get("metme")
	if met_me:
		days_ago = await get_days(met_me)
		if days_ago < 1:
			days_ago = -100
	if not met_me:
		days_ago = 0

	xp = data.get("xp")
	lvl = data.get("level")

	
	list = ctx.bot.blacklist()
	if other_user.id not in list:
		blacklisted = "False"
	else:
		blacklisted = "True"
	wallet = data["wallet"]
	coins = data.get("coins")
	if not coins:
		coins = "ballers"
	msg = f"{other_user.name}'s info:\n\n"

	if xp:
		lvl_end = (lvl * 5) + 50
		msg +=f"XP: {xp:,}/{lvl_end:,}\nLevel: {lvl:,}\n"

	if days_ago:
		if days_ago == 1:
			msg += f"Met Me: {days_ago} day ago\n"
		elif days_ago != -100:
			msg += f"Met Me: {days_ago} days ago\n"
		else:
			msg += "Met Me: Less than a day ago\n"
	
	msg += f"Days: {days:,}\nRank: {rank}\nBio: {bio}\nChat Privacy: {chat_p}\nBans: {len(bans)}\nVerified: {verified}\nBanned: {banned}\nAccount Deleted: {deleted}\nSubscriptions: {sub_to:,}\nSubscribers: {subs:,}\nTotal Posts: {posts+featured:,}\nOriginal Posts: {original+featured:,}\nRepubs: {repubs-original2:,}\nFeatures: {featured:,}\nSmiles Earned: {smiles:,}\nBalance: ${wallet:,} {coins}\nBlacklisted: {blacklisted}"
	data = await get_file(ctx,other_user)
	if data["reason"] != []:
		if len(data["reason"]) >=1:
			reasons = data["reason"]
			msg += f"\nReason for blacklist:"
			index = 0
			for i in reasons:
				message = reasons[index]
				index += 1
				msg += f"{message}, "
				if index >= len(reasons):
					break

	return await chat.send(msg)

@bot.command(help_category="tools",help_message="Invites a user to the chat!",aliases=["summon","inv","invite"])
async def add(ctx,username=None,*args):
	chat = ctx.chat
	chat_type = chat.type
	if chat_type == 1:
		return await chat.send("You cant invite users to a dm.")
	user = ctx.message.author
	if not username:
		return
	user2 = await ctx.user(username)
	if not user2:
		return await chat.send("That user doesnt exist")
	if await chat.has_member(user2):
		return await chat.send("That user is already in the chat")
	status = await chat_invite_check(ctx,user,user2)
	if ctx.message.author.nick == "Scripts":
		status = "allowed"
	if status == "allowed":
		# await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.invite.invite",[],{"users":[f"{user2.id}"],"chat_name":f"{chat.id}"}]))
		await chat.invite(user2)
		return await chat.send(f"{user2.nick} has been invited to the chat")
	elif status == "subs":
		return await chat.send("That user isnt subscribed to you :(")
	else:
		return await chat.send("This user's DMs are closed.")

	
async def chat_invite_check(ctx,user=None,user2=None):

	headers = {
	'Host': 'api.ifunny.mobi',
	'Applicationstate': '1',
	'Accept': 'video/mp4, image/jpeg',
	'Accept-Encoding': 'gzip, deflate',
	'Ifunny-Project-Id': 'iFunny',
	'User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)',
	'Accept-Language': 'en-US;q=1',
	'Authorization': 'Bearer '+bearer,
}

	params = (
		('limit', '100'),
	)

	privacy = requests.get(f"https://api.ifunny.mobi/v4/users/{user2.id}",headers=basicheaders)
	status = privacy.json()
	status = status["data"]["messaging_privacy_status"]
	if status == "public":
		return "allowed"
	if status == "closed":
		return "closed"

	response = requests.get(f'https://api.ifunny.mobi/v4/users/{user2.id}/subscriptions', headers=basicheaders, params=params)
	
	data = response.json()
	data = data["data"]["users"]["items"]
	booley = 0
	index = 0
	for i in data:

		userid = data[index]["id"]
		if userid == user.id:
			booley += 1
			break
		index += 1
		continue
	if booley >= 1:
		return "allowed"
	else:
		return "subs"
	
invite_manager = {}



@bot.event()
async def user_kick(ctx):
	chat = ctx.chat
	user = ctx.user
	data = await get_file(ctx,user)
	if user.auth:
		c = invite_manager.get(chat.id)
		if c:
			ids = invite_manager[chat.id]
			if user.id in ids:
				return
			ids.append(user.id)
			invite_manager[chat.id] = ids
		
			await chat.invite(user)
		else:
			I = []
			I.append(user.id)
			invite_manager[chat.id] = I
			await chat.invite(user)

@bot.event()
async def user_leave(ctx):
	chat = ctx.chat
	user = ctx.user
	data = await get_file(ctx,user=None,chat=ctx.chat)
	ownername = None
	if data['owner'] != []:
		for i in data["owner"]:
			ownername = data["owner"][i]["id"]
	mems = await chat.members()
	index=0
	for i in mems:
		chatuser = mems[index]
		status = chatuser.role
		if chatuser.id == ownername:
			break
		if status == 0:
			if chatuser.id == botid:
				break
			await refresh_file(ctx,chat)
			break
		index += 1
		continue
	if user.id == ownername:
		if chat.role == 0:
			await chat.invite(user)
			await set_owner(ctx,chat,user)
	if not ownername:
		print(f"No owner found in {data['title']}")
	data = await get_file(ctx,user=user)
	if user.auth:
		await chat.invite(user)

@bot.command(help_category = "admin",help_message="Makes it to where users are discouraged from sending images to private chats. If a user sends an image while this is enabled, they will be banned and it is up to an admin to unban the user.")
async def protek(ctx,*args):
	chat = ctx.chat
	user = ctx.message.author
	data = await get_file(ctx,user=None,chat=chat)

	if chat.type == 1 or chat.type == 3:
		return await chat.send("This not a private group chat.")
	
	if user.id not in data["admins"]:
		return await chat.send("You are not an admin")
	
	status = chat.bot_role
	if status != 0:
		return await chat.send("This feature will not work unless i am admin of the chat.")
	protek = data.get("protekmode")
	if not protek:
		protek = False
	if protek == True:
		data["protekmode"] = False
		await chat.send("This Chat is UnProtek :c\n\n(This command is toggle-able, run it again to enable.)")
		return await update_chat(data=data,chat=chat)
	if protek == False:
		data["protekmode"] = True
		await chat.send("This Chat is Protek :3\n\n(This command is toggle-able, run it again to disable.)")
		return await update_chat(data,chat)


@bot.event()
async def on_file(ctx):
	chat = ctx.chat
	file = ctx.message
	user = ctx.message.author

	if chat.type == 1:
		return

	data = await get_file(ctx,user=None,chat=chat)
	
	if user.nick.lower() in bots:
		return

	if user.id not in data["admins"] and user.id not in data["mods"]:
		if data.get("protekmode") == True:
			await kick_user(ctx,chat,user)
			await chat.send("This Chat is Protek :3")
			bans = data["banned"]
			if user.id not in bans:
				bans.append(user.id)
			data["banned"] = bans
			await update_chat(data,chat)


		
		
		
@bot.event()
async def user_join(ctx):
	chat = ctx.chat
	user = ctx.user

	data = await get_file(ctx,user=None,chat = chat)
	ownername = None
	for i in data["owner"]:
		try:
			ownername = data["owner"][i]["id"]
		except:
			ownername = None
	if not ownername:
		return
	if user.id == ownername:
		if chat.type == 3:
			await asyncio.sleep(2)
			return await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.register_operators",[],{"chat_name":f"{chat.id}","operator_ids":[f"{user.id}"]}]))
	
	if user.nick.lower() == "homophobic":
		return await kick_user(ctx,chat,user)

	if user.id in data["banned"]:
		return await kick_user(ctx,chat=chat,user=user)
	lockdown = data['lockdown']
	antibot = data.get("antibot")
	if lockdown == True:
		if user.id not in data["admins"] and user.id not in data["mods"]:
			return await kick_user(ctx,chat=chat,user=user)

	if not antibot:
		data["antibot"] = False
		await update_chat(data,chat)
	if antibot == True:
		with open("bot_list.json","r") as f:
			bots_l = json.load(f)
		if user.id in bots_l:
			await kick_user(ctx,chat,user)
			return await chat.send(f"{user.nick} was kicked by Anti-Bot.")
	nopfp = data["nopfp"]
	pfp = user.pfp
	if nopfp == True:
		if not pfp:
			if user.id not in data["admins"] and user.id not in data["mods"]:
				return await kick_user(ctx,chat=chat,user=user)
	if data.get("welcome"):
		if user.nick.lower() not in bots:
			user_data = await get_file(ctx,ctx.user)
			nickname = ctx.user.nick
			font = user_data.get("font")
			if font:
				str_to_send = f"{font} {nickname}"
				nickname = await encode_special(str_to_send)
			text = data["welcome"]
			text = text.replace(f"%user",f"{nickname}")
			await chat.send(text)

	data = await get_file(ctx,user=None,chat=ctx.chat)
	for i in data["owner"]:
		ownername = data["owner"][i]["id"]
	mems = await chat.members()
	index=0
	for i in mems:
		chatuser = mems[index]
		status = chatuser.role
		if chatuser.id == ownername:
			break
		if status == 0:
			if chatuser.id == botid:
				break
			await refresh_file(ctx,chat)
			break
		index += 1
		continue
	if user.id == ownername:
		if chat.role == 0:
			await set_owner(ctx,chat,user)
	return

async def update_xp(data,clan):
	file_src = f"D:\\iPartyBot\\clans\\{clan}.json"
	with open(file_src,"w") as file:
		json.dump(data,file,indent=1)

async def add_xp(data,lvl_end):
	clan = data.get("clan")
	lvl = data.get("level")
	if not lvl:
		lvl = 1
	if not clan:
		return
	
	data = await get_clan(clan)
	if not data:
		return
	clanxp = data["xp"] + (5*lvl) +50
	data["xp"] = clanxp
	await update_xp(data,clan)


async def level_up(author,xp,level,data):
	
	

	while True:
		lvl_end = (level * 5) + 50
		if data["xp"] >= lvl_end:
			data["xp"] -= lvl_end
			data["level"] += 1
			level += 1
			xp -= lvl_end
			await add_xp(data,lvl_end)
			continue
		else:
			break
		
	if level >= 10 and level <= 24:
		data["font_access"] = True
		data["font_list"] = [r"%bold",r"%italic_bold",r"%italic"]
		if not data.get("font"):
			data["font"] = r"%italic_bold"
	elif level >= 25 and level <= 74:
		data["font_access"] = True
		data["font_list"] = [r"%bold",r"%italic_bold",r"%italic",r"%gothic",r"%gothic_bold",r"%fancy",r"%fancy_bold"]
		if not data.get("font"):
			data["font"] = r"%gothic_bold"
	elif level >= 75 and level <= 174:
		data["font_access"] = True
		data["font_list"] = [r"%bold",r"%italic_bold",r"%italic",r"%gothic",r"%gothic_bold",r"%fancy",r"%fancy_bold",r"%funky",r"%boxed",r"%emoji",r"%bubble",r"%smooth"]
		if not data.get("font"):
			data["font"] = r"%emoji"
	elif level > 175:
		data["font_access"] = True
		data["font_list"] = [r"%bold",r"%italic_bold",r"%italic",r"%gothic",r"%gothic_bold",r"%fancy",r"%fancy_bold",r"%funky",r"%boxed",r"%emoji",r"%bubble",r"%smooth",r"%outline"]
		if not data.get("font"):
			data["font"] = r"%outline"
	else:
		data["font_access"] = False
		data["font_list"] = []
		data["font"] = None
		
	await update_data(data,author)

@bot.command(help_category="fonts",help_message="Set the font your username will show up as using rainbot.\n\nUsage: /setfont (%font_name)")
async def setfont(ctx,font_num=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	data = await get_file(ctx,author)

	msg = "Usage: /setfont [index]\n\nYour available fonts:\n\n"
	fonts = data.get("font_list")
	if not fonts:
		return await chat.send("You must reach level 10 to unlock your first fonts!")
	access = data.get("font_access")
	if not access:
		return await chat.send("You must reach level 10 to unlock your first fonts!")
	index = 1
	for i in fonts:
		str_to_send = f"{i} {author.name}"
		string = await encode_special(str_to_send)
		msg += f"{index}: {string}\n"
		index += 1

	level = data["level"]
	if level >= 10 and level <= 24:
		nxt = "25"
	if level >= 25 and level <= 74:
		nxt = "75"
	if level >= 75 and level <= 174:
		nxt = "175"
	if level <= 174:
		msg += f"\nYou unlock more fonts at lvl {nxt}."

	if not font_num:
		return await chat.send(msg)
	
	count = len(fonts)
	if not font_num.isdigit():
		return await chat.send(msg)
	font_num = int(font_num)
	if font_num <= 0 or font_num > count:
		return await chat.send(msg)
	data["font"] = fonts[font_num-1]
	await update_data(data,author)
	the_font = fonts[font_num-1]
	str_to_send = f"{the_font} {author.name}"
	name = await encode_special(str_to_send)
	return await chat.send(f"Your font has been changed!\n\nYou name will now appear as:\n\n{name}")

@bot.command(help_category="data",help_message="See your XP and levels",aliases=["level","lvl"])
async def xp(ctx,username=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	if username:
		user = await ctx.user(username)
	if not user:
		return await chat.send("No user found.")
	data = await get_file(ctx,user=user)
	level = data.get("level")
	if not level:
		level = 1
		data['level'] = 1
	xp = data["xp"]
	lvl_end = (level * 5) + 50
	return await chat.send(f"{user.nick}'s stats:\nXP: {xp:,}/{lvl_end:,}\nLevel: {level:,}\n")



@bot.command(help_category="tools")
async def names(ctx,username=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	if username:
		user = await ctx.user(username)
		if not user:
			return await chat.send("Invalid user")
	data = await get_file(ctx,user=user)
	past_users = data["past_users"]
	if len(past_users) == 1:
		return await chat.send("That user doesnt have any past names")
	past_users.sort(reverse=True)
	msg = f"{user.nick}'s past names:\n\n"
	index = 0
	for i in past_users:
		index += 1
		msg += f"{i}\n"
		if index > 10:
			break
	return await chat.send(msg)


@bot.command(help_category="general",help_message="Redeem this every hour and get a streak going to get better rewards!")
async def hourly(ctx,*args):
	return
	chat = ctx.chat
	author = ctx.message.author
	data = await get_file(ctx,author)
	hourly = data.get("hourly")
	if not hourly:
		hourly = round(time.time()) - 50
	hourly_added = data.get("h_added")
	if not hourly_added:
		hourly_added = round(time.time()) + 10800
	streak = data.get("hstreak")
	if not streak:
		streak = 0
		data["hstreak"] = 0
	msg = ""
	time_now = round(time.time())
	if time_now > hourly_added:
		streak = 1
		data["hstreak"] = 1
		data["hourly"] = time_now + 3600
		data["h_added"] = time_now + 10800
		msg += "You lost your streak!\n"
	elif time_now < hourly_added and time_now > hourly:
		streak += 1
		data["hstreak"] += 1
		data["hourly"] = time_now + 3600
		data["h_added"] = time_now + 10800
		msg += "You redeemed your hourly!\n"
	else:
		tts = seconds_to_str(hourly - time_now)
		return await chat.send(f"You can redeem your hourly in {tts}\n\nYour streak: {streak}")

	amt = (streak * 50) + 100
	coins = data.get("coins")
	if not coins:
		coins = "coins"
	data["wallet"] += amt
	msg += f"\nYou gain: ${amt} {coins}\nYour streak : {streak}"
	await chat.send(msg)
	await update_data(data,author)


@bot.command(help_category="general",help_message="Redeem this daily and get a streak going to get better rewards!")
async def daily(ctx,*args):
	return
	chat = ctx.chat
	author = ctx.message.author
	data = await get_file(ctx,author)
	hourly = data.get("daily")
	if not hourly:
		hourly = round(time.time()) - 50
	hourly_added = data.get("d_added")
	if not hourly_added:
		hourly_added = round(time.time()) + 86400 + 10800 + 10800
	streak = data.get("dstreak")
	if not streak:
		streak = 0
		data["dstreak"] = 0
	msg = ""
	time_now = round(time.time())
	if time_now > hourly_added:
		streak = 1
		data["dstreak"] = 1
		data["daily"] = time_now + 86400
		data["d_added"] = time_now + (86400+10800+10800)
		msg += "You lost your streak!\n"
	elif time_now < hourly_added and time_now > hourly:
		streak += 1
		data["dstreak"] += 1
		data["daily"] = time_now + 86400
		data["d_added"] = time_now + (10800+86400+10800)
		msg += "You redeemed your daily!\n"
	else:
		tts = seconds_to_str(hourly - time_now)
		return await chat.send(f"You can redeem your daily in {tts}\n\nYour streak: {streak}")

	amt = (streak * 500) + 1000
	coins = data.get("coins")
	if not coins:
		coins = "coins"
	data["wallet"] += amt
	msg += f"\nYou gain: ${amt} {coins}\nYour streak : {streak}"
	await chat.send(msg)
	await update_data(data,author)



queued_bottles = []
async def filter_msg(msg):
	m = str(msg)
	l = ["fag","jew","nigg","pedo","bitch"]
	for i in l:
		m = m.replace(i,random.choice(["emu","noon","ferret"]))
	return m

@bot.command(hide_help=True,auth=True,help_category="maintenance",help_message="Get the username, Chat ID and other info about the last bottle sent in chat.")
async def bottlesrc(ctx,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return await chat.send("no")
	data = await get_file(ctx,user=None,chat=chat)
	bottle_data = data.get("bottle")
	return await chat.send(f"Bottle info for {bottle_data['message'][:20]}...\n\nUser: {bottle_data['author_nick']}\nUser ID: {bottle_data['author_id']}\nChat ID: {bottle_data['chat_id']}")

@bot.command(cooldown=60,help_category="fun",help_message="Send a bottle to another chat!\n\nTo disable the sending and recieving of bottles, just do /disable bottle")
async def bottle(ctx,*args):
	chat = ctx.chat
	if not args:
		return await chat.send("You just wasted a bottle :/")
	msg = ctx.message.args
	msg = await filter_msg(msg)
	author = ctx.message.author
	queued_bottles.append({'message':msg,'author_id':author.id,'author_nick':author.nick,'chat_id':chat.id,'replied':False})
	await chat.send("Bottle has been sent")

@bot.command(help_category="fun",help_message="Reply to a bottle that was sent!")
async def reply(ctx,*args):
	chat = ctx.chat
	og_id = chat.id
	message = ctx.message.args
	author = ctx.message.author
	data = await get_file(ctx,user=None,chat=chat)
	b = data.get("bottle")
	if not b:
		return await chat.send("There arent any bottles to reply to!")
	if data["bottle"]["replied"] == True:
		return await chat.send("There arent any bottles to reply to!")
	ctx.chat.id = data["bottle"]["chat_id"]
	msg = ctx.message.args
	msg = await filter_msg(msg)
	# ctx.chat.id = "tkkzhddnqod_jtskgndsuju_wwwmmfppzpx_mhxrsmiqtel"
	await chat.send(f"Your message \"{data['bottle']['message'][:100]}...\" recieved a reply\n\nIt reads:\n{msg}\n\nReply back with /reply")
	d = await get_chat_by_id(data["bottle"]["chat_id"])
	d["bottle"] = {'message':msg,'author_id':author.id,'author_nick':author.nick,'chat_id':og_id,'replied':False}
	await update_chat_by_name(d,data["bottle"]["chat_id"])
	data["bottle"]["replied"] = True
	ctx.chat.id = og_id
	await update_chat(data,chat)
	return await chat.send("Reply Sent!")



@bot.event()
async def on_message(ctx):
	chat = ctx.chat
	dealership = await get_dealership()
	message = ctx.message
	author = message.author
	all_cars = await get_all_cars()
	color = "blue"
	color2 = "magenta"
	if chat.type != 0:
		if queued_bottles != []:
			cdata = await get_file(ctx,user=None,chat=chat)
			data = queued_bottles[0]
			if data["chat_id"] != ctx.chat.id and "bottle" not in cdata["disabled"]:
				await chat.send(f"A bottle washed up! It reads:\n\n{data['message'][:100]}\n\nReply back with /reply")
				cdata['bottle'] = data
				queued_bottles.remove(data)
				await update_chat(cdata,chat)

	
	rargs = message.args.replace("\n","")
	if len(message.args) < 100:
		cprint((f"{chat.title}", "cyan"),(f"{chat.id}","green"),(f"{author.nick}", f"{color2}"),(f"{rargs}", f"{color}"))

	data = await get_file(ctx,user=None,chat=chat)
	messages = data.get("messages")
	title = data.get("title")
	if title != chat.title:
		data["title"] = chat.title

	if not messages:
		data["messages"] = 0
		messages = 0
	randomlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

	udata = await get_file(ctx,user=author)
	metme = udata.get("metme")
	if not metme:
		udata["metme"] = round(time.time())

	
	time_now = round(time.time())
	end_time = time_now + 30
	last_xp = udata.get("last_xp")
	if not last_xp:
		last_xp = 1
	if last_xp <= time_now:
		udata["xp"] += 1
		udata["last_xp"] = end_time
	xp = udata["xp"]
	level = udata.get("level")
	if not level:
		level = 1
		udata['level'] = 1
	
	if author.name != udata["nick"]:
		udata["nick"] = author.name
		pusers = udata["past_users"]
		if author.name not in pusers:
			pusers.append(author.name)
		udata["past_users"] = pusers
	
	await level_up(author,xp,level,udata)

	if "steal" not in data["disabled"]:
		if messages == -1:

			make_count = len(all_cars["cars"]["make"])
			index = 1
			carlist = []
			carname = []
			carmake = []
			color = await create_color()
			
			for i in randomlist:
				rnumber = random.randint(0,make_count-1)

				make_name = all_cars["cars"]["make"][rnumber]["makename"]
				model_count = len(all_cars["cars"]["make"][rnumber]["models"])
				mnumber = random.randint(0,model_count-1)
				car_name = all_cars["cars"]["make"][rnumber]["models"][mnumber]["name"]
				price = all_cars["cars"]["make"][rnumber]["models"][mnumber]["price"]
				carlist.append(price)
				carmake.append(make_name)
				carname.append(car_name)
				index += 1
				if index > 1:
					break
		
			event = [f"You're walking alone in the street and you see a {color['name'].capitalize()} {carmake[0]} {carname[0]} under a broken streetlamp...",f"You're in a casino gambling away your grandmas retirement money when the {color['name'].capitalize()} {carmake[0]} {carname[0]} on the Jackpot podium catches your eye...",f"You're dancing with the lobsters when you see a {color['name'].capitalize()} {carmake[0]} {carname[0]} in the bottom of the lake...",f"You see a newborn baby driving a {color['name'].capitalize()} {carmake[0]} {carname[0]}..."]
			await chat.send(random.choice(event)+" Use /steal to take this car")
			data["car"] = f"{carmake[0]} {carname[0]}"
			data["worth"] = carlist[0]
			data["color"] = color
			data["messages"] = 0
			data["chase"] = False
			await update_chat(data,chat)
			return

	jsontime = dealership[str('dealership')]["time"]
	currenttime = round(time.time())
	unlock = jsontime + 3600
	if currenttime > unlock:

		make_count = len(all_cars["cars"]["make"])
		index = 1
		carlist = []
		carname = []
		carmake = []
		colorlist = []

		

			
		for i in randomlist:
			rnumber = random.randint(0,make_count-1)

			make_name = all_cars["cars"]["make"][rnumber]["makename"]
			model_count = len(all_cars["cars"]["make"][rnumber]["models"])
			mnumber = random.randint(0,model_count-1)

			car_name = all_cars["cars"]["make"][rnumber]["models"][mnumber]["name"]
			price = all_cars["cars"]["make"][rnumber]["models"][mnumber]["price"]
			if car_name == "Express":
				car_name = "Express 🍬"
			color = await create_color()
			colorlist.append(color)
			carlist.append(price)
			carmake.append(make_name)
			carname.append(car_name)
			index += 1
			if index > 10:
				break
		dealership["dealership"]["dealmake"] = carmake
		dealership["dealership"]["dealmodel"] = carname
		dealership["dealership"]["dealprice"] = carlist
		dealership["dealership"]["colors"] = colorlist
		dealership["dealership"]["time"] = round(time.time())
		with open("user_cars.json","w") as file:
			json.dump(dealership, file, indent = 1)
	messages += 1
	data["messages"] = messages
	await update_chat(data,chat)









@bot.event()
async def on_join(ctx):
	chat = ctx.chat
	chat_type = chat.type
	if chat_type == 1:
		return
	await chat.send("Hello, i am RainBot! My prefix is /\nSay /help for a category list of commands!")
	# await chat.send(f"{ctx.chat.inviter.nick} invited me! \nSay {ctx.bot.prefix}help for info.")
	await get_file(ctx,user=None,chat=ctx.chat)
	return





@bot.command(hide_help=True,auth=True,help_category="userdata",help_message="See entire json data of a user. Best to use /cat for a cleaner, easier way of looking through a file.")
async def viewjson(ctx,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return
	if args:
		author = await ctx.user(args[0])
	if not author:
		return await chat.send("Invalid user")
	userdata = await get_file(ctx,author)

	return await chat.send(f"Json data:\n\n"+str(userdata))
	

@bot.command(help_catgory="fun",help_message="A community piece of art.\nUsage:\n\n/pixel (Sends the canvas)\n/pixel 75 75 {blue} or hexadecimal {#000000}) (Sets the selected pixel to selected color.)")
async def pixel(ctx,*args):
	chat = ctx.chat
	params = ctx.message.args
	path = "imaging/pixel.png"
	path_up = "imaging/pixel_upscaled.png"

	if not params:
		pic = Image.open(path)
		if pic.mode != "RGB":
			pic = pic.convert("RGB")
		pic = pic.resize((pic.size[0]*10,pic.size[1]*10),resample = Image.BOX)
		f = io.BytesIO()
		pic.save(f,"JPEG", optimize=True)
		r = await upload_pixel(chat.id,f,"image/jpeg")
		if r == "Error":
			return await chat.send("I have sent too many images recently. Please try again soon.")
		return await chat.send("Sending image")
	
	values = params.split()

	if len(values) !=3:
		return await chat.send("Specify an X and Y coordinate within the range 0-149")
	pic = Image.open(path)

	x = values[0]
	y = values[1]

	if not x.isdigit or not y.isdigit():
		return await chat.send("One of those coordinates were not a number")

	x = int(x)
	y = int(y)

	if x < 0 or x >= pic.size[0] or y < 0 or y >= pic.size[1]:
		return await chat.send("Pixels must be between 0 - 149")

	try:
		color = tuple([int(i*255) for i in matplotlib.colors.to_rgb(values[2])])
	except:
		return await chat.send("No color was found.")
	pic.putpixel((x,y),color)
	pic.save(path)
	await chat.send("Pixel was set.")




@bot.command(hide_help=True)
async def quiz(ctx,*args):
	chat = ctx.chat
	with open("D:\\iPartybot\\vids\\quiz.json","r") as file:
		quiz = json.load(file)
	count = len(quiz)-1
	choice = random.randint(0,count)
	# if ctx.message.author.nick == "Coding":
	 #   choice = count
	quiz = quiz[choice]
	mp4 = quiz["mp4"]
	answers = quiz["answers"]
	game = quiz["game"]
	console = quiz["console"]
	with open("D:\\iPartybot\\vids\\"+mp4,"rb") as video:
		try:
			await upload(chat_id=chat.id,data=video)
		except Exception as e:
			return await chat.send("An error occured. try again later.\n\nError Msg:\n"+e)
	msg = (f"Guess what game this sound effect comes from!\nHint: This game is playable on these platforms:\n")
	for i in console:
		msg += f"{i}\n"
	await chat.send(msg)
	while message := await chat.input(type=iFunny.Message):
			if isinstance(message, iFunny.Message):
				if message.text.lower() in answers:
					data = await get_file(ctx,message.author)
					points = data.get("points")
					if not points:
						points = 0
					points += 1
					data["points"] = points
					await update_data(data,message.author)
					return await chat.send(f"{message.author.nick} Guessed Right!\nThe game was {game}")


queue = 0

@bot.command(hide_help=True,auth=True,help_category="chats",help_message="Gets info based on a chat ID. Used for the /leave command to get the chat name.")
async def test(ctx,*args):
	if not ctx.message.author.auth:
		return
	chat = ctx.chat
	og_id = ctx.chat.id
	chat_id = args[0]
	if not chat_id:
		return await chat.send("No chat id provided")
	other_chat = await ctx.getchat(chat_id)
	if not other_chat:
		return await chat.send("Invalid chat id")
	other_chat_id = other_chat.name
	print("This is chat id: "+other_chat_id)
	last_msg = other_chat.last_msg
	msg_user = other_chat.last_msg.get("user")
	msg_user_id = msg_user.get("id")
	msg_user_nick = msg_user.get("nick")
	msg_text = other_chat.last_msg.get('text')
	last_msg_type = last_msg.get("type")
	if last_msg_type > 2:
		if last_msg_type == 3:
			msg_text = "User Join (Action)"
		elif last_msg_type == 4:
			msg_text = "User Leave (Action)"
	print(msg_text)
	chat.id = og_id
	return await chat.send(f"Title: {other_chat.title}\nID: {other_chat.name}\nDescription: {other_chat.description}\nUnread Messages: {other_chat.unread}\n\nLast Message Info:\nUser: {msg_user_nick}\nID: {msg_user_id}\nText: {msg_text}")




@bot.command(hide_help=True,auth=True,help_category="chats",help_message="Use this in the chat you want the bot to leave from, or supply the chat ID in rainbot auth to blacklist the chat.")
async def leave(ctx,chat_id=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return await chat.send("no")
	if chat_id:

		if chat.id == "Your Private Chat ID" or author.id == bot.developer:
			if not chat_id:
				return await chat.send("No chat id provided")
			other_chat = await ctx.getchat(chat_id)
			if not other_chat:
				return await chat.send("Invalid Chat ID")
			await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.leave_chat",[],{"chat_name":f"{chat_id}"}]))
			await chat.send(f"I have left {other_chat.title}.\n\nWould you like me to never join that chat again?")
			while message := await chat.input(type=iFunny.Message):
				if isinstance(message, iFunny.Message):
					if message.author.id == author.id:
						if message.text.lower() == "yes":
							ctx.bot.blacklistchat(chat_id)
							return await chat.send(f"Ok, I will now block invites for {other_chat.title}")
						else:
							return await chat.send("Ok, I didn't add that chat to the blacklist.")
	if chat.role != 0:
		await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.leave_chat",[],{"chat_name":f"{chat.id}"}]))

@bot.command(hide_help=True,aliases=["wlc","wlchat"],auth=True,help_category="chats",help_message="Whitelist a previously blocked chat.\nUsage: /wlchat chatid")
async def whitelistchat(ctx,chat_id=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not ctx.message.author.auth:
		return await chat.send("no")
	ochat = await ctx.getchat(chat_id)
	if not ochat:
		return await chat.send("Invalid Chat ID")
	ctx.bot.whitelistchat(chat_id)
	return await chat.send(f"I will now accept invites from {ochat.title}")

@bot.command(hide_help=True,aliases=["blc","blchat"],auth=True,help_category="chats",help_message="Blacklist a chat. This will make the bot reject invited from that chat.\nUsage: /blchat chatid")
async def blacklistchat(ctx,chat_id=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	if not ctx.message.author.auth:
		return await chat.send("no")
	if chat_id:
		ochat = await ctx.getchat(chat_id)
		
		if not ochat:
			await chat.send("Invalid chat ID, however i will add it.")
			return ctx.bot.blacklistchat(chat_id)
		title = ochat.title
		ctx.bot.blacklistchat(chat_id)
		return await chat.send(f"I will now block invites from {title}")
	list = ctx.bot.blacklistchat()
	return await chat.send(list)


bots = ["chessbot","ak40bot","cleverbot","cleverbotus","merpbot","rainbot","eyebot"]




@bot.command(help_category="tools",help_message="Find the current online members of a chat!",aliases=["online"])
async def expose(ctx,*args):
	chat = ctx.chat
	mems = await chat.members()
	msg = "Users online:\n\n"
	index = 0

	for i in range(0,len(mems)):
		user = mems[i]
		userid = user.id

		name = user.nick
		time = user.status
		if time != 0:
			continue
		if name.lower() in bots:
			continue
		data = await get_file(ctx,user=user)
		d = data.get("discord")
		if d:
			name = "👾 "+ name
		b = data.get("font")
		if b:
			name = f"{b} {name}"
			name = await encode_special(name)
		baltop = data.get("baltop")
		if baltop:
			name = f"⭐{name}"
		msg += f"{name}\n"

	
	return await chat.send(msg)


@bot.command(help_category="tools",help_message="Find out how long a member of the chat has been offline for",aliases=["lastseen"])
async def seen(ctx,*args):
	chat = ctx.chat
	mems = await chat.members()
	username = ctx.message.args.lower()
	user2 = await ctx.user(username)
	if not user2:
		return
	check = await chat.has_member(user2)
	if not check:
		return await chat.send("That user must be in this chat!")
	
	msg = ""


	for i in range(len(mems)):
		user = mems[i]
		name = user.nick
		timer = user.status
		timer = str(timer)
		timer = int(timer[:10])
		if username == name.lower():
			if timer == 0:
				msg += f"{user2.nick} is currently online"
				break
			else:
				now = round(time.time())
				times = now-timer
				timestring = seconds_to_str(times)
				msg += f"{user2.nick} was last seen {timestring} ago"
				break
		continue
	
		
	return await chat.send(msg)

@bot.command(help_category="tools",help_message="View current mods of this chat")
async def bans(ctx,*args):
	chat = ctx.chat
	data = await get_file(ctx,user=None,chat=chat)
	bans = data["banned"]
	if bans == []:
		return await chat.send("There are no banned users")
	mems = await chat.members()
	for i in data["owner"]:
		ownername = data["owner"][i]["nick"]
		ownerid = data['owner'][i]['id']
	index = 0
	names = []
	
	for i in bans:
		userid = bans[index]
		index2 = 0
		for user in mems:
			userob = mems[index2]
			if userob.id == ownerid:
				index2 += 1
				continue
			if userob.id == userid:
				names.append(userob.nick)
				bans.remove(userob.id)
			index2 += 1
			continue
		index += 1
		continue
	if bans != []:
		index = 0
		for i in bans:
			user_id = bans[index]
			if user_id == ownerid:
				index+=1
				continue
			data = await ctx.user(user_id)
			if not data:
				nick = "<Deactivated User>"
				names.append(nick)
				index += 1
				continue
			nick = data.nick
			names.append(nick)
			index += 1
			continue

	msg = f"Banned users:\n\n"

	index2 = 0

	for i in names:
		name = names[index2]
		msg += f"{name}\n"
		index2 += 1
		continue
	return await chat.send(msg)



@bot.command(help_category="tools",help_message="See what kind of bans a user has (if any)")
async def stats(ctx,*args):
	chat = ctx.chat
	other_user = await ctx.user(ctx.message.author.nick)
	stat_type = "user"
	if args:
		if "https://ifunny.co/" in args[0]:
			stat_type = "post"
		else:
			other_user = await ctx.user(args[0])
			

	if stat_type == "post":
		post = args[0]
		if "picture" in post:
			post_id = post.replace("https://ifunny.co/picture/","").replace("?s=cl","")
			content = "picture"
			ctype = 'pic'

		if "video" in post:
			post_id = post.replace("https://ifunny.co/video/","").replace("?s=cl","")
			content = "video"
			ctype = 'video_clip'

		if "gif" in post:
			post_id = post.replace("https://ifunny.co/gif/","").replace("?s=cl","")
			content = "gif"
			ctype = 'gif'
		
		response = requests.get(f'https://api.ifunny.mobi/v4/content/{post_id}', headers=bearerheaders).json()
		comments = requests.get(f'https://api.ifunny.mobi/v4/content/{post_id}/comments?state=top&limit=5', headers=bearerheaders).json()
		if response['status'] == 200:
			
			data = response['data']
			msg = ""
			pic = data[ctype]
			user = data['creator']
			num = data['num']
			sex = seconds_to_str(round(time.time())-int(data['publish_at']))
			c = None
			cont = None


			msg +=f"Stats for this {content.capitalize()}:\n\nPosted By: {user['nick']}\n\nPosted: {sex} ago"
			
			if_text = len(comments['data']['comments']['items'])
			if if_text != 0:
				c = comments['data']['comments']['items'][0]['text']
				cont = comments['data']['comments']['items'][0]['attachments']['content']

			if c or cont:
				attach = "False"
				if cont != []:
					attach = "True"
				msg += f"\n\nTop Comment: \n\"{c}\"\n    Linked Post: {attach}\n    User: {comments['data']['comments']['items'][0]['user']['nick']}"
			
			msg += f"\n\nVisibilty: {data['visibility'].capitalize()}\nFeatured: {data['is_featured']}\nLikes: {num['smiles']:,}\nDislikes: {num['unsmiles']:,}\nGuest Smiles: {num['guest_smiles']:,}\nComments: {num['comments']:,}\nViews: {num['views']:,}\nRepubs: {num['republished']:,}\nShares: {num['shares']:,}\nSize: {data['size']['w']}x{data['size']['h']}\nCan Boost: {data['can_be_boosted']}"
		else:
			return await chat.send(f"Failed to load {random.choice(['😔','😢','😳','😧'])}")
	if stat_type == "user":
		if not other_user:
			return await chat.send("Specify a user to check")
		bans = other_user.bans


		ban_count = len(bans)
		if ban_count == 0:
			return await chat.send(f"{other_user.name} has no current bans. :)")
		load = bans
		index = 0
		msg = f"{other_user.name}'s Bans\n\nAmount of bans: {ban_count}\n\n"
		for i in load:

			ban_type = load[index]['type']
			print(ban_type)
			if ban_type == "collective_shadow":
				ban_type = "New posts cannot be seen by users in collective. (Shadow Banned)"
			if ban_type == "content_creation":
				ban_type = "Unable to post content. (Content Creation)"
			if ban_type == "comment_creation":
				ban_type = "Unable to comment on posts. (Comment Creation)"
			if ban_type == "chat_access":
				ban_type = "Unable to connect to chat servers (Chat Banned)"
			if ban_type == "repubing":
				ban_type = "Unable to republish posts. (Repub Banned)"
			ban_time = load[index]['date_until']
			date_time = datetime.fromtimestamp(ban_time)
			sex = seconds_to_str(ban_time-time.time())
			msg += f"Ban Type: {ban_type}\n\nUnban Date:\n {date_time} EST\n\n{sex}\n\n"
			index+= 1
			continue
	return await chat.send(msg)

@bot.command(help_category = "admin",help_message="Purge users that have been inactive for the amount of days you specify")
async def purgesec(ctx,days=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	data = await get_file(ctx,user=None,chat=chat)
	for i in data["owner"]:
		ownername = data["owner"][i]["nick"]
		ownerid = data["owner"][i]["id"]
	if author.id != ownerid:
		return await chat.send(f"Only the chat owner ({ownername}) can use this command")
	if not days:
		return await chat.send("You must specify an amount of days!")
	if not days.isdigit():
		return await chat.send("Specify an amount of days")
	day1 = 86400
	if int(days) < 1:
		return
	#if int(days) >10:
	#	return await chat.send("The max amount of days I can count is 10!")
	if int(days) > 1:
		day1 = int(days)
	timenow = round(time.time())
	edittime = timenow - int(day1)

	mems = await chat.members()

	userstokick = []
	names = []
	for user in mems:
		last_seen = user.status
		if last_seen == 0:
			continue
		last_seen = str(last_seen)[:10]
		last_seen = int(last_seen)
		if last_seen < edittime:
			if user.id not in data["admins"] or user.id not in data["mods"]:
				userstokick.append(user.id)
				names.append(user.name)
	if len(names) == 0:
		return await chat.send(f"There are no users that have been inactive for {days} seconds")
	stops = ["stop","cancel","cancle","no"]

	await chat.send(f"This will kick {len(userstokick)} members from the chat. To view the members, say \"View\", otherwise say \"Confirm\" to kick these members or \"Cancel\" to stop the purge.")
	
	try:
		while message := await chat.input(type=iFunny.Message):
			if isinstance(message, iFunny.Message):
				if message.author.id == author.id:
					if message.text.lower() == "view":
						msg = "Users to kick:\n\n"
						for i in names:
							msg += f"{i}\n"
						await chat.send(msg)
						continue
					if message.text.lower() == "confirm":

						await chat.send("Kicking Members...")
						await asyncio.sleep(1)
						for i in userstokick:
							await kick_user_by_id(ctx,chat=chat,user=i)
						return await chat.send("Done!")
					if message.text.lower() in stops:
						return await chat.send("The purge was canceled.")
	except:
		return await chat.send("The purge was canceled due to inactivity")


@bot.command(help_category = "admin",help_message="Purge users that have been inactive for the amount of days you specify")
async def purge(ctx,days=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	data = await get_file(ctx,user=None,chat=chat)
	for i in data["owner"]:
		ownername = data["owner"][i]["nick"]
		ownerid = data["owner"][i]["id"]
	if author.id != ownerid:
		return await chat.send(f"Only the chat owner ({ownername}) can use this command")
	if not days:
		return await chat.send("You must specify an amount of days!")
	if not days.isdigit():
		return await chat.send("Specify an amount of days")
	day1 = 86400
	if int(days) < 1:
		return
	if int(days) >10:
		return await chat.send("The max amount of days I can count is 10!")
	if int(days) > 1:
		day1 = 86400*int(days)
	timenow = round(time.time())
	edittime = timenow - int(day1)

	mems = await chat.members()

	userstokick = []
	names = []
	for user in mems:
		last_seen = user.status
		if last_seen == 0:
			continue
		last_seen = str(last_seen)[:10]
		last_seen = int(last_seen)
		if last_seen < edittime:
			if user.id not in data["admins"] or user.id not in data["mods"]:
				userstokick.append(user.id)
				names.append(user.name)
	if len(names) == 0:
		return await chat.send(f"There are no users that have been inactive for {days} days")
	stops = ["stop","cancel","cancle","no"]

	await chat.send(f"This will kick {len(userstokick)} members from the chat. To view the members, say \"View\", otherwise say \"Confirm\" to kick these members or \"Cancel\" to stop the purge.")
	
	try:
		while message := await chat.input(type=iFunny.Message):
			if isinstance(message, iFunny.Message):
				if message.author.id == author.id:
					if message.text.lower() == "view":
						msg = "Users to kick:\n\n"
						for i in names:
							msg += f"{i}\n"
						await chat.send(msg)
						continue
					if message.text.lower() == "confirm":

						await chat.send("Kicking Members...")
						await asyncio.sleep(1)
						for i in userstokick:
							await kick_user_by_id(ctx,chat=chat,user=i)
						return await chat.send("Done!")
					if message.text.lower() in stops:
						return await chat.send("The purge was canceled.")
	except:
		return await chat.send("The purge was canceled due to inactivity")

@bot.command(hide_help=True)
async def device(ctx,*args):
	chat = ctx.chat
	message = ctx.message
	if not message.payload:
		await chat.send("Im not sure what device you are using. (payload is missing)")
		return
	elif "client" in message.payload:
		await chat.send("Your client was specified to be:\n\t" + message.payload["client"])
		return
	else:
		if not message.payload.get("local_id"):
			await chat.send("You are using an android device.")
			return
		elif "-" in message.payload["local_id"]:
			await chat.send("You are using an IOS Device")
			return
		elif message.payload["local_id"] == "ifunny.chat":
			await chat.send("You are using ifunny chat for web. (ifunny. chat)")
			return
		else:
			return await chat.send(f"I couldn't detect your device, but i did recieve a payload:\n\n{message.payload['local_id']}")


@bot.command(help_message="Searches Google for an image. \n\nSpecify gif to search Giphy.",help_category="images",aliases=['img','pic'])
async def image(ctx, searchh=None,*args):
	chat = ctx.chat
	message = ctx.message
	author = ctx.author
	search = message.args

	ban = ["ddlg","mdlb","nigg","slave","slavery","fuck","pussy","penis","vagina","urethra","child"]
	if str(author.id) not in str(chat.id):
		for word in ban:
			if word in message.text.lower():
				return



	if not search:
		search = searchh
	if not search:
		return await chat.send("Specify what to search")
	
	if "gif" in search.lower():
		api_key = "7g1ZvOCvAJqGHbqwJe5Q0I2rVV0Wiul2"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key, search, limit=50,rating='pg-13')
			lst = list(api_response.data)
			gif_id = random.choice(lst)
			print(gif_id.id)
			gif_url = f"https://media.giphy.com/media/{gif_id.id}/giphy.gif"
			url = urlopen(gif_url)
			await upload(chat_id=chat.id,data=url)
			
		
		except:
			return await chat.send("The GIF was too large")
			

	images = yandex_client.search(f"{search}")
	if images == []:
		return
	url = random.choice(images)
	url = urlopen(url)
	try:
		await upload(chat_id=chat.id,data=url)
	except:
		return await chat.send("Something went wrong")



@bot.command(hide_help=True)
async def check(ctx,*args):
	chat = ctx.chat
	user = ctx.message.author
	if args:
		user = await ctx.user(args[0])
	if not user:
		return await chat.send("Not a username")
	
	if not user.auth:
		return await chat.send("no")
	else:
		return await chat.send("yes")

@bot.command(hide_help=True)
async def chatid(ctx, *args):
	chat = ctx.chat
	await chat.send(ctx.chat.id)

@bot.command(developer=True,hide_help=True)
async def auth(ctx,thing1=None,*args):
	chat = ctx.chat
	message = ctx.message
	author = ctx.author

	other_user = author

	if args:
		other_user = await ctx.user(args[0])

	if not other_user:
		return await chat.send("Put in an actual username.")
	#data = await get_file(ctx,other_user)
	if thing1 == "add":
		ctx.bot.auth(other_user)
		await chat.send(f"{other_user.name} has been set as an auth")
	if thing1 == "remove":
		ctx.bot.unauth(other_user)
		await chat.send(f"{other_user.name} has been removed as an auth")
	



@bot.command(help_category="Tools",help_message="Provides the link to the chat. Pretty self explanatory")
async def chatlink(ctx, *args):
	chat = ctx.chat
	chat_id = ctx.chat.id
	message = ctx.message

	if args:
		return await chat.send(f"https://ifunny.co/c/{message.args}")
	

	await chat.send(f"https://ifunny.co/c/{ctx.chat.id}")

@bot.command(hide_help=True)
async def chattitle(ctx,*args):
	await ctx.chat.send(ctx.chat.title)


@bot.command(hide_help=True,auth=True,help_category="chats",help_message="Usage: /hop chatID\n\nWill invite you to any chat. Dont be weird.")
async def hop(ctx,*args):
	chat = ctx.chat
	chat_id = ctx.chat.id
	message = ctx.message
	author = message.author
	user = message.author
	data = await get_file(ctx,author)
	if not author.auth:
		return await chat.send("no")
	

	if args:
		if args == "ziti chat":
			message.args = "cjycstcdfen_byeaotolwbr_jryglwlaojy_idenkcciurc"
		chat.id = message.args
		await chat.invite(user)
		chat.id = chat_id
		return await chat.send("Invited!")

	else:
		return await chat.send("Specify a Chat ID")

@bot.command(hide_help=True,auth=True,help_category="chats",help_message="Make the bot say a message in a chat.\nUsage: /runin chatid hello")
async def runin(ctx,chatid=None,*args):
	chat = ctx.chat
	message = ctx.message
	author = message.author
	chat_id2 = chatid
	chat_id = chat.id
	text = message.args
	text2 = text.split(' ',1)[1]

	if not author.auth:
		return await chat.send("no")

	if not args:
		return await chat.send("Enter something to say, dummy")

	if args:
		if chat_id2.isdigit() and int(chat_id2) < 100:
			cdata = await get_file(ctx,user=None,chat=chat)
			all_chats = cdata.get("schats")
			number = int(chat_id2)
			if number <= 0 or number > len(all_chats):
				return await chat.send("invalid index")
			number = number-1
			chatobj = all_chats[number]
			chat_id2 = chatobj["chatid"]
		if chat_id2.lower() == "ziti":
			chat_id2 = "cjycstcdfen_byeaotolwbr_jryglwlaojy_idenkcciurc"
		
		
	ctx.chat.id = chat_id2
	if function := bot.commands.get(args[0].lower()):
		alist = ctx.message.args_list
		alist.pop(0)
		alist.pop(0)
		ctx.message.args_list = alist
		await bot.run_command(function, ctx)
		chat.id = chat_id
		return await chat.send("Your message has been sent")
	await chat.send(f"{text2}")

	chat.id = chat_id
	return await chat.send("Your message has been sent")


@bot.command(help_message="Sends a support message")
async def support(ctx,*args):
	chat = ctx.chat
	message = ctx.message
	author = message.author
	chat_id = chat.id
	with open("support.json","r") as f:
		support = json.load(f)
	if author.id in support:
		return
	

	if args:
		chat.id = "tkkzhddnqod_jtskgndsuju_wwwmmfppzpx_mhxrsmiqtel"
		await chat.send(f"Support Requested:\nUser: {author.name}\nChat: \n\n{chat.title}\n\nChat ID:\n{chat_id}\n\nContent:\n{message.args}")

	if not args:
		chat.id = "tkkzhddnqid_jtskgndsuju_wwwmmfppzpx_mhxrsmiqtel"
		await chat.send(f"Support with no args given by {author.name} in \n\n{chat.title}\n\nChat ID:\n{chat_id}")
		chat.id = chat_id
		return await chat.send("define the issue you have. if its serious someone should be able to help you soon.")
	chat.id = chat_id

	return await chat.send("Your support message has been sent!")

@bot.command(hide_help=True,aliases = ["bl"],auth=True,help_category="userdata",help_message="Blacklist a user if they misbehave.")
async def blacklist(ctx, username=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	author = ctx.message.author
	data = await get_file(ctx,author)
	if not author.auth:
		return await chat.send("no")

	if username:
		if user.nick != "Scripts" and not args:
			return await chat.send("Add a reason after the username to blacklist this person")
	

	if user.nick == "Scripts" or args:
		user = await ctx.user(username)
		message = ctx.message.args
		message = message.replace(username,"")
		if not user:
			return await chat.send("Input a valid username")
		data = await get_file(ctx,user)
		if user.auth:
			return await chat.send("That user cannot be blacklisted")
		ctx.bot.blacklist(user)
		
		data["reason"].append(f"{message} -[{author.name}]")
		await update_data(data,user)
		return await chat.send(f"{user.nick} has been blacklisted")

	list = ctx.bot.blacklist()
	count = len(list)
	msg = f"There are {count} Blacklisted Users"

	await chat.send(msg)

@bot.command(hide_help=True,aliases = ["wl"],auth=True,help_category="userdata",help_message="Whitelist a user.")
async def whitelist(ctx, *args):
	chat = ctx.chat
	user = ctx.message.author
	if not user.auth:
		return await chat.send("no")

	if args:
		user = await ctx.user(args[0])
		ctx.bot.whitelist(user)
		return await chat.send(f"{user.nick} has been whitelisted")

@bot.command(hide_help=True,auth=True,help_category="userdata",help_message="Block a user from using the /support command. Useful for spammers. Run the command again to whitelist a user")
async def supportbl(ctx,username=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return
	user = await ctx.user(username)
	if not user:
		return await chat.send("That user doesnt exist")
	with open("support.json","r") as f:
		support = json.load(f)
	if user.id in support:
		support.remove(user.id)
		with open("support.json","w") as file:
			json.dump(support,file)
		return await chat.send(f"{user.nick} has been removed from the list.")
	support.append(user.id)
	with open("support.json","w") as file:
		json.dump(support,file)
	return await chat.send(f"{user.nick} has been added to the list.")


@bot.command(help_message="Sets a custom name for your coins",help_category="data",aliases=["setcoin"])
async def setcoins(ctx,*args):
	chat = ctx.chat
	bad = ["nigger","hitler","nigg","pedo","fag","nazi"]
	good = ["emu","noon"]
	author = ctx.message.author
	data = await get_file(ctx,user=author)
	coins = ctx.message.args.lower()
	for word in bad:
		if word in coins.lower():
			coins = coins.replace(word,random.choice(good))
	if not coins:
		coins = "ballers"
	coins = coins.replace("\n"," ")    
	data["coins"] = coins[:15]
	await update_data(data,author)
	await chat.send(f"Your coins were set to {coins[:15]}")

@bot.command(hide_help=True,auth=True,help_category="userdata",help_message="Blacklist a users PFP from showing up on the /pfp command.")
async def blpfp(ctx,username=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return await chat.send("no")
	if not username:
		return await chat.send("Input a username")
	user = await ctx.user(username)
	if not user:
		return await chat.send("That user doesn't exist.")
	idata = await get_file(ctx,user)
	if idata["pfp"] == True:
		idata["pfp"] = False
		word = "Whitelisted"
		await update_data(idata,user)
		return await chat.send(f"That user's pfp is now {word}.")
	else:
		idata["pfp"] = True
		word = "Blacklisted"
		await update_data(idata,user)
		return await chat.send(f"That user's pfp is now {word}.")

@bot.command(hide_help=True,auth=True,help_category="userdata",help_message="Whitelist a users PFP.")
async def wlpfp(ctx,username=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return await chat.send("no")
	if not username:
		return await chat.send("Input a username")
	user = await ctx.user(username)
	if not user:
		return await chat.send("That user doesn't exist.")
	idata = await get_file(ctx,user)
	idata["pfp"] = False
	await update_data(idata,user)
	return await chat.send("That user's pfp is now Whitelisted.")

async def get_code(ctx,code=None):
	file_src = f"D:\\iPartyBot\\codes\\{code}.json"
	try:
		with open(file_src,"r") as f:
			file = json.load(f)
			return file
	except:
		return None

async def get_discord(ctx,user=None):
	if user:
		file_src = f"D:\\iPartyBot\\discord_users\\{user}.json"
		try:
			with open(file_src,"r") as f:
				file = json.load(f)

				return file
		except:
			return {}

async def update_user(ctx,user,data):
	file_src = f"D:\\iPartyBot\\user_databases\\{user.id}.json"
	with open(file_src,"w") as file:
		json.dump(data,file,indent=1)


async def update_discord(ctx,user,data):
	file_src = f"D:\\iPartyBot\\discord_users\\{user}.json"
	with open(file_src,"w") as file:
		json.dump(data,file,indent=1)


async def create_code(ctx,code,user):
	file_src = f"D:\\iPartyBot\\codes\\{code}.json"

	data = {}
	data["id"] = user.id
	data["nick"] = user.nick
	with open(file_src,"w") as file:
		json.dump(data,file)


async def delete_code(ctx,code):
	filePath = f'D:\\iPartyBot\\codes\\{code}.json'

	if os.path.exists(filePath):
		os.remove(filePath)
	else:
		print("Can not delete the file as it doesn't exists")


@bot.command(help_category="discord",help_message="Link your discord to iFunny")
async def link(ctx,code = None,*args):
	chat = ctx.chat
	author = ctx.message.author
	data = await get_file(ctx,author)
	discord = data.get("discord")
	if discord:
		return await chat.send("You are already linked to discord!")
	dcode = data.get("code")
	if dcode:
		return await chat.send(f"You already have a code! It is {dcode.upper()}\n\nJoin the discord (/discord in dms) and do /link {dcode.upper()} in the bot channel.")
	if code:
		cdata = await get_code(ctx,code)
		if not cdata:
			return await chat.send("That code isnt valid. Did you mis-type?")
		ifuid = cdata["id"]
		ifname = cdata["nick"]
		if "#" not in ifname:
			return await chat.send("You must provide this code to me on Discord!")
		data = await get_file(ctx,author)
		data["discord"] = True
		data["code"] = code
		data["discord_name"] = ifname
		data["discord_id"] = ifuid
		ddata = await get_discord(ctx,author)
		ddata["ifunny"] = True
		ddata["userid"] = author.id
		ddata["username"] = author.nick
		await update_discord(ctx,ifuid,ddata)
		await update_user(ctx,author,data)
		await delete_code(ctx,code)
		return await chat.send(f"You are now linked as {ifname}")
		

	else:
		alph = ["a","b","c","d","e","f","g","h","j","k","m","n","p","q","r","s","t","u","v","w","x","y","z"]
		num = [1,2,3,4,5,6,7,8,9]
		mcode = ""
		for i in range(0,5):
			c = random.randint(1,2)
			choice = num
			if c == 1:
				choice = alph
			val = random.choice(choice)
			mcode += f"{val}"

		data["code"] = mcode
		await update_user(ctx,author,data)

		await chat.send(f"Your code is {mcode.upper()}\n\nJoin the discord, (link is sent by running the /discord command in dms), and do /link (code) in #bot-commands")
		await chat.send(f"/link {mcode.upper()}")
		await create_code(ctx,mcode,author)
			


@bot.command(help_category="tools",help_message="Display a user's profile picture",cooldown=60)
async def pfp(ctx,*args):
	chat = ctx.chat
	print(ctx.chat.id)
	author = ctx.message.author
	data = await get_file(ctx,user=author)
	if not data.get("level"):
		return await chat.send("Your level isnt high enough for this command!")
	if data["level"] < 20:
		return await chat.send("Your level isnt high enough for this command!")
	if not args:
		other_user = await ctx.user(ctx.message.author.nick)
	if args:
		other_user = await ctx.user(args[0])
	if not other_user:
		return await chat.send("That user doesnt exist")
	odata = await get_file(ctx,other_user)
	pfpcheck = odata.get("pfp")
	if not pfpcheck:
		pfpcheck = False
		odata["pfp"] = False
		await update_data(odata,other_user)
	if odata["pfp"] == True:
		return await chat.send("That user's Profile Picture is Blacklisted.")
	pfplink = other_user.pfp
	url = pfplink.get("url")
	r = urlopen(url)
	try:
		await upload(chat.id,r)
	except:
		return await chat.send("Image failed to send")
	

@bot.command(help_category="tools",help_message="Displays the chat's pfp")
async def chatpfp(ctx,*args):
	chat = ctx.chat
	cover = ctx.chat.cover
	if not cover:
		return await chat.send("This chat doesnt have a picture set!")
	r = urlopen(cover)
	try:
		await upload(chat_id=chat.id,data=r)
	except Exception as e:
		return await chat.send(e)

# @bot.command(cooldown=240)
# async def readme(ctx,*args):
#    chat = ctx.chat
#    return await chat.send("I am currently re-writing the bot to use seperate user files instead of one massive file. You should notice a faster response speed with using economy commands. Most of the original commands are unavailable at this moment but they will be ported over and rewritten to work with the new format. just give me some time.")

@bot.command(hide_help=True,auth=True)
async def auths(ctx,*args):
	chat = ctx.chat
	author = ctx.message.author
	if not author.auth:
		return await chat.send("no")
	data = ctx.bot.auth()
	alist = []
	for userid in data:
		data = await get_file_by_id(userid)
		alist.append(data["nick"])

	msg = "Gayest Users:"
	for nickname in alist:
		msg += f"\n{nickname}"
		continue
			
			
	await chat.send(f"{msg}")
	return

@bot.command(help_category="data",help_message="Display the richest users.")
async def baltop(ctx,*args):
	chat = ctx.chat
	author = ctx.message.author
	author_file = await get_file(ctx,user=author)
	x = os.listdir("./user_databases")
	
	totals = {}
	for user in x:
		print(user)
		data = await get_file_by_name(user)
		total_balance = data["wallet"]
		totals.update({user:total_balance})
	totals_2 = {k: v for k, v in sorted(totals.items(), key=lambda item: item[1])}

	msg = f"Richest Users: ({len(x):,} users)\n"
	alist = []
	total_coins = 0
	for index, user in enumerate(reversed(totals_2)):
		index += 1
		data = await get_file_by_name(user)
		name = data["nick"]
		coins = data['wallet']
		total_coins += coins
		balance = totals_2[user]
		balt = data.get("baltop")
		font = data.get("font")
		
		if data == author_file:
			print("adding index")
			alist.append({"index":index})
		if balt == True:
			data["baltop"] = False
			await update_data_by_name(data,user)
		
		if index <= 10:
			if font:
				name = await encode_special(string = f"{font} {name}")
			msg += f"\n{index}. {name}: ${balance:,}"
			data["baltop"] = True
			await update_data_by_name(data,user)
		continue
	
	if alist != []:
		msg += f"\n\n#{alist[0]['index']}. You: ${author_file['wallet']:,}"

	msg += f"\n\nTotal amount of coins: ${total_coins:,}"
	data = await get_file(ctx,user=author)
	coind = data.get("coins")
	if not coind:
		coind = "ballers"
	highest_bal = data.get("highest")
	if highest_bal:
		msg += f"\n\nHighest Recorded Balance:\n${highest_bal:,} {coind}"
			
			
	await chat.send(f"{msg}")
	return

quid = "9490"
qtoken = "xajhX1viG23kZXnd"
@bot.command(help_category="Fun",aliases=["quotes","q"],help_message="Display a random quote, or put a name after the command to search for quotes by that person. \n\nExample: /quote Benjamin Franklin")
async def quote(ctx,*args):
	chat = ctx.chat
	if args:
		message = ctx.message.args
		query = message.replace(" ","+")

		url = f"https://www.stands4.com/services/v2/quotes.php?uid={quid}&tokenid={qtoken}&searchtype=AUTHOR&query={query}&format=json"
		r = requests.get(url)
		data = json.loads(r.text)
		if data == {}:
			return await chat.send("I couldn't find any quotes from that person")
		else:
			count = data["result"]
			pick = random.randint(0,len(count))
			quote = data["result"][pick]["quote"]
			author = data["result"][pick]["author"]
			return await chat.send(f"{quote}\n\n~{author}")
	url = f"https://www.abbreviations.com/services/v2/quotes.php?uid={quid}&tokenid={qtoken}&searchtype=RANDOM&format=json"
	r = requests.get(url)
	data = json.loads(r.text)
	quote = data["result"]["quote"]
	author = data["result"]["author"]
	return await chat.send(f"{quote}\n\n~{author}")

@bot.command(hide_help=True)
async def fmk(ctx, *args):
	chat = ctx.chat
	message = ctx.message
	author = message.author
	members = await chat.members()
	member1 = random.choice(members)
	member2 = random.choice(members)
	member3 = random.choice(members)

	
		

	await chat.send(f"{author.name}\n\nYou fucked:😳💦\n{member1.name}\n\nYou married:💕💍\n{member2.name}\n\nYou killed:🔪💀\n{member3.name}")

@bot.command(help_category="general")
async def say(ctx, *args):
	"""I will repeat you"""

	chat = ctx.chat
	message = ctx.message
	text = ctx.message.args

	await chat.send(text)

@bot.command(help_category="cars",help_message="View the cars in your garage")
async def garage(ctx,page=None,username=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	if username:
		user = await ctx.user(username)
	if not user:
		return await chat.send("Couldnt find that user")
	data = await get_file(ctx,user)
	garage = data["garage"]
	count = len(garage)
	if count == 0:
		if not username:
			return await chat.send("You have no cars in your garage! Buy one from the \n/dealership or steal one when the opportunity arises")
		else:
			return await chat.send(f"{user.nick} Does not own any cars.")
	if not page or not page.isdigit():
		page = 1
	page = int(page)

	pagemax = math.ceil(count/10)
	if page > pagemax:
		if not username:
			return await chat.send("You dont have that many cars!")
		return await chat.send(f"{user.nick} doesnt have that many cars!")
	msg = f"{user.name}'s garage [{page}/{pagemax}]:\n"
	
	index2 = page*10
	index = index2 -10
	

	for i in garage:
		if index >= index2:
			break
		if index >= count:
			break
		coun = index + 1
		carobj = garage[index]
		car = carobj["name"]
		emoji = carobj["color"]["emoji"]
		msg += f"{coun}: {emoji} {car}\n"
		index += 1
		

	return await chat.send(msg)

async def get_dealership():
	with open("user_cars.json","r") as file:
		users = json.load(file)

	return users

@bot.command(help_message="View the current cars you can buy! This is paired with the /buy command.",help_category="cars")
async def dealership(ctx,*args):
	chat = ctx.chat
	user = ctx.message.author
	return
	data = await get_file(ctx,user)
	dealership = await get_dealership()
	currenttime = round(time.time())
	jsontime = dealership[str('dealership')]["time"]
	# if not ctx.author.is_developer:
	unlock = jsontime + 3600
	time_to_wait = unlock - currenttime
	remaining_time_str = seconds_to_str(time_to_wait)
		# if currenttime <= unlock:
			# return await chat.send(f"You must wait {remaining_time_str} before you can use this command again")
	randomlist = [1,2,3,4,5,6,7,8,9,10,11,12]
	msg = f"Current Inventory:\n\n"
	
	
	indexx = 0
	for i in randomlist:
		car_make = dealership[str('dealership')]['dealmake'][indexx]
		car_model = dealership[str('dealership')]['dealmodel'][indexx]
		car_price = dealership[str('dealership')]['dealprice'][indexx]
		color = dealership["dealership"]["color"][indexx]
		emoji = color['emoji']
		emoji = f"{emoji} "
		if car_price == 0:
			emoji = ""
		count = indexx + 1
		msg += f"{count}. {emoji}{car_make} {car_model}\nPrice: ${car_price:,}\n"
		indexx += 1
		if indexx == 10:
			break

	
			
	await chat.send(f"{msg}\nDealership will have new cars in {remaining_time_str}")
	return

async def get_all_cars():
	with open("car_data.json","r") as file:
		all_cars = json.load(file)

	return all_cars



@bot.command(hide_help=True,auth=True,help_category="cars",help_message="Update the dealership.")
async def ds(ctx,*args):
	chat = ctx.chat
	user = ctx.message.author
	if not user.auth:
		return
	all_cars = await get_all_cars()
	dealership = await get_dealership()
	currenttime = round(time.time())
	randomlist = [1,2,3,4,5,6,7,8,9,10,11,12]
	msg = "Updating Dealership...\n"

	if ctx.author.auth:
		make_count = len(all_cars["cars"]["make"])
		index = 1
		carlist = []
		carname = []
		carmake = []
		colors = []


			
		for i in randomlist:
			rnumber = random.randint(0,make_count-1)

			make_name = all_cars["cars"]["make"][rnumber]["makename"]
			model_count = len(all_cars["cars"]["make"][rnumber]["models"])
			mnumber = random.randint(0,model_count-1)

			car_name = all_cars["cars"]["make"][rnumber]["models"][mnumber]["name"]
			price = all_cars["cars"]["make"][rnumber]["models"][mnumber]["price"]
			color = await create_color()
			if car_name == "Express":
				car_name = "Express 🍬"
			msg += f"{index}. {color['emoji']} {car_name}\nPrice: ${price:,}\n"
			carlist.append(price)
			carmake.append(make_name)
			carname.append(car_name)
			colors.append(color)
			index += 1
			if index > 10:
				break
		dealership["dealership"]["dealmake"] = carmake
		dealership["dealership"]["dealmodel"] = carname
		dealership["dealership"]["dealprice"] = carlist
		dealership["dealership"]["color"] = colors
		dealership["dealership"]["time"] = round(time.time())
		with open("user_cars.json","w") as file:
			json.dump(dealership, file, indent = 1)
		return await chat.send(msg)




@bot.command(help_category="cars",help_message="Respray your car for $5,000!\n\nUsage: /paint (index of car) (new color)",aliases=["respray"])
async def paint(ctx,index = None,color = None,*args):
	return
	chat = ctx.chat
	author = ctx.message.author
	if not index or not index.isdigit():
		return await chat.send("Input the index of your car")
	if not color:
		return await chat.send("Choose a color to respray to!")
	colors = ["red","orange","yellow","green","blue","purple","tan","black","white"]
	if color.lower() not in colors:
		return await chat.send("Thats not an available color!\nPlease choose from Red, Orange, Yellow, Green, Blue, Purple, Tan, Black, or White")
	emojis = ["🔴","🟠","🟡","🟢","🔵","🟣","🟤","⚫","⚪"]
	color_emoji = emojis[colors.index(color.lower())]

	data = await get_file(ctx,author)
	garage = data["garage"]
	count = len(garage)
	if count == 0:
		return await chat.send("You have no cars in your garage! Buy one from the \n/dealership or steal one when the opportunity arises")
	index = int(index) - 1
	og_color = garage[index]["color"]
	if og_color["name"] == color.lower():
		return await chat.send(f"Your car is already {color.capitalize()}!")
	car_obj = garage[index]
	cdata = {}
	cdata["name"] = color.lower()
	cdata["emoji"] = color_emoji
	carname = car_obj["name"]
	await chat.send(f"Are you sure you want to respray your {carname} to {color.capitalize()} {color_emoji} for $5,000?")

	while message := await chat.input(type=iFunny.Message):
			   if isinstance(message, iFunny.Message):
				   if message.author.id == author.id:
					   if message.text.lower() == "yes":
						   bal = data["wallet"]
						   price = 5000
						   if price > bal:
							   return await chat.send(f"You do not have enough for this upgrade! Your balance is {bal:,}")
						   bal = bal - price
						   data["wallet"] = bal
						   garage.remove(car_obj)
						   car_obj["color"] = {"name":color.lower(),"emoji":color_emoji}
						   garage.insert(index,car_obj)
						   data["garage"] = garage

						   await update_data(data,author)
						   return await chat.send(f"You resprayed your car!\n\nIt is now {color_emoji}")
					   if message.text.lower() == "no":
						   return await chat.send("You didnt respray your car.")

@bot.command(help_category="cars",help_message="usage: /buy (index of car in dealership)\n\nBuy a car and put it in your /garage!")
async def buy(ctx,index=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	return
	data = await get_file(ctx,user)
	timenow = round(time.time())
	jailed = data.get("jailed")
	if not jailed:
		jailed = 0
	if timenow < jailed:
		count = jailed - timenow
		strtime = seconds_to_str(count)
		return await chat.send(f"You are still in jail! You will be released in {strtime}")
	garage = data["garage"]
	dealership = await get_dealership()
	user = ctx.message.author
	
	if not index:
		return await chat.send("Input a number from the dealership or \"upgrade\" to upgrade your garage")
	if not index.isdigit():
		# if index.lower() == "kit":
		#    kits = data.get("kit")
		#    if not kits:
		#        kits = 0
		#    price = 15000
		#    bal = data["wallet"]
		#    if price > bal:
		#        return await chat.send(f"You do not have enough for this upgrade! Your balance is ${bal:,}")
		#    if kits >= 10:
		#        return await chat.send("You have enough kits! You dont have any room to store any more on you.")
		#    bal = bal - price
		#    data["wallet"] = bal
		#    kits = kits + 1
		#    data["kit"] = kits
		#    await update_data(data,user)
		#    return await chat.send(f"You bought a kit!\nYou now have {kits} kits.\nYour balance is now ${bal:,} ")

		if index.lower() == "upgrade":
			storage = data.get("storage")
			upgraded = data.get("upgrade_status")
			if not upgraded:
				data["upgrade_status"] = 1
				upgraded = 1
			if not storage:
				storage = 10
			if storage == 10:
				price = upgraded * 1500000
			else:
				price = upgraded * 2000000
			await chat.send(f"Do you want to increase your storage to {storage + 10:,} cars for {price:,}?\n\n(send a one-word response saying yes or no)")
			while message := await chat.input(type=iFunny.Message):
				if isinstance(message, iFunny.Message):
					if message.author.id == user.id:
						if message.text.lower() == "yes":
							bal = data["wallet"]
							if price > bal:
								return await chat.send(f"You do not have enough for this upgrade! Your balance is {bal:,}")
							bal = bal - price
							data["wallet"] = bal
							data["storage"] += 10
							data["upgrade_status"] += 1
							await update_data(data,user)
							return await chat.send(f"You can now store {storage + 10:,} vehicles in your garage! Your balance is now {bal:,} ")
						if message.text.lower() == "no":
							return await chat.send("You didnt upgrade your garage.")
			
		return await chat.send("Thats not for sale! Try putting in a number?")
	i = int(index)
	if i > 10 or i < 1:
		return await chat.send("There's only 10 cars in the dealership!")
	
	count = len(garage)
	storage = data.get("storage")
	if not storage:
		data["storage"] = 10
		storage = 10

	if count >= storage:
		return await chat.send(f"You can only store {storage} vehicles in your garage!\nBuy an upgrade by doing /buy upgrade")
	index = i - 1
	author_bal = data["wallet"]
	makes = dealership['dealership']["dealmake"]
	models = dealership['dealership']["dealmodel"]
	prices = dealership['dealership']["dealprice"]
	colors = dealership['dealership']['color']
	make = makes[index]
	if make == "Sold":
		return await chat.send("Nobody touches the Invisible Boatmobile >:(\n\n(This car is sold out)")
	model = models[index]
	price = prices[index]
	color = colors[index]
	if price > author_bal:
		return await chat.send("Not enough money for that item!")

	data["wallet"] -= price
	
	dealership["dealership"]["dealmake"][index] = "Sold"
	dealership["dealership"]["dealmodel"][index] = "Out"
	dealership["dealership"]["dealprice"][index] = 0
	garage.append({"name":f"{make} {model}","price":price,"users":[user.nick],"color":color})
	data["garage"] = garage
	await update_data(data,user)
	
	with open("user_cars.json","w") as file:
		json.dump(dealership, file, indent=1)
	
	return await chat.send(f"{user.name} just bought the {color['emoji']} {make} {model} for ${price:,}!\n\nIt has been added to your garage!")

def shuffle_word(word):
	from random import shuffle
	word = list(word)
	shuffle(word)
	return ''.join(word)

@bot.command(help_category="cars",help_message="Use this command when you have a random chance of a car appearing.")
async def steal(ctx,*args):
	chat = ctx.chat
	user = ctx.message.author
	return
	if args:
		return await chat.send(f"You stole {ctx.message.args}!")
	chatdata = await get_file(ctx,user=None,chat=chat)
	if chat.type == 1:
		return await chat.send("Cant do this in DM's.")
	# if chatdata.get("chase"):
	#    return await chat.send(f"{chatdata['chaseinfo']['name']} is already attempting to steal this car!")
	car_name = chatdata["car"]
	if car_name == "None" or not car_name:
		return
		# return await chat.send(random.choice(["Now's not the right time to steal a car...","It's too busy to steal a car right now...","Bro, theres a cop right there..."]))
	from random_word import RandomWords
	rwords = RandomWords()
	while True:

		word = rwords.get_random_word(maxLength=6)
		if not word:
			continue
		break
	

	print(word)
	worth = int(chatdata["worth"])
	data = await get_file(ctx,user)
	timenow = round(time.time())
	jailed = data.get("jailed")
	if not jailed:
		jailed = 0
	if timenow < jailed:
		count = jailed - timenow
		strtime = seconds_to_str(count)
		return await chat.send(f"You are still in jail! You will be released in {strtime}")
	garage = data["garage"]
	color = chatdata["color"]
	
	count = len(data["garage"])
	storage = data.get("storage")
	if not storage:
		data["storage"] = 10
		storage = 10
	if count >= storage:
		return await chat.send(f"You can only store {storage} vehicles in your garage!")
	
	kit = data.get("kit")
	if not kit:
		kit = 0
	police = 0
	if kit >= 1:
		police = 0
		kit = kit - 1
		data["kit"] = kit
		await update_data(data,user)
	chance = random.randint(0,100)
	scramble = shuffle_word(word)
	start_time = round(time.time())
	end_time = start_time + 120
	if chance < police:
		chatdata['chase'] = True
		chatdata['chaseinfo'] = {}
		chatdata['chaseinfo']['name'] = ctx.message.author.nick

		await update_chat(chatdata,chat)

		await chat.send(f"You tried to steal the {car_name} but the police noticed you! Unscramble this word to get away:\n\n{scramble}")
		retry = 1
		try:

			while message := await chat.input(type=iFunny.Message):
				if isinstance(message, iFunny.Message):
					if message.author.id == user.id:
						if message.text.lower() == word.lower():
							break
						
						if end_time < round(time.time()):
							bal = data["wallet"]
							if int(bal) < 35000:
								if garage == []:
									data["lockdown"] = round(time.time()) + 21600
									await update_data(data,user)
									chatdata["chase"] = False
									chatdata["car"] = "None"
									chatdata["worth"] = 0
									await update_chat(chatdata,chat)

									return await chat.send(f"You got taken to jail! (You cannot steal or buy a car for 6 Hrs)")

								rcar = random.choice(garage)
								rcar_color = rcar["color"]["emoji"]
								rcar_name = rcar["name"]
								garage.remove(rcar)
								data["garage"] = garage
								chatdata["chase"] = False
								chatdata["car"] = "None"
								chatdata["worth"] = 0
								await update_chat(chatdata,chat)
								await update_data(data,user)
								return await chat.send(f"You got caught and you didnt have enough money to pay the charges, so the police took your {rcar_color} {rcar_name}!")

							bal = bal - 35000
							data["wallet"] = bal
							await update_data(data,user)
							chatdata["chase"] = False
							chatdata["car"] = "None"
							chatdata["worth"] = 0
							await update_chat(chatdata,chat)
							return await chat.send("The police caught you! You lost the car and had to pay a charge of $35,000.\n\n(maybe use a kit next time?)")
						
						elif retry <= 2:
							retry += 1

							continue
							
						else:
							bal = data["wallet"]
							if int(bal) < 35000:
								if garage == []:
									data["lockdown"] = round(time.time()) + 21600
									await update_data(data,user)
									chatdata["chase"] = False
									chatdata["car"] = "None"
									chatdata["worth"] = 0
									await update_chat(chatdata,chat)

									return await chat.send(f"You got taken to jail! (You cannot steal or buy a car for 6 Hrs)")

								rcar = random.choice(garage)
								rcar_color = rcar["color"]["emoji"]
								rcar_name = rcar["name"]
								garage.remove(rcar)
								data["garage"] = garage
								chatdata["chase"] = False
								chatdata["car"] = "None"
								chatdata["worth"] = 0
								await update_chat(chatdata,chat)
								await update_data(data,user)
								return await chat.send(f"You got caught and you didnt have enough money to pay the charges, so the police took your {rcar_color} {rcar_name}!")

							bal = bal - 35000
							data["wallet"] = bal
							await update_data(data,user)
							chatdata["chase"] = False
							chatdata["car"] = "None"
							chatdata["worth"] = 0
							await update_chat(chatdata,chat)
							return await chat.send("The police caught you! You lost the car and had to pay a charge of $35,000.\n\n(maybe use a kit next time?)")
					print("this is time 2 "+str(round(time.time())))
					if round(time.time()) > end_time:
						chatdata["chase"] = False
						await update_chat(chatdata,chat)
						return await chat.send("You took too long!")

		except:
			chatdata["chase"] = False
			await update_chat(chatdata,chat)
			return
	
	garage.append({"name":f"{car_name}","price":worth,"users":[user.nick],"color":color})
	data["garage"] = garage

	chatdata["car"] = "None"
	chatdata["worth"] = 0
	chatdata["chase"] = False

	await update_data(data,user)
	await update_chat(chatdata,chat)
	return await chat.send(f"{user.name} successfully stole the {color['emoji']} {car_name}")

#@bot.command(help_category="minecraft",help_message="View info on the bedrock server")
#async def server(ctx,console=None,*args):
#	chat = ctx.chat
#
#	if console:
#		return await chat.send("To join the server, you must either download an app on your phone called \"Bedrock Together\" or set your DNS IP in your internet settings to 173. 82. 100. 84 and 8. 8. 8. 8")
#	
#	return await chat.send("Come join the Minecraft bedrock server!\n\nIP: iFunny. ddns. net\nPORT: 25566\n\nIf youre on a console, do /server (console) for instructions on how to join an external server.")

@bot.command(hide_help=True,developer=True)
async def spawncar(ctx,cmake=None,cname=None,cprice=None,*args):
	chat = ctx.chat
	chats = await get_file(ctx,user=None,chat=chat)
	all_cars = await get_all_cars()
	
	make_count = len(all_cars["cars"]["make"])
	index = 1
	carlist = []
	carname = []
	carmake = []
	randomlist = [1]
	color = await create_color()
	
	for i in randomlist:
		rnumber = random.randint(0,make_count-1)
		make_name = all_cars["cars"]["make"][rnumber]["makename"]
		model_count = len(all_cars["cars"]["make"][rnumber]["models"])
		mnumber = random.randint(0,model_count-1)
		car_name = all_cars["cars"]["make"][rnumber]["models"][mnumber]["name"]
		price = all_cars["cars"]["make"][rnumber]["models"][mnumber]["price"]
		carlist.append(price)
		carmake.append(make_name)
		carname.append(car_name)
		index += 1
		if index > 1:
			break
	if cname:
		carlist = [f"{cprice}"]
		carname = [f"{cname}"]
		carmake = [f"{cmake}"]
	emoji = color["emoji"]

		
	event = [f"You're walking alone in the street and you see a {emoji} {carmake[0]} {carname[0]} under a broken streetlamp...",f"You're in a casino gambling away your grandmas retirement money when the {emoji} {carmake[0]} {carname[0]} on the Jackpot podium catches your eye...",f"You're dancing with the lobsters when you see a {emoji} {carmake[0]} {carname[0]} in the bottom of the lake...",f"You see a newborn baby driving a {emoji} {carmake[0]} {carname[0]}..."]
	await chat.send(random.choice(event)+" Use /steal to take this car")
	chats["car"] = f"{carmake[0]} {carname[0]}"
	chats["worth"] = carlist[0]
	chats["color"] = color
	await update_chat(chats,chat)
	return
	

@bot.command(hide_help=True)
async def jail(ctx,user=None,seconds=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	data = await get_file(ctx,user=author)
	if not author.auth:
		return
	if not user:
		return await chat.send("Put in a username\nUsage: /jail user seconds")
	if not seconds or not seconds.isdigit():
		return await chat.send("Put in a timeframe\nUsage: /jail user seconds")
	seconds = int(seconds)
	now = round(time.time())
	now = now + seconds
	other_user = await ctx.user(user)
	if not other_user:
		return await chat.send("That user doesnt exist!")
	if seconds <= 0 or seconds >= 86400:
		return await chat.send("Too much or too little time provided!")
	data2 = await get_file(ctx,user=other_user)
	data2["jailed"] = now
	await update_data(data2,other_user)
	return await chat.send(f"{other_user.nick} was jailed for {seconds_to_str(seconds)}")

@bot.command(hide_help=True)
async def convert(ctx,*args):
	chat = ctx.chat
	author = ctx.message.author
	data = await get_file(ctx,author)
	bal = data['wallet']
	garage = data['garage']
	xp = 0
	for i in garage:
		price = i['price']
		if price > 1000000:
			xp += 45
			continue
		xp += round(price/400)
		print(round(price/400))

	if bal >= 1000000000:
		xp+= 10000
	elif bal >= 10000001 and bal <= 999999999:
		xp += 7500
	elif bal <= 10000000 and bal >= 10000:
		xp += 5000
	else:
		if bal:
			xp += 1000
	if xp == 0:
		return await chat.send("You have nothing to convert!")
	await chat.send(f"Are you sure you want to convert all your ({len(garage):,}) cars and ({bal:,}) balance to {xp:,} XP?")
	while message := await chat.input(type=iFunny.Message,timeout=60):
			if isinstance(message, iFunny.Message):
				if message.author.id == author.id:
					if message.text.lower() == "yes":
						data['xp'] += xp
						data['garage'] = []
						data['wallet'] = 0
						await update_data(data,author)
						return await chat.send(f"You gained {xp:,} XP!")
					else:
						return await chat.send("ok :(")

	
@bot.command(hide_help=True)
async def getoutofbed(ctx,*args):
	return await ctx.chat.send("You got out of bed! Gm :3")



@bot.command(hide_help=True,developer=True)
async def lock(ctx,username=None,*args):
	chat = ctx.chat
	if chat.role != 0:return
	user = await ctx.user(username)
	if not user:
		return await chat.send("Misspelled")
	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.edit_chat",[],{"set":{"admin":user.id},"chat_name":chat.id,"unset":[]}]))
	await chat.send(f"{user.nick} was locked in the chat. they now cannot leave.")



@bot.command(help_message="Usage:\n/sell (index of car in your garage) (username {if selling to user}) (price {if selling to user})\n\nif not selling to a user it will sell back to dealership for 3/4ths the original price",help_category="cars")
async def sell(ctx,index=None,username=None,sellprice=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	return
	data = await get_file(ctx,user)
	timenow = round(time.time())
	jailed = data.get("jailedy")
	if not jailed:
		jailed = 0
	if timenow < jailed:
		count = jailed - timenow
		strtime = seconds_to_str(count)
		return await chat.send(f"You are still in jail! You will be released in {strtime}")
	message = ctx.message
	start = round(time.time())
	end = start + 40
	


	garage = data["garage"]
	if not index or not index.isdigit():
		return await chat.send("No such car exists... Try putting in a number?")
	count = len(data["garage"])
	
	if count == 0:
		return await chat.send("You have no cars in your garage! Buy one from the \n/dealership or steal one when the opportunity arises")

	index = int(index)
	choice = index - 1
	if index > count:
		return await chat.send("You dont have that many cars.. Check your garage.")
	car_obj = garage[choice]
	car_name = car_obj.get("name")
	car_worth = car_obj.get("price")
	users = car_obj.get("users")
	color = car_obj.get("color")

	if username:
		if not sellprice:
			return await chat.send("Specify a price!")
		
		try:
			sellprice = int(str(sellprice).replace("k", "000").replace("m","000000").replace("b","000000000").replace("t","000000000000").replace("q","000000000000000").replace("qt","0000000000000000000"))
		except:
			await chat.send("The amount specified is not a number.")
			return
		other_user = await ctx.user(username)
		if not other_user:
			return await chat.send("That user doesnt exist!")
		other_data = await get_file(ctx,other_user)
		jailed = other_data.get("jailed")
		if not jailed:
			jailed = 0
		if timenow < jailed:
			count = jailed - timenow
			strtime = seconds_to_str(count)
			return await chat.send(f"{other_user.nick} is still in jail! They will be released in {strtime}")
		other_bal = other_data["wallet"]
		other_garage = other_data["garage"]
		if not await chat.has_member(other_user):
			return await chat.send(f"{other_user.original_nick} is not in this chat!")
		sellprice = int(sellprice)
		other_bal = int(other_bal)
		if sellprice >= other_bal:
			return await chat.send(f"{other_user.original_nick} is too broke to buy this car!")
		storage = other_data.get("storage")
		if not storage:
			other_data["storage"] = 10
			storage = 10
		other_count = len(other_garage)
		if other_count >= storage:
			return await chat.send(f"{other_user.original_nick} can only store {storage} vehicles in their garage!")
		
		await chat.send(f"FINAL TRANSACTION\n\nYou are trying to sell a {color['emoji']} {car_name} to {other_user.original_nick} for ${sellprice:,}. If {other_user.original_nick} wants to accept, please type \"accept\".\nTo Stop this transaction just type \"Stop\"")
		while message := await chat.input(type=iFunny.Message):
			if isinstance(message, iFunny.Message):
				if message.author.id == other_user.id or message.author.id == user.id:
					if message.text.lower() == "stop":
						return await chat.send("The transaction was cancelled.")
				
				if message.author.id == other_user.id:
					if message.text.lower() == "accept":
						data2 = await get_file(ctx,user=user)
						garage2 = data2["garage"]
						car_obj_check = garage2[choice]
						if car_obj_check != car_obj:
							return await chat.send("This glitch doesnt work anymore")
						if other_user.nick not in users:
							users.append(other_user.nick)
						other_garage.append({"name":f"{car_name}","price":car_worth,"users":users,"color":color})
						garage.remove(car_obj)
						data["garage"] = garage
						other_data["garage"] = other_garage
						data["wallet"] += sellprice
						other_data["wallet"] -= sellprice
						await update_data(data,user)
						await update_data(other_data,other_user)
						return await chat.send("Transaction was a success!")
				if round(time.time()) > end:
					return await chat.send("You waited too long to reply to this offer. It is now closed.")
	if car_worth > 1000000:
		if data.get("supercar"):
			if round(time.time()) < data["supercar"]:
				return await chat.send(f"You've already sold a supercar today! You have {seconds_to_str(data['supercar']-round(time.time()))} left until you can sell another.")
		else:  
			data["supercar"] = round(time.time()) + 43200
			await update_data(data,user)
	newprice = car_worth * 0.75
	newprice = round(newprice)
	await chat.send(f"Are you sure you want to sell your {car_name} for ${newprice:,}?")
	while message := await chat.input(type=iFunny.Message):
			if isinstance(message, iFunny.Message):
				
				
				if message.author.id == user.id:
					if message.text.lower() == "no":
						return await chat.send("You decided not to sell your car.")
					if message.text.lower() == "yes":
						data = await get_file(ctx,user=user)
						garage = data["garage"]
						car_obj_check = garage[choice]
						if car_obj_check != car_obj:
							return await chat.send("This glitch doesnt work anymore")
						garage.remove(car_obj)
						data["garage"] = garage
						data["wallet"] += newprice
						await update_data(data,user)
						return await chat.send(f"You sold your {car_name} back to the dealership for ${newprice:,}.")
				if round(time.time()) > end:
					return await chat.send("You waited too long to reply to this offer. It is now closed.")


@bot.command(help_message="Try to roll for a 1, two 1's is a snake eye!",aliases=["se"],help_category="games")
async def snakeeye(ctx,bet=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	data = await get_file(ctx,user)
	
	if not bet:
		return await chat.send("Enter a bet amount! Minimum bet amount is 1000, max is 100,000")
	if str(bet.lower()) == "max":
		bet = 100000
	if not int(bet):
		return await chat.send("Enter a bet amount! Minimum bet amount is 1000, max is 100,000")
	bet = int(bet)
	if bet < 1000:
		return await chat.send("Your bet must be higher than 1000!")
	if bet > 100000:
		return await chat.send("Your bet must be lower than 100k!")
	wallet = data["wallet"]
	if bet > wallet:
		return await chat.send("Your bet amount is higher than your wallet!")
	d1 = "1"
	d2 = "2"
	d3 = "3"
	d4 = "4"
	d5 = "5"
	d6 = "6"
	dice = [d1,d2,d3,d4,d5,d6]
	coins = data.get("coins")
	if not coins:
		coins = "ballers"
	
	dice1 = random.choice(dice)
	dice2 = random.choice(dice)
	await chat.send("Rolling the dice...🎲🎲")
	
	msg = f"{user.nick}'s SnakeEye game\n\n"
	await asyncio.sleep(2.25)
	
	if dice1 == d1 and dice2 == d1:
		win = round(bet * 5)
		data["wallet"] = wallet + win
		msg += f"You got a snake eye! You win 5x your bet! ({round(bet*5):,})\n\n{dice1}🎲 {dice2}🎲\n\nYou now have {wallet + win:,} {coins}\n\ndo /help se for how to play"
		await chat.send(msg)
		await update_data(data,user)
		return

	if dice1 == d1 or dice2 == d1:
		win = round(bet * 1.2)
		data["wallet"] = wallet + win
		msg += f"You got one eye! You win 1.2x your bet! ({round(bet*1.2):,})\n\n{dice1}🎲 {dice2}🎲\n\nYou now have {wallet+win:,} {coins}\n\ndo /help se for how to play"
		await chat.send(msg)
		await update_data(data,user)
		return
	else:
		data["wallet"] = wallet - bet
		msg += f"You didnt get any eyes! You lost your bet!\n\n{dice1}🎲 {dice2}🎲\n\nYou now have {wallet-bet:,} {coins}\n\ndo /help se for how to play"
		await chat.send(msg)
		await update_data(data,user)
		return


@bot.command(help_category="cars",help_message="Displays the previous owners of your vehicle\n\nUsage: /carfax (index of car in garage)")
async def carfax(ctx,index=None,*args):
	chat = ctx.chat
	user = ctx.message.author
	data = await get_file(ctx,user)
	garage = data["garage"]
	if not index or not index.isdigit():
		return await chat.send("Input the index of the car")
	index = int(index)
	count = 0
	count1 = len(data["garage"])
	
	if count1 == 0:
		return await chat.send("You have no cars in your garage! Buy one from the \n/dealership or steal one when the opportunity arises")
	if index > count1:
		return await chat.send("You dont have that many cars.. Check your garage.")

	car_obj = garage[index-1]
	price = car_obj.get("price")
	car = car_obj.get("name")
	users = car_obj.get("users")
	color = car_obj.get("color")

	msg = f"Resale value of this {car} is: ${round(price*0.75):,}\n\n"

	msg += f"Color of this car: {color['name'].capitalize()} {color['emoji']}\n\n"

	msg += f"Users who previously owned this vehicle:\n"
	count2 = 1
	users = sorted(users,key=users.index,reverse=True)
	for names in users:
		msg += f"{count2}: {names}\n"
		count2 += 1
		if count2 >= 11:
			break
	
	return await chat.send(msg + "\n\n\"Show me the CARFAX!\"🦊📄")


@bot.command(aliases=["minecraft"],help_category="minecraft",help_message="Usage: /minecraft (minecraft username)\n\nGets the previous names of minecraft users and their uuid")
async def mc(ctx,username=None,*args):
	chat = ctx.chat
	if not username:
		return await chat.send("Input a minecraft username!")
	
	url = f"https://some-random-api.ml/mc?username={username}"
	r = requests.get(url)
	data = json.loads(r.text)
	if "error" in data:
		return await chat.send("That account doesnt exist")
	user = data["username"]
	uuid = data["uuid"]
	past_count = len(data["name_history"])
	index = 0
	msg = f"{user}'s Minecraft Data:\n\nuuid: {uuid}\n\nPast names count: {past_count}\n"
	if past_count == 0:
		return await chat.send(msg)
	msg += "Past Usernames:\n"
	for i in [1,2,3,4,5,6,7,8,9,10,11,2,4,2,4,3,3,5,3,4,5,3]:
		name = data["name_history"][index]["name"]
		date = data["name_history"][index]["changedToAt"]
		msg += f"{name} {date}\n"
		index += 1
		if index >= past_count:
			break
	return await chat.send(msg)

@bot.command(hide_help=True)
async def lyrics(ctx,*args):
	chat = ctx.chat
	title = ctx.message.args
	title = title.replace(" ","+")
	user = ctx.message.author
	if user.nick.lower() == "scripts" or user.nick.lower() == "cursed":
		url = f"https://some-random-api.ml/lyrics?title={title}"
		resp = requests.get(url)
		lyr = json.loads(resp.text)
		lyrics = lyr["lyrics"]
		title = lyr['title']
		author = lyr['author']
		return await chat.send(f"{title} by {author}:\n\n{lyrics}")
	return


@bot.command(help_category="fun",help_message="Sends a kanye quote")
async def kanye(ctx,*args):
	chat = ctx.chat
	u = requests.get("https://api.kanye.rest/")
	load = json.loads(u.text)
	quote = load["quote"]
	return await chat.send(f"{quote}\n-Kanye West")

@bot.command(hide_help=True)
async def userdata(ctx,*args):
	chat = ctx.chat
	user = ctx.user
	author = ctx.message.author
	if args:
		author = await ctx.user(args[0])
	data = await get_file(ctx,author)

	await chat.send(data)

@bot.command(hide_help=True)
async def cat(ctx,username=None,cat=None,*args):
	chat = ctx.chat
	author = ctx.message.author
	data = await get_file(ctx,user=author)
	if not author.auth:
		return await chat.send("no")

	test = ctx.message.args
	print(args)
	
	if not username:
		return

	user = await ctx.user(username)
	if not user:
		return await chat.send("User doesn't exist")
	data = await get_file(ctx,user=user)
	if not cat:
		msg = "List of available categories:\n"
		for i in data:
			msg += f"{i}\n"
		return await chat.send(msg)
	cat = cat.lower()
	send = data.get(cat)
	return await chat.send(send)

	

@bot.command(help_category="tools",help_message="Search for a user")
async def user(ctx,*args):
	chat = ctx.chat
	user = await ctx.user(args[0])
	if not user:
		return await chat.send("That user doesn't exist.")
	return await chat.send(f"https://ifunny.co/user/{user.nick.lower()}")

@bot.command(help_category="fun")
async def dice(ctx,amount=None,*args):
	chat = ctx.chat
	message = ctx.message


	if args:
		amount = len(ctx.message.args)

	if amount == None:
		amount = 6

	amount =int(amount)

	if amount > 1000:
		await chat.send("Thats a little too many sides...")
		return
	if amount <= 0:
		return await chat.send("How are you supposed to roll nothing?")

	result = random.randint(1,amount)

	return await chat.send(f"You rolled a {amount} sided die and it came up {result}")

@bot.command(help_category="fun")
async def draw(ctx,*args):
	chat = ctx.chat
	result = random.randint(1,4)
	text = None
	members = await chat.members()
	other = random.choice(members)
	other2 = random.choice(members)
	start = round(time.time())
	end = int(start) + 10

	if args:
		return

	if result == 1:
		text = "BANG"
	if result == 2:
		text = "POW"
	if result == 3:
		text = "PEW"
	if result == 4:
		text = "BOOM"

	secondss = random.randint(3,5)

	await chat.send(f"3... 2... 1...")
	await asyncio.sleep(secondss)
	await chat.send(f"💥{text}💥")

	
	while message := await chat.input(type=iFunny.Message):
		final = [f"{message.author.name} drew their gun the fastest. {other.name} is now dead.",f"{other.name} got their brains spewed across the ground by {message.author.name}.",f"{message.author.name} just became the fastest gunslinger in the chat! The bullet went through {other.name}'s head then ricochets into {other2.name}'s earhole! Impressive!"]
		if isinstance(message, iFunny.Message):
			if message.text.lower() == text.lower():
				return await chat.send(f"{random.choice(final)}")
		if message.text.lower() == "stop":
			return await chat.send(f"the law stopped the draw. nobody died today")
		if round(time.time()) >= end:
			return await chat.send("Oh you missed that one... Try another!")

@bot.command(help_category="fun",help_message="What, you dont know how to have sex?\n\nOriginal code credit goes to https://ifunny.co/user/Vice")
async def sex(ctx,*args):
	message = ctx.message
	chat = ctx.chat
	author= message.author
	members = await chat.members()

	if not members:
		# await chat.send("there are not enough people in this chat")
		return
	if chat.type == 1:
		return
	index = 0
	bots = ["bots","ipartybot","cleverbot","cleverbotus","ak40bot","merpbot","eyebot","rainbot"]
	i = 0
	while index == 0:
		other = random.choice(members)
		if i == 10:
			return await chat.send("There arent enough users in this chat to use this command")
		if other.name.lower() == author.name.lower():
			i += 1
			continue
		if other.name.lower() in bots:
			i += 1
			continue
		index += 1
		


	for x in range(1):
		x = random.randint(0,100)
		if x < 4:
			await chat.send("you had sex with nobody, what a fucking loser")
			return

		else:
			messages = [f"you had sex with {other.name} and your partner walked in and caught you 😬" , f"you had awful sex with {other.name} and neither of you enjoyed it ☹️" , f"you had amazing sex with {other.name} and both of you came all over the place 🤤" , f"you had sex with {other.name} and you ended up getting tied to the bed. kinky 😏"]
		response = random.choice(messages)

		await chat.send(response)

@bot.command(help_category="fun",help_message="randomly dies.\n\nOriginal code credit goes to https://ifunny.co/user/Vice")
async def die(ctx,*args):
	message = ctx.message
	chat = ctx.chat
	author = message.author
	user_id = author.id
	members = await chat.members()

	if args:
		return

	if not members:
		await chat.send("there are not enough people in this chat")
		return

	other = random.choice(members)

	for x in range(1):
		x = random.randint(0,100)
		if x < 2:
			await chat.send("Shrek snuck into your room proceeded to spread your ass cheeks, then shoved his massive 20 inch ogre cock into your ass. You lay there in amazement enjoying every second, wondering how grateful you are that Shrek chose you and made you his bitch for the night. You didn't die that night but his massive cock made it feel as if you were close to dying as he came directly into your ass. You came right along with him. What a rememberable night.. one you’ll cherish forever.")
			return

		else:
			messages = ["You went to your local aquarium and jumped into the piranha tank", "You slipped on an ice cube and bashed your head into your fridge", "you got hit by a car" , f"{other.name} shot you" , "you got into a fight and literally got beat to death, what a loser" , "you went swimming and fucking drowned" , "you went skydiving and your parachute failed to pull. ypu screamed like a little bitch as you fell to the ground" , "you ate a dorito and fucking choked, really bro" , "you didnt let the dolphin rape you so it mauled you. yea man idfk either" , "you decided to poke a venomus snake and died, fucking retard" , "you shoved a fork into an outlet" , f"you died from eating too much kfc" , f"you decided to mess with the geese, they all swarmed you and killed you" , f"you didn't look both ways before crossing the street and got hit by a plane" , f"you went to a 7/11 and got attacked by the crackhead" , f"you encountered a karen, instead of listening to her you shot yourself" , f"{other.name} lauched a bottle rocket at you" , f"you got into the bath with a toaster and plugged it in and then tossed that bitch into the tub with you",
f"you ate a sweater and then choked and died. like wtf why bruh" , f"you fucked {other.name}'s mone and got multiple STDs and died" , "you fell and drowned in your toilet. retard" , "you didnt use your floaties when eating soup and drowned" ,f"you tried to deepthroat a banana to impress your friends. you choked and died" , f"{other.name} quietly placed their dick against your lips, then proceeded to shove their whole giant dick down your throat without giving you air to breathe. As they push and pull, you try to gasp for some air, but ultimately failed, resulting in a gruesome, but hot death" , f"You were chopped into pieces by a helicopter fan" , f"You suffocated underneath some femboy’s cheeks" , f"Got KIA when you found Clinton’s emails", f"you dated a rednecks daughter. he didn't like that so he shot you"]
			response = random.choice(messages)

	if author.name == "3ree":
		response = "you accidentally sucked dick and died choking"

	await chat.send(response)

@bot.command(help_category="fun",help_message="Original code credit goes to https://ifunny.co/user/Vice")
async def gta(ctx,*args):
	message = ctx.message
	chat = ctx.chat
	author = message.author
	user = ctx.user
	members = await chat.members()

	if args:
		return

	if not members:
		await chat.send("there are not enough people in this chat")
		return

	other = random.choice(members)

	for x in range(1):
		x = random.randint(0,100)
		if x < 4:
			await chat.send("you stole a bag of dog shit from the lamborghini you could of easily stolen, the fuck is wrong with you?")
			return

		else:
			messages = [f"you successfully stole a Lamborghini aventador" , f"you failed to steal a Lamborghini aventador" , f"you successfully stole a Ferrari 458 spider" , f"you failed to steal a Ferrari 458 spider" , f"you successfully stole a Bugatti chiron" , f"you failed to steal a Bugatti chiron" , f"you successfully stole a Corvette z06" , f"you failed to steal a Corvette z06" , f"you successfully stole a 1956 Chevrolet bel air" , f"you failed to steal a 1956 Chevrolet bel air" , f"you successfully stole a mustang" , f"you failed to steal a mustang" , f"you successfully stole a Nissan skyline" , f"you failed to steal a Nissan skyline" , f"you successfully stole a Kia soul" , f"you failed to steal a Kia soul" , f"you successfully stole a Dodge Ram" , f"you failed to steal a Dodge Ram" , f"you successfully stole a tank" , f"you failed to steal a tank" , f"you successfully stole a jet" , f"you failed to steal a jet" , f"you successfully stole a bike" , f"you failed to steal a bike\n\n...really nigga" , f"you successfully stole an Escalade" , f"you failed to steal an Escalade"]
			response = random.choice(messages)

	await chat.send(response)

async def create_color():
	colors = ["red","orange","yellow","green","blue","purple","tan","black","white"]
	emojis = ["🔴","🟠","🟡","🟢","🔵","🟣","🟤","⚫","⚪"]

	rcolor = random.choice(colors)

	rcolor_emoji = emojis[colors.index(rcolor)]
	data = {}
	data["name"] = rcolor
	data["emoji"] = rcolor_emoji
	return data

@bot.command(hide_help=True,developer=True)
async def colors(ctx,*args):
	chat = ctx.chat

	x = os.listdir("./user_databases")
	index = 0
	totals = {}
	for user in x:
		data = await get_file_by_name(user)
		garage = data["garage"]
		for i in garage:
			i["color"] = await create_color()

		data["garage"] = garage
		print(garage)
		index += 1
		
		await update_data_by_name(data,user)
	msg = f"TEST\n\nEveryone's colors was set"
			
			
	await chat.send(f"{msg}")
	return

	s = await create_color()
	return await chat.send(s)
	





@bot.command(hide_help=True,developer=True)
async def reset(ctx,money=None,*args):
	chat = ctx.chat
	if not money:
		return
	x = os.listdir("./user_databases")
	
	totals = {}
	for user in x:
		data = await get_file_by_name(user)
		
		data["wallet"] = int(money)
		await update_data_by_name(data,user)
	msg = f"Everyone's balance was set to {money}"
			
			
	await chat.send(f"{msg}")
	return

@bot.command(help_category="cars",help_message="Organize your garage! \n\nUsage: /move (index of car you want to move) (spot you want to move it to)\n\n/move 5 1")
async def move(ctx,car=None,spot=None,*args):
	chat = ctx.chat
	if not car or not spot:
		return await chat.send("Usage: /move (index of car you want to move) (spot you want to move it to)")
	if not car.isdigit() or not spot.isdigit():
		return await chat.send("invalid car position or spot.")
	car = int(car)
	spot = int(spot)
	if car == spot:
		return await chat.send("Your car failed to start, so you didnt move it.")
	author = ctx.message.author
	data = await get_file(ctx,user=author)
	garage = data["garage"]
	
	carcount = len(garage)
	if car > carcount or car <= 0:
		return await chat.send("You dont have that many cars.")
	if spot > carcount or spot <= 0:
		return await chat.send("Invalid spot")
	car = car - 1
	spot = spot - 1
	carobj = garage[car]
	garage.remove(carobj)
	garage.insert(spot,carobj)
	data["garage"] = garage
	await update_data(data,author)
	return await chat.send(f"Your #{car+1} car was moved to the {spot+1} spot.")
	
async def decode_special(string):
		import unicodedata
		
		norm = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
			
		fonts = [
			"𝔄𝔞𝔅𝔟ℭ𝔠𝔇𝔡𝔈𝔢𝔉𝔣𝔊𝔤ℌ𝔥ℑ𝔦𝔍𝔧𝔎𝔨𝔏𝔩𝔐𝔪𝔑𝔫𝔒𝔬𝔓𝔭𝔔𝔮ℜ𝔯𝔖𝔰𝔗𝔱𝔘𝔲𝔙𝔳𝔚𝔴𝔛𝔵𝔜𝔶ℨ𝔷",
			"𝕬𝖆𝕭𝖇𝕮𝖈𝕯𝖉𝕰𝖊𝕱𝖋𝕲𝖌𝕳𝖍𝕴𝖎𝕵𝖏𝕶𝖐𝕷𝖑𝕸𝖒𝕹𝖓𝕺𝖔𝕻𝖕𝕼𝖖𝕽𝖗𝕾𝖘𝕿𝖙𝖀𝖚𝖁𝖛𝖂𝖜𝖃𝖝𝖄𝖞𝖅𝖟",
			"𝒜𝒶𝐵𝒷𝒞𝒸𝒟𝒹𝐸𝑒𝐹𝒻𝒢𝑔𝐻𝒽𝐼𝒾𝒥𝒿𝒦𝓀𝐿𝓁𝑀𝓂𝒩𝓃𝒪𝑜𝒫𝓅𝒬𝓆𝑅𝓇𝒮𝓈𝒯𝓉𝒰𝓊𝒱𝓋𝒲𝓌𝒳𝓍𝒴𝓎𝒵𝓏",
			"𝓐𝓪𝓑𝓫𝓒𝓬𝓓𝓭𝓔𝓮𝓕𝓯𝓖𝓰𝓗𝓱𝓘𝓲𝓙𝓳𝓚𝓴𝓛𝓵𝓜𝓶𝓝𝓷𝓞𝓸𝓟𝓹𝓠𝓺𝓡𝓻𝓢𝓼𝓣𝓽𝓤𝓾𝓥𝓿𝓦𝔀𝓧𝔁𝓨𝔂𝓩𝔃",
			"卂𝓐乃вＣⓒ𝓭Ďᵉ𝐄𝐟ＦgǤⓗ卄𝐈ι𝓳𝕁Ҝ𝐊Ĺᒪ𝐌爪几ηㄖόƤρǪq𝐫ᖇｓˢᵗtⓤ𝓾Ⓥᵛⓦ𝔴ｘxƳ𝐲ᶻz"
		]
		
		final = ""
		
		for char in string:
			the_font = None
			for font in fonts:
				if char in font:
					the_font = font
					break
			
			if not the_font:
				final += char
				continue
			
			normalized_char = norm[the_font.index(char)]
			final += normalized_char

		return(unicodedata.normalize('NFKC', final))

async def searchchats(query):
	query = query.replace(" ","+")

	params = (('limit', '100'),('q', query),)

	response = requests.get('https://api.ifunny.mobi/v4/chats/open_channels', headers=bearerheaders, params=params).json()
	if response.get("status") == 200:
		if response["data"]["channels"]["items"] != []:
			return response["data"]["channels"]["items"]

async def getexplore():

	response = requests.get('https://api.ifunny.mobi/v4/chats/trending', headers=bearerheaders).json()
	if response.get("status") == 200:
		if response["data"]["channels"] != []:
			return response["data"]["channels"]



@bot.command(help_category="chat",help_message="Displays the current chats on the explore page.\nJoin then using /join [index]")
async def explore(ctx,*args):
	chat = ctx.chat
	cdata = await get_file(ctx,user=None,chat=chat)
	ex = await getexplore()
	all_chats = []
	for i in ex:
		chat_obj = {}
		chat_obj["title"] = i["title"]
		chat_obj["chatid"] = i["name"]
		chat_obj["type"] = i["type"]
		if chat_obj not in all_chats:
			all_chats.append(chat_obj)
	count = len(all_chats)
	msg = f"Current {count} chats on explore:\n\n"
	all_chats = sorted(all_chats, key = lambda i: i['title'])
	cdata["schats"] = all_chats
	await update_chat(cdata,chat)
	index = 1
	for i in all_chats:
		
		msg += f"{index}. {i['title']}\n"
		index += 1
		if index == 16:
			break
	msg += "\n/join [index]"
			
	await chat.send(f"{msg}")
	return
	

@bot.command(help_message="Search for open chats using keywords.\nYou can join these chats by using /join [index]\nUsage: /sc purple",help_category="chat",aliases=["sc"])
async def searchchat(ctx,*args):
	chat = ctx.chat
	author = ctx.message.author
	auth = author.auth
	data = await get_file(ctx,user=author)
	query = ctx.message.args
	if not query:# or len(query) == 1:
		return await chat.send("Input something longer to search for!")
	
	search = await searchchats(query)
	
	all_chats = []
	if search:
		for i in search:
			if query.lower() in i["title"].lower() or query.lower() in i["name"].lower():
				chat_obj = {}
				chat_obj["title"] = i["title"]
				chat_obj["chatid"] = i["name"]
				chat_obj["type"] = i["type"]
				if chat_obj not in all_chats:
					all_chats.append(chat_obj)
	
	x = os.listdir("./chat_databases")
	totals = []
	for user in x:
		chat_data = await get_chat_by_name(user)

		title = chat_data["title"]
		title = await decode_special(title)
		chat_id = chat_data.get("chat_id")
		if not chat_id:
			continue
		if query.lower() in title.lower() or query.lower() in chat_id.lower():
			if botid.lower() not in chat_data["chat_id"].lower():
				chat_obj = {}
				chat_obj["title"] = chat_data["title"]
				chat_obj["chatid"] = chat_data["chat_id"]
				chat_obj["type"] = chat_data["type"]
				if chat_data["type"] == 2:
					if auth:
						if chat_obj not in all_chats:
							all_chats.append(chat_obj)
							continue
				if chat_data["type"] == 3:
					if chat_obj not in all_chats:
						all_chats.append(chat_obj)
				continue
	count = len(all_chats)
	if count == 0:
		return await chat.send("No chats were found.")
	pagemax = math.ceil(count/10)
	msg = f"{count} Chats Found: [1/{pagemax}]\n\n"
	cdata = await get_file(ctx,user=None,chat=chat)
	all_chats = sorted(all_chats, key = lambda i: i['title'])
	cdata["schats"] = all_chats
	await update_chat(cdata,chat)
	index = 1
	for i in all_chats:
		emoji = "🅾️"
		if i['type'] == 2:
			emoji = "🅿️"
		msg += f"{index}. {emoji} {i['title']}\n"
		index += 1
		if index == 11:
			break
				
		# await update_data_by_name(data,user)
	# msg = f"Everyone's balance was set to {money}"
	msg += "\n/join [index]\n/page [number]"
			
	await chat.send(f"{msg}")
	return

@bot.command(help_category="chat",help_messge="Scroll through /searchchat pages")
async def page(ctx,number=None,*args):
	chat = ctx.chat
	if not number:
		return
	if not number.isdigit():
		return
	author = ctx.message.author
	data = await get_file(ctx,user=author)
	cdata = await get_file(ctx,user=None,chat=chat)
	all_chats = cdata.get("schats")
	if not all_chats:
		return
	count = len(all_chats)
	number = int(number)
	pagemax = math.ceil(count/10)
	if number > pagemax or number <= 0:
		return
	msg = f"{count} Chats Found: [{number}/{pagemax}]\n\n"
	index = 1
	index2 = number*10
	chatindex = index2 -10

	for i in all_chats:
		if chatindex >= index2:
			break
		if chatindex >= count:
			break
		coun = chatindex + 1
		carobj = all_chats[chatindex]
		
		emoji = "🅾️"
		if carobj['type'] == 2:
			emoji = "🅿️"
		msg += f"{coun}. {emoji} {carobj['title']}\n"
		index += 1
		chatindex += 1

	msg += "\n/join [index]\n/page [number]"

	await chat.send(msg)

@bot.command(hide_help=True,auth=True,help_category ="chats",help_message="Use this when using /sc to get the chat id of the selected chat")
async def url(ctx,number=None,*args):
	chat = ctx.chat
	og_id = chat.id
	author = ctx.message.author
	data = await get_file(ctx,user=author)
	cdata = await get_file(ctx,user=None,chat=chat)
	if not number or not number.isdigit():
		return
	all_chats = cdata.get("schats")
	number = int(number)
	if number <= 0 or number > len(all_chats):
		return await chat.send("invalid index")
	number = number - 1
	chatobj = all_chats[number]
	chat_id = chatobj["chatid"]
	chat_type = chatobj["type"]
	if chat_type == 2:
		if not ctx.message.author.auth:
			return await chat.send("no")
	return await chat.send(chat_id)


	

@bot.command(help_category="chat",help_message="Usage: /join [index]\nUse this command to join open chats in the /searchchat command")
async def join(ctx,number=None,*args):
	chat = ctx.chat
	og_id = chat.id
	author = ctx.message.author
	data = await get_file(ctx,user=author)
	cdata = await get_file(ctx,user=None,chat=chat)
	if not number or not number.isdigit():
		return
	all_chats = cdata.get("schats")
	number = int(number)
	if number <= 0 or number > len(all_chats):
		return await chat.send("invalid index")
	number = number - 1
	chatobj = all_chats[number]
	chat_id = chatobj["chatid"]
	chat_type = chatobj["type"]
	if chat_type == 2:
		if not ctx.message.author.auth:
			return await chat.send("no")
	chat.id = chat_id
	await chat.invite(author)
	chat.id = og_id
	return await chat.send("invited!")


@bot.command(hide_help=True,developer=True)
async def resetmil(ctx,money=None,*args):
	chat = ctx.chat
	
	x = os.listdir("./user_databases")
	
	totals = {}
	for user in x:
		data = await get_file_by_name(user)
		if data['wallet'] == 10000000:
			data["wallet"] = 3000
			await update_data_by_name(data,user)
	msg = f"Everyone's balance that was 10 mil was set to 3k"
			
			
	await chat.send(f"{msg}")
	return



	


# @bot.command(help_category="money",help_message="Usage: \n/rat {1-5} {bet amount} \n\nWill randomly select a rat and if you guess right you win your bet amount!")
# async def rat(ctx,thing1=None,amount=None,*args):
#    chat = ctx.chat
#    author = ctx.author
#    message = ctx.message
#    user = message.author
#    data = await get_file(ctx,author)
#    bal = data["wallet"]
#    author_bal = bal
#
#    if amount not in ['all', 'half']:
#        try:
#            amount = int(str(amount).replace("k", "000").replace("m","000000").replace("b","000000000").replace("t","000000000000").replace("q","000000000000000"))
#        except:
#            await chat.send("The amount specified is not a number.")
#            return
#    else:
#        if amount.lower() == 'all':
#            amount = author_bal
#        elif amount.lower() == 'half':
#            amount = int(author_bal/2)
#    
#    amount =int(amount)
#    if amount ==int(0):
#        await chat.send("Can't bet nothing")
#        return
#
#
#    if amount > bal:
#        await chat.send("Not enough money for that bet")
#        return
#    if amount < 0:
#        await chat.send("Why did you try that?")
#        return
#    
#
#    e = random.randint(1,5)
#
#    if e == 1:
#        url = "https://s3rg.me/3txz"
#    if e == 2:
#        url = "https://s3rg.me/rfmq"
#    if e == 3:
#        url = "https://s3rg.me/nqdg"
#    if e == 4:
#        url = "https://s3rg.me/f8ox"
#    if e == 5:
#        url = "https://s3rg.me/tsnh"
#
#    thing1 =int(thing1)
#
#    if thing1 < 1:
#        return await chat.send("Choose a number between 1 and 5")
#    if thing1 > 5:
#        return await chat.send("Choose a number between 1 and 5")
#
#    #async with aiohttp.ClientSession() as session:
#        #async with session.get(url) as r:
#
#            #try:
#                #await chat.upload(await r.read())
#            #except:
#                #await chat.send("Error sending image")
#
#    if thing1 == e:
#        data["wallet"] += amount*5
#        await update_data(data,author)
#        await chat.send(f"You guessed right! {amount * 5} ballers has been awarded to your wallet")
#        return
#    else:
#        data["wallet"] -= amount
#        await update_data(data,author)
#        await chat.send(f"The correct one was {e}, You lost {amount} ballers")
#        return

@bot.command(help_message="Sends a random FML from the fmylife website",help_category='fun')
async def fml(ctx,*args):
	chat = ctx.chat
	headers = {"X-VDM-Api-Key":"4dccf019bdfac"}
	r = requests.get("http://www.fmylife.com/api/v2/article/list?page[number]=1&page[bypage]=20&status[]=4&orderby[RAND()]=ASC", headers = headers)
	response = r.text
	loaded = json.loads(r.text)
	msg = ""
	msg += loaded["data"][0]["content_hidden"]
	upvote = loaded["data"][0]["metrics"]["votes_up"]
	downvote = loaded["data"][0]["metrics"]["votes_down"]
	msg += f"\n\nYour life sucks: {upvote}\nYou deserved it: {downvote}"

	return await chat.send(msg)

@bot.command(help_category="fun")
async def stinky(ctx, *args):
	"""I will call this user stinky and smelly"""

	chat = ctx.chat
	message = ctx.message

	if args:
		await chat.send(f"{message.args}, You are very smelly and also stinky. Go take a shower plz")
	else:
		await chat.send("Please specify a user you want to call stinky :)")

@bot.command(hide_help=True)
async def kunt(ctx,*args):
	chat = ctx.chat
	return await chat.send("Shrimp Alfredo")

@bot.command(help_category="fun",help_message="tells you how something something is.")
async def how(ctx,thing1 = None, thing2 = None,*args):
	chat = ctx.chat
	message = ctx.message
	author = ctx.message.author
	randomm = random.randrange(0,100)

	if ctx.author.name.lower() == "cursed":
		randomm = 100

	if not thing2:
		thing2 = author.name
	if args:
		return

	return await chat.send(f"{thing2} is {randomm}% {thing1}")





@bot.command(hide_help=True, developer=True)
async def backup(ctx, *args):
	chat = ctx.chat
	msg = "Saving...\n\n"
	index = 0
	for file in files:
		if file == "libs": continue
		if file == "__pycache__": continue
		if file == ".idea": continue
		if file == "users": continue
		text = file.replace(".",". ")
		msg += f"{text}\n"
		index += 1
		shutil.copy(file, dest)
		shutil.copy(file, dest2)
	
	if os.path.isfile(file):
		shutil.copy(file, dest)
		shutil.copy(file, dest2)
	
	msg += f"\nsaved {index} files"
	
	return await chat.send(msg)


@bot.command(help_category="data",help_message="Set your clan name")
async def setclan(ctx,clan=None,*args):
	chat = ctx.chat
	if not clan:
		return await chat.send("Usage: /setclan ClanName")
	abcs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	for i in clan:
		if i.lower() not in abcs:
			return await chat.send("Only english letters are supported.")
	if len(clan) > 15:
		return await chat.send("Your clan name is too long!")
	clan = clan.lower()
	bad = ["nigger","niggers","jew","pedo","pedophile","emuphile","emu","child","children","racist","nigg","kkk","elle"]
	for i in bad:
		if i in clan:
			return await chat.send("no")
	clan = clan.capitalize()
	data = await get_file(ctx,user=ctx.message.author)
	await get_or_create_clan(clan)
	data["clan"] = clan
	await update_data(data,ctx.message.author)
	return await chat.send(f"Your clan was set to {clan}.")

@bot.command(help_category="data",help_message="View your clan name")
async def clan(ctx,*args):
	chat = ctx.chat
	user = ctx.message.author
	data = await get_file(ctx,user=user)
	clan = data["clan"]
	if not clan:
		return await chat.send("You havent joined a clan! do /setclan (ClanName) to join one!")
	return await chat.send(f"{user.nick}'s Clan:\n{clan}")

async def get_or_create_clan(clan):
	try:
		with open(f"D:\\iPartybot\\clans\\{clan}.json","r") as f:
			data = json.load(f)
			return data
		
	except:
		data = {}
		data["name"] = clan
		data["xp"] = 0
		with open(f"D:\\iPartybot\\clans\\{clan}.json","w") as f:
			json.dump(data,f,indent=1)
		return data

async def get_clan(clan):
	try:
		with open(f"D:\\iPartybot\\clans\\{clan}.json","r") as f:
			data = json.load(f)
			return data
		
	except:
		return None


@bot.command(help_category="data",help_message="View the top clans based on members or XP")
async def clantop(ctx,*args):
	chat = ctx.chat
	if args:
		clans = {}
		x = os.listdir("./user_databases")
		for i in x:
			data = await get_file_by_name(i)
			clan = data["clan"]
			if clan:
				bal = clans.get(clan)
				if not bal:
					bal = 0
				bal += 1
				clans.update({clan:bal})
			
		msg = "Top Clans by Member Count:\n"
		
	
		totals_2 = {k: v for k, v in sorted(clans.items(), key=lambda item: item[1])}

		for index, user in enumerate(reversed(totals_2)):
			index += 1

			balance = totals_2[user]

			if index <= 10:
				msg += f"\n{index}. {user}: {balance:,}"
			if index > 10:
				break
			continue
		return await chat.send(msg)

	totals = {}
	x = os.listdir("./clans")
	for i in x:
		clan = i.replace(".json","")
		data = await get_clan(clan)
		total_balance = data["xp"]
		totals.update({i:total_balance})
	totals_2 = {k: v for k, v in sorted(totals.items(), key=lambda item: item[1])}

	msg = f"Top Clans by XP:\n"
	for index, user in enumerate(reversed(totals_2)):
		index += 1
		balance = totals_2[user]
		user = user.replace(".json","")
		
		if index <= 10:
			msg += f"\n{index}. {user}: {balance:,}"
		if index > 10:
			break
		continue
	return await chat.send(msg)




@bot.command(help_category="games",help_message="Play Hangman!\n\nThis was created by LUSTFMAB")
async def hangman(ctx,*args):
	chat = ctx.chat
	words_to_guess =["naggers","curse","hex","witch","cheese","drugs","ball","poggers","dank","rank","stank","illegal","ziti","twenty","milk","hell","heaven","purgatory","void","love", "apple", "banana", "gorilla", "orange", "yellow", "brown", "green", "pinky", "boobies","mouse", "cat", "kitten", "giraffe", "sandwich", "heart", "sandals", "halloween", "basketball", "soccer", "baseball", "sushi", "football", "mascara", "lipstick", "alligator", "crocodile", "ocean", "seaweed", "spaghetti", "walrus", "kobra", "teeth", "finger", "bones", "bitch", "demon", "angel", "spider", "doctor", "damage", "soup","january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants", "sluts", "donkey", "baby"]
	word = random.choice(words_to_guess)
	if ctx.message.author.name.lower() == "scripts":
		word = words_to_guess[0]
	length = len(word)
	og_word = word
	print(og_word)
	count = 0
	display = '-' * length
	already_guessed = []
	play_game = ""
	limit = 9
	await chat.send("This is the Hangman Word:\n\n" + display + "\n\nPlease guess a letter:")
	index = 1
	while message := await chat.input(type=iFunny.Message):
		if isinstance(message, iFunny.Message):
			guess = message.text.lower().strip()
			guess_spaceless = guess.replace(" ","")
			if message.text.lower() == "stop":
				return await chat.send("The game has been ended")

			if guess_spaceless == og_word:
				return await chat.send("Congrats! You have guessed the correct word!!!!")

			elif len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
				continue

			elif guess_spaceless in already_guessed:
				await chat.send(f"Do you have amnesia? You guessed this letter. Please try another letter.\nLetters guessed: {already_guessed}")
				continue
			

			elif guess_spaceless in og_word:
				already_guessed.extend([guess_spaceless])
				index = re.finditer(guess_spaceless,og_word)
				index_positions = [match.start() for match in index]
				# print(index_positions)
				for i in index_positions:
					word = word[:i]+word[i + 1:]
					# print(word)
					display = display[:i]+guess_spaceless + display[i + 1:]

				if display.replace("-","") == og_word:
					return await chat.send(f"Congrats! You guessed the correct word!!!!\nThe word was {og_word}.")
				
				await chat.send(f"Word: \n{display}\nLetters guessed: \n{already_guessed}")
				continue

			else:
				already_guessed.extend([guess])
				count += 1
				msg = f"Letters guessed: {already_guessed}\n"

				if count == 1:
					msg +="   _____ \n  |      \n  |      \n  |      \n  |      \n  |      \n  |      \n_|_\n"
					msg += f"\n{display}\nWrong guess. " + str(limit - count) + " guesses remaining\n"
					await chat.send(msg)
					continue
				

				elif count == 2:
					
					msg += "   _____ \n  |     | \n  |     |\n  |      \n  |      \n  |      \n  |      \n_|_\n"
					msg += f"\n{display}\nWrong guess. " + str(limit - count) + " guesses remaining\n"
					await chat.send(msg)
					continue

				elif count == 3:
				   
				   msg += "   _____ \n  |     | \n  |     |\n  |     | \n  |      \n  |      \n  |      \n_|_\n"
				   msg += f"\n{display}\nWrong guess. " + str(limit - count) + " guesses remaining\n"
				   await chat.send(msg)
				   continue

				elif count == 4:
					
					msg += "   _____ \n  |     | \n  |     |\n  |     | \n  |     O \n  |      \n  |      \n_|_\n"
					msg += f"\n{display}\nWrong guess. " + str(limit - count) + " guesses remaining\n"
					await chat.send(msg)
					continue

				elif count == 5:
					
					msg+= "   _____ \n  |     | \n  |     |\n  |     | \n  |     O \n  |     |  \n  |        \n_|_\n"
					msg += f"\n{display}\nWrong guess. " + str(limit - count) + " guesses remaining\n"
					await chat.send(msg)

				elif count == 6:
					
					msg+= "   _____ \n  |     | \n  |     |\n  |     | \n  |     O \n  |    /|  \n  |        \n_|_\n"
					msg += f"\n{display}\nWrong guess. " + str(limit - count) + " guesses remaining\n"
					await chat.send(msg)

				elif count == 7:
					
					msg+= "   _____ \n  |     | \n  |     |\n  |     | \n  |     O \n  |    /|\ \n  |        \n_|_\n"
					msg += f"\n{display}\nWrong guess. " + str(limit - count) + " guesses remaining\n"
					await chat.send(msg)

				elif count == 8:
					
					msg+= "   _____ \n  |     | \n  |     |\n  |     | \n  |     O \n  |    /|\ \n  |      \ \n_|_\n"
					msg += f"\n{display}\nWrong guess. " + str(limit - count) + " last guess remaining\n"
					await chat.send(msg)

				elif count == 9:
					
					msg +="   _____ \n  |     | \n  |     |\n  |     | \n  |     O \n  |    /|\ \n  |    / \ \n_|_\n"
					msg += f"You lost the game. The word was {og_word}"
					return await chat.send(msg)

@bot.command(hide_help=True)
async def ping(ctx,*args):
	pang = ctx.message.ping
	if ctx.message.ping < 0:
		pang = random.randint(40,90)
	return await ctx.chat.send(f"Pong! {pang}ms")

@bot.command(hide_help=True,developer=True)
async def say(ctx,*args):
	chat = ctx.chat
	return await chat.send(ctx.message.args)

@bot.command(help_category="cats",help_message="adopt a cat!")
async def adopt(ctx,*args):
	return
	



os.chdir("D:\\iPartyBot")

host = "http://api.ifunny.mobi"


async def get_request(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as r:
			return await r.json()



async def gen_basic():
	from secrets import token_hex
	from hashlib import sha1
	from base64 import b64encode
	client_id = "JuiUH&3822"
	client_secret = "HuUIC(ZQ918lkl*7"
	device_id = token_hex(32)
	hashed = sha1(f"{device_id}:{client_id}:{client_secret}".encode('utf-8')).hexdigest()
	basic = b64encode(bytes(f"{f'{device_id}_{client_id}'}:{hashed}", 'utf-8')).decode()
	return basic





# fun stuff



def seconds_to_str(t):
	
	y, r = divmod(t, 31557600)
	month, r = divmod(r, 2629800)
	d, r = divmod(r, 86400)
	h, r = divmod(r, 3600)
	m, s = divmod(r, 60)
	durations = [[int(y),"year"],[int(month),"month"],[int(d),"day"],[int(h),"hour"],[int(m),"minute"],[int(s),"second"]]
	durations = [i for i in durations if i[0]]
	s_durations = []

	for count, i in enumerate(durations):
		if i[0] > 1:
			durations[count][1] += "s"
			
	durations = [str(i[0])+" "+i[1] for i in durations]
	total = ", ".join(durations)

	if t > 0:
		return total
	
	return "1 second"









bot.run()
