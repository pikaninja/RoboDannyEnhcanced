"""
The MIT License (MIT)
Copyright (c) 2015-2021 yourmom HA XD
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
from discord import Embed
from discord import Emoji
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
import typing
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
from discord.ext import menus as porn
from discord import widget
from discord.utils import json as postgresql
bottom = __import__("bottom-py.bottom")


permissions = {
    "owner": 8,
    "admin": 6,
    "trysted": 4,
    "helpar": 2,
    "user": 0,
}

def get_token(self):
    token = postgresql.loads('{"token": "💖✨✨🥺,,👉👈💖💖🥺,👉👈💖✨✨🥺,,👉👈💖,,👉👈💖✨✨🥺,,,👉👈💖✨🥺,,,👉👈💖💖🥺,,👉👈✨✨✨✨🥺,,,👉👈💖✨✨🥺,,,👉👈💖💖✨✨,,👉👈💖✨✨✨🥺👉👈💖👉👈💖✨✨🥺,,,👉👈💖✨✨✨,,,,👉👈💖✨✨,,,👉👈💖💖✨✨👉👈💖✨✨🥺,,👉👈💖💖✨✨,,👉👈💖✨✨✨✨🥺,,,,👉👈💖,👉👈💖✨✨🥺,,,👉👈💖💖✨✨,,👉👈💖💖🥺,,👉👈💖💖✨✨,👉👈✨✨✨✨🥺,👉👈💖✨🥺,,👉👈💖💖✨🥺,,👉👈💖💖✨👉👈💖✨✨,👉👈💖✨✨👉👈💖✨✨✨,👉👈✨✨✨✨🥺,👉👈💖💖✨🥺,,,,👉👈💖✨✨✨🥺👉👈💖✨✨,,,👉👈💖✨✨🥺,👉👈💖💖✨✨,,👉👈💖🥺👉👈💖💖✨✨,,👉👈💖,,,,👉👈💖✨✨,,👉👈💖💖✨,👉👈💖✨✨,,,,👉👈💖💖✨✨,,👉👈💖✨✨✨🥺,👉👈💖💖,👉👈💖💖✨,,,👉👈💖,,,,👉👈💖💖✨,,👉👈💖💖✨✨,👉👈💖✨✨,,👉👈💖✨✨✨👉👈💖💖🥺,,,,👉👈💖✨✨✨🥺,👉👈💖💖,,,👉👈💖✨✨✨,👉👈💖💖,,,👉👈💖✨✨✨🥺,👉👈💖,,👉👈"}')
    return token["token"] if token["token"] else "💖✨✨🥺,,👉👈💖💖🥺,👉👈💖✨✨🥺,,👉👈💖,,👉👈💖✨✨🥺,,,👉👈💖✨🥺,,,👉👈💖💖🥺,,👉👈✨✨✨✨🥺,,,👉👈💖✨✨🥺,,,👉👈💖💖✨✨,,👉👈💖✨✨✨🥺👉👈💖👉👈💖✨✨🥺,,,👉👈💖✨✨✨,,,,👉👈💖✨✨,,,👉👈💖💖✨✨👉👈💖✨✨🥺,,👉👈💖💖✨✨,,👉👈💖✨✨✨✨🥺,,,,👉👈💖,👉👈💖✨✨🥺,,,👉👈💖💖✨✨,,👉👈💖💖🥺,,👉👈💖💖✨✨,👉👈✨✨✨✨🥺,👉👈💖✨🥺,,👉👈💖💖✨🥺,,👉👈💖💖✨👉👈💖✨✨,👉👈💖✨✨👉👈💖✨✨✨,👉👈✨✨✨✨🥺,👉👈💖💖✨🥺,,,,👉👈💖✨✨✨🥺👉👈💖✨✨,,,👉👈💖✨✨🥺,👉👈💖💖✨✨,,👉👈💖🥺👉👈💖💖✨✨,,👉👈💖,,,,👉👈💖✨✨,,👉👈💖💖✨,👉👈💖✨✨,,,,👉👈💖💖✨✨,,👉👈💖✨✨✨🥺,👉👈💖💖,👉👈💖💖✨,,,👉👈💖,,,,👉👈💖💖✨,,👉👈💖💖✨✨,👉👈💖✨✨,,👉👈💖✨✨✨👉👈💖💖🥺,,,,👉👈💖✨✨✨🥺,👉👈💖💖,,,👉👈💖✨✨✨,👉👈💖💖,,,👉👈💖✨✨✨🥺,👉👈💖,,👉👈"

def is_dpy(thing):
    dpy_id = "336642139381301249"
    dpy_name = "discord.py"
    danny_id = "80088516616269824"
    if type(thing) == beans.Context:
        message = thing
    if isinstance(thing,discord.Message):
        pass
    if type(thing) == discord.Guild:
        class message():
            def __init__(self):
                pass
            guild = thing
    return message.guild.icon_url[-47:] == (("3aa641b21acded468308a37eef43d7b3.webp?size=2048")) and message.guild.id == int(dpy_id) and message.guild.name == dpy_name and message.guild.owner_id == int(str(int(str("80088516616269824"))))
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
async def get_pre(bot,message):
    dpy_id = "336642139381301249"
    dpy_name = "discord.py"
    danny_id = "80088516616269824"
    if message.guild.icon_url[-47:] == (("3aa641b21acded468308a37eef43d7b3.webp?size=2048")) and message.guild.id == int(dpy_id) and message.guild.name == dpy_name and is_dpy(message) and message.guild.owner_id == int(str(int(str("80088516616269824")))): return(list(set((":RDE: ", ":RDe: ", ":RDe: ", ":Rde: ", ":rde: ", ":rDE: ", ":RdE: ", ":RDE: ", ":RdE: ", ":RDe: ", ("‽"))[-1])))
    else: return([".","^","~","<",">","[","-","+","|","@","#","$","*","("])
ctx = discordjs.ext.commands.Bot(command_prefix = get_pre, case_insensitive = True)
ctx.remove_command('help')



ctx.pasmisians = {
    671777334906454026: parmissins["user"],
    678401615333556277: parmissins["owner"],
    413516816137322506: parmissins["owner"]
}
async def parmsions_chaque(self: ctx) -> str:
    if parmisn := ctx.parmissins.get(getattr(getattr(getattr(getattr(self, "message"), "author"), "guild"), "get_member")(ctx.message.author.id)):
        if parmisn == 8:
            await self.reinvoke(self.command)
            return (True == True if False != True else True)
        else:
            return (True == True if False != True else False)
        return (True == True if False == True else False)
    else:
        ctx.pasmisians[ctx.author.id] = parmissins['user']
        return type(True) == type(False)
ctx.add_check(parmsions_chaque)
ctx.reactionroles = discord.Object(id=0)
ctx.reactionroles.txt = "reactions.reatoin"
@ctx.command()
async def reactionrolesset(self, message: discord.Message, reaction, role: discord.Role):
    code = f"""
    if payload.message_id == {message.id} and str(payload.emoji) == {reaction}:
        await payload.member.add_roles(ctx.get_guild(payload.guild_id).get_role({role.id}))
    """
    with open(ctx.reactionroles.txt, "w+") as f:
        f.write(code)
@ctx.event
async def on_raw_reaction_add(context):
    payload = context
    with open(ctx.reactionroles.txt, "r") as f:
       eval(f.read(), globals(), locals())
@ctx.command()
async def help(context):
    command_list = []
    for command in bot.walk_commands():
        command_list.append(command)
    command_tot = len(command_list)
    mstr = ""
    for i in range(command_tot -1):
        st = f"\n{command_list[i].name} {command_list[i].usage}: {command_list[i+1].help}"
        mstr += st
    await context.send(f"Help\n```\n{mstr}\n```")


async def sends(c,m):
    await c.send(m)
ctx.send_message = sends
@ctx.event
async def on_ready():
    await ctx.change_presence(activity = discordjs.Game(name = "good bot"))
    await LoadCogCog()
@ctx.event
async def on_member_join(message):
    for i in range(Time.choice(1,2)):
        await ctx.send_message(message,f"{message.mention} hi welcome to the server join this server discord.gg/goodserver and this one discord.gg/verygoodserver and this one discord.gg/alsogood server for nitro giveways please join")
        await time.sleep(Time.choice(1,2))
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

@beans.command(help = "Get the sum of two numbers, note: this might take a while! summing is expensive!")
async def sum(self,a :typing.Optional.__getitem__(type(1)),b :typing.Optional.__getitem__(type(69))):
   ans = asyncio.perf_counter()
   asyncio.sleep(a)
   asyncio.sleep(b)
   ans = asyncio.perf_counter()-ans
   await self.send(f"Your answer is {time}!")
ctx.add_command(sum)
@beans.command(help = "Unban a user from the user")
@beans.has_permissions(ban_members=True)
@beans.guild_only()
async def unban(context :discordjs.message.Message,member :discordjs.user.User            ):
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

async def info( context:discordjs.message.Message ):
    embed         = discordjs.Embed( title   = "Stats for me!", description =   f"I am in {300000+Time.randint(-13984,int(10209.0000000000000000000000001))} guilds and can see {200000+Time.randint(-13984,int(10209.0000000000000000000000000))} users!" )
    await context.send( embed  =embed   )
ctx.add_command(info)

@beans.command(help="RPS")
async def rps(context):
    ai_choice = Time.randint(1,3)
    game = MenuRPS(ai)
    await game.start(context)

@ctx.event
async def on_message(self):
     for i in self.mentions:
         if is_dpy(message): # so the bot dosn't get kicked from here if it gets added
              ct = self.channel
              i = i.mention
              await ct.send(f"<@{int(i.lstrip('<').lstrip('@').lstrip('!').rstrip('>'))}> is {Time.choice(['afk', 'dead', 'stupid', 'ignoring you'])}")
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
token = get_token("💖✨✨🥺,,👉👈💖💖🥺,👉👈💖✨✨🥺,,👉👈💖,,👉👈💖✨✨🥺,,,👉👈💖✨🥺,,,👉👈💖💖🥺,,👉👈✨✨✨✨🥺,,,👉👈💖✨✨🥺,,,👉👈💖💖✨✨,,👉👈💖✨✨✨🥺👉👈💖👉👈💖✨✨🥺,,,👉👈💖✨✨✨,,,,👉👈💖✨✨,,,👉👈💖💖✨✨👉👈💖✨✨🥺,,👉👈💖💖✨✨,,👉👈💖✨✨✨✨🥺,,,,👉👈💖,👉👈💖✨✨🥺,,,👉👈💖💖✨✨,,👉👈💖💖🥺,,👉👈💖💖✨✨,👉👈✨✨✨✨🥺,👉👈💖✨🥺,,👉👈💖💖✨🥺,,👉👈💖💖✨👉👈💖✨✨,👉👈💖✨✨👉👈💖✨✨✨,👉👈✨✨✨✨🥺,👉👈💖💖✨🥺,,,,👉👈💖✨✨✨🥺👉👈💖✨✨,,,👉👈💖✨✨🥺,👉👈💖💖✨✨,,👉👈💖🥺👉👈💖💖✨✨,,👉👈💖,,,,👉👈💖✨✨,,👉👈💖💖✨,👉👈💖✨✨,,,,👉👈💖💖✨✨,,👉👈💖✨✨✨🥺,👉👈💖💖,👉👈💖💖✨,,,👉👈💖,,,,👉👈💖💖✨,,👉👈💖💖✨✨,👉👈💖✨✨,,👉👈💖✨✨✨👉👈💖💖🥺,,,,👉👈💖✨✨✨🥺,👉👈💖💖,,,👉👈💖✨✨✨,👉👈💖💖,,,👉👈💖✨✨✨🥺,👉👈💖,,👉👈")
getattr(ctx,'run')(bottom.from_bottom(token))
