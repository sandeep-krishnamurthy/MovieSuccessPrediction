import sys;
from YouTubeDataProvider import getYouTubeComments
from TwitterDataProvider import get_tweets
import IOHelper
import DataPreprocessor

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

twitter_data = []
is_tweet_from_file = False

# check if data is already present or should be fetched
if (IOHelper.checkIfFileExists('../Data/TwitterDataContainer', key_word + '.csv')):
    print "Data already present !! Skipping data fetch from twitter"
    twitter_data = IOHelper.readCsvToStringList('../Data/TwitterDataContainer/'+ key_word + '.csv')
    print "Completed fetching tweets from file !!\n\n"
    is_tweet_from_file = True
else:
    # Fetch data from twitter
    print "Fetching tweets from Twitter for keyword = ' " + key_word +" '. Please wait.....\n"
    twitter_data = get_tweets(key_word, 10)
    print "Completed fetching tweets from Twitter !!\n\n"


#--------------------------------------- STEP 3: YOUTUBE DATA---------------------------------------------

youTube_data = []
is_yt_comment_from_file = False

# check if data is already present or should be fetched
if (IOHelper.checkIfFileExists('../Data/YouTubeDataContainer', key_word + '.csv')):
    print "Data already present !! Skipping data fetch from YouTube"
    youTube_data = IOHelper.readCsvToStringList('../Data/YouTubeDataContainer/'+ key_word + '.csv')
    print "Completed fetching youtube comments from file !!\n\n"
    is_yt_comment_from_file = True
else:
    # Fetch data from youtube
    print "Fetching videos and comments from YouTube for keyword = ' " + key_word + ' Trailer' +" '. Please wait.....\n"
    youTube_data = getYouTubeComments(key_word+' Trailer', 10)
    print "Completed fetching YouTube comments !!"

#--------------------------------------- STEP 4: PREPROCESS TWITTER DATA---------------------------------------

if (is_tweet_from_file):
    print "Data is already pre-processed !! Skipping twitter data pre-processing"
else:
    twitter_data = DataPreprocessor.PreprocessStringList(twitter_data)
    print "Twitter Data pre-processing complete !!"

#--------------------------------------- STEP 5: PREPROCESS YOUTUBE DATA---------------------------------------    

if (is_yt_comment_from_file):
    print "Data is already pre-processed !! Skipping youtube data pre-processing"
else:
    youTube_data = DataPreprocessor.PreprocessStringList(youTube_data)
    print "YouTube Data pre-processing complete !!"
    
#--------------------------------------- STEP 6: STORE TWITTER AND YOUTUBE DATA-----------------------------------

if( not is_tweet_from_file):
    IOHelper.writeStringListToCsv('../Data/TwitterDataContainer/'+ key_word + '.csv', twitter_data)
    print "Succesfully stored retrieved twitter data to file !!\n\n"

if( not is_yt_comment_from_file):
    IOHelper.writeStringListToCsv('../Data/YouTubeDataContainer/'+ key_word + '.csv', youTube_data)
    print "Succesfully stored retrieved youtube data to file !!\n\n"

#--------------------------------------- STEP 7: STORE TWITTER AND YOUTUBE DATA-----------------------------------
    
# Calculate using SVM Classifier
print "Using SVM Classification Technique. Please wait...\n"

print "SVM based prediction done !!!\n"

# Calculate using Naive Bayes Classifier
print "Using Naive Bayes Classification Technique. Please wait...\n"

print "Naive Bayes based prediction done !!!\n"

# Calculate using Maximum Entropy Classifier
print "Using Maximum Entropy Classification Technique. Please wait...\n"

print "Maximum Entropy based prediction done !!!\n"

# Print Results of all 3 methods.


