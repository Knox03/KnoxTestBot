import discord
import os
import insults
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


def run_discord_bot():
    TOKEN = os.getenv('STanni_TOKEN')
    owner_id = 64637190816137216
    guild_id = 1097884698899914803
    text_category_id = 1097884698899914804
    voice_category_id = 1097884698899914805

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    def is_owner(ctx):
        return ctx.author.id == owner_id
         
    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')
        global tts_state
        tts_state = False
        print(tts_state)
        
    @bot.event
    async def on_member_join(member):
        channel = bot.get_channel(1097884698899914806)
        await channel.send(f"Welcome {member.name}")
        await member.send(f"Welcome to Server von Knox")

    @bot.command()
    async def tts_check(ctx):
        print(tts_state)

    @bot.command()
    async def say(ctx, message):
        print(tts_state)
        await ctx.send(str(message), tts = tts_state)

    @bot.command()
    async def maul(ctx):
        await ctx.send(f"Dann halt ich mein Maul, du Arsch")
        global tts_state
        tts_state = False
        print(tts_state)
    
    @bot.command()
    async def rede(ctx):
        await ctx.send(f"Viel Spaß mit meiner Kackstimme")
        global tts_state
        tts_state = True
        print(tts_state)

    @bot.command()
    async def insult(ctx):
        await ctx.send(insults.choose_insult(), tts = tts_state)


    @bot.command()
    @commands.check(is_owner)
    async def shutdown(ctx):
        await ctx.send('shutting down')
        exit()

    @bot.command()
    @commands.check(is_owner)
    async def members(ctx):
        m_list = []
        for guild in bot.guilds:
            for m in guild.members:
                m_list.append(m)
        user = await bot.fetch_user(owner_id)
        await user.send(f"{m_list}")

    @bot.command()
    @commands.check(is_owner)
    async def channels(ctx):
        c_list = []
        for guild in bot.guilds:
            for c in guild.channels:
                c_list.append(str(c))
        user = await bot.fetch_user(owner_id)
        await user.send(f"{c_list}")
    
    @bot.command()
    @commands.check(is_owner)
    async def new_text(ctx, name,):
        guild = bot.get_guild(guild_id)
        category = get(guild.categories, id=text_category_id)
        await guild.create_text_channel(name, category=category)

    @bot.command()
    @commands.check(is_owner)
    async def new_voice(ctx, name):
        guild = bot.get_guild(guild_id)
        category = get(guild.categories, id=voice_category_id)
        await guild.create_voice_channel(name, category=category)

    @bot.command()
    async def mare(ctx):
        embed = discord.Embed(
            title='Mares Leben', 
            url = 'https://www.youtube.com/watch?v=61u15V02Xwo', 
            color = 0xFF5733, 
            description = 'Mares Leben da er no bitches hat',
            type = 'image'
            )
        
        embed.add_field(name = 'kek', value = '```hurensohn```', inline = True)
        embed.add_field(name = 'kek2', value = '`hurensohn2`', inline = False)
        embed.set_image(url = 'http://imgur.com/VH8U8wOb.jpg')
        await ctx.send(embed = embed)




    
    bot.run(TOKEN)
    
    # @bot.event
    # async def on_message(message):
    #     if message.author == bot.user:
    #         return
    #     if message.content[0] == '$':
    #         return
        
    #     username = str(message.author)
    #     user_message = str(message.content)
    #     channel = str(message.channel)

    #     print(f"{username} said: '{user_message}' in {channel}")

    #     if user_message[0] == '?':
    #         user_message = user_message[1:]
    #         await send_message(message, user_message, is_private=True)
    #     else:
    #         await send_message(message, user_message, is_private=False)
    
    
    

# async def send_message(message, user_message, is_private):
#     try:
#         response = responses.handle_responses(user_message)
#         print(response)
        
#         await message.author.send(response) if is_private else await message.channel.send(response)
#     except Exception as e:
#         print(e)
