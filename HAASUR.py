import telebot
import requests
import datetime

TOKEN = "6626020995:AAEnvONL4dC_grKk1kcsBJemS6r9UFH4ZFY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = """
اهلا بك في مقبرة GH YT. يرجى كتابة -- قبل أي ايدي وسوف يتم وضعه في المقبرة.
    /start --Player ID
    مثال:
    /start --1234567890
    """
    bot.send_message(message.chat.id, welcome_message)
    
    additional_message = """
    ➪ : @XMODHPG

    𝑨𝑳𝑳 𝑽𝑰𝑺𝑰𝑻𝑺 𝑯𝑨𝑽𝑬 𝑩𝑬𝑬𝑵 
    𝑺𝑬𝑵𝑻𖤐

    𓅓GH YT           ?𖤍 

    ┏━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃💡
    ┣━━━━━━━━━━━━━━━━━━━━━━━━┫
    ┃ 👀 
    ┃ 🔴 
    ┃ 🟢 
    ┣━━━━━━━━━━━━━━━━━━━━━━━━┫
    ┃ ✨ 𝙋𝙡𝙚𝙖𝙨𝙚 𝙧𝙚𝙨𝙩𝙖𝙧𝙩 𝙜𝙖𝙢𝙚 
    ┃ 𝙖𝙣𝙙 𝙘𝙝𝙚𝙘𝙠 𝙫𝙞𝙨𝙞𝙩𝙨 ✨
    ┗━━━━━━━━━━━━━━━━━━━━━━━━┛

ضع قبل أي ايدي --'
    /start --Player ID
    مثال:
    /start --1234567890

    💻 تطوير: @https://t.me/XMODHPG

    /البوت خاص بي https://t.me/XMODHPG GH YT
    """
    bot.send_message(message.chat.id, additional_message)

@bot.message_handler(func=lambda message: '--' in message.text)
def get_player_info(message):
    player_id = message.text.split('--')[1].strip()
    region = "me"

    url = f'https://freefireapi.com.br/api/search_id?id={player_id}&region={region}'
    response = requests.get(url)
    
    if response.status_code == 200:
        player_data = response.json()
        basic_info = player_data.get('basicInfo', {})
        
        name = basic_info.get('nickname', 'Name not found')
        level = basic_info.get('level', 'Level not found')
        player_id = basic_info.get('accountId', 'Player ID not found')
        exp = basic_info.get('exp', 'Experience not found')
        liked = basic_info.get('liked', 'Likes not found')
        last_login = datetime.datetime.utcfromtimestamp(int(basic_info.get('lastLoginAt', 0)))
        creation_date = datetime.datetime.utcfromtimestamp(int(basic_info.get('createAt', 0)))

        answer_message = (
            f"👑 معلومات اللاعب 👑\n\n"
            f"🔹 الإسم: {name}\n"
            f"🔹 المستوى: {level}\n"
            f"🔹 معرف اللاعب: #{player_id}\n"
            f"🔹 الخبرة: {exp} HP\n"
            f"🔹 الإعجابات: {liked}\n"
            f"🔹 آخر تسجيل دخول: {last_login}\n"
            f"🔹 تاريخ الإنشاء: {creation_date}\n"
        )
        
        bot.reply_to(message, answer_message, parse_mode='HTML')
    else:
        bot.reply_to(message, "تم وضع العب في المقبرة بنجاح مقبرة:@XMODHPGBOT  جار تعذيب العب")

bot.infinity_polling()
