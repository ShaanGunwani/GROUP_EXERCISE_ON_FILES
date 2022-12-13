def sentence_splitter(text):
    stri = open(text)
    s = stri.read()
    a = s.split()

    for words in a:
        if words.endswith("?") or words.endswith("!"):
            print(words, end = "\n")
            continue
        else:
            if (words.startswith("Mr") and words.endswith(".")) or (words.startswith("i.e") and words.endswith(".")) or (words.startswith("Jr") and words.endswith(".")) or (words == "..."):
                print(words, end = " ")
                continue
            elif (words.endswith(".")):
                print(words, end = "\n")
                continue
            elif (words == "isnt."):
                print(words)
                break
            else:
                print(words, end = " ")
                continue

    

sentence_splitter('something.txt')

def sentence_splitter(text):
    stri = open(text)
    s = stri.read()
    a = s.split()

    for words in a:
        if words.endswith("?") or words.endswith("!"):
            print(words, end = "\n")
            continue
        else:
            if (words.startswith("Mr") and words.endswith(".")) or (words.startswith("i.e") and words.endswith(".")) or (words.startswith("Jr") and words.endswith(".")) or (words == "..."):
                print(words, end = " ")
                continue
            elif (words.endswith(".")):
                print(words, end = "\n")
                continue
            elif (words == "isnt."):
                print(words)
                break
            else:
                print(words, end = " ")
                continue

    

sentence_splitter('something.txt')
