N-grams

Let's build some n-gram models with the nltk Python library. 💛

Import the ngrams and word_tokenize packages from the nltk library.

import nltk
from nltk import word_tokenize
from nltk.util import ngrams

Tokenize a phrase, you can use your favorite quote!

sample_text = 'I am learning NLP(Natural Language Processing)'
tokens = word_tokenize(sample_text)

Generate unigrams, bigrams, and trigrams from the tokens.
# Unigram
unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

# Bigram
bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

# Trigram
trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)

Take a look at the output and see how the n-grams are generated from the tokens!
