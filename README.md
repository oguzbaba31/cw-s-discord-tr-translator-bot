# cw-s-translator
cw's translator simple discord translator bot. currently available en to tr.

This code defines a Discord bot that can translate text using the Helsinki-NLP/opus-mt-tc-big-en-tr model from the Hugging Face Transformers library. The bot listens for messages starting with the command prefix '!' and then uses the Translation class to translate the content of the message. The Translation class preprocesses the text by tokenizing it and using the WordNet module from the Natural Language Toolkit (nltk) library to handle word order differences between languages.

The Translation class has three methods:

init(): This initializes the class by creating an instance of the Helsinki-NLP/opus-mt-tc-big-en-tr model using the Transformers library and caching the results using functools.lru_cache with a maxsize of 128.

preprocess_content(content): This method takes in a string of text and preprocesses it by tokenizing the text using nltk.word_tokenize and then using WordNet to handle word order differences between languages. The method returns the preprocessed text as a string.

get_translation(content): This method takes in a string of text and first preprocesses it using preprocess_content. Then, it passes the preprocessed text to the Helsinki-NLP/opus-mt-tc-big-en-tr model to get a translation. The method returns the translated text as a string.

The main function of the bot is the cevir command, which takes in a string of text as input and passes it to the translate method of the Translation class. The translate method splits the input text into lines and creates an asyncio task for each line to get the translation using the get_translation method of the Translation class. The tasks are then gathered using asyncio.gather and the translated text is sent back to the Discord channel using the ctx.send method. If an error occurs during the translation process, the bot sends an error message to the Discord channel.

Overall, this code uses the Discord API, the Transformers library, and the nltk library to create a simple translation bot for Discord.

Here's a breakdown of the code:

The necessary libraries are imported:

discord: A Python wrapper for the Discord API that provides an easy way to interact with Discord servers and users.

pipeline from transformers: A library that provides easy-to-use APIs for using pre-trained transformer models.

commands from discord.ext: An extension of the discord library that provides additional functionality for creating commands and managing them.

asyncio: A library for writing asynchronous code in Python.

uuid: A library for generating UUIDs.

functools: A library that provides tools for working with functions.

nltk: A library for natural language processing in Python.

wordnet from nltk.corpus: A lexical database for English that provides synonyms and antonyms for words.

The wordnet database is downloaded using nltk.download('wordnet').


An instance of the commands.Bot class is created with the prefix ! and all intents enabled.

The Translation class is defined. It contains the following methods:

__init__: Initializes the class by creating an instance of the translation pipeline.

preprocess_content: Processes the content by tokenizing the words and applying morphology to account for differences in word order between languages.

get_translation: Translates the content by passing it through the translation pipeline.

translate: Accepts a command context and content to be translated, splits the content into separate lines, and creates tasks to translate each line asynchronously. It then sends the translations as separate messages to the Discord server.

An instance of the Translation class is created.


The cevir command is defined using the @bot.command() decorator. It accepts a command context and a string argument content and passes them to the translate method of the Translation class.

The Discord bot is started by calling the run method on the bot instance and passing in a bot token.

Overall, this script creates a translation bot that can be used in a Discord server by invoking the !cevir command followed by the content to be translated. The bot uses the Helsinki-NLP/opus-mt-tc-big-en-tr model to translate Turkish to English.
