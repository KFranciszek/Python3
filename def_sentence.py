def word():
    ask = input("Give sentence")
    return ask
    
def split_word(ask):
    split_title = ask.title().split()
    return split_title

def big(split_title):
    bigt = split_title
    for element, i in enumerate(bigt):
        if len(i) < 3:
            bigt[element] = bigt[element].lower()
    print(bigt)

    
ask = word()
split_title = split_word(ask)
big(split_title)
