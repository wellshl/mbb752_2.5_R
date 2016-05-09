### Title: DEGI.py
### Version: 1.0
### Purpose: A tool that identifies differentially expressed genes from a GCT file
### Created Date: 08 May 2016
### Created By: Heather Wells

### Usage: python DEGI.py -g <gene expression gct file> -c <class label file>
### Example: python DEGI.py -g all_aml_train.gct -c all_aml_train.cls

### Notes: Requires input file in GCT format as well as class label file in CLS format.

import numpy
from scipy import stats
import statsmodels.stats.multitest as smm

#import arguments
import argparse
parser=argparse.ArgumentParser(description='DEGI')
parser.add_argument('-g', '--gctfile', help='gene expression gct file', required=True)
parser.add_argument('-c', '--clsfile', help='class label cls file', required=True)
parser.add_argument('-n', '--number', help='number of permutations', default=200, type=int)
args=parser.parse_args()

def DEGI(gctfile,clsfile,number):

    #open and save input files
    with open(gctfile) as gct:
        gct=numpy.genfromtxt(gct,dtype=None,delimiter="\t",missing_values="NA",invalid_raise=False,skip_header=2)
        gct_exp=gct[1:,2:].astype(float) #matrix of expression values
        gct_genes=gct[1:,1] #list of gene names
    with open(clsfile) as label:
        label=label.read().splitlines()
        label=label[2].split() #list of class labels

    #initialize empty list for p-values
    pvals=[]

    #first, caluclate difference in means with original labels
    for i in range(0,len(gct_genes)):
        class0=[]
        class1=[]
        for j in range(0,len(label)):
            if label[j]=="0":
                class0.append(gct_exp[i,j])
            if label[j]=="1":
                class1.append(gct_exp[i,j])
        mean0=sum(class0)/len(class0)
        mean1=sum(class1)/len(class1)
        null_diff=abs(mean0-mean1)

        #then, calculate difference in means with permutated labels
        #p-value is determined by the proportion of permutated differences that are less than the original difference
        greater=0.
        for k in range(0,number):
            label_shuffle=numpy.random.permutation(label)
            class0_shuffle=[]
            class1_shuffle=[]
            for j in range(0,len(label_shuffle)):
                if label_shuffle[j]=="0":
                    class0_shuffle.append(gct_exp[i,j])
                if label_shuffle[j]=="1":
                    class1_shuffle.append(gct_exp[i,j])
            mean0_shuffle=sum(class0_shuffle)/len(class0_shuffle)
            mean1_shuffle=sum(class1_shuffle)/len(class1_shuffle)
            alt_diff=abs(mean0_shuffle-mean1_shuffle)
            if null_diff>=alt_diff:
                greater+=1.
        pvals.append(greater/number)

    #correct for multiple hypothesis tests using benjamini-hochberg
    bh=smm.multipletests(pvals,alpha=0.05,method='fdr_bh')
    bh_sig=bh[0]
    bh_pvals=bh[1].astype(str)

    sig=0
    for i in range(0,len(bh_sig)):
        if bh_sig[i]==True:
            print gct_genes[i]+" is differentially expressed.\nThe adjusted p-value is "+bh_pvals[i]+"\n"
            sig+=1
    if sig==0:
        print "There are no differentially expressed genes."
            


            
DEGI(args.gctfile,args.clsfile,args.number)
    
