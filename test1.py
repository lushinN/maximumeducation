violator_songs = {
    'Close eyes': 4.86,
    'Phonky town': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Jajoja': 6.07,
    'Enjoy the Silence': 4.20,
    'This Feeling': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
count = int(input('Сколько песен выбрать? '))
all_time = 0.0
for i in range(count):
    query = f'Название {i + 1} песни: '
    song_name = input(query)
    all_time += violator_songs.get(song_name, 0)
print(f'Общее время звучания песен: {round(all_time, 2)} минут')
