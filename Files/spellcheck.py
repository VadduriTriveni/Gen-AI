Spell Check

1.Call the TextBlob library. Create a new python file with the code below.
from textblob import TextBlob

2.Make a mistake. Create a text variable with a spelling error.
text = 'I love progamming and machine learnig.'

3.Create a TextBlob object with the text.
blob = TextBlob(text)

4.Check your spelling
corrected_text = blob.correct()

5.# Print the corrected text
print('Original Text:', text)
print('Corrected Text:', corrected_text)

Your output should return Corrected Text: I love programming and machine learning.
