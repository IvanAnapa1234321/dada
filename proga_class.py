from datetime import date


class Text:
    def qwerty__init__(self):
        d = date.today()
        text = input("введите текст : ")
        add = open("oops.txt", "at")
        print(d, text, file=add)
        add.close()

    def consol__init__(self):
        d = date.today()
        text = input("введите текст : ")
        print(d, text)


t = Text()
t.qwerty__init__()
t.consol__init__()
