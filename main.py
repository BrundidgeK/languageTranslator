from googletrans import Translator
from langdetect import detect, detect_langs
from tkinter import *

# Stores the inputs of user into googletrans languages
languages = {
    "English": "en",
    "Spanish": "es",
    "German": "de"
}

root = Tk()

# checks sentence for possible errors
def check_sentence(sen, src):
    words = sen.split()
    language = src

    for i in range(0, len(words)):
        lan = detect(words[i])
        con = float(str(detect_langs(sen)[0])[3:])

        if con < .85:
            print("The language of your input is unclear")
            return 0
        elif lan != language:
            print("The sentence contains a language not specified")
            return 0

    print("Sorry! Couldn't find the error")


def translate():
    sentences = entry.get().split(".")
    src = languages.get(src_input.get())
    dest = languages.get(dest_input.get())

    trans = Translator()
    paragraph = ""

    for s in sentences:
        translation = trans.translate(s, src=src, dest=dest)
        if translation.text != entry.get():
            paragraph += translation.text + "."
        else:
            check_sentence(s)
            return

    output.config(text=paragraph)



src_input = StringVar()
src_input.set("English")
src_drop = OptionMenu(root, src_input, "English", "Spanish", "German")
Label(root, text="Source Language").pack()
src_drop.pack()

dest_input = StringVar()
dest_input.set("Spanish")
dest_drop = OptionMenu(root, dest_input, "English", "Spanish", "German")
Label(root, text="Destination Language").pack()
dest_drop.pack()

entry = Entry(root)
entry.pack()

enterButton = Button(root, text="Enter", command=translate)
enterButton.pack()

output = Label(root, text="Enter Your text")
output.pack()
root.mainloop()

#src = languages.get(input("What language are you starting with "))
#text = input("What would you like to translate: ")
#dest = languages.get(input("What language translate to "))


