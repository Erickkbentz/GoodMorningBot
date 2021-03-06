
import discord
import os
import catapi
import keep_alive

api = catapi.CatApi(api_key=os.getenv('CAT_API_KEY'))

client = discord.Client() 

@client.event
async def on_ready():
  pfp_path = 'CatPFP.jpg'

  with open(pfp_path, "rb") as pfp:
        await client.user.edit(password=None, avatar=pfp.read())

  print("profile picture changed")
  
  return


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  command_list = ['gm', 'good morning', 'morning', 'goodmorning']

  if message.content.lower() in command_list:
    results = await api.search_images(limit=1)
    print(results[0].url)

    embed = discord.Embed(
      title="Good Morning, Fuckers!",
      color=0xf708ef
    )
    embed.set_image(url=results[0].url)

    await message.channel.send(embed=embed)
    return
    
keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))
