import json
import discord
from discord.ext import commands
import os
import ctypes
import Commands
import keyboard
import datetime
import colorama
import json
import asyncio
import shutil
import webbrowser
import urllib
import requests
import subprocess
import tkinter as tk
import importlib.util
from tkinter import ttk
from PIL import Image, ImageFilter
from pytube import YouTube
from colorama import Fore, Style
from discord.ext.commands import check
from io import BytesIO
import aiohttp
from pystyle import Colorate, Colors, Center, Box

with open('selfbot.py', 'r', encoding='utf-8') as file:
    code = file.read()

def save_config(config_data):
    with open('config.json', 'w') as file:
        json.dump(config_data, file, indent=4)

with open('config.json') as f:
    config = json.load(f)
    prefix = config['prefix']
    token = config['token']

selfbot = commands.Bot(command_prefix=prefix, self_bot = True)

@selfbot.event
async def on_command(ctx):
    print(f'{COMMAND} {ctx.message.content}')

SUCCESS = f"{datetime.datetime.now().strftime('%H:%M')} │ \033[1;92m[SUCCESS]\033[0m │ "
INFO = f"{datetime.datetime.now().strftime('%H:%M')} │ \033[1;94m[INFO]\033[0m │ "
ERROR = f"{datetime.datetime.now().strftime('%H:%M')} │ \033[91m[ERROR]\033[0m │ "
COMMAND = f"{datetime.datetime.now().strftime('%H:%M')} │ \033[36m[COMMAND]\033[0m │ "

logo = Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, """


    ███████╗██╗   ██╗███╗   ██╗████████╗██╗  ██╗██████╗  ██████╗ ████████╗    ██╗   ██╗██████╗ 
    ██╔════╝╚██╗ ██╔╝████╗  ██║╚══██╔══╝██║  ██║██╔══██╗██╔═══██╗╚══██╔══╝    ██║   ██║╚════██╗
    ███████╗ ╚████╔╝ ██╔██╗ ██║   ██║   ███████║██████╔╝██║   ██║   ██║       ██║   ██║ █████╔╝
    ╚════██║  ╚██╔╝  ██║╚██╗██║   ██║   ██╔══██║██╔══██╗██║   ██║   ██║       ╚██╗ ██╔╝██╔═══╝ 
    ███████║   ██║   ██║ ╚████║   ██║   ██║  ██║██████╔╝╚██████╔╝   ██║        ╚████╔╝ ███████╗
    ╚══════╝   ╚═╝   ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝         ╚═══╝  ╚══════╝

                                        
"""))

def SYNTHBOTLOADED():
    print(logo)

os.system(f"mode con: cols=99 lines=45")

@selfbot.event
async def on_ready():
    friends_count = len(selfbot.user.friends)
    server_count = len(selfbot.guilds)
    print(Colorate.Vertical(Colors.purple_to_blue, f"""
┌──────────────────────────────────────────────────────────────────────┐
                Successfully logged into \033[0m{selfbot.user.name}  

                Account information ►                   

                   Prefix  ►  \033[0m{config['prefix']} \n
└──────────────────────────────────────────────────────────────────────┘                                    
"""))
    print(f"""

┌──────────────────────────────────────────────────────────────────┐
│                        Develepor Information                     │
└──────────────────────────────────────────────────────────────────┘      
 """)
    print(f"Discord version  ►  {discord.__version__} \n")
    print("_______________________________________________________________________________________")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Synthbot - v1 - Welcome back {selfbot.user.name} ")
    Commands.setup(selfbot)
    colorama.init()

SYNTHBOTLOADED()

try:
    selfbot.run(token, bot=False)
except discord.errors.LoginFailure:
    print(f"Status ► \033[1;91mNot Connected\033[0m")
    print(f"{INFO}Make sure The Token Is Correct.")
