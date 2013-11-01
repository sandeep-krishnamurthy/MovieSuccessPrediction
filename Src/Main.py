import sys;

# Entry point of complete project.

# Get all parameters required for execution.
movie_name = raw_input("Enter Movie Name: ");
movie_language = raw_input("Language of '"movie_name"' movie? "); 
#movie_released = (int)raw_input("Is this movie already released? 0-No 1-Yes: ");

# Build keywords for search.
#key_words = []
key_word = (movie_name+ " " + movie_language + " Movie Trailer");

#if(movie_released):
#    key_words.append(movie_name+ " " + movie_language + " Movie Review");


# Call method to perform training
print "Systems is learning and getting trained to predict :) :)....\n"


# Fetch data from twitter
print "Fetching tweets from Twitter for keyword = ' " + key_word =" '. Please wait.....\n"

# Fetch data from youtube
print "Fetching tweets from YouTube for keyword = ' " + key_word =" '. Please wait.....\n"

# Clean twitter data
print "Cleaning tweets. Please wait.....\n"

# Clean YouTube data
print "Cleaning youtube data. Please wait.....\n"

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


