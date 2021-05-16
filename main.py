import asyncio
import json
import time
import traceback
import random
from random import randint
import discord
from discord.ext import commands
import requests

prefix = "-"
bot = commands.Bot(command_prefix=prefix,  self_bot=False)


servers = len(bot.guilds)
members = 0
for guild in bot.guilds:
  members += guild.member_count - 1


from discord.ext import tasks

@tasks.loop(seconds=60.0)
async def my_background_task():
    """Will loop every 60 seconds and change the bots presence"""
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="discord.gg/bloxiscripts"))
    time.sleep(20)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="tickets"))
    time.sleep(20)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"-help on {len(bot.guilds)} servers!"))
    time.sleep(20)
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f'{servers} servers and {members} members'
    ))




    


@bot.event
async def on_ready():
    # Waiting until the bot is ready
    await bot.wait_until_ready()
    # Starting the loop
    my_background_task.start()
    print("ready")
  
keys = ["GPMSQLEGVMSWE23", "EZT2389094BZFS"]

snipe_message_author = {}
snipe_message_content = {}

bot.owner_ids = [405082152800354314, 674010830987067392, 832548865327759362]
bot.developer = 832548865327759362
bot.limited_guilds = [786083492710187025]
bot.prefix = "-"
bot.bypassallowed = [809422434327330836, 832548865327759362]

@bot.event
async def on_message_delete(message):
  bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

bot.sniped_messages = {}
@bot.command(name = 'snipe', aliases=['s', 'sn'])
async def snipe(ctx):
  contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]

  embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
  embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
  embed.set_footer(text=f"Deleted in : #{channel_name}")

  await ctx.channel.send(embed=embed)

@bot.command(name = 'cf', aliases=['coinflip', 'flipacoin'])
async def cf(message):
  outcome = ['heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'COIN LANDED ON ITS SIDE HOW THE HECK', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails', 'heads', 'tails']
  await message.channel.send(random.choice(outcome))

@bot.command()
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def embed(ctx, *, args):
  one, two, delete = args.split('|')
  embedVar = discord.Embed(title="{}".format(one), description="{}".format(two), color=discord.Color.green())
  if delete == 'y':
    await ctx.message.delete()
    await asyncio.sleep(0.1)
    bot.sniped_messages = {}
    await ctx.send(embed=embedVar)
  else:
    delete = 'n'
    if delete == 'n':
      await ctx.send(embed=embedVar)


@bot.command()
async def rip(message, *, args):
  author = message.author.mention
  deaths = ['{} hit the ground too hard.'.format(args), '{} was brutally murdered with a dandelion.'.format(args), '{} walked into the wrong theater and died of embarrassment.'.format(args), '{} only got a 98 on their math test and died.'.format(args), '{} stepped on a lego.'.format(args), '{}\'s mom said they had to order their own food so they died of social anxiety.'.format(args), '{} just straight up stopped existing.'.format(args), '{} picked a fight with the wrong neckbeard. (They got used as a chair)'.format(args), '{} made the mistake of telling an anime watcher how the manga goes.'.format(args), '{} tried to swim in lava.'.format(args), '{} got popcorn stuck in their gums.'.format(args), "{} didn't see the LITERAL AIRPLANE FALLING ON TOP OF THEM.".format(args), "{} managed to overdose on oxygen.".format(args), "{} didn't slap bass and died.".format(args), "{} found Herobrine and died.".format(args), "{} jammed a pencil up their nose.".format(args), "{} just got avada kedavra'd.".format(args), "{} died because they watched their crush swipe left.".format(args), "{} just didn't know anymore.".format(args), "{} fell from a high place.".format(args), "{} got a massage a bit too hard and died.".format(args), "{} burnt to a crisp.".format(args), "{} was pricked to death.".format(args), "{} tried to skydive but was struck by the plane elbow.".format(args), "{} told a simp Aqua was useless.".format(args), "{} was struck by lightning.".format(args), "{} told JEDIPUPPY255 that Japanese metal was bad and was eaten alive by Bloxhub.".format(args), "{} tried to eat [Bubble Bass's order](https://www.youtube.com/watch?v=0A67YpUs6sQ).".format(args), "{} clicked on [this link](https://www.youtube.com/watch?v=dQw4w9WgXcQ).".format(args), "Magikarp used splash... on dry land... but it was a critical hit and {} fainted and then died of hypothermia.".format(args), "{} tried to explain oxymoron to a moron... let's say it didnt go too well.".format(args), "{} tried to hug the grim reaper.".format(args), "{} got stabbed by the purple shirt eye stabber.".format(args), "{} tried to change skins in real life.".format(args), "{} tried to find their true soulmate but accidentally swiped right on a cannibal.".format(args), "{} was hit by Truck-sama.".format(args), "{} roasted themselves.".format(args), "{} forced the finger that wouldn't pop.".format(args), "{} got sick of {}'s crap and took {} to the grave with them.".format(args, author, author), "{} deflected for once. {} died instead.".format(args, author), "Huh. {} missed.".format(author), "{} ate a rat and died of the bubonic plague like an idiot.".format(args), "As it turns out, {} had terrible aim. {} lived to see another day.".format(author, args), "{} didn't listen to the Minecraft soundtrack enough and freaking died of uncultured-itis.".format(args), "{} sat too close to the guy with an AK-47 in each hand.".format(args), "{} didn't press F when asked to, forfeiting their life.".format(args), "{} encountered an angry chungus.".format(args), "{} was LITERALLY RIPPED IN HALF HOW THE HECK!?".format(args), "{} watched part 2 before part 1 and tried to understand what was going on.".format(args), "{} had their yubis stolen whilst watching HoloLive VTubers.".format(args), "{} was bonned.".format(args), "{} died while hiding in a bush trying to kill {}.".format(author, args), "{} didn't look both ways running across the street to kill {}.".format(author, args), "{} fell off of the train they tried to push {} off of.".format(author, args)]
  embedVar = discord.Embed(
        title="REST IN PEACE",
        description=(random.choice(deaths)),
        color=0x8b0000)
  await message.channel.purge(limit=1)
  await asyncio.sleep(0.1)
  bot.sniped_messages = {}
  await message.channel.send(embed=embedVar)


