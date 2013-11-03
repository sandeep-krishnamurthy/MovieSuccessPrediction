from os import listdir
import csv

''' Helper methods to perform of file operations.'''
'''
Checks if all characters are ascii. If not skip that comment.
'''
def is_ascii(sentence):
    return all(ord(c) < 128 for c in sentence)
    
'''
Description: Write given list of strings to specified filename. Overwrites contents if file already exists.
Input: filename and string list
Output: None
'''
def writeStringListToCsv(filename, listofitems):
    outFile = open(filename,'wb')
    writer = csv.writer(outFile)
    for item in listofitems:
        # some error arises due to non-ascii characters. skip it.
        #try:
            #if is_ascii(item):
        writer.writerow([item])
        #except Exception as e:
            #print e
         #   pass

    outFile.close()
    return


'''
Description: List each row from csv as string and build list of strings.
Input: filename from where to read. Full path should be provided
Output: List of strings.
'''
def readCsvToStringList(filename):
    infile = open(filename, 'rb')
    reader = csv.reader(infile)
    mylist = []
    for row in reader:
        mylist.append(row[0])

    infile.close()
    return mylist

'''
Description: Given a full path or relative path, checks if file already exists
input: Directory path and filename to be searched, only name of file must be provided.
Output: True or False based on file found or not.
'''
def checkIfFileExists(dirpath, filename):
    return (filename in listdir(dirpath))
