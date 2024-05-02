from googletrans import Translator


def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


tt = input("Enter the text you want to translate: ")
tl = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")

translated_t = translate_text(tt, tl)
print("Translated text:")
print(translated_t)
