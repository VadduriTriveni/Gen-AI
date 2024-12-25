Machine Translation

1.Import the Library
from translate import Translator

2.Create a Translator Object
translator = Translator(to_lang='es')  # Spanish

3.Choose a Phrase
# Text to be translated
text = 'Hello, how are you?'

4.Translate
# Perform the translation
translation = translator.translate(text)

5.# Print the translated text
print('Translated Text:', translation)

