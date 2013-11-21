import sys;
from YouTubeDataProvider import getYouTubeComments
from TwitterDataProvider import get_tweets
import IOHelper
import DataPreprocessor
import KeywordClassifier
import NaiveBayesClassifier
import libsvm_classifier
import datetime

print "START TIME: ", datetime.datetime.time(datetime.datetime.now())

# Entry point of complete project.

# Get all parameters required for execution.
movie_name = raw_input("Enter Movie Name: ");
movie_language = raw_input("Language of '"+ movie_name + "' movie? "); 
#movie_released = (int)raw_input("Is this movie already released? 0-No 1-Yes: ");

#--------------------------------------- STEP 1: KEYWORD PREPARATION -------------------------------------

#key_words = []
key_word = (movie_name+ " " + movie_language + " Movie");

#if(movie_released):
#    key_words.append(movie_name+ " " + movie_language + " Movie Review");


# Call method to perform training
#print "Systems is learning and getting trained to predict :) :)....\n"


#--------------------------------------- STEP 2: TWITTER DATA---------------------------------------------

twitter_data = {}
is_tweet_from_file = False

# check if data is already present or should be fetched
if (IOHelper.checkIfFileExists('../Data/TwitterDataContainer', key_word + '.csv')):
    print "Data already present !! Skipping data fetch from twitter"
    twitter_data[0] = IOHelper.readCsvToStringList('../Data/TwitterDataContainer/'+ key_word + '.csv')
    print "Completed fetching tweets from file !!\n\n"
    is_tweet_from_file = True
else:
    # Fetch data from twitter
    #print "Fetching tweets from Twitter for keyword = ' " + key_word +" '. Please wait.....\n"
    print "Fetching tweets from Twitter for keyword = ' " + movie_name + " Movie" +" '. Please wait.....\n"
    #twitter_data[0] = get_tweets(key_word, 100)
    twitter_data[0] = get_tweets(movie_name+' Movie', 10)
    print "Completed fetching tweets from Twitter !!\n\n"


#--------------------------------------- STEP 3: YOUTUBE DATA---------------------------------------------

youTube_data = {}
is_yt_comment_from_file = False

# check if data is already present or should be fetched
if (IOHelper.checkIfFileExists('../Data/YouTubeDataContainer', key_word + '.csv')):
    print "Data already present !! Skipping data fetch from YouTube"
    youTube_data[0] = IOHelper.readCsvToStringList('../Data/YouTubeDataContainer/'+ key_word + '.csv')
    print "Completed fetching youtube comments from file !!\n\n"
    is_yt_comment_from_file = True
else:
    # Fetch data from youtube
    print "Fetching videos and comments from YouTube for keyword = ' " + key_word + ' Trailer' +" '. Please wait.....\n"
    youTube_data[0] = getYouTubeComments(key_word+' Trailer', 10)
    print "Completed fetching YouTube comments !!"

#--------------------------------------- STEP 4: PREPROCESS TWITTER DATA---------------------------------------

if (is_tweet_from_file):
    print "Data is already pre-processed !! Skipping twitter data pre-processing"
else:
    twitter_data[0] = DataPreprocessor.PreprocessStringList(twitter_data[0])
    print "Twitter Data pre-processing complete !!"

#--------------------------------------- STEP 5: PREPROCESS YOUTUBE DATA---------------------------------------    

if (is_yt_comment_from_file):
    print "Data is already pre-processed !! Skipping youtube data pre-processing"
else:
    youTube_data[0] = DataPreprocessor.PreprocessStringList(youTube_data[0])
    print "YouTube Data pre-processing complete !!"
    
#--------------------------------------- STEP 6: STORE TWITTER AND YOUTUBE DATA-----------------------------------

if( not is_tweet_from_file):
    IOHelper.writeStringListToCsv('../Data/TwitterDataContainer/'+ key_word + '.csv', twitter_data[0])
    print "Succesfully stored retrieved twitter data to file !!\n\n"

if( not is_yt_comment_from_file):
    IOHelper.writeStringListToCsv('../Data/YouTubeDataContainer/'+ key_word + '.csv', youTube_data[0])
    print "Succesfully stored retrieved youtube data to file !!\n\n"

#--------------------------------------- STEP 7: BASELINE CLASSIFICATION -----------------------------------

print "Twitter classification Results:\n\n"



bc = KeywordClassifier.KeywordClassifier(twitter_data, key_word)
bc.classify()
bc.printResults('twitter', 0) # 0 is for marking figure number - 0 and 1 is used here

print "\n\nYoutube data classification Results:\n\n"
bc = KeywordClassifier.KeywordClassifier(youTube_data, key_word)
bc.classify()
bc.printResults('youtube', 2) 

#--------------------------------------- STEP 8: SVM CLASSIFICATION -----------------------------------

print "Using SVM Classification Technique. Please wait...\n"

# SVM on Twitter
print "Using SVM Classification Technique on Twitter Data. Please wait...\n"

#trainingDataFile = 'data/training_trimmed.csv'
trainingDataFile = '../Data/SVM/trimmed_training_dataset_2000.csv'
classifierDumpFile = '../Data/SVM/svm_test_model.pickle'
trainingRequired = 0
sc = libsvm_classifier.SVMClassifier(twitter_data, key_word, trainingDataFile, classifierDumpFile, trainingRequired)
sc.classify()
sc.printResults('twitter', 4)
#sc.accuracy()

#SVM on YouTube Data

print "Using SVM Classification Technique on YouTube Data. Please wait...\n"

trainingRequired = 0
#trainingDataFile = 'data/full_training_dataset.csv'                
sc = libsvm_classifier.SVMClassifier(youTube_data, key_word, trainingDataFile, classifierDumpFile, trainingRequired)
sc.classify()
sc.printResults('youtube',  6)

print "SVM based prediction done !!!\n"

#--------------------------------------- STEP 9: NAIVE BAYES CLASSIFICATION -----------------------------------

# Calculate using Naive Bayes Classifier
print "Using Naive Bayes Classification Technique on Twitter Data. Please wait...\n"

trainingDataFile = '../Data/NaiveBayes/full_training_dataset.csv'
# Here we can use some other training data set - shortened for speeding process.
classifierDumpFile = '../Data/NaiveBayes/naivebayes_test_model.pickle'
trainingRequired = 0 # Set to 0 when not required after pickle file is created.
time = 'today'
nb = NaiveBayesClassifier.NaiveBayesClassifier(twitter_data, key_word, time,trainingDataFile, classifierDumpFile, trainingRequired)
nb.classify()
#nb.accuracy()
#nb.writeOutput('nboutput1.txt')
nb.printResults('twitter', 8)

print "Using Naive Bayes Classification Technique on YouTube Data. Please wait...\n"
trainingRequired = 0
nb = NaiveBayesClassifier.NaiveBayesClassifier(youTube_data, key_word, time,trainingDataFile, classifierDumpFile, trainingRequired)
nb.classify()
#nb.accuracy()
#nb.writeOutput('nboutput2.txt')
nb.printResults('youtube',  10)
    
print "Naive Bayes based prediction done !!!\n"

print "END TIME: ", datetime.datetime.time(datetime.datetime.now())
