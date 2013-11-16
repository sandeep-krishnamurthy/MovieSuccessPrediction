import re


'''
Description: Pre-process and clean all strings provided as input.
Input: List of strings to be cleaned or preprocessed.
Output: List of cleaned and preprocessed strings.
'''

def PreprocessStringList(inputList):

    newList = []
    for sentence in inputList:
        if sentence is not None:
            #Convert to lower case
            sentence = sentence.lower()
            #Convert https?://* to URL
            sentence = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',sentence)
            #Convert @username to AT_USER
            sentence = re.sub('@[^\s]+','AT_USER',sentence)    
            #Remove additional white spaces
            sentence = re.sub('[\s]+', ' ', sentence)
            #Replace #word with word
            sentence = re.sub(r'#([^\s]+)', r'\1', sentence)
            #trim
            sentence = sentence.strip()
            #remove first/last " or 'at string end
            sentence = sentence.rstrip('\'"')
            sentence = sentence.lstrip('\'"')
            #remove all non-ascii characters
            sentence = "".join(c for c in sentence if ord(c)<128)       

            newList.append(sentence)

    return newList


