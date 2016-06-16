# -*- coding: utf-8 -*-


import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.

import json
import requests
import urllib
from key import *

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

def obtener(m,namex,cid):
    boolxd = namex[:21] == '/score@imdb_score_bot'
    
    if boolxd == True:
        name = namex[22:]
       
    else:
        name = namex[7:]
        
    url = 'http://www.omdbapi.com/?t=' + name 
    r = requests.get(url)

    json_object = r.json()
    parsed_data = json.dumps(json_object)

    lol = json.loads(parsed_data)

    if lol["Response"]=='True':
        if lol["Poster"] != "N/A":
            caption = 'Title: ' + (lol["Title"]) + '\n' +  '\n' + 'IMDb:  ' + (lol["imdbRating"]) + '/10   (' + lol["imdbVotes"] + ' votes)'  + '\n' + 'Metacritic:  ' + (lol["Metascore"])
            urlpic = (lol["Poster"])    
            urllib.urlretrieve(urlpic, "1.jpg")
            file = open('1.jpg', 'rb')
            bot.send_photo(cid,file,caption=caption)
        else:
            caption = 'Title: ' + (lol["Title"]) + '\n' +  '\n' + 'IMDb:  ' + (lol["imdbRating"]) + '/10   (' + lol["imdbVotes"] + ' votes)'  + '\n' + 'Metacritic:  ' + (lol["Metascore"])
            bot.send_message(cid,caption)
    else:
        bot.reply_to(m,'Content not found in IMDb!')


 
@bot.message_handler(commands=['score']) 
def command_score(m):  
    cid = m.chat.id
    obtener(m,m.text,cid)
 
@bot.message_handler(commands=['start']) 
def command_bisi(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message(cid, "Use the command /score and the name of the film/serie in order to get the score")

bot.polling(none_stop=True)
while True: 
    time.sleep(300) # Hacemos que duerma durante un periodo largo de tiempo para que la CPU no esté trabajando innecesáremente.
