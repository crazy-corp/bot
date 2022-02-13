import telebot
import wolframalpha
import wikipedia

client = wolframalpha.Client("Your_ID")

API_KEY ="Your api key"

bot= telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message,"Hey! How are you!?")
    
@bot.message_handler(func=lambda message: True)
def wolframalpha(message):
    try:
        res = client.query(message.text)
        res1 = wikipedia.summary(message.text, sentences=4)
        jo="Wiki Says : "+res1+"\nWolframalpha says : " +next(res.results).text
        bot.reply_to(message,jo)
    except:
        try:
            res1 = wikipedia.summary(message.text, sentences=4)
            jo="Wiki Says : "+res1
            bot.reply_to(message,jo)
        except:
            try:
                res = client.query(message.text)
                jo="Wolframalpha says : " +next(res.results).text
                bot.reply_to(message,jo)
            except:   
                bot.reply_to(message,"Sorry, No results! :) ")
    
bot.polling()