@bot.command()
async def qna(ctx, *, question=None):
  if question is None:
    await ctx.send('You need to ask a question, try again.')
  if question is not None:
    embeda = discord.Embed(title=f"{ctx.message.author.name}#{ctx.message.author.discriminator} asks:", description=question, color=discord.Color.purple(), timestamp=ctx.message.created_at)
    embeda.set_footer(text=f'Q&A created with the "-qna" command')
    await ctx.message.delete()
    await asyncio.sleep(0.1)
    bot.sniped_messages = {}
    await ctx.send(embed=embeda)


@bot.command(name = 'peepee', aliases=['pp'])
async def peepee(message, *, args):
  length = ["8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D", "8=======D", "8========D", "8=========D", "8==========D", "8===========D", "8============D", "8=============D", "8==============D", "8===============D", "8================D", '8=================D', "8==================D", "8===================D", "8====================D", "8=====================D"]
  embedVar = discord.Embed(title="pp size".format(args), description="{}'s peepee\n{}".format(args, random.choice(length)), color=0x00ff00)
  await message.channel.send(embed=embedVar)

@bot.command(name = 'pressf', aliases=['pf'])
async def pressf(message, *, args):
  embedVar = discord.Embed(title="F in the chat real quick", description="Press f for {}.".format(args), color=0x8b0000)
  await message.channel.send(embed=embedVar)

@bot.command()
async def relatable(message, *, args):
  embedVar = discord.Embed(title="This is so relatable!!!11!1!", description="{}".format(args), color=0x00ff00)
  await message.channel.send(embed=embedVar)


