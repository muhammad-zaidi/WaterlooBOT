import discord
from discord.ext import commands
from translate import Translator


class translation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("translation.py is ready")

    @commands.command()
    async def translate(self, ctx, *, message):
        if message == "help":
            await ctx.send(
                "Type !translation x y [the word/sentence you want to be translated] where x and y are the ISO 639-1 CODES of the languages you want to be translated.")
            await ctx.send(
                "x is the language you want to translate from. y is the language you want to translate to")
        else:
            init_lang = message[0:2]
            to_lang = message[3:5]
            trans_message = message[6:]
            translator = Translator(from_lang=init_lang, to_lang=to_lang)
            translation = translator.translate(trans_message)
            await ctx.send(translation)


def setup(client):
    client.add_cog(translation(client))
