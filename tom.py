import discord
import os
import random


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)
    if message.content.startswith('python nedir?'):
        await message.channel.send("Python bir programlama dilidir.")
    if message.content.startswith('memgonder'):
        with open("/Users/esrahazinedar/Desktop/USCODE klasör/Dudul mendekatimu.jpeg", "rb") as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
    if message.content.startswith("rastgele mem gonder"):
        liste = os.listdir("resimler")
        secilenresim = random.choice(liste)
        with open(f'resimler/{secilenresim}', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
    if message.content.startswith("bana ordek fotoğrafı ver."):
        image_url = get_duck_image_url()
        await message.channel.send(image_url)
    if message.content.startswith('selam'):
        await message.channel.send("Merhabalar, bugün çevre kirliliği hakkında bilgi edinmek istermisiniz?")
    if message.content.startswith('evet'):
        await message.channel.send("Çevre kirliliği, insan faaliyetleri sonucu doğada meydana gelen zararlı değişikliklerdir ve başlıca beş türde incelenir: hava kirliliği, su kirliliği, toprak kirliliği, gürültü kirliliği ve ışık kirliliği. Bu türler, ekosistem dengelerini bozarak insan sağlığını tehdit eder. Başka sorunuz var mı?")
    elif message.content.startswith('hayır'):
        with open("/Users/esrahazinedar/Desktop/USCODE klasör/Silly angry cat.jpeg", "rb") as f:
            picture = discord.File(f)
    if message.content.startswith('dogada ne kadar surede yok olur'):
        await message.channel.send("Plastik bir şişe 450cam 4000-4500 arası, ve poşet en az 1000 yıl civarı sürede yok olmaktadır. Başka sorunuz?")
    if message.content.startswith('yok'):
        await message.channel.send("Ozaman görüşmek üzere tekrar bir sorunuz olduğunda sormaktan çekinmeyin.")

client.run("ıdhfıdhfıefksjf")
