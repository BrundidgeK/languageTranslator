import tkinter.filedialog

from googletrans import Translator
from langdetect import detect, detect_langs
from tkinter import *
import speech_recognition as sr

# Stores the inputs of user into googletrans languages
languages = {
    "English": "en-US",
    "Spanish": "es-ES",
    "German": "de-DE"
}

root = Tk()
r = sr.Recognizer()


# checks sentence for possible errors
def check_sentence(sen, src):
    words = sen.split()
    language = src

    for i in range(len(words)):
        # Finds what language each word originates and
        # how confident the ai is in its prediction
        lan = detect(words[i])
        con = float(str(detect_langs(sen)[0])[3:])

        if con < .85:
            output.config(text="ERROR: The language of your input is unclear")
            return 0
        elif lan != language:
            output.config(text="ERROR: The sentence contains a language not specified")
            return 0

    output.config(text="ERROR: Could not translated")


def translate():
    src = languages.get(src_input.get())
    dest = languages.get(dest_input.get())
    # Splits input into sentences
    if var == 1:
        speech_to_text(src)

    sentences = entry.get().split(".")

    trans = Translator()
    paragraph = ""

    for s in sentences:
        translation = trans.translate(s, src=src[:, 1], dest=dest[:, 1])
        if translation.text != entry.get():
            paragraph += translation.text + "."
        else:
            check_sentence(s)
            return

    output.config(text=paragraph)

    # Empties the entry
    entry.config(text="")


def speech_to_text(lan):
    with sr.AudioFile(entry.get()) as source:

        audio_text = r.listen(source)

        try:
            text = r.recognize_google(audio_text, language=lan)
            return text
        except:
            print("Can't understand")

def set_up_audio():
    if var == 1:
        entry.destroy()

    else:
        entry.pack()

# User picks source language
src_input = StringVar()
src_input.set("English")
src_drop = OptionMenu(root, src_input, "English", "Spanish", "German")
Label(root, text="Source Language").pack()
src_drop.pack()

# User picks destination language
dest_input = StringVar()
dest_input.set("Spanish")
dest_drop = OptionMenu(root, dest_input, "English", "Spanish", "German")
Label(root, text="Destination Language").pack()
dest_drop.pack()

var = IntVar()
using_audio = Checkbutton(root, text="Using an Audio File?", command=set_up_audio, variable=var).pack()
audioFile = tkinter.filedialog.askopenfilename()

# User inputs the sentences to translate
entry = Entry(root)
enterButton = Button(root, text="Enter", command=translate)
enterButton.pack()

# Outputs the translation in the desired language
output = Label(root, text="Enter Your text")
output.pack()
root.mainloop()
