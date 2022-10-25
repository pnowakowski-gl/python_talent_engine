songs_db = [ {
 'artist': 'Led Zeppelin', 
 'title': 'Stairways to heaven', 
 'playback': '09:20' 
}, {
 'artist': 'Metallica', 
 'title': 'Master of puppets', 
 'playback': '04:30' 
}, {
 'artist': 'Nirvana', 
 'title': 'The Man who sold the world', 
 'playback': '03:10' 
}, {
 'artist': 'Stepan Galyabarda', 
 'title': 'Lyst do mamy', 
 'playback': '02:20' 
}]

def get_song(db, len_seconds):
    get_songs = dict()
    for i in range(len(db)):
        playtime = db[i]['playback']
        playtime = playtime.split(':')
        playtime = int(playtime[0]) * 60 + int(playtime[1])
        if playtime < len_seconds:
            get_songs[i] = playtime
    if get_songs == dict():
        return False
    songs_index = max(get_songs, key=get_songs.get)
    
    return f"Best possible song: {db[songs_index]['artist']}/{db[songs_index]['title']}"

print(get_song(songs_db, 190))