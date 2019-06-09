# reductions: msg = message; pt = pattern; kb = keyboard

first_state = 'primary_state'
seconds_error = 60

msg_start_text = '''
Привет! Любишь слушать музыку? Тогда тебе к нам!😜
Создавай плейлисты, скачивай музыку и наслаждайся🎶
'''
kb_start = ['😎 Начать']

kb_yes_no = ['✔️ Да', '✖️ Нет']

msg_help_text = '''
Техническая справка'''

msg_primary = '<b>Главное меню</b>'
kb_primary = [
    '💽 Создавай плейлист',
    '🗂 Твои плейлисты'
]

msg_create_playlist = '''
Как назовешь свой плейлист?🤩 
P.S. оно должно быть не более 20 символов и без emoji
'''
kb_create_playlist = ['🔙 Назад']
msg_title_not_match = 'Прости, но название не подходит😩'

msg_fill_playlist = '''
Загружайте или пересылайте треки, мы их добавим в плейлист😉
'''
kb_fill_playlist = ['❌ Отменить', '💾 Сохранить']
msg_pt_track_saved = '<code>[добавлен]</code> <b>{}</b>'  #имя файла

msg_playlist_saved = '<code>[плейлист сохранен]</code>'
msg_playlist_extended = '<code>[плейлист обновлен]</code>'
msg_no_playlists = '<code>[пока нет ни одного плейлиста]</code>'
msg_no_tracks = '<code>[в этом плейлисте пока нет треков]</code>'

msg_playlist_exist = '''
К сожалению, такое название уже существует🤯
'''
msg_nonexist_playlist = '''
<code>[плейлист с таким названием не существует]</code>
'''

msg_choice_playlist = '<b>Список плейлистов</b>'
kb_choice_playlist = ['🔙 Назад']


#title part
msg_pt_playlist_menu = '<code>[меню плейлиста]</code> <b>{}</b>'
kb_playlist_menu = [
    ['🔙 Назад', '📤 Добавить треки'],
    '🗑 Удалить плейлист',
    '✏️ Переименовать плейлист',
    '🎶 Выдать все треки',
    '📃 Список тереков'
]

msg_approve_del_playlist =  '<b>Точно удалить</b> этот плейлист?'
msg_pt_playlist_deleted = '<code>[удален плейлист]</code> <b>{}</b>'

msg_pt_playlist_title = '<code>[треки плейлиста]</code> <b>{}</b>'

kb_extend_playlist = ['💾 Сохранить']

msg_rename_playlist = msg_create_playlist
msg_playlist_renamed = '<code>[плейлист переименован]</code>'

msg_track_list = '<code>[список треков плейлиста]</code>'
pt_track_name = '{num:02d}. {title}'
pt_track_title = '{performer} – {title}'

msg_track_menu = '<code>[опции трека]</code>'
kb_track_menu = [
    #только для треков
    '🔙 Назад', '🗑 Удалить трек из плейлиста'
]

msg_pt_del_track = 'Вы точно хотите удалить трек <b>{}</b> из плейлиста?'
msg_track_deleted = '<code>[трек удален]</code>'
