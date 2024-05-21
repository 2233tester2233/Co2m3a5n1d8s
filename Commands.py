# commands.py
from discord.ext import commands
import discord
import asyncio
import requests
import subprocess
import urllib

import os
import random
from pytube import YouTube
from bs4 import BeautifulSoup
import json
from discord.ext import tasks
from datetime import datetime, timedelta
from colorama import Fore, Style
from discord.ext import commands,tasks
from PIL import Image, ImageDraw, ImageFont
from pystyle import Colorate, Colors, Center, Box

with open('selfbot.py', 'r', encoding='utf-8') as file:
    code = file.read()

def save_config(config_data):
    with open('config.json', 'w') as file:
        json.dump(config_data, file, indent=4)

with open('config.json') as f:
    config = json.load(f)
    prefix = config['prefix']

def setup(selfbot):
    @selfbot.command(name="search", description="Lets you search")
    async def search(ctx, *, query):
        query_string = urllib.parse.urlencode({'q': query})
        await ctx.send(f"[{query_string}](https://www.google.com/search?{query_string})")
        
    @selfbot.command()
    async def test(ctx):
        await ctx.send("sucessfull")
        
    @selfbot.command()
    async def prefix(new_prefix):
        with open('config.json', 'r') as f:
            prefixes = json.load(f)
        prefixes["prefix"] = new_prefix
        with open('config.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        print(f"Prefix changed to: {new_prefix}")
