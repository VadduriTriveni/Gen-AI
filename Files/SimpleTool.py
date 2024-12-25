To build a simple tool to help you decide if a movie is worth watching based on text reviews. 
By analyzing if the reviews are positive or negative, you can get a sense of whether people liked the movie or not.

Let’s get start!

1.Set Up Your Environment
Start a Python script and make sure the necessary Python libraries have been installed:

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

2.Gather Your Data
Create a list of sample movie reviews, ask some friends or pick the top online reviews. Each review should express either a positive or negative opinion.
Label Your Data
Label each review as either "positive" or "negative." Example:

reviews = ['This movie was fantastic! A must-watch.',
           'I didn\'t enjoy this movie at all.',
           'Amazing storyline and great acting!',
           'The plot was dull and predictable.',
           'Loved the cinematography! Highly recommended.']

labels = ['positive', 'negative', 'positive', 'negative', 'positive']

3.Vectorize the Text Data
Convert your text data into numbers that the computer can understand using CountVectorizer:

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)

4.Split the Data
Split your data into training and testing sets so the computer can learn from some data and be tested on the rest:

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

5.Train the Model
Create a Naive Bayes classifier and train it using the training data:

model = MultinomialNB()
model.fit(x_train, y_train)

6.Test the Model
Use the trained model to predict the vibes of the test data:

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)

7.Interpret the Results
Finally, you can decide if the movie has "Good vibes!" based on the accuracy of your model. 
If the accuracy is above 80%, print "Good vibes!"

if accuracy > 0.8:
  print('Good vibes. Book the ticket!')
else:
  print('Needs more work!')
