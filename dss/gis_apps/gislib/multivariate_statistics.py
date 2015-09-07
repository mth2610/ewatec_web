import numpy as np
import pandas
import csv
#from matplotlib import dates
import matplotlib as mpl
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image, StringIO
import matplotlib.pyplot as plt
import scipy.stats as st
from datetime import datetime
import time
from matplotlib.ticker import MaxNLocator
from matplotlib.dates import DateFormatter
from pandas.tools import plotting
import itertools

def scatterplot_matrix(data, names, **kwargs):
    """Plots a scatterplot matrix of subplots.  Each row of "data" is plotted
    against other rows, resulting in a nrows by nrows grid of subplots with the
    diagonal subplots labeled with "names".  Additional keyword arguments are
    passed on to matplotlib's "plot" command. Returns the matplotlib figure
    object containg the subplot grid."""
    numvars, numdata = data.shape
    
    fig, axes = plt.subplots(nrows=numvars, ncols=numvars, figsize=(8,8))
    fig.subplots_adjust(hspace=0.05, wspace=0.05)

    for ax in axes.flat:
        # Hide all ticks and labels
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        # Set up ticks only on one side for the "edge" subplots...
        if ax.is_first_col():
            ax.yaxis.set_ticks_position('left')
        if ax.is_last_col():
            ax.yaxis.set_ticks_position('right')
        if ax.is_first_row():
            ax.xaxis.set_ticks_position('top')
        if ax.is_last_row():
            ax.xaxis.set_ticks_position('bottom')
    
    
    # Label the diagonal subplots...
    for i, label in enumerate(names):
        n, bins, patches = axes[i,i].hist((data[i])[~np.isnan(data[i])], normed=1, facecolor='blue', alpha = 0.5)
        axes[i,i].annotate(label, (0.5, 0.9), xycoords='axes fraction',
                ha='center', va='center',size = 15)
        
    # Plot the data.
    for i, j in zip(*np.triu_indices_from(axes, k=1)):
        for x, y in [(j,i)]:
            print x,y
            
            axes[x,y].scatter(data[y], data[x], **kwargs)
            
            if x == (numvars - 1):   
                axes[x,y].xaxis.set_visible(True)
                axes[x,y].xaxis.set_major_locator(MaxNLocator(4))
            
            if y == 0:
                axes[x,y].yaxis.set_visible(True)
                axes[x,y].yaxis.set_major_locator(MaxNLocator(4))
            
            
            pearson_correlation = st.pearsonr(data[y],data[x])
            axes[y,x].annotate("%.3f" %pearson_correlation[0], (0.5, 0.5), xycoords='axes fraction',
                ha='center', va='center',size = 30*np.sqrt(pearson_correlation[0]**2))
            
            if pearson_correlation[1] <= 0.001:
                axes[y,x].annotate("***", (0.8, 0.8), xycoords='axes fraction',
                    ha='center', va='center',size = 20, color = "red")
            elif 0.001 < pearson_correlation[1] <= 0.01:
                axes[y,x].annotate("**", (0.8, 0.8), xycoords='axes fraction',
                    ha='center', va='center',size = 20, color = "red")
            elif 0.01 < pearson_correlation[1] <= 0.05:
                axes[y,x].annotate("*", (0.8, 0.8), xycoords='axes fraction',
                    ha='center', va='center',size = 20, color = "red")
            elif 0.05 < pearson_correlation[1] <= 0.1:
                axes[y,x].annotate(".", (0.8, 0.8), xycoords='axes fraction',
                    ha='center', va='center',size = 20, color = "red")
            else:
                pass
    
#     Turn on the proper x or y axes ticks.

    axes[0,0].yaxis.set_visible(True)
    axes[0,0].yaxis.set_major_locator(MaxNLocator(4))
    axes[-1,-1].xaxis.set_visible(True)
    axes[-1,-1].xaxis.set_major_locator(MaxNLocator(4))
#    axes[-1,-1].yaxis.set_visible(True)
#    axes[-1,-1].yaxis.set_major_locator(MaxNLocator(4))
    
#    for i, j in zip(range(numvars), itertools.cycle((-1, 0))):
#        
#        
#        if (i,j) in zip(*np.triu_indices_from(axes, k=1)):
#            pass 
#        else:
#            axes[j,i].xaxis.set_visible(True)
#            axes[j,i].xaxis.set_major_locator(MaxNLocator(4))
#            axes[i,j].yaxis.set_visible(True)
#            axes[j,i].yaxis.set_major_locator(MaxNLocator(5))
#            
    
    
    return fig


class general_statistic():
    def __init__(self,DF):
        self.DF = DF
        
    def multi_timeserise_plot(self):
        DF = self.DF
        datetime = np.array(DF.index.values)
        figure = plt.figure(facecolor='white')
        print "testn"
        i = 0
        n_colums = (DF.shape)[1]
        for e in DF:
            try:
                if i == 0:
                    subplot0 = figure.add_subplot(n_colums,1,1+i)
                    plot0, = subplot0.plot(datetime,DF[e])
                    subplot0.legend([str(e)],prop={'size':7})
                    subplot0.xaxis.set_major_locator(MaxNLocator(6))
                    subplot0.yaxis.set_major_locator(MaxNLocator(4))
                    setp(subplot0.get_xticklabels(), visible=False)
                else:
                    subplot = figure.add_subplot(n_colums,1,1+i,sharex=subplot0)
                    plot, = subplot.plot(datetime,DF[e])
                    subplot.legend( [str(e)],prop={'size':7})
                    subplot.xaxis.set_major_locator(MaxNLocator(6))
                    subplot.yaxis.set_major_locator(MaxNLocator(4))
                    if i + 1 == n_colums:
                        setp(subplot.get_xticklabels(), visible=True)
                    else:
                        setp(subplot.get_xticklabels(), visible=False)
            except Exception as inst:
                print type(inst)     # the exception instance
                print inst.args      # arguments stored in .args
                print inst
                
            i = i + 1

        
        # Store image in a string buffer
            
        buffer = StringIO.StringIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()
        pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
        pilImage.save(buffer, "PNG")
        pylab.close()
        img = str((buffer.getvalue()).encode('Base64'))      
        
        return img
    
    def scatter_plot(self):
        DF = self.DF
        
        DF = DF.dropna()
        data = (DF.as_matrix()).T
        variable = list(DF.keys())

        figuge = scatterplot_matrix(data,variable)
        print dir(figuge)
        figuge.set_facecolor('white')
#        figure.patch.set_facecolor('white')
        # Store image in a string buffer
        
        buffer = StringIO.StringIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()
        pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
        pilImage.save(buffer, "PNG")
        pylab.close()
        img = str((buffer.getvalue()).encode('Base64'))
        
        return img