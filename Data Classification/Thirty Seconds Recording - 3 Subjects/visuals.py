###########################################
# Suppress matplotlib user warnings
# Necessary for newer version of matplotlib
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
#
# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
###########################################

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

def distribution(data, value, transformed = False):
    """
    Visualization code for displaying skewed distributions of features
    """
    # Create figure
    fig = plt.figure(figsize = (11,5));

    # Skewed feature plotting
    for i, feature in enumerate([value]):
        ax = fig.add_subplot(1, 1, i+1)
        ax.hist(data[data.columns[feature-1]], bins = 25, color = '#00A0A0')
        ax.set_title("'%s' Feature Distribution"%(data.columns[feature-1]), fontsize = 14)
        ax.set_xlabel("Value")
        ax.set_ylabel("Number of Records")
        ax.set_ylim((0, 500))
        ax.set_yticks([0, 100, 200, 300, 400, 500])

    # Plot aesthetics
    if transformed:
        fig.suptitle("Log-transformed Distributions of Continuous EEG Data Features", \
            fontsize = 16, y = 1.03)
    else:
        fig.suptitle("Skewed Distributions of Continuous EEG Data Features", \
            fontsize = 16, y = 1.03)

    fig.tight_layout()

def biplot(good_data, reduced_data, labels, pca):
    '''
    Produce a biplot that shows a scatterplot of the reduced
    data and the projections of the original features.
    
    good_data: original data, before transformation.
               Needs to be a pandas dataframe with valid column names
    reduced_data: the reduced data (the first two dimensions are plotted)
    pca: pca object that contains the components_ attribute

    return: a matplotlib AxesSubplot object (for any additional customization)
    
    This procedure is inspired by the script:
    https://github.com/teddyroland/python-biplot
    '''

    fig, ax = plt.subplots(figsize = (14,8))
    colors = ['red','yellow','blue']
    # scatterplot of the reduced data    
    ax.scatter(x=reduced_data.loc[:, 'Dimension 1'], y=reduced_data.loc[:, 'Dimension 2'],
	c=labels.loc[:], edgecolors='none', s=70, alpha=0.5, cmap=matplotlib.colors.ListedColormap(colors))
    
    feature_vectors = pca.components_.T
    
    # we use scaling factors to make the arrows easier to see
    arrow_size, text_pos = 7.0, 8.0

    # projections of the original features
    for i, v in enumerate(feature_vectors):
        ax.arrow(0, 0, arrow_size*v[0], arrow_size*v[1], 
                  head_width=0.2, head_length=0.2, linewidth=2, color='red')
        ax.text(v[0]*text_pos, v[1]*text_pos, good_data.columns[i], color='black', 
                 ha='center', va='center', fontsize=18)
    
    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Focused',
                          markerfacecolor='r', markersize=8),
		       Line2D([0], [0], marker='o', color='w', label='De-Focused',
                          markerfacecolor='y', markersize=8),
		       Line2D([0], [0], marker='o', color='w', label='Drowsy',
                          markerfacecolor='b', markersize=8)]
    ax.legend(handles=legend_elements, loc='upper left')
    ax.set_xlabel("Dimension 1", fontsize=14)
    ax.set_ylabel("Dimension 2", fontsize=14)
    ax.set_title("PC plane with original feature projections.", fontsize=16);
    return ax

def triplot(reduced_data, labels, pca):

    #fig, ax = plt.subplots(figsize = (14,8))
    fig = plt.figure(figsize = (14,8))
    ax = fig.add_subplot(111, projection='3d')
    colors = ['red','yellow','blue']
    # scatterplot of the reduced data    
    ax.scatter(xs=reduced_data.loc[:, 'Dimension 1'], ys=reduced_data.loc[:, 'Dimension 2'], zs=reduced_data.loc[:, 'Dimension 3'],
	c=labels.loc[:], edgecolors=None, s=70, alpha=1, cmap=matplotlib.colors.ListedColormap(colors))
    
    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Focused',
                          markerfacecolor='r', markersize=8),
		       Line2D([0], [0], marker='o', color='w', label='De-Focused',
                          markerfacecolor='y', markersize=8),
		       Line2D([0], [0], marker='o', color='w', label='Drowsy',
                          markerfacecolor='b', markersize=8)]
    ax.legend(handles=legend_elements, loc='upper left')
    ax.set_xlabel("Dimension 1", fontsize=14)
    ax.set_ylabel("Dimension 2", fontsize=14)
    ax.set_zlabel("Dimension 3", fontsize=14)
    ax.set_title("PC three dimensional view.", fontsize=16);
    return ax
