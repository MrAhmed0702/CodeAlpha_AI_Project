from googletrans import Translator


def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


tt = input("Enter the text you want to translate: ")
tl = input("Enter the target language ('fr' for French, 'ar' for Arabic): ")

translated_t = translate_text(tt, tl)
print("Translated text:" + translated_t)
