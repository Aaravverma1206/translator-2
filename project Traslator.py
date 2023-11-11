from tkinter import *
from googletrans import Translator

root = Tk()
root.geometry("500x500")
root.title("Translator App")
root.configure(background="cyan")

input_label = Label(root, text="Enter text:", bg="cyan")
input_label.pack()

def translate_text():
    input_text = entry.get()
    translator = Translator()
    translation = translator.translate(input_text, dest=target_language.get())
    output_label.config(text=f"Translation: {translation.text}")

entry = Entry(root, width=40)
entry.pack()

languages = ["english",
     "es",
    "fr",
    "de",
    "ja",
    "ko",
    "zh-CN",
    'af',
    'sq',
    'am',
    'ar',
    'hy',
    'az',
    'eu',
    'be',
    'bn',
    'bs',
    'bg',
    'ca',
    'ceb',
    'ny' ,
    'zh-cn',
    'zh-tw' ,
    'co',
    'hr',
    'cs',
    'da',
    'nl',
    'en',
    'eo',
    'et',
    'tl',
    'fi',
    'fr',
    'fy',
    'hi', 
    'zu',]
target_language_label = Label(root, text="Select target language:", bg="cyan")
target_language_label.pack()

target_language = StringVar(root)
target_language.set("en")

language_dropdown = OptionMenu(root, target_language, *languages)
language_dropdown.pack()

translate_button = Button(root, text="Translate", command=translate_text)
translate_button.pack()

output_label = Label(root, text="")
output_label.pack()

root.mainloop()
