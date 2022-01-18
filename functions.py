from fileinput import close

import ast


def tilebuild1(tile,change):
    tilebuildings1[tile] = change

def tilebuild2(tile,change):
    tilebuildings1[tile] = change

def tilebuild3(tile,change):
    tilebuildings1[tile] = change

def tilebuild4(tile,change):
    tilebuildings1[tile] = change

def tilebuild5(tile,change):
    tilebuildings1[tile] = change

def tilebuild6(tile,change):
    tilebuildings1[tile] = change

def tilebuild7(tile,change):
    tilebuildings1[tile] = change

def tilebuild8(tile,change):
    tilebuildings1[tile] = change

def tilebuild9(tile,change):
    tilebuildings1[tile] = change




global tilemessage
tilemessage = ""

global output
output = ""

global buildinglist
buildinglist = ["none", "House"]

'''
#each thing in the list is each tile, tilebuildings[1] is the first tile (x = 1). Being (y,1)
tilebuildings1 =["null","House","House","House","House","House","House","House","House","House"]
tilebuildings2 =["null","House","House","House","House","House","House","House","House","House"]
tilebuildings3 =["null","House","House","House","House","House","House","House","House","House"]
tilebuildings4 =["null","House","House","House","House","House","House","House","House","House"]
tilebuildings5 =["null","House","House","House","House","House","House","House","House","House"]
tilebuildings6 =["null","House","House","House","House","House","House","House","House","House"]
tilebuildings7 =["null","House","House","House","House","House","House","House","House","House"]
tilebuildings8 =["null","House","House","House","House","House","House","House","House","House"]
tilebuildings9 =["null","House","House","House","House","House","House","House","House","House"]
'''
tiles = open("tiles.txt","r+")

tiles.seek(0)
Lines = tiles.readlines()
 
count = 0

# Strips the newline character
for line in Lines:
    count += 1
    if count == 1:
        tilebuildings1 = (line.strip())
        tilebuildings1 = (ast.literal_eval(tilebuildings1))
    elif count == 2:
        tilebuildings2 = (line.strip())
        tilebuildings2 = (ast.literal_eval(tilebuildings2))
    elif count == 3:
        tilebuildings3 = (line.strip())
        tilebuildings3 = (ast.literal_eval(tilebuildings3))
    elif count == 4:
        tilebuildings4 = (line.strip())
        tilebuildings4 = (ast.literal_eval(tilebuildings4))
    elif count == 5:
        tilebuildings5 = (line.strip())
        tilebuildings5 = (ast.literal_eval(tilebuildings5))
    elif count == 6:
        tilebuildings6 = (line.strip())    
        tilebuildings6 = (ast.literal_eval(tilebuildings6))
    elif count == 7:
        tilebuildings7 = (line.strip())
        tilebuildings7 = (ast.literal_eval(tilebuildings7))
    elif count == 8:
        tilebuildings8 = (line.strip())
        tilebuildings8 = (ast.literal_eval(tilebuildings8))
    elif count == 9:
        tilebuildings9 = (line.strip())
        tilebuildings9 = (ast.literal_eval(tilebuildings9))
 

'''
tileterrain1 =("null","Land","Land","Land","Land","Land","Land","Land","Land","Land")
tileterrain2 =("null","Land","Land","Land","Land","Land","Land","Land","Land","Land")
tileterrain3 =("null","Land","Land","Land","Land","Land","Land","Land","Land","Land")
tileterrain4 =("null","Land","Land","Land","Land","Land","Land","Land","Land","Land")
tileterrain5 =("null","Land","Land","Land","Land","Land","Land","Land","Land","Land")
tileterrain6 =("null","Land","Land","Land","Land","Land","Land","Land","Land","Land")
tileterrain7 =("null","Land","Land","Land","Land","Land","Land","Land","Land","Land")
tileterrain8 =("null","Land","Land","Land","Land","Land","Land","Land","Land","Land")
tileterrain9 =("null","Land","Land","Land","Land","Land","Land","Land","Land","Land")
'''

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    if count == 10:
        tileterrain1 = ((line.strip()))
        
        tileterrain1 = (ast.literal_eval(tileterrain1))
    elif count == 11:
        tileterrain2 = (line.strip())
        tileterrain2 = (ast.literal_eval(tileterrain2))
    elif count == 12:
        tileterrain3 = (line.strip())
        tileterrain3 = (ast.literal_eval(tileterrain3))
    elif count == 13:
        tileterrain4 = (line.strip())
        tileterrain4 = (ast.literal_eval(tileterrain4))
    elif count == 14:
        tileterrain5 = (line.strip())
        tileterrain5 = (ast.literal_eval(tileterrain5))
    elif count == 15:
        tileterrain6 = (line.strip())    
        tileterrain6 = (ast.literal_eval(tileterrain6))
    elif count == 16:
        tileterrain7 = (line.strip())
        tileterrain7 = (ast.literal_eval(tileterrain7))
    elif count == 17:
        tileterrain8 = (line.strip())
        tileterrain8 = (ast.literal_eval(tileterrain8))
    elif count == 18:
        tileterrain9 = (line.strip())
        print(ast.literal_eval(tileterrain9))



#tile coordinate y building tuple
global tilecoordybt
tilecoordybt = ("null",tilebuildings1,tilebuildings2,tilebuildings3,tilebuildings4,tilebuildings5,tilebuildings6,tilebuildings7,tilebuildings8,tilebuildings9)
#same as the buildings, but can't be changed
global tilecoordytt
tilecoordytt =("null",tileterrain1,tileterrain2,tileterrain3,tileterrain4,tileterrain5,tileterrain6,tileterrain7,tileterrain8,tileterrain9)


global build
build = ""

global game
game = False

