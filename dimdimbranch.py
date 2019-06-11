def playlist_menu(msg, text, chat_id):
    kb_array = Const.kb_playlist_menu
    playlist = utils.get_var(chat_id, 'current_playlist')

    if text == kb_array[0][0]:
        playlists = utils.get_playlists(chat_id)
        bot.send_message(
            chat_id, Const.msg_choice_playlist,
            reply_markup=get_keyboard(
                Const.kb_choice_playlist + playlists),
            parse_mode='HTML'
        )
        utils.apply_state(chat_id, 'choice_playlist')

    elif text == kb_array[0][1]:
        bot.send_message(
            chat_id, Const.msg_fill_playlist,
            reply_markup=get_keyboard(Const.kb_extend_playlist)
        )
        utils.apply_state(chat_id, 'extend_playlist')

    elif text == kb_array[1]:
        bot.send_message(
            chat_id, Const.msg_approve_del_playlist,
            reply_markup=get_keyboard(Const.kb_yes_no, inline=True),
            parse_mode='HTML'
        )
        utils.apply_state(chat_id, 'approve_del_playlist')

    elif text == kb_array[2]:
        bot.send_message(
            chat_id, Const.msg_rename_playlist,
            reply_markup=get_keyboard(Const.kb_create_playlist)
        )
        utils.apply_state(chat_id, 'rename_playlist')

    elif text == kb_array[3]:
        tracks = utils.get_tracks(chat_id, playlist)
        if tracks:
            bot.send_message(
                chat_id, Const.msg_pt_playlist_title.format(playlist),
                parse_mode='HTML'
            )
            for track in tracks:
                bot.send_audio(chat_id, track['file_id'])
        else:
            bot.send_message(chat_id, Const.msg_no_tracks, parse_mode='HTML')

    elif text == kb_array[4]:
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


def rename_playlist(msg, text, chat_id):
    def send():
        bot.send_message(
            chat_id, Const.msg_playlist_renamed,
            reply_markup=get_keyboard(Const.kb_playlist_menu),
            parse_mode='HTML'
        )

    if text == Const.kb_create_playlist[0]:
        send()
        utils.apply_state(chat_id, 'playlist_menu')

    elif title_check(text):
        target = utils.get_var(chat_id, 'current_playlist')
        utils.rename_playlist(chat_id, target, text)
        send()
        utils.apply_state(chat_id, 'playlist_menu')

    else:
        bot.send_message(chat_id, Const.msg_title_not_match)


def extend_playlist(msg, text, chat_id):
    playlist = utils.get_var(chat_id, 'current_playlist')

    if msg.content_type == 'audio':
        title = Const.pt_track_title.format(
            performer=msg.audio.performer, title=msg.audio.title
        )
        utils.add_track(
            chat_id, playlist,
            title=title, file_id=msg.audio.file_id
        )
        bot.send_message(
            chat_id, Const.msg_pt_track_saved.format(title),
            parse_mode='HTML'
        )

    elif msg.content_type == 'text':

        if text == Const.kb_extend_playlist[0]:
            bot.send_message(
                chat_id, Const.msg_playlist_extended,
                reply_markup=get_keyboard(Const.kb_playlist_menu),
                parse_mode='HTML'
            )
            utils.apply_state(chat_id, 'playlist_menu')

        else:
            pass
