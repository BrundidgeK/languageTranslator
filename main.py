from googletrans import Translator
from langdetect import detect, detect_langs
from tkinter import *

# Stores the inputs of user into googletrans languages
languages = {
    "English": "en",
    "Spanish": "es",
    "German": "de",

}

root = Tk()


# translates the user input
def translate():

    src = languages.get(src_input.get())
    dest = languages.get(dest_input.get())
    if src == dest:
        output.config(text="This sentence is already in " + str(src_input.get()))
        return

    # Breaks paragraph into sentences (easier to translate)
    sentences = entry.get().split(".")

    trans = Translator()
    paragraph = ""

    for s in sentences:
        translation = trans.translate(s, src=src, dest=dest)
        if translation.text != entry.get():
            paragraph += translation.text + ". "
        else:
            output.config(text=check_sentence(s, src))
            return

    output.config(text=paragraph)


# checks sentence for possible errors
def check_sentence(sen, src):
    words = sen.split()
    language = src

    # Checks individual words to find the problem
    for i in range(0, len(words)):
        lan = detect(words[i])  # finds the language
        con = float(str(detect_langs(sen)[0])[3:])  # Find confidence score in translation

        if con < .85:
            return "The language of your input is unclear"
        elif lan != language:
            return "The sentence contains a language not specified"

    return "Sorry! Unable to find the error"


# Tkinter user interface
# Gets input for the original language
src_input = StringVar()
src_input.set("English")
src_drop = OptionMenu(root, src_input, *languages.keys())
Label(root, text="Source Language").pack()
src_drop.pack()

# Gets the desired language to output
dest_input = StringVar()
dest_input.set("Spanish")
dest_drop = OptionMenu(root, dest_input, *languages.keys())
Label(root, text="Destination Language").pack()
dest_drop.pack()

# Text field for user to input paragraph
entry = Text(root)
entry.pack()

enterButton = Button(root, text="Enter", command=translate)
enterButton.pack()

output = Label(root, text="Enter Your text")
output.pack()
root.mainloop()
