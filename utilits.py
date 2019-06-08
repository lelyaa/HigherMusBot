import shelve
from copy import deepcopy
import configurations as Config
import constants as Const


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