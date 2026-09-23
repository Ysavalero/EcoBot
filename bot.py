import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f"EcoBot está conectado como {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("¡Hola! 🌱 Soy EcoBot.")


@bot.command()
async def tip(ctx):
    await ctx.send("🌱 Un pequeño cambio también cuenta. ¡Intentá reducir el uso de productos descartables!")


bot.run("TU_TOKEN_ACÁ")

