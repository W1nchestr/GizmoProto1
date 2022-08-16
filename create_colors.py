import random
import json
import asyncio
import os


async def get_file_by_name(name=None):
    file_src = f"C:\\Users\\Admin\\Desktop\\iPartyBot\\user_databases\\"+name
    with open(file_src,"r") as file:
        data = json.load(file)

    return data

async def update_data_by_name(data=None,user=None):
    file_src = f"C:\\Users\\Admin\\Desktop\\iPartyBot\\user_databases\\{user}"
    with open(file_src,"w") as chatfile:
        json.dump(data,chatfile,indent=1)


async def create_color():
    colors = ["red","orange","yellow","green","blue","purple","tan","black","white"]
    emojis = ["🔴","🟠","🟡","🟢","🔵","🟣","🟤","⚫","⚪"]

    rcolor = random.choice(colors)

    rcolor_emoji = emojis[colors.index(rcolor)]
    data = {}
    data["name"] = rcolor
    data["emoji"] = rcolor_emoji
    return data


async def colors():


    x = os.listdir("./user_databases")
    index = 0
    totals = {}
    for user in x:
        data = await get_file_by_name(user)
        garage = data["garage"]

        data["garage"] = []
        data['wallet'] = 0
        data['job'] = ""
        data['last_worked'] = 0
        data['next_shift'] = 0
        data['wage'] = 0
        data['hours'] = 0
        data['listed'] = []
        data['searched'] = 0
        if data.get("auth"):
            del data['auth']
        if data.get('kit'):
            del data['kit']
        if data.get('chess_wins'):
            del data['chess_wins']
        if data.get('chance'):
            del data['chance']
        print(index)
        index += 1
        
        await update_data_by_name(data,user)
    msg = f"TEST\n\nEveryone's colors was set"
    print(msg)

asyncio.run(colors())

