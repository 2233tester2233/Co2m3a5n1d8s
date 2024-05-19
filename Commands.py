# commands.py
from discord.ext import commands

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
    
    @selfbot.command()
    async def copy(ctx, *urls):
        await ctx.message.delete()
        folder = "videos"
        if not os.path.exists(folder):
            os.makedirs(folder)
        for url in urls:
            try:
                youtube = YouTube(url)
                if youtube.length and youtube.description and youtube.length < 60 and youtube.description.startswith("Shorts"):
                    video = youtube.streams.filter(only_video=True).order_by('resolution').desc().first()
                else:
                    video = youtube.streams.get_highest_resolution()
                video.download(output_path=folder)
                print(tk.END, f"{SUCCESS} Video copyied: {url}")
            except Exception as e:
                print(f"{ERROR} {str(e)}")
