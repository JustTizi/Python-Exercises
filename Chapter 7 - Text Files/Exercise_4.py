def main():
    with open("Python-Exercises\Chapter 7 - Text Files\FilesChapter7\irish_song.txt") as file:
        phrase = file.readline().rstrip()
        shortest_phrase = phrase.rstrip()
        while phrase:
            if len(phrase) < len(shortest_phrase):
                shortest_phrase = phrase
            phrase = file.readline().rstrip()
    print(f"The shortest line has {len(shortest_phrase)} characters")
    print(shortest_phrase)


if __name__ == '__main__':
    main()