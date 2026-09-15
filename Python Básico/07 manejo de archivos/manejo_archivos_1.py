def sort_songs():
    with open("canciones.txt", "r") as file:
        songs = file.readlines()

    songs.sort()

    with open("canciones_ordenadas.txt", "w") as file:
        for song in songs:
            file.write(song)

    print("Canciones ordenadas correctamente.")


sort_songs()