N-grams

Let's build some n-gram models with the nltk Python library. 💛

1.Import the ngrams and word_tokenize packages from the nltk library.

import nltk
from nltk import word_tokenize
from nltk.util import ngrams

2.Tokenize a phrase, you can use your favorite quote!

sample_text = 'I am learning NLP(Natural Language Processing)'
tokens = word_tokenize(sample_text)

3.Generate unigrams, bigrams, and trigrams from the tokens.
# Unigram
unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

# Bigram
bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

# Trigram
trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)

Your output should return list of ngrams.
Unigrams: [('I',), ('am',), ('learning',), ('NLP',), ('(',), ('Natural',), ('Language',), ('Processing',), (')',)]
Bigrams: [('I', 'am'), ('am', 'learning'), ('learning', 'NLP'), ('NLP', '('), ('(', 'Natural'), ('Natural', 'Language'), ('Language', 'Processing'), ('Processing', ')')]
Trigrams: [('I', 'am', 'learning'), ('am', 'learning', 'NLP'), ('learning', 'NLP', '('), ('NLP', '(', 'Natural'), ('(', 'Natural', 'Language'), ('Natural', 'Language', 'Processing'), ('Language', 'Processing', ')')]
