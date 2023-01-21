import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.command()
async def giveadmin(ctx, member: discord.Member):
    admin_role = discord.utils.get(ctx.guild.roles, name="admin")
    await member.add_roles(admin_role)
    await ctx.send(f'{member.mention} has been given the admin role.')

@client.command()
async def showadmincommands(ctx):
    commands = ['!ban', '!kick', '!mute', '!unmute']
    await ctx.send('Admin commands: ' + ', '.join(commands))

client.run('MTA2NjM4NTQ5MzMyOTE5MTA3NA.G3ykmj.suCx57BC-50X-ci9eMrFvnpIqp6a1MqIA3kb7U')
import discord
from discord.ext import commands
import random
from datetime import timedelta
import asyncio

client = commands.Bot(command_prefix = '!')

# Generate a random code for admin access
admin_code = str(random.randint(100000, 999999))

# Store the expiration time for temporary admin access
temp_admin_expire = None

@client.command()
async def giveadmin(ctx, member: discord.Member):
    # Check if the member already has the admin role
    admin_role = discord.utils.get(ctx.guild.roles, name="admin")
    if admin_role in member.roles:
        await ctx.send(f'{member.mention} already has the admin role.')
        return

    # Check if the user has temporary admin access
    if temp_admin_expire is not None and temp_admin_expire > ctx.message.created_at:
        await member.add_roles(admin_role)
        await ctx.send(f'{member.mention} has been given temporary admin access.')
    else:
        # Send the code to the user and wait for them to enter it
        await ctx.send(f'Please send the code {admin_code} to {member.mention}')
        def check(m):
            return m.content == admin_code and m.author == member
        try:
            msg = await client.wait_for('message', check=check, timeout=60.0)
            await member.add_roles(admin_role)
            await ctx.send(f'{member.mention} has been given the admin role.')
        except asyncio.TimeoutError:
            await ctx.send(f'{member.mention} did not provide the code in time.')

@client.command()
async def radmin(ctx, member: discord.Member):
    global temp_admin_expire
    temp_admin_expire = ctx.message.created_at + timedelta(hours=24)
    await ctx.send(f'{member.mention} has been given temporary admin access for 24 hours')
    
@client.command()
async def code111(ctx, member: discord.Member):
    admin_role = discord.utils.get(ctx.guild.roles, name="admin")
    await member.add_roles(admin_role)
    await ctx.send(f'{member.mention} has been given the admin role permanently')

@client.command()
async def showadmincommands(ctx):
    commands = ['!ban', '!kick', '!mute', '!unmute' '!radmin' '!code111']
    await ctx.send('Admin commands: ' + ', '.join(commands))
    
# Add new commands here
@client.command()
async def command1(ctx, args):
    # Your code here
    pass

@client.command()
async def command2(ctx):
    # Your code here
    pass

@client.command()
async def command3(ctx, args1, args2):
    # Your code here
  pass