@bot.command(name = 'userinfo', aliases=['whois', 'ui'])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles[1:]]
    embed = discord.Embed(colour=discord.Colour.blue(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
  await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)  
async def role(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")


@bot.command(pass_context=True)
async def verify(ctx, args):
  if args in keys:
    role_variable = discord.utils.get(ctx.guild.roles, name=f"Member")
    await ctx.message.author.add_roles(role_variable)
    await ctx.send(f"Verified")
  else:
    await ctx.send("Wrong key! Get one from https://up-to-down.net/139931/VE")

@bot.command(pass_context=True)
async def getkey(ctx):
  await ctx.send("https://up-to-down.net/139931/VE")


@bot.command()
async def say(ctx, *, text=None):
    await ctx.channel.purge(limit=1)
    await asyncio.sleep(0.1)
    bot.sniped_messages = {}
    await ctx.channel.send(text)


@bot.command()
@discord.ext.commands.has_permissions(ban_members=True)
async def ban(message, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await message.channel.send(f"{user.mention} was banned for {reason}.")
  await user.send(f"You were banned from {message.guild.name}. Reason: {reason}.")

@bot.command()
@discord.ext.commands.has_permissions(ban_members = True)
async def unban(ctx, user: discord.Member = None):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = user.split("#")

  for ban_entry in banned_users:
    user = ban_entry.user
        
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.channel.send(f"Unbanned: {user.mention}")

@bot.command()
@discord.ext.commands.has_permissions(kick_members=True)
async def kick(message, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await message.channel.send(f"{user} was kicked for {reason}.")
  await user.send(f"You were kicked from {message.guild.name}. Reason: {reason}.")
@bot.command()
async def pm(message, user: discord.Member = None, *, text=None):
  if message.guild.id not in bot.limited_guilds:
    time = message.message.created_at
    embed = discord.Embed(title=f"Message from {message.message.author.name}#{message.message.author.discriminator}!", description=text, timestamp=time)
    embed.set_footer(text=f"Use the {bot.prefix}pm command in a server you share with this user to respond! If you don't know how the command works, use {bot.prefix}help in a server that Bloxhub is in.")
    embed1 = discord.Embed(title=f"Message to {user.name}#{user.discriminator}!", description=text, timestamp=time)
    embed1.set_footer(text="Hope they respond!")
    await message.channel.purge(limit=1)
    await asyncio.sleep(0.1)
    bot.sniped_messages = {}
    if user is None:
      await message.channel.send('My guy who you wanna message lol doofus')
    if user is not None:
      if text is None:
        await message.channel.send('Mate I can\'t just DM them nothingness.')
      if text is not None:
        await user.send(embed=embed)
        await message.message.author.send(embed=embed1)
  else:
    await message.channel.send('This server is limited (meaning some commands are disabled by JEDIPUPPY255#0050).')

@bot.command()
async def apm(ctx, user: discord.Member = None, *, text=None):
  if ctx.message.author.id in bot.owner_ids:
    time = ctx.message.created_at
    embed = discord.Embed(title=f"Message from anonymous!", description=text, timestamp=time)
    embed.set_footer(text=f"Use the {bot.prefix}pm command in a server you share with this user to respond! If you don't know how the command works, use {bot.prefix}help in a server that Bloxhub is in.")
    embed1 = discord.Embed(title=f"Message to {user.name}#{user.discriminator}!", description=text, timestamp=time)
    embed1.set_footer(text="Hope they respond!")
    await ctx.channel.purge(limit=1)
    await asyncio.sleep(0.1)
    bot.sniped_messages = {}
    if user is None:
      await ctx.send('My guy who you wanna message lol doofus')
    if user is not None:
      if text is None:
        await ctx.send('Mate I can\'t just DM them nothingness.')
      if text is not None:
        await user.send(embed=embed)
        await ctx.message.author.send(embed=embed1)
  else:
     await ctx.send('You don\'t have permission to do that.')

@bot.command()
async def ipm(ctx, fake, user: discord.Member = None, *, text=None):
  if ctx.message.author.id in bot.owner_ids:
    time = ctx.message.created_at
    embed = discord.Embed(title=f"Message from {fake}!", description=text, timestamp=time)
    embed.set_footer(text=f"Use the {bot.prefix}pm command in a server you share with this user to respond! If you don't know how the command works, use {bot.prefix}help in a server that Bloxhub is in.")
    embed1 = discord.Embed(title=f"Message to {user.name}#{user.discriminator}!", description=text, timestamp=time)
    embed1.set_footer(text="Hope they respond!")
    await ctx.channel.purge(limit=1)
    await asyncio.sleep(0.1)
    bot.sniped_messages = {}
    if user is None:
      await ctx.send('My guy who you wanna message lol doofus')
    if user is not None:
      if text is None:
        await ctx.send('Mate I can\'t just DM them nothingness.')
      if text is not None:
        await user.send(embed=embed)
        await ctx.message.author.send(embed=embed1)
  else:
     await ctx.send('You don\'t have permission to do that.')

@bot.command()
@discord.ext.commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="Muted", description=f"{member.mention} was muted", color=discord.Color.green())
    embed.add_field(name="Reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" You have been muted in: {guild.name}. Reason: {reason}")

@bot.command(name = "tempmute", aliases=['tm'])
@discord.ext.commands.has_permissions(manage_messages=True)
async def tempmute(ctx, member: discord.Member, time, *, reason=None):
    guild = ctx.guild
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    time_convert = {"s":1, "m":60, "h":3600,"d":86400}
    tempmute = int(time[:-1]) * time_convert[time[-1]]
    await member.add_roles(muted_role, reason=reason)
    embeda = discord.Embed(title="Muted", description= f"{member.mention} was muted for {time}.", color=discord.Color.green())
    embeda.add_field(name="Reason:", value=reason, inline=False)
    await ctx.send(embed=embeda)
    await member.send(f" You have been muted in: {guild.name} for {tempmute} seconds. Reason: {reason}")
    await asyncio.sleep(tempmute)
    await member.remove_roles(muted_role)

@bot.command()
@discord.ext.commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="Unmuted", description=f"{member.mention} was unmuted", color=discord.Color.green())
    await ctx.send(embed=embed)
    await member.remove_roles(mutedRole)
    await member.send(f"You have been unmuted in {guild.name}.")   





@bot.command()
@discord.ext.commands.has_permissions(manage_messages=True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
        await ctx.send("Nuked the Channel sucessfully!")

    else:
        await ctx.send(f"No channel named {channel.name} was found!")



        
bot.run("ODQzNDkyNzYwNTM0MTIyNTA2.YKEp2Q.3LcHA1ISAMt5DRE0Ksw9B6hnA8A", bot=True) 
