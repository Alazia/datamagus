import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_setting(title=None,x_text='',y_text='',
                 fig1=5,fig2=5,labelsize=10):
    plt.figure(figsize=(fig1, fig2))
    ax = plt.subplot(111)
    ax.tick_params(labelsize=labelsize)
    ax.set_ylabel(y_text, fontweight='bold', fontsize=labelsize)
    ax.set_xlabel(x_text, fontweight='bold', fontsize=labelsize)
    if title is not None:
        ax.set_title(title, fontweight='bold', fontsize=labelsize)

def plot_savefig(title='output',type='pdf'):
    plt.savefig(title+'.'+type,bbox_inches='tight',dpi=400)


def plot_density(df:pd.DataFrame):
    sns.kdeplot(df.unstack())