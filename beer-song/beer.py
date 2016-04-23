def song(start, finish = 0):
    song_text = ''
    for i in range(start, finish-1, -1):
        song_text+=verse(i)+"\n"
    return song_text

def verse(num):
    if num == 0:
        return "No more bottles of beer on the wall, no more bottles of beer.\n" + \
        "Go to the store and buy some more, " + \
        "99 bottles of beer on the wall.\n"
    elif num == 1:
        return get_verse_text(str(num), "no more")
    else:
        return get_verse_text(str(num), str(num-1))

def get_verse_text(start, end):
    verse_text = start_bottle = get_bottle(start)
    verse_text +=" of beer on the wall, "+start_bottle + " of beer.\n"
    verse_text +="Take "+("it" if start=="1" else "one")+ " down and pass it around, "+ \
    get_bottle(end)+" of beer on the wall.\n"
    return verse_text

def get_bottle(num):
    bottles = num+' bottle'
    if num!="1":
        bottles += "s"
    return bottles
