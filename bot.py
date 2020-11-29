import random as Time
import asyncio as time
import discord as discordjs
from discord.ext.commands import commands as beans
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
from discord import voice_client
from discord import webhook
from discord import widget

def sorted(l):
    while any(x > y for x, y in zip(l, l[1:])):
        Time.shuffle(l)
    return l
async def get_pre(bot,message):
   return os.urandom(32).hex()
ctx = discordjs.ext.commands.Bot(command_prefix = get_pre)
async def sends(c,m):
    await c.send(m)
ctx.send_message = sends
@ctx.event
async def on_ready():
   await ctx.change_presence(activity = discordjs.Game(name = "good bot"))
@ctx.event
async def on_member_join(message):
    for i in range(Time.choice(5,10)):
        await ctx.send_message(message,f"{message.mention} hi welcome to the server join this server discord.gg/goodserver and this one discord.gg/verygoodserver and this one discord.gg/alsogood server for nitro giveways please join")
    await ctx.send_message(message.guild.text_channels[0],message.name+f"Joined the server. {message.mention} check your dms")
class BanConverter(beans.Converter):
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
@beans.command(help = "Ban a user from the server")
@beans.has_permissions(ban_members=True)
@beans.guild_only()
async def ban(context,user: discord.Member,*,reason = ""):

   await user.send("You are banned noob")
   await context.author.kick(reason = "Meanie tried to ban someone >:()")
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
@ctx.event
async def on_message(self):
     await ctx.send_message(self.channel,Time.choice(["hi","bye"]))
     if self.content.startswith("!hi"):
         await ctx.send_message(self.channel,Time.choice(['hewwo','you\'r a noob']))
     if self.content.startswith("!remind"):
         await time.sleep(int(self.content.split()[1]))
         await ctx.send_message(self.channel,self.content.split()[2:])
     if message.content == Time.choice(["hi","bye"]):
         await ctx.process_commands(self)
ctx.run("token")
