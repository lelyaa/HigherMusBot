import shelve
from copy import deepcopy
from emoji import UNICODE_EMOJI
import constants as Const
import configurations as Config


def apply_state(chat_id, state):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        user_data['state'] = state
        return user_data


def return_state(chat_id):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        return user_data


def state_vars(chat_id, **vars_):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        user_data['vars'].update(vars_)


def get_vars(chat_id, *vars_):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        user_vars = user_data['vars']
        d = {}
        for key in vars_:
            d[key] = user_vars[key]
        return d


def get_var(chat_id, var):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        return user_data['vars'].get(var)


def create_playlist(chat_id, playlist_title):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        user_data['playlists'][playlist_title] = []


def add_track(chat_id, playlist, title, _id):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        user_data['playlists'][playlist].append(
            {'title': title, 'file_id': file_id}
        )


def get_platlists(chat_id):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        return list(user_data['playlists'])


def get_tracks(chat_id, playlist):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        return user_data['playlists'][playlist]


def del_playlist(chat_id, playlist):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        del user_data['playlists'][playlist]


def del_track(chat_id, playlist, track_ind):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        del user_data['playlists'][playlist][track_ind]


def rename_playlist(chat_id, target_pl, new_title):
    with shelve.open(config.storage, writeback = True) as storage:
        chat_id = str(chat_id)
        if chat_id not in storage:
            storage[chat_id] = {
                'state': Const.first_state,
                'vars': {},
                'playlists': {}
            }
        user_data = storage[chat_id]
        playlists = user_data['playlists']
        tracks = deepcopy(playlists[target_pl])
        del playlists[target_pl]
        playlists[new_title] = tracks


def contains_emoji(string, emojis = set(UNICODE_EMOJI)):
    if set(string) & emojis:
        return True
    else:
        False