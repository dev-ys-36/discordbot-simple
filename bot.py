import discord
import base64

token_key = 'OTQwNjAxNzE4OTA1OTIxNTk2.YgJxnQ.ck2fuepwlVV9vdG4qpmp4p6YNNE'

client = discord.Client()

@client.event
async def on_ready():
    print(f'Start on {client.user}')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content.startswith('^encode'):
        msg = message.content[8:]
        base64_ = base64.b64encode(msg.encode('utf-8'))
        await message.channel.send(base64_)

    if message.content.startswith('^decode'):
        msg = message.content[8:]
        base64_ = base64.b64decode(msg).decode('utf-8')
        await message.channel.send(base64_)

client.run(token_key)
