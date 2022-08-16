import requests
import json
import urllib
import urllib.parse
import re
import time
import os
import random
import io
from PIL import Image
import aiohttp
import fleep


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
