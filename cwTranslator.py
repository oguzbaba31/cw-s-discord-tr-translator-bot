import discord
from transformers import pipeline
from discord.ext import commands
import asyncio
import uuid
import functools
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

class Translation:
    def __init__(self):
        self.translator = functools.lru_cache(maxsize=128)(pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-tr"))

    async def preprocess_content(self, content):
        # Dil önişlemesi yaparak kelime sırası farklılıklarını ele al
        words = nltk.word_tokenize(content)
        words = [wordnet.morphy(word) or word for word in words]
        return " ".join(words)

    async def get_translation(self, content):
        content = await self.preprocess_content(content)
        translated_text = self.translator(content)
        return translated_text[0]["translation_text"]

    async def translate(self, ctx, content):
        try:
            lines = content.split('\n')
            tasks = []

            for line in lines:
                task = asyncio.create_task(self.get_translation(line))
                tasks.append(task)

            translations = await asyncio.gather(*tasks)

            sent_messages = set()

            for i, translation in enumerate(translations):
                if translation not in sent_messages:
                    sent_messages.add(translation)
                    await ctx.send(f"{translation}")

        except Exception as e:
            await ctx.send(f"Hata oluştu: {e}")

translation = Translation()

@bot.command()
async def cevir(ctx, *, content: str):
    await translation.translate(ctx, content)

bot.run('BOT_TOKEN)
