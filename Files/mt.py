Machine Translation

Import the Library
from translate import Translator

Create a Translator Object
translator = Translator(to_lang='es')  # Spanish

Choose a Phrase
# Text to be translated
text = 'Hello, how are you?'

Translate
# Perform the translation
translation = translator.translate(text)

# Print the translated text
print('Translated Text:', translation)

