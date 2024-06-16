from discord.ext import commands
import discord

def setup(selfbot):
    @selfbot.command()
    async def test(ctx):
        await ctx.send("sucessfull")
