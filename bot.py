import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'hola soy {bot.user} y te voy ayudar a reciclar :)')

@bot.command()
async def adolescentes(ctx):
    await ctx.send(f'Te voy a dar unos consejos para inicies reciclar 🤭')
    await ctx.send(f'Aquí tienes 5 consejos prácticos para comenzar a reciclar siendo adolescente:')
    await ctx.send(f'1.Aprende a separar los residuos: Investiga cómo se clasifican los residuos en tu ciudad o escuela (orgánicos, papel, plástico, vidrio, metales). Puedes poner contenedores separados en tu casa o cuarto.')
    await ctx.send(f'2.Reduce y reutiliza antes de reciclar: Evita usar cosas desechables como botellas de plástico o bolsas. Reutiliza libretas, ropa o frascos antes de tirarlos.')
    await ctx.send(f'3.Involucra a tu familia y amigos: Cuéntales lo que estás haciendo y por qué es importante. Juntos pueden hacer más, y quizás hasta crear un mini centro de reciclaje en casa o en el cole.')
    await ctx.send(f'4.Infórmate y comparte en redes: Usa tu celular para seguir cuentas de reciclaje, ver videos o leer tips. Compartir lo que aprendes puede inspirar a otros adolescentes como tú.')
    await ctx.send(f'5.Haz pequeños proyectos de reciclaje creativo (upcycling): Convierte objetos viejos en algo útil o decorativo, como latas en macetas o camisetas viejas en bolsas. ¡Es divertido y ayuda al planeta!')

@bot.command()
async def adultos(ctx):
    await ctx.send(f'Te voy a dar unos consejos y recomendaciones para aplicar las tres R en tu vida diaria 😁')
    await ctx.send(f'♻ 1. Reducir')
    await ctx.send(f'-Objetivo: Consumir menos y evitar el desperdicio.')
    await ctx.send(f'-Compra solo lo necesario: Planifica tus compras para evitar alimentos que se echen a perder o productos que no usarás.')
    await ctx.send(f'-Evita productos con mucho empaque: Elige opciones a granel o sin plástico innecesario.')
    await ctx.send(f'-Lleva tus propios envases: Usa botellas reutilizables, bolsas de tela y recipientes para comida.')
    await ctx.send(f'-Desconecta aparatos eléctricos que no uses: Ahorras energía y reduces tu impacto ambiental.')
    await ctx.send(f'♻ 2. Reutilizar')
    await ctx.send(f'-Objetivo: Darle una segunda vida a los objetos.')
    await ctx.send(f'-Dale nueva vida a lo viejo: Usa frascos de vidrio como organizadores o ropa vieja como trapos de limpieza.')
    await ctx.send(f'-Repara antes de reemplazar: Arregla ropa, electrodomésticos o muebles antes de tirarlos.')
    await ctx.send(f'-Compra de segunda mano: Ahorras dinero y evitas la fabricación de nuevos productos.')
    await ctx.send(f'-Usa papel por ambos lados: En casa o en la oficina, maximiza el uso del papel.')
    await ctx.send(f'♻ 3. Reciclar')
    await ctx.send(f'-Objetivo: Transformar residuos en nuevos productos.')
    await ctx.send(f'-Separa correctamente tus residuos: Aprende qué materiales se reciclan en tu zona (papel, cartón, plástico, vidrio, etc.).')
    await ctx.send(f'-Limpia los envases antes de reciclarlos: Los residuos sucios no se pueden reciclar bien.')
    await ctx.send(f'-Lleva residuos especiales a centros de acopio: Como pilas, electrónicos o aceite usado.')
    await ctx.send(f'-Infórmate sobre los puntos verdes locales: Muchos supermercados, escuelas o municipios tienen centros de reciclaje.')

@bot.command()
async def viejos(ctx):
    await ctx.send(f'Te voy a dar unas ideas para decorar tu casa reciclando lo que no usas 😉')
    await ctx.send(f'https://www.youtube.com/results?search_query=ideas+para+hacer+decoraciones+reciclando')

@bot.command()
async def bye(ctx):
    await ctx.send(f'bye :)')

bot.run("Pon tu token aqui")
