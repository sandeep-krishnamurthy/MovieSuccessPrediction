"""
Plots a pie chart. Uses matplotlib and pylab.

"""

import matplotlib.pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages

from os import system
from os import path

def generate_piechart(title, pos_percent, neg_percent, fig_num):
    # make a square figure and axes
    fig = plot.figure(fig_num, figsize=(6,6))
    #ax = fig.add_subplot(axes([0.1, 0.1, 0.8, 0.8]))

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Positive', 'Negative'
    fracs = [pos_percent, neg_percent]
    explode=(0.05, 0.01)

    mypie = plot.pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

    plot.title(title, bbox={'facecolor':'0.8', 'pad':5})

    return fig

def create_TitlePage(title, fig_num):
    fig = plot.figure(fig_num, figsize=(6,6))
    fig.suptitle(title, fontsize=14, fontweight='bold')
    return fig
'''
# Example of how to call.

plot0 = create_TitlePage('Our Verdict\nTwitter-Hit\nNB-Hit\nSVM-Flop', 0)
plot1 = generate_piechart('NB Classification on Twitter Data on Movie:RAM LEELA',76, 24,1) 
plot2 = generate_piechart('SVM Classification on Twitter Data on Movie:RAM LEELA',56, 44, 2)
plot3 = generate_piechart('Baseline Classification on Twitter Data on Movie:RAM LEELA',46, 24, 3) 
keyword = 'test'
pp = PdfPages(path.abspath('../Results/KeywordClassifier/'+ keyword+ '.pdf'))
pp.savefig(plot0)
pp.savefig(plot1)
pp.savefig(plot2)
pp.savefig(plot3)
pp.close()

system('start ' + path.abspath('../Results/KeywordClassifier/'+ keyword+ '.pdf'))

'''
