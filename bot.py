import discord
import os


def token():
    with open("WaterlooBOT/token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = token()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run(token)
