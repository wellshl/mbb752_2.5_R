# Project DEGC.r

Author: Calvin Rhodes

The tool that calculates the level of gene expression given pre-defined data sets is called GEED. GEED stands for **G**ene **E**xpression **E**nrichment calculator given pre-defined **D**ata sets.

http://www.broadinstitute.org/cancer/software/genepattern/modules/docs/ComparativeMarkerSelection/10

## General
GEED.r will take gene expression data, class label data, and a pre-defined geneset to calculate a gene set enrichment analysis value.

GEED.r requires 3 inputs: a gct file (gene expression data), a cls file (class label data, with 0's defining one class and 1's defining the other class), and a txt file (list of genes in geneset). The code will run after loading the function from the GEED.r file.

## Input Options for GEED:

* gctfile - the name of the gene expression data file (Ex: "all_aml_train.gct")
* clsfile - the name of the class label data file (Ex: "all_aml_train.cls")
* geneset - the name of the text file with a list of genes in our pre-defined geneset (Ex: "geneset.txt")

## Input Example

All code is based on the following paper: http://www.pnas.org/content/102/43/15545.full.pdf. Our gctfile and clsfile are also derived from the paper; the two class labels are ALL (acute lymphocytic leukemia) and AML (acute myelogenous leukemia). We incorporated an arbitrarily constructed pre-defined geneset (geneset.txt), which features 12 genes that overlap with the data from the gct file.

```{r}
GEED("all_aml_train.gct", "all_aml_train.cls", "geneset.txt")
```

