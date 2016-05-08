DEGI <- function (gctfile, clsfile) {
  
  GCT <- read.table(gctfile, sep = "\t", stringsAsFactors = FALSE, skip = 2, header = TRUE)
  GCT <- GCT[-dim(GCT)[1],] #last row is NAs --> gets rid of that row
  Names <- GCT$Name
  GCT <- GCT[,-c(1,2)] #cleaning
  
  CLS <- read.table(clsfile, skip = 2) #assumes class vector is in third row
  
  pVals <- data.frame()
  for (i in (1:dim(GCT)[1])) {
    t <- t.test(GCT[i,CLS==0],GCT[i,CLS==1]) #runs t test across phenotypes to generate our statistic
    ourstat <- diff(t$estimate)
    stats <- rep(NA, 200)
    for (k in 1:length(stats)) { #runs 200 resampling permutation test across our statistic
      simCLS <- sample(CLS) 
      tsim <- t.test(GCT[i,simCLS==0],GCT[i,simCLS==1])
      diff(tsim$estimate)
      stats[k] <- diff(tsim$estimate)
    }
    pV <- ( sum(abs(stats) >= abs(ourstat)) / length(stats) )
    pVals <- rbind (pVals, pV)
  }
  pVals$Name <- Names
  names(pVals)[2] <- "pV"
  
  #Correct the pVals: BH for MHT
  pVals$pV.adjust <- p.adjust(pVals$pV, method = "BH")
  sig.genes <- pVals$Name[pVals$pV.adjust <= 0.05]
  return (sig.genes)
}

DEGI ("all_aml_train.gct", "all_aml_train.cls")
