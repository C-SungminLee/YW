# Discord Bot

from tkinter import Y
from functions import output
from functions import buildinglist
from functions import tilecoordytt
from functions import tilecoordybt


import discord
from discord.activity import Game
#maybe use this ^^^^, check it out in the future
from discord.user import User


client = discord.Client()
tiles = open("tiles.txt","r+")
Lines = tiles.readlines()


def updatetilestxt(x,y):

    z=""

    print(tilecoordybt[x][y])
    for s in range(len(tilecoordybt)):
        if s >0:
            z = "["
            for i in range(len(tilecoordybt[s])):
                if i < 9:
                    z = z +'"'+ tilecoordybt[s][i] +'",'
                else:
                    z = z +'"'+ tilecoordybt[s][i]+'"]'

            tiles.writelines(z + "\n")

    for s in range(len(tilecoordytt)):
        if s >0 and s < 9:
            z = "("
            for i in range(len(tilecoordytt[s])):
                if i < 9:
                    z = z +'"'+ tilecoordytt[s][i] +'",'
                else:
                    z = z +'"'+ tilecoordytt[s][i]+'")'

            tiles.writelines(z + "\n")

    tiles.writelines(tilecoordytt[9])

    tiles.close



def tile(x,y):
    global output
    global tilecoordybt
    global tilecoordytt
    #global discovery
    # if the tile has been discovered yet
    #global detection
    # if the tile is in range of the player(s) and needs to be "actively" shown (Show if troops were on the tile)
    location = (x,y)

    print(location)
    output = tilecoordytt[x][y] + ", location: " + str(location) + ", building: " + tilecoordybt[x][y]



@client.event
async def on_ready():
    print("We have logged in as YW".format(client))


@client.event
async def on_message(message):
    

    global tilemessage
    global output
    global buildinglist
    global build
    global game
    if message.author == client.user:
        return

    elif message.content.startswith('$help'):
        await message.channel.send('These are the commands, \n$why, $hello')

    elif message.content.startswith('$why'):
            await message.channel.send('Why not?') 

    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        '''elif message.content.lower == ('$changetile'):'''

    
    elif message.content.startswith('$tiles'):
        await message.channel.send('which tile? \n(x,y)')
        #tile info
        msg = await client.wait_for('message', timeout=60.0)
        counter = -1
        for i in msg.content:
            counter +=1
        while msg.content[0] == ('(') and msg.content[counter] == (')'):
            tile(int(msg.content[1]),int(msg.content[3]))

            await message.channel.send(output + "\nDone.")
            break
        while msg.content[0] != ('(') and msg.content[counter] != (')'):
            await message.channel.send("Try again. \n(x,y)")
            msg = await client.wait_for('message', timeout=60.0)

            while msg.content[0] == ('(') and msg.content[counter] == (')'):
                tile(int(msg.content[1]), int(msg.content[3]))
                await message.channel.send(output + "\nDone.")
                tiles.close()
                break

        

    elif message.content.startswith('$changetile'):
        await message.channel.send('Okay. Which tile?')
        msg = await client.wait_for('message', timeout=60.0)
        #need to put the numbers for all the tiles, would need to change into x,y format and the program would need to seperate the , in the x,y.
        counter = -1
        for i in msg.content:
            counter +=1

        while msg.content[0] == ('(') and msg.content[counter] == (')'):
            x = int(msg.content[1])
            y = int(msg.content[3])
            await message.channel.send('Okay. To what?')
            msg = await client.wait_for('message', timeout=60.0)
            if msg.author == client.user:
                 return
            elif msg.content.lower() == buildinglist[0] or buildinglist[1]:
                await message.channel.send("Are you sure you want to do '"+(msg.content)+"'?")
                buildreplacement = msg.content.lower()
                msg = await client.wait_for('message', timeout=60.0)
                if msg.author == client.user:
                    return
                elif msg.content.lower() == "no":
                    await message.channel.send("Okay.")
                    break
                
                elif msg.content.lower() == 'yes' or 'y':
                    tilecoordybt[x][y] = buildreplacement
                    tiles
                    tiles.truncate(0)
                    tiles.seek(0)
                    tiles.flush()
                    updatetilestxt(x,y)
                    await message.channel.send('Okay. Building on tile ' + str(x) +',' + str(y) + ' is '+tilecoordybt[x][y]+'.')
                    break

                else:
                    await message.channel.send("Try again.")
            else:
                await message.channel.send("Try again.")

            '''
            elif msg.content.lower() == buildinglist[1]:
                await message.channel.send("Are you sure you want to do '"+(msg.content)+"'?")
                msg = await client.wait_for('message', timeout=60.0)
                if msg.content.lower() == 'yes' or 'y':
                    tilebuild1(tilen,buildinglist[1])
                    await message.channel.send('Okay. Building on tile (x,' + str(tilen) + ") is "+(tilebuildings1[tilen])+".")
            '''



'''

    elif message.content.startswith('$map'):
        for item in range(1,31):
            x = x + " " +str(item)
        for item in range(1,21):
            y = y + " \n" +str(item)
        await message.channel.send("_"+x + y)
'''

client.run('OTI3Njg2MzQ4NTc4NjIzNTY5.YdN1PQ.GAX1Ofart8n6x6MViNJh9XUSAs4')

'''
    elif message.content.startswith('$startgame') or ('$sg') and str(message.author) == ('Sungmin#6222') and game == False:
        print(message.author)
        or (a list with players):
        await message.channel.send('Okay. Game started')
        game = True
        return
    elif message.content.startswith('$startgame') or ('$sg') and not str(message.author) == ('Sungmin#6222') and not game == False:
        await message.channel.send("Unfortunatly you cannot start a game because one is active or you don't have permision.")
        print(User)
        return
    
    elif message.content.startswith('$endgame') or ('$eg') and str(message.author) == ('Sungmin#6222') and game == True:
        print(message.author)
        or (a list with players):
        await message.channel.send('Okay. Game Ended')
        game = False
        return
    elif message.content.startswith('$endgame') or ('$eg') and not str(message.author) == ('Sungmin#6222') and not game == True:
        await message.channel.send("Unfortunatly you cannot end the game because one is not active or you don't have permision.")
        print(User)
        return
    '''