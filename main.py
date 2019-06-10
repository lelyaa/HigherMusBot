import time
import traceback

import telebot
from telebot import types

import utilits
import config as Config
import constants as Const

bot = telebot.TeleBot(Config.token)
telebot.apihelper.proxy = Config.proxy

def get_keyboard(buttons, row_with = 2, inline = False):
    keyboard =  types.ReplyKeyboardMarkup(
        row_width=row_with, resize_keyboard=True)
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
    if 0 < len(title) < 21 and not utilits.contains_emoji(title):
        return True
    else:
        return False

@bot.message_handler(content_types=['text', 'audio'])
def main_handler(msg):
    try:
        chat_id, text = msg.chat.id, msg.text

        if text == '/start':
            if utilits.return_state(chat_id) == Const.first_state:
                keyboard = get_keyboard(Const.kb_start)
            else:
                keyboard = None
            bot.send_message(
                chat_id, Const.msg_start_text,
                parse_mode='HTML', reply_markup=keyboard
            )
        elif text == '/help':
            bot.send_message(chat_id, Const.msg_help_text, parse_mode='HTML')
        else:
            # Все состояния:
            # primary_state
            # first_choice
            # create_playlist
            # fill_playlis
            # choice_playlist
            # playlist_menu
            # rename_playlist
            # extend_playlist
            # approve_del_playlist
            # choice_track
            # track_menu
            # approve_del_track

        state = utilits.return_state(chat_id)

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

def primary_message(chat_id):
    bot.send_message(
        chat_id, Const.msg_primary,
        reply_markup=get_keyboard(Const.kb_primary),
        parse_mode='HTML'
    )

def primary_state(msg, text, chat_id):
    primary_message(chat_id)
    utilits.apply_state(chat_id, 'first_choice')

def first_choice(msg, text, chat_id):
    kb_array = Const.kb_primary

    if text == kb_array[0]:
        bot.send_message(
            chat_id, Const.msg_create_playlist,
            reply_markup = get_keyboard(Const.kb_create_playlist)
        )
        utilits.apply_state(chat_id, 'create_playlist')

    elif text == kb_array[1]:
        playlist = utilits.get_playlist(chat_id)
        if playlist:
            bot.send_message(
                chat_id, Const.msg_choice_playlist,
                reply_markup = get_key_keyboard(
                    Const.kb_choice_playlist + playlists),
                parse_mode = 'HTML'
            )
            utilits.apply_state(chat_id, 'Choice_playlist')
        else:
            bot.send_message(
                chat_id, Const.msg_no_playlists,
                parse_mode = "HTML"
            )
    else:
        bot.send_message(chat_id, Const.msg_warn_use_keyboard)

def create_playlist(msg, text, chat_id):
    if text == Const.kb_create_playlist[0]:
        primary_message(chat_id)
        utilits.apply_state(chat_id, 'first_choice')

    elif title_check(text):
        playlists = utilits.get_playlists(chat_id)

        if text not in playlists:
            utilits.create_playlists(chat_id, text)
            utilits.set_vars(chat_id, current_playlist=text)
            bot.send_message(
                chat_id, Const.msg_fill_playlist,
                reply_markup=get_keyboard(
                    Const.kb_fill_playlist, inline=True)
            )
            utilits.apply_state(chat_id, 'fill_playlist')
        else:
            bot.send_message(chat_id, Const.msg_title_not_match)

def fill_playlist(msg, text, chat_id):
    playlist = utilits.get_var(chat_id, 'current_playlist')

    if msg.content_type == 'audio':
        title = Const.pt_track_title.format(
            performer=msg.audio.performer, title=msg.audio.title
        )
        utilits.add_track(
            chat_id, playlist,
            title=title, file_id=msg.audio.file_id
        )
        bot.send_message(
            chat_id, Const.msg_pt_track_saved.format(title),
            parse_mode='HTML'
        )
    elif msg.content_type == 'text':
        kb_array = Const.kb_fill_playlist

        if text == kb_array[0]:
            utilits.del_playlist(chat_id, playlist)
            primary_message(chat_id)
            utilits.apply_state(chat_id, 'first_choice')
        elif text == kb_array[1]:
            bot.send_message(
                chat_id, Const.msg_playlist_saved,
                reply_markup=get_keyboard(Const.kb_primary),
                pars_mode='HTML'
            )
            utilits.apply_state(chat_id, 'first_choice')

def cjoice_playlist(msg, text, chat_id):
    playlists = utilits.get_playlist(chat_id)

    if text == Const.kb_choice_playlist[0]:
        primary_message(chat_id)
        utilits.apply_state(chat_id, 'first_choice')

    elif not playlists:
        bot.send_message(chat_id, Const.msg_no_playlists)

    elif text in playlists:
        utilits.set_vars(chat_id, current_playlist=text)
        bot.send_message(
            chat_id,
            Const.msg_pt_playlist_menu.format(text),
            reply_markup=get_keyboard(Const.kb_playlist_menu),
            parse_mode='HTML'
        )
        utilits.play_state(chat_id, 'playlist_menu')

    else:
        bot.send_message(
            chat_id, Const.msg_noexist_playlist,
            parse_mode='HTML'
        )