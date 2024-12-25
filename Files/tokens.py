Tokenization

In your code editor, create a new tokens.py file.

1.Import the tokenize library with the following code:

import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

2.Use the code below to perform a simple tokenization task:

sample_text = 'I love programming!'
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)

Your output should return a list of strings that represent the tokens in the sample_text.
