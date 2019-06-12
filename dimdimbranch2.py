def choice_track(msg, text, chat_id):
    playlist = utils.get_var(chat_id, 'current_playlist')
    splitted = text.split('. ', maxsplit=1)
    num = splitted[0]

    if text == Const.kb_create_playlist[0]:
        bot.send_message(
            chat_id, Const.msg_pt_playlist_menu.format(playlist),
            reply_markup=get_keyboard(Const.kb_playlist_menu),
            parse_mode='HTML'
        )
        utils.apply_state(chat_id, 'playlist_menu')

    elif len(splitted) == 2 and num.isdigit() and int(num) > 0:
        title = splitted[1]
        track_ind = int(num) - 1
        tracks = utils.get_tracks(chat_id, playlist)
        try:
            track_title = tracks[track_ind]['title']
        except IndexError:
            pass
        else:
            if track_title == title:
                utils.set_vars(chat_id, track_ind=track_ind, track_title=title)
                bot.send_audio(chat_id, tracks[track_ind]['file_id'])
                bot.send_message(
                    chat_id, Const.msg_track_menu,
                    reply_markup=get_keyboard(Const.kb_track_menu),
                    parse_mode='HTML'
                )
                utils.apply_state(chat_id, 'track_menu')
            else:
                pass

    else:
        pass


def track_menu(msg, text, chat_id):
    kb_array = Const.kb_track_menu
    playlist = utils.get_var(chat_id, 'current_playlist')

    if text == kb_array[0]:
        tracks = utils.get_tracks(chat_id, playlist)
        tracks_titles = []
        for i in range(len(tracks)):
            tracks_titles.append(
                Const.pt_track_name.format(
                    num=i + 1, title=tracks[i]['title']
                )
            )
        bot.send_message(
            chat_id, Const.msg_track_list,
            parse_mode='HTML',
            reply_markup=get_keyboard(
                Const.kb_create_playlist + tracks_titles
            )
        )
        utils.apply_state(chat_id, 'choice_track')

    elif text == kb_array[1]:
        title = utils.get_var(chat_id, 'track_title')
        bot.send_message(
            chat_id, Const.msg_pt_del_track.format(title),
            parse_mode='HTML',
            reply_markup=get_keyboard(Const.kb_yes_no, inline=True)
        )
        utils.apply_state(chat_id, 'approve_del_track')

    else:
        pass


def approve_del_track(msg, text, chat_id):
    kb_array = Const.kb_yes_no
    playlist = utils.get_var(chat_id, 'current_playlist')
    track_ind = utils.get_var(chat_id, 'track_ind')

    tracks = utils.get_tracks(chat_id, playlist)

    if text == kb_array[0]:
        utils.del_track(chat_id, playlist, track_ind)
        tracks.pop(track_ind)
        bot.send_message(chat_id, Const.msg_track_deleted, parse_mode='HTML')
        tracks_titles = []
        for i in range(len(tracks)):
            tracks_titles.append(
                Const.pt_track_name.format(
                    num=i + 1, title=tracks[i]['title']
                )
            )
        bot.send_message(
            chat_id, Const.msg_track_list,
            parse_mode='HTML',
            reply_markup=get_keyboard(
                Const.kb_create_playlist + tracks_titles
            )
        )
        utils.apply_state(chat_id, 'choice_track')

    elif text == kb_array[1]:
        bot.send_message(
            chat_id, Const.msg_track_menu,
            reply_markup=get_keyboard(Const.kb_track_menu),
            parse_mode='HTML'
        )
        utils.apply_state(chat_id, 'track_menu')
