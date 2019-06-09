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
        else:
            #Все состояния:
            #primary_state
            #first_choice
            #create_playlist
            #fill_playlis
            #choice_playlist
            #playlist_menu
            #rename_playlist
            #extend_playlist
            #approve_del_playlist
            #choice_track
            #track_menu
            #approve_del_track

        state = utils.return_state(chat_id)

        if state == 'primary_state':
            primary_state(msg, text, chat_id)

        elif state == 'first_choice':
            first_choice(msg, text, chat_id)

        elif state == 'create_playlist':
            create_playlist(msg, text, chat_id)

        elif state == 'fill_playlis':
            fill_playlis(msg, text, chat_id)

        elif state == 'choice_playlist':
            choice_playlist(msg, text, chat_id)

        elif state == 'playlist_menu':
            playlist_menu(msg, text, chat_id)

        elif state == 'rename_playlist':
            rename_playlist(msg, text, chat_id)

        elif state == 'extend_playlist':
            first_choice(msg, text, chat_id)

        elif state == 'approve_del_playlist':
            approve_del_playlist(msg, text, chat_id)

        elif state == 'choice_track':
            first_choice(msg, text, chat_id)

        elif state == 'track_menu':
            track_menu(msg, text, chat_id)

        elif state == 'first_choice':
            approve_del_track(msg, text, chat_id)

    except Exception as e:
        raise e
        print(traceback.format_exc())