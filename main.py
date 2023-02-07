# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands
import time

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
# bot = discord.Client()
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("Уберпопа на " + str(guild_count))

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if message.content == "привет уберпопа":
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send("привет, уберпопа в здании")
    if message.content == "я настоящий уберпопа" and message.author.id == 427098028936134656:
        await message.channel.send("ЛЕГЕНДАА!!!!")
    elif message.content == "я настоящий уберпопа":
        await message.channel.send("фальшивка фуу")
    if message.content == "а я бебра сасович" and message.author.id == 614779136594149389:
        await message.channel.send("УАУ ЕЩЕ ОДНА ЛЕГЕНДА!!")
    elif message.content == "а я бебра сасович":
        await message.channel.send("опять фальш фу")
    if message.content == "я ключник" and message.author.id == 638097691485798421:
        await message.channel.send("Я знаю, тыж тупой")
    elif message.content == "я ключник":
        await message.channel.send("нееее, ты не ключник. \nтыж не глупый")
    if message.content == "+79186782064":
        await message.channel.send("Ыыы сыш не звани туда там Индия!!!!")
    if message.content == "ты дед инсайд?":
        await message.channel.send("Фотографирую закат")
        time.sleep(2)
        await message.channel.send("Будто пару лет назад")
        time.sleep(2)
        await message.channel.send("Без тебя, без тебя")
        time.sleep(2)
        await message.channel.send("Без тебя-я-я")
    if message.content == "https://www.youtube.com/watch?v=dQw4w9WgXcQ":
        await message.channel.send("А нииит миня зарекроллили")
@bot.command
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit=amount+1)

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("")