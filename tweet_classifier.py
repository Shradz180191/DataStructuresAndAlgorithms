# Improting necessary modules
import numpy as np
import pandas as pd
import re
import nltk
from sklearn.datasets import load_files
import pickle
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier


# Step 1 - Load the data from the provided train file 
tweets_data = pd.read_csv("C:/Users/Shraddha/python/train.tsv", sep='\t')

# Step 1.1 - The train data doesn't have the column names
# associated, so I'm assigning column names to the data
tweets_data.columns = ['tweet_id', 'tweet', 'label']

# Step 1.2 - Here I'm filtering out X and y for our 
# classifaction problem, tweet text as x and label as our predictor
X, y = tweets_data.tweet, tweets_data.label


# Step 2 - Text Pre processing
# The idea is that the text is very open, we would ideally want to 
# remove special characters, punctuations, extra spaces and I need 
# all of them to be in lower case
all_tweets = []
stemmer = WordNetLemmatizer()

for sen in range(0, len(X)):
    # Remove all the special characters
    tweet = re.sub(r'\W', ' ', str(X[sen]))
    
    # remove all single characters
    tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', tweet)
    
    # Remove single characters from the start
    tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', tweet) 
    
    # Substituting multiple spaces with single space
    tweet = re.sub(r'\s+', ' ', tweet, flags=re.I)
    
    # Removing prefixed 'b'
    tweet = re.sub(r'^b\s+', '', tweet)
    
    # Converting to Lowercase
    tweet = tweet.lower()
    
    # Lemmatization
    tweet = tweet.split()

    tweet = [stemmer.lemmatize(word) for word in tweet]
    tweet = ' '.join(tweet)
    
    all_tweets.append(tweet)


# Step 3 - Computers in general cannot interpret characters, so ideally
# we would want to convert them to digits, which we are doing here 
tfidfconverter = TfidfVectorizer(max_features=1000, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(all_tweets)


# step 4 - In order to build a model we need both the Training and validation sets
# so we are splitting the train data into both training and validation sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# step 5 - build a random forest classifier on the training data
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train) 

# step 6 - get the predictions for the training dataset 
y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))



# Step 7 - Save the model in a file, so we don't have 
# to train the model every time. rb original but changed it to w 
with open('C:/Users/Shraddha/python/tweet_classifier.pkl', 'wb') as pf:
	pickle.dump(classifier, pf)


#########################################################33

# Step 8 - We have a new test.tsv file on which we have 
# to make the predictions 

# So we load the model first. 
# Test it on the training set 
with open('C:/Users/Shraddha/python/tweet_classifier.pkl', 'rb') as training_model:
	classifier = pickle.load(training_model)

# Read the new test.tsv data
test_data = pd.read_csv("C:/Users/Shraddha/python/test.tsv", sep='\t')
test_data.columns = ['tweet_id', 'tweet', 'label']
X_test, y_test = test_data.tweet, test_data.label




all_tweets_test = []

for sen in range(0, len(X_test)):
    # Remove all the special characters
    tweet = re.sub(r'\W', ' ', str(X_test[sen]))
    
    # remove all single characters
    tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', tweet)
    
    # Remove single characters from the start
    tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', tweet) 
    
    # Substituting multiple spaces with single space
    tweet = re.sub(r'\s+', ' ', tweet, flags=re.I)
    
    # Removing prefixed 'b'
    tweet = re.sub(r'^b\s+', '', tweet)
    
    # Converting to Lowercase
    tweet = tweet.lower()
    
    # Lemmatization
    tweet = tweet.split()

    tweet = [stemmer.lemmatize(word) for word in tweet]
    tweet = ' '.join(tweet)
    
    all_tweets_test.append(tweet)

X_test = tfidfconverter.transform(all_tweets_test)



# Make predictions on the test data using our model 
y_pred2 = classifier.predict(X_test)


# Replace the label column value in the test dataframe
# and export it to the test.tsv file so we have the predicted
# labels in the file :) 
test_data.label = y_pred2
test_data.to_csv('C:/Users/Shraddha/python/test_result.tsv', index=False, header=False, sep='\t')
