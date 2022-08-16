import requests

import json
import asyncio
import aiohttp
import traceback
from termcolor import colored
from datetime import datetime
import time
import textwrap
import sys
import sqlite3
import os
from . import ws_client
from . import captcha_bypass
from . import fleep

host = "http://api.ifunny.mobi"
host2 = "http://api.ifunny.chat"



def cprint(*args, end_each=" ", end_all=""):
	dt = str(datetime.fromtimestamp(int(time.time())))
	print(colored(dt, "white"), end=end_each)
	for i in args:
		print(colored(str(i[0]), i[1].lower()), end=end_each)
	print(end_all)
	
	
async def get_request(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as r: 
			return await r.json()
			
			
async def post_request(url, data=None):
	async with aiohttp.ClientSession() as session:
		async with session.post(url, data=data) as r: 
			return await r.json()
			
async def get_file(ctx,chat=None):

    if chat:
        file_src = f"D:\\iPartyBot\\chat_databases\\{chat.id}.json"
        try:
            with open(file_src,"r") as f:
                file = json.load(f)
                return file
        except:
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

			
class LoginError(Exception): pass
			
class Parser:

	version = "7b2274797065223a2022626f74227d"

	@staticmethod
	async def chat_list(bot, ctx, frame):
		
		bot.chats = [Chat(i, bot) for i in frame["chat_list"]]


	@staticmethod
	async def invitations(bot, ctx, frame):
		
		for i in frame["invitations"]:
			ctx.chat = Chat(i["chat"], bot)
			ctx.chat.inviter = User(i["inviter"], bot)
			if ctx.chat.id in bot.blacklistchat():
				print("uwu")
				return await bot.reject_invite(ctx)
			await bot.accept_invite(ctx)
			cprint(("Joined chat", "magenta"), (i["chat"]["id"], "yellow"))
				
				
	@staticmethod
	async def error(bot, ctx, frame):
		
		if frame["error"] == "message_rate_limit":
			bot.ratelimit()
			if package := bot.unconfirmed_queue.get(frame["response_to"]):
				await asyncio.sleep(0.5)
				await bot.message_queue.put(package)
			
			
	@staticmethod
	async def affirmation(bot, ctx, frame):
		
		if bot.unconfirmed_queue.get(frame["response_to"]):
			del bot.unconfirmed_queue[frame["response_to"]]
				
				
	@staticmethod
	async def chat_event(bot, ctx, frame):
		
		if function := bot.events.get(frame["chat_event"]):
			ctx.chat = Chat(frame["chat"], bot)
			
			if frame["user"]:
				if frame["user"]["id"] == bot.user_id: return
				ctx.user = User(frame["user"], bot)
			
			ctx.chat.yield_ratelimit = True
			bot.run_callback(function, ctx)
				
				
	@staticmethod
	async def member_list(bot, ctx, frame):
		
		if chat_id := bot.member_request_ids.get(frame["response_to"]):
			if q := bot.member_list_queues.get(chat_id):
				await q.put(frame["member_list"])
		
		
	@staticmethod
	async def message(bot, ctx, frame):
		
		user_id = frame["user"]["id"]
		
		if user_id == bot.user_id: return
		if frame["user"].get("is_bot"): return
		if user_id in bot.blacklist() and user_id != bot.developer: return
		
		ctx.chat = Chat(frame["chat"], bot)
		ctx.message = Message(frame["message"], bot)
		ctx.author = User(frame["user"], bot)
		ctx.message.author = ctx.author
		ctx.chat.message = ctx.message
		ctx.message.chat = ctx.chat
		ctx.chat.author = ctx.author
		ctx.author.is_developer = ctx.author.id == bot.developer
		
		frame["message"]["text"] = frame["message"]["text"].strip()
				
		if frame["message"]["text"].startswith(bot.prefix):

			if command_items := frame["message"]["text"].strip(bot.prefix).strip().split():
				base_name = command_items[0].lower()
				
				if function := bot.commands.get(base_name):
					d = await get_file(ctx,ctx.chat)
					if base_name in d["disabled"]:
						return
					await bot.run_command(function, ctx)
				
		else:
			await bot.siphon_input(bot.on_message, ctx)
				
				
	@staticmethod
	async def file(bot, ctx, frame):
		
		user_id = frame["user"]["id"]
		
		#if user_id == bot.user_id: return
		#if frame["user"].get("is_bot"): return
		if user_id in bot.blacklist() and user_id != bot.developer: return

		if bot.on_file:
			
			ctx.chat = Chat(frame["chat"], bot)
			ctx.message = File(frame["file"], bot)
			ctx.author = User(frame["user"], bot)
			ctx.message.author = ctx.author
			ctx.chat.message = ctx.message
			ctx.message.chat = ctx.chat
			ctx.author.is_developer = ctx.author.id == bot.developer
			await bot.siphon_input(bot.on_file, ctx)
	
	
basicauth = "Get your own basic auth token"

async def user_by_nick(nick: str, bot=None):
	userheader = {
    'Host': 'api.ifunny.mobi',
    'Accept': 'video/mp4, image/jpeg',
    'Applicationstate': '1',
    'Accept-Encoding': 'gzip, deflate',
    'Ifunny-Project-Id': 'iFunny',
    'User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)',
    'Accept-Language': 'en-US;q=1',
    'Authorization': 'Basic '+basicauth,}

	data = requests.get(host+'/v4/users/by_nick/'+nick, headers=userheader)
	data = data.json()
	
	if data["status"] == 200:
		return User(data["data"], bot)
		
		
		
async def user_by_id(user_id: str, bot=None):

	userheader = {
    'Host': 'api.ifunny.mobi',
    'Accept': 'video/mp4, image/jpeg',
    'Applicationstate': '1',
    'Accept-Encoding': 'gzip, deflate',
    'Ifunny-Project-Id': 'iFunny',
    'User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)',
    'Accept-Language': 'en-US;q=1',
    'Authorization': 'Basic '+basicauth,}

	data = requests.get(host+"/v4/users/"+user_id,headers=userheader)
	data = data.json()
	if data["status"] == 200:
	
		return User(data["data"], bot)

async def get_profile():

	with open("D:\\iPartyBot\\bearer.json","r") as bearer_file:
			s = json.load(bearer_file)

			bearerer = s["bearer"]

	

	url = host+"/v4/account"
	daheader = {"Authorization":"Bearer "+bearerer,'Ifunny-Project-Id': 'iFunny','User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)'}
	req = requests.get(url,headers = daheader).json()
	if req["status"] == 200:
		return True
	else:
		return False

class CTX:
	
	chat = None
	message = None
	author = None
	user = None
	inviter = None
	
	def __init__(self, bot=None):
		self.bot = bot

	async def getchat(self,chat_id):
		return await(getchat(chat_id,self.bot))
		
	async def user(self, nick_or_id):
		return await(user(nick_or_id, self.bot))
		
	async def user_by_nick(self, nick: str):
		return user_by_nick(nick, self.bot)
		
	async def user_by_id(self, user_id: str):
		return user_by_id(nick, self.bot)
		
		
class CTXtype:
	
	def __init__(self, data, bot):
		self.bot = bot
		for k, v in data.items():
		  setattr(self, k, v)
		
			
class User(CTXtype):
	
	def __init__(self, data, bot):
		super().__init__(data, bot)
		
		
		self.chat_id = bot.user_id+"_"+self.id
		self.meme_experience = data.get("meme_experience")
		self.privacy = data.get("messaging_privacy_status")
		self.bans = data.get("bans")
		self.bio = data.get("about")
		self.cover = data.get("cover_url")
		self.num = data.get("num")
		self.name = self.nick
		self.role = data.get("role")
		self.status = data.get("last_seen_at")
		self.is_bot = data.get("is_bot")
		self.pfp = data.get("photo")
		self.verified = data.get("is_verified")
		self.banned = data.get("is_banned")
		self.deleted = data.get("is_deleted")
		self.og_nick = data.get("original_nick")
		self.auth = self.id in bot.auth()
		self.blacklisted = self.id in bot.blacklist()
		self.developer = self.id == bot.developer
		
	def __eq__(self, other):
		return self.id == other.id
		
	def __ne__(self, other):
		return self.id != other.id
		
	async def send(self, message):
		await self.bot.send_message(self.chat_id, message)
		
	async def upload(self, data, messageid):
		await self.bot.upload(self.chat_id, data=data, messageid=messageid)
		
		
async def user(nick_or_id: str, bot=None):
	
	nick_or_id = nick_or_id.lower()
	
	if len(nick_or_id) == 24 and nick_or_id[0].isdigit() and sum([1 for i in nick_or_id if ord(i) >= 96]): #most likely to be an id
		if test_user := await user_by_id(nick_or_id, bot):
			return test_user
	
	return await user_by_nick(nick_or_id, bot)
	

class Message(CTXtype):
	
	def __init__(self, data, bot):
		super().__init__(data, bot)
		self.author = None
		self.chat = None
		self.text = self.text.strip()
		self.payload = data.get("payload")
		self.args_list = self.text.split(" ")[int(bool(self.text.startswith(bot.prefix))):]
		self.args = " ".join(self.args_list)
		self.ts = self.pub_at
		self.ping = int(time.time()*1000)-self.ts
		
	def __eq__(self, other):
		return self.text == other.text
		
	def __ne__(self, other):
		return self.text != other.text
		
		
class File(CTXtype):
	
	def __init__(self, data, bot):
		super().__init__(data, bot)
		for k, v in data["file"].items():
		  setattr(self, k, v)
		
		self.author = None
		self.chat = None
		self.ts = self.pub_at
		self.ping = int(time.time()*1000)-self.ts
		
	def __eq__(self, other):
		return self.hash == other.hash
		
	def __ne__(self, other):
		return self.hash != other.hash
		
		
class Chat(CTXtype):
	
	def __init__(self, data, bot):
		super().__init__(data, bot)
		self.bot_role = data.get("role") #0 is owner, 1 is operator(public chats), 2 is member
		self.type = data.get("type") #1 is dm, 2 is private, 3 is public
		self.type_name = data.get("type_name")
		self.description = data.get("description")
		self.cover = data.get("cover")
		self.name = data.get("name")
		self.title = data.get("title")
		self.total_members = data.get("members_total")
		self.unread = data.get("messages_unread")
		self.last_msg = data.get("last_msg")
		
		self.author = None
		self.message = None
		self.inviter = None
		self.yield_ratelimit = False
		
	def __eq__(self, other):
		return self.id == other.id
		
	def __ne__(self, other):
		return self.id != other.id
		
	async def send(self, message):
		if self.yield_ratelimit and self.bot.ratelimited: return
		author_name = None
		if self.author and self.type != 1: author_name = self.author.nick
		await self.bot.send_message(self.id, message, author_name)
		
	async def upload(self, data, messageid):
		await self.bot.upload(self.id, data=data, messageid=messageid)
		
	async def members(self):
		return await self.bot.get_members(self.id)
	

		
	async def has_member(self, user):
		for i in await self.members():
			if user == i: return True
		return False
		
	async def invite(self, user):
		await self.bot.invite(self.id, user.id)
		
	async def input(self, type=Message, timeout=None):
		return await self.bot.input(self.id, type, timeout)

async def getchat(chat_id:str,bot=None):

	await bot.buff.send_ifunny_ws(json.dumps([48,bot.buff.ifunny_ws_counter,{},"co.fun.chat.get_chat",[],{"chat_name":chat_id}]))
	await asyncio.sleep(2)
	data = ws_client.chat_info
	if data == []:
		return None
	else:
		data = data[0]
	return Chat(data["chat"],bot)



class Bot:
	
	def __init__(self, email: str, password: str, region: str, prefix: str,basicauth:str):
	
		assert(prefix), "Prefix string cannot be empty"
	
		self.email = email
		self.password = password
		self.region = region
		self.prefix = prefix
		self.basicauth = basicauth
		
		regions = {"United States": "ifunny", "Brazil": "ifunny_brazil"}
		
		assert(region in regions), "Invalid region"
		
		self.ws_region = regions[region]
		
		cprint(("Starting bot...", "magenta"))
		
		self.user_id = ""
		self.nick = ""
		self.commands = {}
		self.events = {}
		self.cooldowns = {}
		self.timekeeping = {}
		self.developer_commands = []
		self.auth_commands = []
		self.developer = None
		self.help_categories = {}
		self.auth_help_categories = {}
		self.command_help_messages = {}
		self.auth_command_help_messages = {}
		self.member_list_queues = {}
		self.member_request_ids = {}
		self.chat_request_ids = {}
		self.chat_list_queues = {}
		self.chats = []
		self.ratelimited = False
		self.open = True
		self.on_join = self.on_message = self.on_file = None
		self.prev_chat_id = self.prev_message = self.prev_nick = None
		self.unconfirmed_queue = {}
		self.siphons = {}
		self.generate_help_command()
		self._blacklist = set()
		self._blacklistc = set()
		self._auth = set()
		self.load_blacklist()
		self.load_blacklistchat()
		self.load_auth()
		try:
			self.run(ws_client.Buffer)
		except:
			self.login()


	def login(self):
		url = host+"/v4/oauth2/token"
		paramz = {'grant_type':'password',
                   'username': self.email,
                   'password': self.password
                }
		header = {'Host': 'api.ifunny.mobi','Applicationstate': '1','Accept': 'video/mp4, image/jpeg','Content-Type': 'application/x-www-form-urlencoded','Authorization': 'Basic '+self.basicauth,'Content-Length':'77','Ifunny-Project-Id': 'iFunny','User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)','Accept-Language': 'en-US;q=1','Accept-Encoding': 'gzip, deflate'}

		while True:
			with open("D:\\iPartyBot\\bearer.json","r") as bearerfile:
				logindata = json.load(bearerfile)
				user_bearer = logindata["bearer"]
				userid = logindata["user_id"]
			try:
				self.buff = ws_client.Buffer(user_bearer, userid, self.ws_region, self.parse)
				return
			except:
				login = requests.post(url,headers=header,data=paramz)
				login = login.json()
			#print(login)
			
			if "error" in login:

				if login["error"] == "captcha_required":
					cprint(("Captcha required, Bypassing...","red"))
					captcha_id = login["data"]["captcha_url"]
					key = captcha_bypass.captchasolve(captcha_id)
					#payload = f'g-recaptcha-response={key}'
					#paramz1 = {'Host': 'api.ifunny.mobi','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://api.ifunny.mobi','Content-Length': f'{len(payload)}','Accept-Language': 'en-us','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148','Referer': f'{captcha_id}','Accept-Encoding': 'gzip, deflate'}
					#r = requests.post(url=captcha_id,headers=paramz1,data=payload,allow_redirects=False)
					
					cprint(("Logging in...","green"))
					try:
						login = requests.post(url,headers=header,data=paramz)
						login = login.json()
						print(login)
					except:
						raise LoginError("No worky")


					break
				if login["error"] == "unsupported_grant_type":
					time.sleep(10)
					continue
				if login["error"] == "too_many_user_auths":
					cprint(("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA (Too many user auths)","red"))
					raise LoginError("oops")
				if login["error"] == "forbidden":
					time.sleep(40)
					continue
			break
				

        

		token = login["access_token"]
		url = host+"/v4/account"
		daheader = {"Authorization":"Bearer "+token,'Ifunny-Project-Id': 'iFunny','User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)'}
		req = requests.get(url,headers = daheader)
		res = req.json()



		self.bearer = login["access_token"]
		self.user_id = res["data"]["id"]
		with open("D:\\iPartyBot\\bearer.json","r") as bearer_file:
			s = json.load(bearer_file)

			s["bearer"] = self.bearer
			s["user_id"] = self.user_id
			with open("D:\\iPartyBot\\bearer.json","w") as fi:
				json.dump(s,fi,indent=1)


		
		self.buff = ws_client.Buffer(self.bearer, self.user_id, self.ws_region, self.parse)
		
		
	def command(self, *args, **kwargs):
		def container(function):
		
			name = kwargs.get("name")
			if not name: name  = function.__name__
			name = name.lower()
			self.commands[name] = function
			
			if not kwargs.get("hide_help"):
				help_category = kwargs.get("help_category")
				if help_category: help_category = str(help_category).lower()
				
				if not self.help_categories.get(help_category):
					self.help_categories[help_category] = []
				
				self.help_categories[help_category].append(name)
				help_message = function.__doc__
				if kwargs.get("help_message"): help_message = kwargs.get("help_message")
				self.command_help_messages[function] = help_message
				
			if aliases := kwargs.get("aliases"):
				for alias in aliases:
					self.commands[alias] = function
					
			if cooldown := kwargs.get("cooldown"):
				self.cooldowns[function] = cooldown
				
			if kwargs.get("developer"):
				self.developer_commands.append(function)

			if kwargs.get("auth"):
				help_category = kwargs.get("help_category")
				if help_category: help_category = str(help_category).lower()
				
				if not self.auth_help_categories.get(help_category):
					self.auth_help_categories[help_category] = []
				
				self.auth_help_categories[help_category].append(name)
				help_message = function.__doc__
				if kwargs.get("help_message"): help_message = kwargs.get("help_message")
				self.auth_command_help_messages[function] = help_message
			
			def decorator(*dargs, **dkwargs):
				return function(*dargs, **dkwargs)
			
			return decorator
		return container
		
		
	def event(self, *args, **kwargs):
		def container(function):
		
			name = function.__name__
			valid_types = ("user_join", "user_leave", "user_kick", "channel_change", "on_join", "on_message", "on_file")
			assert (name in valid_types), "Function name for an event must be in "+", ".join(valid_types)
			
			if name in valid_types[4:]: setattr(self, name, function)
			else: self.events[name] = function

			def decorator(*dargs, **dkwargs):
				function(*dargs, **dkwargs)

			return decorator
		return container
		

	def run(self):
		
		try:
			asyncio.run(self.run_tasks())
		
		except KeyboardInterrupt:
			print()
			cprint(("Bot has shut down", "red"))
		
		except:
			cprint(("Bot has shut down due to error", "red"))
			traceback.print_exc()
		
		finally:
			self.blacklist_db_con.commit()
			self.blacklist_db_con.close()
			sys.exit(0)
			
		
	def disconnect(self):
		cprint(("Shutting down bot...", "red"))
		self.buff.disconnect()
		self.open = False
		

	async def run_tasks(self):
	
		self.message_queue = asyncio.Queue()
		await asyncio.gather(
			asyncio.create_task(self.message_queuer()),
			asyncio.create_task(self.buff.run()))
				
				
	async def siphon_input(self, callback, ctx):
		
		if ctx.chat.id in self.siphons:
			for t, q in self.siphons[ctx.chat.id].items():
				if t == any or type(ctx.message) == t:
					await q.put(ctx.message)
		
		if callback:
			self.run_callback(callback, ctx)
			
			
	async def input(self, chat_id, type=Message, timeout=None):
		
		if not self.siphons.get(chat_id):
			self.siphons[chat_id] = {}
			
		if not self.siphons[chat_id].get(type):
			self.siphons[chat_id].update({type: asyncio.Queue()})
		
		try:
			message = await asyncio.wait_for(self.siphons[chat_id][type].get(), timeout)
		
		except:
			message = None
			
		del self.siphons[chat_id][type]
		if not self.siphons[chat_id]:
			del self.siphons[chat_id]
			
		return message
		
		
	def blacklist(self, user=None):
		
		if not user:
			return list(self._blacklist)
		
		if isinstance(user, User):
			user = user.id
		
		if user == self.developer:
			return False
			
		self._blacklist.add(user)
		self.blacklist_db_con.execute("INSERT INTO users VALUES (?)", (user,))
		self.blacklist_db_con.commit()
		return True
		
		
	def whitelist(self, user):
		
		if isinstance(user, User):
			user = user.id
			
		if user not in self._blacklist:
			return False
			
		self._blacklist.remove(user)
		self.blacklist_db_con.execute("DELETE FROM users WHERE id = ?", (user,))
		self.blacklist_db_con.commit()
		return True


	def blacklistchat(self, chat=None):
		
		if not chat:
			return list(self._blacklistc)
		
		if isinstance(chat, Chat):
			chat = chat.id
	
			
		self._blacklistc.add(chat)
		self.blacklistc_db_con.execute("INSERT INTO users VALUES (?)", (chat,))
		self.blacklistc_db_con.commit()
		return True

	def whitelistchat(self, chat):
		
		
			
		if chat not in self._blacklistc:
			return False
			
		self._blacklistc.remove(chat)
		self.blacklistc_db_con.execute("DELETE FROM users WHERE id = ?", (chat,))
		self.blacklistc_db_con.commit()
		return True

	def auth(self, user=None):
		
		if not user:
			return list(self._auth)
		
		if isinstance(user, User):
			user = user.id
		
		#if user == self.developer:
		#	return False
			
		self._auth.add(user)
		self.auth_db_con.execute("INSERT INTO users VALUES (?)", (user,))
		self.auth_db_con.commit()
		return True

	def unauth(self, user):
		
		if isinstance(user, User):
			user = user.id
			
		if user not in self._auth:
			return False
			
		self._auth.remove(user)
		self.auth_db_con.execute("DELETE FROM users WHERE id = ?", (user,))
		self.auth_db_con.commit()
		return True

	def load_blacklist(self):
		
		self.blacklist_db_con = sqlite3.connect("libs/data/blacklist.db")
		self.blacklist_db_cur = self.blacklist_db_con.cursor()
		self.blacklist_db_cur.execute("CREATE TABLE IF NOT EXISTS users (id TEXT, unique(id))")
		self.blacklist_db_con.commit()
		self._blacklist = set([i[0] for i in self.blacklist_db_cur.execute("SELECT * FROM users")])

	def load_blacklistchat(self):
		
		self.blacklistc_db_con = sqlite3.connect("libs/data/chats.db")
		self.blacklistc_db_cur = self.blacklistc_db_con.cursor()
		self.blacklistc_db_cur.execute("CREATE TABLE IF NOT EXISTS users (id TEXT, unique(id))")
		self.blacklistc_db_con.commit()
		self._blacklistc = set([i[0] for i in self.blacklistc_db_cur.execute("SELECT * FROM users")])

	def load_auth(self):
		
		self.auth_db_con = sqlite3.connect("libs/data/auth.db")
		self.auth_db_cur = self.auth_db_con.cursor()
		self.auth_db_cur.execute("CREATE TABLE IF NOT EXISTS users (id TEXT, unique(id))")
		self.auth_db_con.commit()
		self._auth = set([i[0] for i in self.auth_db_cur.execute("SELECT * FROM users")])
			

	async def message_queuer(self):
	
		while self.open:
		
			if self.ratelimited:
				await asyncio.sleep(60)
				self.unratelimit()
				self.unconfirmed_queue = {}
				
				queue_dict = {}
				
				while not self.message_queue.empty():
					chat_id, message, nick = await self.message_queue.get()
					message = str(message)
					if not queue_dict.get(chat_id): queue_dict[chat_id] = []
					#if nick: message = nick+": "+message
					queue_dict[chat_id].append(message)
					
				for k, v in queue_dict.items():
					message = "\n\n".join(v)
					await self.message_queue.put((k, message, None))
					
				continue
					
			chat_id, message, nick = await self.message_queue.get()
			
			if self.ratelimited:
				await self.message_queue.put((chat_id, message, nick))
				continue
			
			try:
				payload = json.loads(bytes.fromhex(Parser.version).decode("utf-8"))
			
			except:
				return self.disconnect()
				
			request_id = int(time.time()*1000000)
			package = (chat_id, message, nick)
			self.unconfirmed_queue[request_id] = package
			
			try:
				await self.buff.send_ifunny_ws(await self.buff.form_ifunny_frame(
					{"type": "message", "message": message,
					"chat_id": chat_id,
					"request_id": request_id,
					"payload": payload}))
				
			except Exception as ex:
				cprint(("Failed to send message because:", "magenta"), (str(ex), "red"))
				
			
			
	async def send_message(self, chat_id, message, nick=None):
	
		chunks = textwrap.wrap(str(message), 500, break_long_words=True, replace_whitespace=False)
		
		for message in chunks:
			await self.message_queue.put((chat_id, message, nick))



	async def accept_invite(self, ctx):
		await self.buff.send_ifunny_ws(await self.buff.form_ifunny_frame({"type": "accept_invitation", "chat_id": ctx.chat.id}))
		if self.on_join:
			await asyncio.sleep(0.1)
			self.run_callback(self.on_join, ctx)
	async def reject_invite(self, ctx):
		await self.buff.send_ifunny_ws(await self.buff.form_ifunny_frame({"type": "decline_invitation", "chat_id": ctx.chat.id}))
		cprint(("Rejected invite from blacklist:","red"),(f"{ctx.chat.title}","cyan"))

	async def get_chat(self,chat_id):
		request_id = int(time.time()*1000)
		self.member_request_ids[request_id] = chat_id
		
		self.chat_list_queues[chat_id] = asyncio.Queue()
		await self.buff.send_ifunny_ws(await self.buff.form_ifunny_frame({"type": "get_chat","chat_id": chat_id, "request_id": request_id}))
		try:
			chat_info = await asyncio.wait_for(self.chat_list_queues[chat_id].get(), 3)
		except asyncio.TimeoutError:
			chat_info = []

		del self.chat_list_queues[chat_id]
		return chat_info
			
	async def get_members(self, chat_id):
		request_id = int(time.time()*1000)
		self.member_request_ids[request_id] = chat_id
		self.member_list_queues[chat_id] = asyncio.Queue()
		await self.buff.send_ifunny_ws(await self.buff.form_ifunny_frame({"type": "list_members", "chat_id": chat_id, "request_id": request_id}))
		
		try:
			member_list = await asyncio.wait_for(self.member_list_queues[chat_id].get(), 3)
		except asyncio.TimeoutError:
			member_list = []
			
		del self.member_list_queues[chat_id]
		member_list = [User(i, self) for i in member_list]
		return member_list
		
		
	async def invite(self, chat_id, user_id):
		await self.buff.send_ifunny_ws(await self.buff.form_ifunny_frame({"type": "send_invitation", "user_id": user_id, "chat_id": chat_id}))
		
		
	async def upload(self,chat_id,data,messageid=None):
		with open("bearer.json","r") as bearerfile:
				logindata = json.load(bearerfile)
				user_bearer = logindata["bearer"]
		print(len(data))
		print(messageid)
	
		


		headers = {
		    'Host': 'api.ifunny.mobi',
		    'Applicationstate': '1',
		    'Accept': 'video/mp4, image/jpeg',
		    'Content-Type': 'multipart/form-data; boundary=Boundary+363AD4A8776A5A3A',
		    'Authorization': 'Bearer '+user_bearer,
		    'Content-Length': f'{len(data)}',
		    'Ifunny-Project-Id': 'iFunny',
		    'User-Agent': 'iFunny/8.1.1(22616) iphone/14.0.1 (Apple; iPhone8,4)',
		    'Accept-Language': 'en-US;q=1',
		    'Accept-Encoding': 'gzip, deflate',
		}

		iFunnyContent.Content.__init__(self=iFunnyContent.Content,data=data,message_id=messageid,headers=headers)
		await iFunnyContent.Content.upload(self=iFunnyContent.Content)
		
		printout = await iFunnyContent.Content.status(self=iFunnyContent.Content)
		print(printout)
		

		
		#if response["error"]:
			#raise Exception(response)
			
		
	async def parse(self, frame):
	
		ctx = CTX(self)
	
		if hasattr(Parser, frame["type"]):
			await getattr(Parser, frame["type"])(self, ctx, frame)
						
						
	def ratelimit(self):
		if not self.ratelimited:
			self.ratelimited = True
			cprint(("Ratelimited", "red"))
		
		
	def unratelimit(self):
		if self.ratelimited:
			self.ratelimited = False
			cprint(("Ratelimit unlocked", "magenta"))
		
		
	async def run_command(self, function, ctx):
	
		if function in self.developer_commands and not ctx.author.is_developer:
			return
	
		ratelimit = self.cooldowns.get(function)
		now = time.time()
		
		if not ctx.author.is_developer:
			if ratelimit:
				user_timekeeping = self.timekeeping.get(ctx.author.id)
				if user_timekeeping:
					ratelimit_expires_at = user_timekeeping.get(function)
					if ratelimit_expires_at:
						if now < ratelimit_expires_at:
							remaining_time = int(ratelimit_expires_at-now)
							remaining_time_str = seconds_to_str(remaining_time)
							return await ctx.chat.send(f"You must wait {remaining_time_str} before you can use this command again")
						else:
							del self.timekeeping[ctx.message.author.id][function]
		
		if not self.timekeeping.get(ctx.author.id):
			self.timekeeping[ctx.author.id] = {}
			
		if self.cooldowns.get(function):
			self.timekeeping[ctx.author.id][function] = now+self.cooldowns[function]
		
		cprint((ctx.author.id, "yellow"), (ctx.author.nick, "green"), (ctx.message.text, "cyan"))
		self.run_callback(function, ctx, *ctx.message.args_list)
		
		
	def run_callback(self, function, *args):
		asyncio.get_event_loop().create_task(function(*args))


	def generate_help_command(self):
	
		@self.command(hide_help=True)
		async def help(ctx, *args):
			
			self = ctx.bot
		
			if args:
				
				if command_list := self.help_categories.get(args[0].lower()):
					response = "List of commands"
					response += f"\n▼{args[0].title()}\n\n"
					response += "\n".join([self.prefix+i for i in command_list
						if (not self.commands[i] in self.developer_commands or
						(ctx.author.is_developer and self.commands[i] in self.developer_commands))])
					response += f"\n\nUse \"{ctx.bot.prefix}help (command name)\" for detailed usage help."
			
				elif function := self.commands.get(args[0]):
					try:
						function_help = self.command_help_messages[function]
						if not function_help: function_help = "No help message for this command has been written"
						response = f"{self.prefix}{function.__name__}\n\n{function_help}"
					except:
						response = f"A category or command with that name does not exist. Check \"{self.prefix}help\" for the full list of commands."

					
				else:
					response = f"A category or command with that name does not exist. Check \"{self.prefix}help\" for the full list of commands."
				
			else:
				response = "List of command categories:\n\n"
				response += "\n".join(["‣"+i for i in self.help_categories.keys() if i])
				
				if None in self.help_categories:
					response += "\n\nFor support and feedback:\n"
					response += "\n".join([self.prefix+i for i in self.help_categories[None]
						if (not self.commands[i] in self.developer_commands or
						(ctx.author.is_developer and self.commands[i] in self.developer_commands))])
					
				response += f"\n\nUse \"{self.prefix}help (category)\" for detailed usage help."
				
			await ctx.chat.send(response)

		@self.command(hide_help=True)
		async def ahelp(ctx, *args):
			
			self = ctx.bot
			author = ctx.message.author
			if not author.auth:
				return
		
			if args:
				
				if command_list := self.auth_help_categories.get(args[0].lower()):
					response = "List of auth commands"
					response += f"\n▼{args[0].title()}\n\n"
					response += "\n".join([self.prefix+i for i in command_list
						if (not self.commands[i] in self.auth_commands or
						(ctx.author.auth and self.commands[i] in self.auth_commands))])
					response += f"\n\nUse \"{ctx.bot.prefix}ahelp (command name)\" for detailed usage help."
			
				elif function := self.commands.get(args[0]):
					function_help = self.auth_command_help_messages[function]
					if not function_help: function_help = "No help message for this command has been written"
					response = f"{self.prefix}{function.__name__}\n\n{function_help}"
					
				else:
					response = f"A category or command with that name does not exist. Check \"{self.prefix}help\" for the full list of commands."
				
			else:
				response = "List of auth categories:\n\n"
				response += "\n".join(["‣"+i for i in self.auth_help_categories.keys() if i])
				
				if None in self.auth_help_categories:
					response += "\n\nUncategorized Commands:\n"
					response += "\n".join([self.prefix+i for i in self.auth_help_categories[None]
						if (not self.commands[i] in self.developer_commands or
						(ctx.author.is_developer and self.commands[i] in self.developer_commands))])
					
				response += f"\n\nUse \"{self.prefix}ahelp (category)\" for detailed usage help."
				
			await ctx.chat.send(response)
		
		
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
		
class Content:
	
	upload_type = ""
	upload_status = "not_uploaded"
	task_id = None
	task_data = {}
	host = "https://api.ifunny.mobi/v4"

	def __init__(self, data, message_id, headers):

		self.data = data
		self.message_id = message_id
		self.headers = headers

	async def upload(self):	

		mime = fleep.get(self.data).mime
		self.mime = "image/jpeg"

		if mime:
			self.mime = mime[0]
		
			if self.mime.startswith("image/"):
				self.upload_type = "pic"
				
				if self.mime.endswith("/gif"):
					self.upload_type = "gif"
					
			elif self.mime.startswith("video/"):
				self.upload_type = "video_clip"
				
		else:
			print("Something went wrong here)")
			return {"error": True, "message": "Invalid file type"}
			
			
		form = aiohttp.FormData()
		form.add_field("type", self.upload_type)
		form.add_field("visibility", "chats")
		form.add_field("message_id", self.message_id)
			
		filename = f"{int(time.time()*1000)}.tmp"
		
		if self.upload_type in ("pic", "gif"):
			form.add_field("image", self.data, filename=filename, content_type="multipart/form-data")
		elif self.upload_type == "video_clip":
			form.add_field("video", self.data, filename=filename, content_type="multipart/form-data")
			
		async with aiohttp.ClientSession() as session:
			async with session.post(self.host+"/content", data=form, headers=self.headers) as r:
				response = await r.json()
				
				if response["status"] > 202:
					response["error"] = False
					return response
					
				else:
					self.task_id = response["data"]["id"]		
					self.upload_status = response["data"]["state"]
					return {"error": False, "message": "Uploading"}


	async def status(self, task_id=None):
	
		if not task_id:
			task_id = self.task_id
			
		if task_id:
			
			async with aiohttp.ClientSession() as session:
				async with session.get(self.host+"/tasks/"+task_id, headers=self.header) as r:
					return await r.json()
