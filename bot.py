import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


# Cuando el bot se conecta
@bot.event
async def on_ready():
    print(f"EcoBot está conectado como {bot.user}")


# Comando de bienvenida
@bot.command()
async def hello(ctx):
    await ctx.send(
        " ¡Hola! Soy EcoBot.\n"
        "Estoy acá para ayudarte a aprender sobre el ambiente "
        "y los hábitos sostenibles."
    )


# Lista de consejos
consejos = [
    " Intentá reducir el uso de productos descartables.",
    " Cerrá la canilla mientras te cepillás los dientes.",
    " Apagá las luces cuando no las estés usando.",
    " Usá bolsas reutilizables cuando puedas.",
    " Si es posible, elegí caminar o andar en bicicleta para distancias cortas.",
    " Cuidar los espacios verdes también ayuda al ambiente."
]


# Comando de consejos
@bot.command()
async def tip(ctx):
    consejo = random.choice(consejos)
    await ctx.send(f" Consejo ecológico:\n{consejo}")


# Lista de retos
retos = [
    " Separá los residuos reciclables durante todo el día.",
    " Intentá ahorrar agua hoy.",
    " Caminá en lugar de usar un vehículo para un trayecto corto.",
    " Usá una botella reutilizable durante el día.",
    " Apagá las luces de las habitaciones que no estés usando.",
    " Durante hoy, evitá un producto descartable."
]


# Comando de retos
@bot.command()
async def reto(ctx):
    reto_elegido = random.choice(retos)
    await ctx.send(f" Tu reto ecológico de hoy es:\n{reto_elegido}")


# Información sobre reciclaje
@bot.command()
async def reciclaje(ctx):
    await ctx.send(
        " Guía rápida de reciclaje:\n\n"
        " Cartón y papel → residuos reciclables.\n"
        " Latas → residuos reciclables.\n"
        " Vidrio → residuos reciclables si está limpio.\n"
        " Restos de comida → residuos orgánicos.\n"
        " Pilas y electrónicos → necesitan puntos de recolección especiales."
    )


# Información sobre cambio climático
@bot.command()
async def clima(ctx):
    await ctx.send(
        " El cambio climático es una alteración a largo plazo "
        "de las temperaturas y los patrones climáticos.\n\n"
        "Una de sus principales causas actuales es el aumento de gases "
        "de efecto invernadero producido por actividades humanas.\n\n"
        " Reducir el desperdicio y usar los recursos de manera "
        "responsable son algunas formas de contribuir al cuidado del ambiente."
    )


# Pregunta educativa
preguntas = [
    {
        "pregunta": "¿Qué gas contribuye al efecto invernadero?",
        "respuesta": "El dióxido de carbono (CO₂) es uno de los principales gases de efecto invernadero."
    },
    {
        "pregunta": "¿Qué significa reciclar?",
        "respuesta": "Reciclar significa transformar materiales usados para poder utilizarlos nuevamente."
    },
    {
        "pregunta": "¿Por qué es importante ahorrar agua?",
        "respuesta": "Porque el agua dulce disponible es limitada y es necesaria para los seres vivos."
    }
]


@bot.command()
async def pregunta(ctx):
    pregunta_elegida = random.choice(preguntas)

    await ctx.send(
        f" {pregunta_elegida['pregunta']}\n\n"
        f" Respuesta: {pregunta_elegida['respuesta']}"
    )


# Comando de ayuda
@bot.command()
async def ayuda(ctx):
    await ctx.send(
        "COMANDOS DE ECOBOT"
        "$hello → Te doy la bienvenida.\n"
        "$tip → Te doy un consejo ambiental.\n"
        "$reto → Te propongo un reto sostenible.\n"
        "$reciclaje → Te explico cómo separar algunos residuos.\n"
        "$clima → Te cuento sobre el cambio climático.\n"
        "$pregunta → Te hago una pregunta educativa.\n"
        "$eco → Te doy un mensaje para motivarte."
    )


# Mensaje motivador
@bot.command()
async def eco(ctx):
    mensajes = [
        "Cada pequeño hábito puede formar parte de un cambio más grande.",
        "Cuidar el planeta también empieza con nuestras decisiones diarias.",
        "No hace falta hacerlo todo perfecto. ¡Empezar ya es importante!",
        "Tus acciones de hoy pueden ayudar a construir un futuro más sostenible."
    ]

    await ctx.send(random.choice(mensajes))


# Iniciar el bot
bot.run("TU_TOKEN_ACÁ")
