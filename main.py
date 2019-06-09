import time
import traceback

import telebot
from telebot import types

import utils
import config as Config
import constants as Const

bot = telebot.TeleBot(config.token)
telebot.apihelper.proxy = Config.proxy

def get_keyboard(buttons, row_with = 2, inline = False):
    keyboard =  types.ReplyKeyboardMarkup(
        row_width = row_with, resize_keyboard = True)
    if not inline:
        for button in buttons:
            if isinstance(button, (list, tuple, set)):
                keyboard.add(*button)
            else:
                keyboard.add(button)
    else:
        keyboard.add(*buttons)

    return keyboard


def title_check(title):
    if 0 < len(title) < 21 and not utils.contains_emoji(title):
        return True
    else:
        return False

@bot.message_handler(content_types = ['text', 'audio'])
def main_handler(msg):
    try:
        chat_id, text = msg.chat.id, msg.text

        if text == '/start':
            if utils.return_state(chat_id) == Const.first_state:
                keyboard = get_keyboard(Const.kb_start)
            else:
                keyboard = None
            bot.send_message(
                chat_id, Const.msg_start_text,
                parse_mode = 'HTML', reply_markup = keyboard
            )
        elif text == '/help':
            bot.send_message(chat_id, Const.msg_help_text, parse_mode = 'HTML')