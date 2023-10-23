from googletrans import Translator
from langdetect import detect, detect_langs

# Stores the inputs of user into googletrans languages
languages = {
    "english": "en",
    "spanish": "es",
    "german": "de"
}


# checks sentence for possible errors
def check_sentence(sen):
    words = sen.split()
    language = detect(words[0])

    for i in range(1, len(words)):
        lan = detect(words[i])
        con = float(str(detect_langs(text)[0])[3:])

        if con < .85:
            print("The language of your input is unclear")
            return 0
        elif lan != language:
            print("The sentence contains different languages")
            return 0

    print("Sorry! Couldn't find the error")


src = languages.get(input("What language are you starting with "))
text = input("What would you like to translate: ")
dest = languages.get(input("What language translate to "))

sentences = text.split(".")

trans = Translator()

for s in sentences:
    translation = trans.translate(s, src=src, dest=dest)
    if translation.text != text:
        print(text)
        print(f"{translation.text}.")
    else:
        check_sentence(s)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
