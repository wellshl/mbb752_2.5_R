# Project DEGI.r

Author: Calvin Rhodes

The tool that identifies differential expressed genes from a GCT file of gene expressions is called DEGI. DEGI stands for **D**ifferentially **E**xpressed **G**ene **I**dentifier.

## General
DEGI.r will take gene expression data and class label data and identify genes that are differentially expressed across classes.

DEGI.r will do this by calculating a 2 sample t test statistic across classes, then running a resampling procedure to calculate the appropriate p-value. The p-values are then corrected using the BH procedure to control the false discovery rate (FDR) in multiple hypothesis testing.

DEGI.r requires 2 inputs: a gct file (gene expression data) and a cls file (class label data, with 0's defining one class and 1's defining the other class). The code will run after loading the function from the DEGI.r file. Be warned! The code is very slow - this is what happens when you have a resampling procedure that requires a t-test for every resampling.

DEGI.r will return a list of differentially expressed genes among the two classes (\alpha = 0.05).

## Input Options for DEGI:

* gctfile - the name of the gene expression data file (Ex: "all_aml_train.gct")
* clsfile - the name of the class label data file (Ex: "all_aml_train.cls")

## Input Example

All code is based off of the Broad Institute's Comparative Marker Selection:
http://www.broadinstitute.org/cancer/software/genepattern/modules/docs/ComparativeMarkerSelection/10. Our gctfile and clsfile are derived from the training examples used in Comparative Marker Selection; the two class labels are ALL (acute lymphocytic leukemia) and AML (acute myelogenous leukemia).

```{r}
DEGI("all_aml_train.gct", "all_aml_train.cls")
```

