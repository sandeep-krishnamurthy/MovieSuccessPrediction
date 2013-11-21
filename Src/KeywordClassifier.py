import sys
import os
import re
import pickle

from matplotlib.backends.backend_pdf import PdfPages
from os import system
from os import path
import subprocess
import os

import Result_Calculator
import chart_helper

class KeywordClassifier:
    """ Classifier using baseline method aka keyword based classification. """
    
    def __init__(self, data, keyword):
        #Remove duplicates        
        self.dataLen = len(data)
        self.origData = self.getUniqData(data)
        self.processedData = self.getProcessedTweets(self.origData)

        self.total_count = len(self.origData[0])
        #print 'important, ', len(data[0]), len(self.origData[0])
        
        self.results = {}
        self.neut_count = [0] * self.dataLen
        self.pos_count = [0] * self.dataLen
        self.neg_count = [0] * self.dataLen

        self.keyword = keyword
    #end
    
    #start getUniqData
    def getUniqData(self, data):
        uniq_data = {}        
        for i in data:
            d = data[i]
            u = []
            for element in d:
                if element not in u:
                    u.append(element)
            #end inner loop
            uniq_data[i] = u            
        #end outer loop
        return uniq_data
    #end
    
    #start getProcessedTweets or youtube comments
    def getProcessedTweets(self, data):        
        tweets = {}        
        for i in data:
            d = data[i]
            tw = []
            for t in d:
                tw.append(t) #Already processed at this point.
            tweets[i] = tw            
        #end loop
        return tweets
    
    #start classify
    def classify(self):
        #load positive keywords file          
        inpfile = open('../Data/KeywordClassifierData/pos_mod.txt', "r")            
        line = inpfile.readline()
        positive_words = []
        while line:
            positive_words.append(line.strip())
            line = inpfile.readline()
            
        #load negative keywords file    
        inpfile = open('../Data/KeywordClassifierData/neg_mod.txt', "r")            
        line = inpfile.readline()
        negative_words = []
        while line:
            negative_words.append(line.strip())
            line = inpfile.readline()
        #start processing each tweet or youtube comment        
        for i in self.processedData:
            tw = self.processedData[i]
            count = 0
            res = {}
            for t in tw:
                neg_words = [word for word in negative_words if(self.string_found(word, t))]
                pos_words = [word for word in positive_words if(self.string_found(word, t))]
                if(len(pos_words) > len(neg_words)):
                    label = 'positive'
                    self.pos_count[i] += 1
                elif(len(pos_words) < len(neg_words)):
                    label = 'negative'
                    self.neg_count[i] += 1
                else:
                    if(len(pos_words) > 0 and len(neg_words) > 0):
                        label = 'positive'
                        self.pos_count[i] += 1
                    else:
                        label = 'neutral'
                        self.neut_count[i] += 1
                result = {'text': t, 'tweet': self.origData[i][count], 'label': label}
                res[count] = result                
                count += 1         
            #end inner loop
            self.results[i] = res
        #end outer loop   
        filename = '../Data/KeywordClassifierData/results_lastweek.pickle'
        outfile = open(filename, 'wb')        
        pickle.dump(self.results, outfile)        
        outfile.close()
        '''
        inpfile = open('data/results_lastweek.pickle')
        self.results = pickle.load(inpfile)
        inpfile.close()
        '''
    #end
    
    #start substring whole word match
    def string_found(self, string1, string2):
        if re.search(r"\b" + re.escape(string1) + r"\b", string2):
            return True
        return False
    #end
    
    #start writeOutput
    def writeOutput(self, filename, writeOption='w'):
        fp = open(filename, writeOption)
        for i in self.results:
            res = self.results[i]
            for j in res:
                item = res[j]
                text = item['text'].strip()
                label = item['label']
                writeStr = text+" | "+label+"\n"
                fp.write(writeStr)
            #end inner loop
        #end outer loop      
    #end writeOutput
    
    #start printStats
    # Here utilize this data for plotting google chart.                
    def printResults(self, source, fig_num):
        '''
        print self.keyword
        print self.results
        
        print "Positive: ", self.pos_count
        print "Negative: ", self.neg_count
        print "Neutral: ", self.neut_count

        '''
        
        
        positive_count = self.pos_count[0]
        negative_count = self.neg_count[0]
        neutral_count = self.neut_count[0]
        
        res = Result_Calculator.perform_analysis(self.total_count, positive_count, negative_count, neutral_count)

        
        title = None
        outfile_path = path.abspath('../Results/KeywordClassifier/'+ self.keyword+' ' + source + '.pdf')
        
        if res == "Cannot Predict":
            output = "We don't have sufficient data to predict result for " + self.keyword + " sorry :( :("
            title = chart_helper.create_TitlePage(output, fig_num)
            pp = PdfPages(outfile_path)
            pp.savefig(title)
            pp.close()

            os.startfile(outfile_path, 'start')
            
            print output                     
            return

        # Calculate percentages of positive and negative
        if positive_count >= negative_count:
            positive_count = float(positive_count) + (0.7 * float(neutral_count))
            negative_count = float(negative_count) + (0.3 * float(neutral_count))
        else:
            positive_count = float(positive_count) + (0.3 * float(neutral_count))
            negative_count = float(negative_count) + (0.7 * float(neutral_count))

        
        positive_percent = (float(positive_count) / float(self.total_count)) * 100
        negative_percent = (float(negative_count) / float(self.total_count)) * 100
    
        output = "KEYWORD CLASSIFIER PREDICTION:\n\n" + self.keyword+ " is going to be "+ res
        print output

        title = chart_helper.create_TitlePage(output, fig_num)
        p_chart = chart_helper.generate_piechart('Keyword Classifier Results', positive_percent, negative_percent, fig_num+1)
        
        pp = PdfPages(outfile_path)
        pp.savefig(title)
        pp.savefig(p_chart)
        pp.close()

        os.startfile(outfile_path, 'open')
            
        
        # 
        #return self.html.getResultHTML(self.keyword, self.results, self.time, self.pos_count, \
         #                              self.neg_count, self.neut_count, 'baseline')
    #end
#end class    
