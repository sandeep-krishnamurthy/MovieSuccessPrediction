'''
Performs result calculations. Following model is used for calculations.
Input: Total count, Positive count, negative count, neutral count.
Output: Blockbuster : if positive percent > 70
        Good: if  60 < positive percent < 70
        Average: if 50 < positive percent < 60
        Mediocore: if 40 < positive percent < 50
        Poor: if positive percent < 40
        Cannot Predict : if total_count == 0
Some tweaks: if neutral count is too large it may affect overall performance of model
            hence with lot of trial and error I have come across model in which if postive count > negative count
            then we add 70% of neutral count to postive and 30% of neutral count to negative count and also vice versa if negative count > positive count.
            In case of equal, I will give benefit of doubt to postivity.    
'''

def perform_analysis(total_count, pos_count, neg_count, neut_count):

    #print 'pos count : ', pos_count
    #print 'neg count : ', neg_count
    #print 'neut count : ', neut_count
    #print 'total count : ', total_count

    #print '------------------------------------------'
    if total_count <=0:
        return "Cannot Predict"
    
    if pos_count >= neg_count:
        pos_count = float(pos_count) + (0.7 * float(neut_count))
        neg_count = float(neg_count) + (0.3 * float(neut_count))
    else:
        pos_count = float(pos_count) + (0.3 * float(neut_count))
        neg_count = float(neg_count) + (0.7 * float(neut_count))

    pos_percent = (float(pos_count) / float(total_count)) * 100
    neg_percent = (float(neg_count) / float(total_count)) * 100

    #print 'positive percent:', pos_percent
    #print 'negative percent:', neg_percent

    #print 'positive count:', pos_count
    #print 'negative count:', neg_count
    #print 'total count:', total_count

    #print '---------------------------------------------'
    if pos_percent >= 70.0:
        return "Blockbuster !!"
    elif pos_percent >= 60.0 and pos_percent < 70.0:
        return "Good !!"
    elif pos_percent >= 50.0 and pos_percent < 60.0:
        return "Average !!"
    elif pos_percent >= 40.0 and pos_percent < 50.0:
        return "Mediocore !!"
    elif pos_percent < 40.0:
        return "Poor !!"
    else:
        return " Cannot Predict"
