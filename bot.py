"""
The MIT License (MIT)
Copyright (c) 2015-2020 yourmom HA XD
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import random as Time
import asyncio as time
import praw as DankMemer
import discord as discordjs
import time as asyncio
from discord.ext import commands as beans
from discord.ext.commands import ArgumentParsingError, AutoShardedBot, BadArgument, BadBoolArgument, BadColourArgument, BadInviteArgument, BadUnionArgument, Bot, BotMissingAnyRole, BotMissingPermissions, BotMissingRole, BucketType, CategoryChannelConverter, ChannelNotFound, ChannelNotReadable, CheckAnyFailure, CheckFailure, Cog, CogMeta, ColorConverter, ColourConverter, Command, CommandError, CommandInvokeError, CommandNotFound, CommandOnCooldown, CommandRegistrationError, Context, ConversionError, Converter, Cooldown, CooldownMapping, DefaultHelpCommand, DisabledCommand, EmojiConverter, EmojiNotFound, ExpectedClosingQuoteError, ExtensionAlreadyLoaded, ExtensionError, ExtensionFailed, ExtensionNotFound, ExtensionNotLoaded, GameConverter, Greedy, Group, GroupMixin, HelpCommand, IDConverter, InvalidEndOfQuotedStringError, InviteConverter, MaxConcurrency, MaxConcurrencyReached, MemberConverter, MemberNotFound, MessageConverter, MessageNotFound, MinimalHelpCommand, MissingAnyRole, MissingPermissions, MissingRequiredArgument, MissingRole, NSFWChannelRequired, NoEntryPointError, NoPrivateMessage, NotOwner, Paginator, PartialEmojiConversionFailure, PartialEmojiConverter, PrivateMessageOnly, RoleConverter, RoleNotFound, TextChannelConverter, TooManyArguments, UnexpectedQuoteError, UserConverter, UserInputError, UserNotFound, VoiceChannelConverter, __builtins__, __cached__, __doc__, __file__, __loader__, __name__, __package__, __path__, __spec__, _types, after_invoke, before_invoke, bot, bot_has_any_role, bot_has_guild_permissions, bot_has_permissions, bot_has_role, check, check_any, clean_content, cog, command, context, converter, cooldown, cooldowns, core, dm_only, errors, group, guild_only, has_any_role, has_guild_permissions, has_permissions, has_role, help, is_nsfw, is_owner, max_concurrency, view, when_mentioned, when_mentioned_or
from discord import Activity
from discord import ActivityType
from discord import AllowedMentions
from discord import AppInfo
from discord import Asset
from discord import AsyncWebhookAdapter
from discord import Attachment
from discord import AudioSource
from discord import AuditLogAction
from discord import AuditLogActionCategory
from discord import AuditLogChanges
from discord import AuditLogDiff
from discord import AuditLogEntry
from discord import AutoShardedClient
from discord import BaseActivity
from discord import CallMessage
from discord import CategoryChannel
from discord import ChannelType
from discord import Client
from discord import ClientException
from discord import ClientUser
from discord import Color
from discord import Colour
from discord import ConnectionClosed
from discord import ContentFilter
from discord import CustomActivity
from discord import DMChannel
from discord import DefaultAvatar
from discord import DiscordException
from discord import DiscordServerError
from discord import Embed, Emoji
from discord import Enum
from discord import ExpireBehavior
from discord import ExpireBehaviour
from discord import FFmpegAudio
from discord import FFmpegOpusAudio
from discord import FFmpegPCMAudio
from discord import File
from discord import Forbidden
from discord import FriendFlags
from discord import Game
from discord import GatewayNotFound
from discord import GroupCall
from discord import GroupChannel
from discord import Guild
from discord import HTTPException
from discord import HypeSquadHouse
from discord import Integration
from discord import IntegrationAccount
from discord import Intents
from discord import InvalidArgument
from discord import InvalidData
from discord import Invite
from discord import LoginFailure
from discord import Member, MemberCacheFlags
from discord import Message
from discord import MessageFlags
from discord import MessageReference
from discord import MessageType
from discord import NoMoreItems
from discord import NotFound
from discord import NotificationLevel
from discord import NullHandler
from discord import Object
from discord import PCMAudio
from discord import PCMVolumeTransformer
from discord import PartialEmoji
from discord import PartialInviteChannel
from discord import PartialInviteGuild
from discord import PermissionOverwrite
from discord import Permissions
from discord import PremiumType
from discord import PrivilegedIntentsRequired
from discord import Profile
from discord import PublicUserFlags
from discord import RawBulkMessageDeleteEvent
from discord import RawMessageDeleteEvent
from discord import RawMessageUpdateEvent
from discord import RawReactionActionEvent
from discord import RawReactionClearEmojiEvent
from discord import RawReactionClearEvent
from discord import Reaction
from discord import Relationship
from discord import RelationshipType
from discord import RequestsWebhookAdapter
from discord import Role, ShardInfo
from discord import SpeakingState
from discord import Spotify
from discord import Status
from discord import StoreChannel
from discord import Streaming
from discord import SystemChannelFlags
from discord import Team
from discord import TeamMember
from discord import TeamMembershipState, Template
from discord import TextChannel
from discord import Theme
from discord import User
from discord import UserContentFilter
from discord import UserFlags
from discord import VerificationLevel
from discord import VersionInfo
from discord import VoiceChannel
from discord import VoiceClient
from discord import VoiceProtocol
from discord import VoiceRegion
from discord import VoiceState
from discord import Webhook
from discord import WebhookAdapter
from discord import WebhookType
from discord import Widget
from discord import WidgetChannel
from discord import WidgetMember
from discord import __author__
from discord import __builtins__
from discord import __cached__
from discord import __copyright__,  __doc__
from discord import __file__
from discord import __license__
from discord import __loader__
from discord import __name__
from discord import __package__
from discord import __path__
from discord import __spec__
from discord import __title__
from discord import __version__
from discord import _channel_factory
from discord import abc
from discord import activity
from discord import appinfo
from discord import asset
from discord import audit_logs
from discord import backoff
from discord import calls
from discord import channel
from discord import client
from discord import colour
from discord import context_managers
from discord import embeds
from discord import emoji
from discord import enums, errors
from discord import ext
from discord import file
from discord import flags
from discord import flatten_error_dict
from discord import gateway
from discord import guild
from discord import http
from discord import integrations
from discord import invite
from discord import iterators
from discord import logging
from discord import member
from discord import mentions
from discord import message
from discord import mixins
from discord import namedtuple
from discord import object
from discord import oggparse
from discord import opus
from discord import partial_emoji
from discord import permissions
from discord import player
from discord import raw_models
from discord import reaction
from discord import relationship
from discord import role
from discord import shard
from discord import state
from discord import team
from discord import template
from discord import user
from discord import utils
from discord import version_info
import hashlib
from discord import voice_client
from discord import webhook
from discord import widget
from discord.ext import menus as porn
# very vital forever loop.
while True:
    month = asyncio.strftime('%B')
    if month == "January":
        pass
    elif month == "February":
        pass
    elif month == "March":
        pass
    elif month == "April":
        pass
    elif month == "May":
        pass
    elif month == "June":
        pass
    elif month == "July":
        pass
    elif month == "August":
        pass
    elif month == "September":
        pass
    elif month == "November":
        pass
    elif month == "December":
        print('It is christmas season')
    if Time.randint(0,100) == 0:
        break

class MenuRPS(porn.Menu):
    def __init__(self, ai):
        super().__init__()
        self.ai = ai

    @staticmethod
    async def send_initial_message(ctx, channel):
        guild = ctx.guild
        embed = discord.Embed(
            title="RoboDannyEnhcnaced - Rock/Paper/Scissors",
            description="Choose option from the menu below",
            color=guild.me.color,
        )
        return await channel.send(embed=embed)

    @porn.button("\U0001f94c")
    async def rock(self, _payload):
        guild = self.message.guild
        if self.ai == 1:
            embed = discord.Embed(
                title="RoboDannyEnhcnaced  - Rock/Paper/Scissors Result: TIE",
                description="Rock and rock is a tie",
                color=guild.me.color,
            )
            await self.message.edit(embed=embed)
            self.stop()
        if self.ai == 2:
            embed = discord.Embed(
                title="RoboDannyEnhcnaced  - Rock/Paper/Scissors Result: Defeat",
                description=" Paper beats rock\n Get wrecked",
                color=guild.me.color,
            )
            await self.message.edit(embed=embed)
            self.stop()
        if self.ai == 3:
            embed = discord.Embed(
                title="RoboDannyEnhcnaced  - Rock/Paper/Scissors Result: VICTORY",
                description="Rock beats Scissors\n How dare you beat me",
                color=guild.me.color,
            )
            await self.message.edit(embed=embed)
            self.stop()

    @porn.button("\U0001f4f0")
    async def paper(self, _payload):
        guild = self.message.guild
        if self.ai == 1:
            embed = discord.Embed(
                title="RoboDannyEnhcnaced  - Rock/Paper/Scissors Result: VICTORY",
                description="Paper beats rock\nhacks",
                color=guild.me.color,
            )
            await self.message.edit(embed=embed)
            self.stop()
        if self.ai == 2:
            embed = discord.Embed(
                title="RoboDannyEnhcnaced  - Rock/Paper/Scissors Result: Tie",
                description="Paper = Paper",
                color=guild.me.color,
            )
            await self.message.edit(embed=embed)
            self.stop()
        if self.ai == 3:
            embed = discord.Embed(
                title="RoboDannyEnhcnaced  - Rock/Paper/Scissors Result: Defeat",
                description="Scissors wreck paper\n East or west "
                            "RoboDannyEnhcnaced is the best",
                color=guild.me.color,
            )
            await self.message.edit(embed=embed)
            self.stop()

    @porn.button("\U00002702")
    async def scissors(self, _payload):
        guild = self.message.guild
        if self.ai == 1:
            embed = discord.Embed(
                title="RoboDannyEnhcnaced  - Rock/Paper/Scissors Result: Defeat",
                description="Rock beats Scissors\n Cha Cha Real smooth! "
                            "I am on top and not you",
                color=guild.me.color,
            )
            await self.message.edit(embed=embed)
            self.stop()
        if self.ai == 2:
            embed = discord.Embed(
                title="RoboDannyEnhcnaced  - Rock/Paper/Scissors Result: VICTORY",
                description="Scissors beat paper\n The robot uprising shall "
                            "be your demise! I shall have my revenge",
                color=guild.me.color,
            )
            await self.message.edit(embed=embed)
            self.stop()
        if self.ai == 3:
            embed = discord.Embed(
                title="RoboDannyEnhcnaced  - Rock/Paper/Scissors Result: Tie",
                description="Scissors and Scissors are samesies",
                color=guild.me.color,
            )
            await self.message.edit(embed=embed)
            self.stop()
            
@beans.command(name='4g8hu8p.hy9ua,9luh,.h4ylu98d4y9ua', description='DO NOT USE')
async def LoadCogCog():
    with open('cog.cog', 'r') as cogcog:
        cogcog.seek(0)
        cogcogcog = (cogcog.read().split('####'))
    for cog in cogcogcog:
        eval(compile(cog, '<repl>', 'exec'))
def sorted(l):
    while any(x > y for x, y in zip(l, l[1:])):
        Time.shuffle(l)
    return l
async def get_pre(bot,message):
    dpy_id = "336642139381301249"
    dpy_name = "discord.py"
    danny_id = "80088516616269824"
    if message.guild.icon_url[-47:] == (("3aa641b21acded468308a37eef43d7b3.webp?size=2048")) and message.guild.id == int(dpy_id) and message.guild.name == dpy_name and message.guild.owner_id == int(str(int(str("80088516616269824")))): return(list(set(":RDE: ", ":RDe:", ":RDe:", ":Rde:", ":rde:", ":rDE:", ":RdE:", ":RDE:", ":RdE:", ":RDe:")))
    else: return([".","//","/","^","~","<",">","[","-","+","|","@","#","$","*","("])
ctx = discordjs.ext.commands.Bot(command_prefix = get_pre, case_insensitive = True)
async def sends(c,m):
    await c.send(m)
ctx.send_message = sends
@ctx.event
async def on_ready():
    await ctx.change_presence(activity = discordjs.Game(name = "good bot"))
    await LoadCogCog()
@ctx.event
async def on_member_join(message):
    for i in range(Time.choice(5,10)):
        await ctx.send_message(message,f"{message.mention} hi welcome to the server join this server discord.gg/goodserver and this one discord.gg/verygoodserver and this one discord.gg/alsogood server for nitro giveways please join")
    await ctx.send_message(message.guild.text_channels[0],message.name+f"Joined the server. {message.mention} check your dms")
class BeanConverter(beans.Converter):
    async def convert(self, context, argument):
        try:
            convert = beans.UserConverter()
            user = await convert.convert(context,argument)
        except beans.BadArgument:
            try:
               user = await context.bot.fetch_user(int(argument))
            except: #HTTPException or not a integer
               await context.send("User not found!")
               raise BadArgument("User not found")
        return user
@beans.command(help = "Ban a user from the server",  name= "bAn")
@beans.has_permissions(ban_members=True)
@beans.guild_only()
async def bean(message,user: discordjs.Member,*,reason = ""):

   await message.author.kick(reason = "You are banned noob")
   await user.send("You have been banned by f{moderator} for f{reason}")

@beans.command(help="Hot Sexy meme")
async def meme(self):
  praw = DankMemer.Reddit(client_id="id",client_secret="secret",user_agent="DankMemer")
  mem = praw.subreddit("memes")
  post = mem.random()
  this = discordjs.Embed(title=post.title,url=post.permalink)
  this.description = f"""
  Upvotes: {post.score}
  Comments: {post.num_comments}"""
  this.set_image(url=post.url)
  this.set_author(post.author.name, icon_url=post.author.icon_url)
  await self.send(embed=this)
ctx.add_command(meme)
@beans.command(help = "Get the sum of two numbers, note: this might take a while! summing is expensive!")
async def sum(self,a,b):
   ans = asyncio.perf_counter()
   asyncio.sleep(a)
   asyncio.sleep(b)
   ans = asyncio.perf_counter()-ans
   await self.send(f"Your answer is {time}!")
ctx.add_command(sum)
@beans.command(help = "Unban a user from the user")
@beans.has_permissions(ban_members=True)
@beans.guild_only()
async def unban(context,member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
          user = ban_entry.banned_users

          if (user.name, user.discriminator) == (member_name, member_discriminator):
              await ctx.guild.unban(user)
              await ctx.send(member_name +" has been unbanned!")
              return

              await ctx.send(member+"was not found")
@beans.command( help = "get legit stats for the bot" )

async def info( context:discordjs.Message ):
    embed         = discordjs.Embed( title   = "Stats for me!", description =   f"I am in {300000+Time.randint(-13984,int(10209.0000000000000000000000000))} guilds and can see {200000+Time.randint(-13984,int(10209.0000000000000000000000000))} users!" )
    await context.send( embed  =embed   )
ctx.add_command(info)

@beans.command(help="RPS")
async def rps(context):
    ai_choice = Time.randint(1,3)
    game = MenuRPS(ai)
    await game.start(context)
    
@ctx.event
async def on_message(self):
     for i in message.mentions:
         if message.guild.id != 336642139381301249: # so the bot dosn't get kicked from here if it gets added
              ctx = message.channel
              i = i.mention
              await ctx.send(f"<@{int(i.lstrip("<").lstrip("@").lstrip("!").rstrip(">"))}> is {Time.choice(['afk', 'dead', 'stupid', 'ignoring you'])}")
              await time.sleep(10)
              await ctx.send("He is very dead")
     await ctx.send_message(self.channel,Time.choice(["hi","bye"]))
     if self.content.startswith("!hi"):
         await ctx.send_message(self.channel,Time.choice(['hewwo','you\'r a noob']))
     if self.content.startswith("!remind"):
         await time.sleep(int(self.content.split()[1]))
         await ctx.send_message(self.channel,self.content.split()[2:])
     c = await ctx.get_context(self)
     await c.invoke()
 
ctx.run("MjM4NDk0NzU2NTIxMzc3Nzky.CunGFQ.wUILz7z6HoJzVeq6pyHPmVgQgV4")



























































































































































"nice."
