def main():
    songs = []

    with open("D:\OneDrive\Documents\Python-Exercises\Chapter 7 - Text Files\FilesChapter7\playlist.txt", encoding="utf-8") as file:
        line = file.readline()
        print("Playlist")
        
        while line:
            if line != "\n":
                songs.insert(0, line.rstrip().split(";"))
            line = file.readline()

        for song in songs:
            print(f"{song[0]}\t{song[1].upper()} ({song[2].lower()})")
        

if __name__ == "__main__":
    main()