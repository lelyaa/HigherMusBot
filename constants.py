# reductions: msg = message; pt = pattern; kb = keyboard

first_state = 'primary_state'

msg_start_text = '''
Привет! Любишь слушать музыку? Тогда тебе к нам!😜
Создавай плейлисты, скачивай музыку и наслаждайся🎶
'''
kb_start = ['😎 Начать']

kb_yes_no = ['✔️ Да', '✖️ Нет']

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
msg_playlist_improved = '<code>[плейлист обновлен]</code>'
msg_no_playlists = '<code>[пока нет ни одного плейлиста]</code>'
msg_no_tracks = '<code>[в этом плейлисте пока нет треков]</code>'
