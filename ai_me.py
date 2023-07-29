import telebot
import random
from config import API_TOKEN
from telebot import types

bot = telebot.TeleBot(API_TOKEN)
controller = {}

INVALID_ANS = "зайка, напиши или выбери что-нибудь другое, этот бот не такой умный как я"


def menu(message):
    user_id = message.from_user.id
    user_state = controller.get(user_id, 'choose')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_cats = types.KeyboardButton("хочу посмотреть котиков!")
    button_my_photos = types.KeyboardButton("хочу увидеть ваню🥺")
    button_she = types.KeyboardButton("а я правда красивая?")
    button_miss_u = types.KeyboardButton("я соскучилааась...")
    markup.add(button_cats, button_my_photos, button_she, button_miss_u)

    bot.send_message(user_id, "что такое, солнышко?", reply_markup=markup)


@bot.message_handler(commands=['start'])  # приветствие
def start_message(message):
    bot.send_message(message.from_user.id,
                     "привет, солнышко! я написал этого бота, чтобы быть рядом с тобой, даже если я занят")
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEJy4VkvilKioPSzvgj_xCj0ObEYQc11wACQCYAAqfRQEmHno1kvKZ05S8E")

    controller[message.from_user.id] = 'choose'
    menu(message)


@bot.message_handler(content_types=['text']) # ответ на ее запрос
def start_message(message):  # выдача запроса
    user_id = message.from_user.id
    her_answer = message.text
    if her_answer == "хочу посмотреть котиков!":
        pic_number = str(random.randint(1, 25))
        pic_path = 'cats/cat' + pic_number + '.png'
        pic = open(pic_path, 'rb')

        bot.send_photo(user_id, pic)
        # комплект фоток с котиками (25 штук)
    elif her_answer == "хочу увидеть ваню🥺":
        pic_number = str(random.randint(1, 18))
        pic_path = 'vans/me' + pic_number + '.png'
        pic = open(pic_path, 'rb')

        bot.send_message(user_id, "извини, ваня тяжелый) нужно немножко подождать!")
        bot.send_photo(user_id, pic, timeout=60)
        # комплект фоток со мной (18 штук)
    elif her_answer == "а я правда красивая?":
        stick_list = ["CAACAgIAAxkBAAEJ2H1kxNwxf7TdFLFh6hvkU6U3ovFPhwACcwADokkeMmK4dXwMgReiLwQ",
                      "CAACAgIAAxkBAAEJ2H9kxNxLV2EGWgABVSLq2iP_z02asvcAAkchAAIL8yhJnuHjBm57pMwvBA",
                      "CAACAgIAAxkBAAEJ2HtkxNuNKJiMIsXdTSNoX6_V-kZKdAACpR8AAne9KUlOc3_h-UenUi8E",
                      "CAACAgIAAxkBAAEJ2IFkxN0rVgdHVNdlo0S_vqNsOSvT4QACmyoAAiQ-wEhDyTtdXtCAlC8E",
                      "CAACAgIAAxkBAAEJ2JhkxPrdR_mqCJKWc7cVhb0xTvfgVQACqTAAAlRqwEgKh0BXYKsMHC8E",
                      "CAACAgIAAxkBAAEJ2JpkxPtAsNt-CGc7ZaB9Oxpqg76WnQACYzEAArzuwEjjkzXp_yb3mC8E"]
        comp_number = str(random.randint(1, 6))
        comp_path = 'compliments/comp' + comp_number + '.txt'
        comp = open(comp_path, encoding='utf-8')
        line = comp.read()

        bot.send_message(user_id, line)
        bot.send_sticker(user_id, stick_list[int(comp_number) - 1])
    # комплекты комплимент+стикер (5 пар)
    elif her_answer == "я соскучилааась...":
        bot.send_message(user_id, "я тоже ужасно соскучился(")
    elif her_answer == "я тебя люблю":
        bot.send_message(user_id, "я тоже тебя люблю, кошечка")
        bot.send_message(user_id, "больше всего на свете!")
        bot.send_sticker(user_id, "CAACAgIAAxkBAAEJzh5kv1_0cf5_tbplPApYvEtuHz1eEQACvykAAgy8wEjCOpgiq6Us-S8E")
    else:
        bot.send_message(user_id, INVALID_ANS)


bot.polling()
