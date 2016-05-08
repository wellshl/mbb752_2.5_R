# Project DEGI.r

Author: Calvin Rhodes

The tool that identifies differential expressed genes from a GCT file of gene expressions is called DEGC. DEGC stands for **D**ifferentially **E**xpressed **G**ene **I**dentifier.

## General
DEGI.r will take gene expression data and class label data, and a pre-defined geneset to calculate a gene set enrichment analysis value.

DEGI.r requires 2 inputs: a gct file (gene expression data) and a cls file (class label data, with 0's defining one class and 1's defining the other class). The code will run after loading the function from the DEGI.r file. Be warned! The code is very slow - this is what happens when you have a resampling procedure that requires a t-test for every resampling.

DEGI.r will output a list of p-values along with the name of the gene.

## Input Options for GEED:

* gctfile - the name of the gene expression data file (Ex: "all_aml_train.gct")
* clsfile - the name of the class label data file (Ex: "all_aml_train.cls")

## Input Example

All code is based off of the Broad Institute's Comparative Marker Selection:
http://www.broadinstitute.org/cancer/software/genepattern/modules/docs/ComparativeMarkerSelection/10. Our gctfile and clsfile are derived from the training examples used in Comparative Marker Selection; the two class labels are ALL (acute lymphocytic leukemia) and AML (acute myelogenous leukemia).

```{r}
DEGI("all_aml_train.gct", "all_aml_train.cls")
```

