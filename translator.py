
from translate import Translator

def translate_to_italian(word):
    translator = Translator(to_lang="it")
    translation = translator.translate(word)
    return translation

word = input("Enter an English word to translate: ")
print(translate_to_italian(word))
