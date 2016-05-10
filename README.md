# Title: DEGI.py  
Purpose: A tool that identifies differentially expressed genes from a GCT file  
Created Date: 08 May 2016  
Created By: Heather Wells  

## Notes:  
 * Requires gene expression input file in GCT format as well as class label file in CLS format.  
 * Optionally accepts user-specified number of permutations for permutation test. If none is specified, the default is 200.  
 * Returns a list of differentially expressed gene names as well as adjusted p-values. 

## General  
DEGI.py uses a permutation test to determine differential expression of genes between two phenotype classes. The difference in mean expression between the two classes is calculated first. Then, the class labels are randomly permutated a large number of times and the difference in mean expression between the two random classes is calculated for each permutation. A p-value is calculated by determining the proportion of random permutations in which the original true difference in means is larger than the permutatated difference in means. This process is repeated for each gene. P-values are adjusted for multiple hypothesis testing using the Benjamini Hochberg method. If the adjusted p-value is less than the significance level of 0.05, the name of the gene is returned along with the adjusted p-value.

All code is based off of the Broad Institute's Comparative Marker Selection:
http://www.broadinstitute.org/cancer/software/genepattern/modules/docs/ComparativeMarkerSelection/10. Our gctfile and clsfile are derived from the training examples used in Comparative Marker Selection; the two class labels are ALL (acute lymphocytic leukemia) and AML (acute myelogenous leukemia).  

An R tool that accomplishes the same task can be found [here](https://github.com/calvinrhodes/mbb752_2.5_R)

## Usage:  
```
python DEGI.py -g <gene expression gct file> -c <class label file> -n <number of permutations>
```
## Example:  
```
python DEGI.py -g all_aml_train.gct -c all_aml_train.cls -n 1000
```


