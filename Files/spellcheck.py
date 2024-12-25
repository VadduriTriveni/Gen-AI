Call the TextBlob library. Create a new python file with the code below.
from textblob import TextBlob

Make a mistake. Create a text variable with a spelling error.
text = 'I love progamming and machine learnig.'

Create a TextBlob object with the text.
blob = TextBlob(text)

Check your spelling
corrected_text = blob.correct()

# Print the corrected text
print('Original Text:', text)
print('Corrected Text:', corrected_text)
