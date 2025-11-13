``` r
#!/usr/bin/env Rscript
# de.R
library(tximport)
library(readr)
library(DESeq2)
```

    ## Loading required package: S4Vectors

    ## Loading required package: stats4

    ## Loading required package: BiocGenerics

    ## Loading required package: parallel

    ## 
    ## Attaching package: 'BiocGenerics'

    ## The following objects are masked from 'package:parallel':
    ## 
    ##     clusterApply, clusterApplyLB, clusterCall, clusterEvalQ,
    ##     clusterExport, clusterMap, parApply, parCapply, parLapply,
    ##     parLapplyLB, parRapply, parSapply, parSapplyLB

    ## The following objects are masked from 'package:stats':
    ## 
    ##     IQR, mad, sd, var, xtabs

    ## The following objects are masked from 'package:base':
    ## 
    ##     anyDuplicated, append, as.data.frame, basename, cbind,
    ##     colMeans, colnames, colSums, dirname, do.call, duplicated,
    ##     eval, evalq, Filter, Find, get, grep, grepl, intersect,
    ##     is.unsorted, lapply, lengths, Map, mapply, match, mget, order,
    ##     paste, pmax, pmax.int, pmin, pmin.int, Position, rank, rbind,
    ##     Reduce, rowMeans, rownames, rowSums, sapply, setdiff, sort,
    ##     table, tapply, union, unique, unsplit, which, which.max,
    ##     which.min

    ## 
    ## Attaching package: 'S4Vectors'

    ## The following object is masked from 'package:base':
    ## 
    ##     expand.grid

    ## Loading required package: IRanges

    ## Loading required package: GenomicRanges

    ## Loading required package: GenomeInfoDb

    ## Loading required package: SummarizedExperiment

    ## Loading required package: Biobase

    ## Welcome to Bioconductor
    ## 
    ##     Vignettes contain introductory material; view with
    ##     'browseVignettes()'. To cite Bioconductor, see
    ##     'citation("Biobase")', and for packages 'citation("pkgname")'.

    ## Loading required package: DelayedArray

    ## Loading required package: matrixStats

    ## 
    ## Attaching package: 'matrixStats'

    ## The following objects are masked from 'package:Biobase':
    ## 
    ##     anyMissing, rowMedians

    ## Loading required package: BiocParallel

    ## 
    ## Attaching package: 'DelayedArray'

    ## The following objects are masked from 'package:matrixStats':
    ## 
    ##     colMaxs, colMins, colRanges, rowMaxs, rowMins, rowRanges

    ## The following objects are masked from 'package:base':
    ## 
    ##     aperm, apply

    ## Registered S3 methods overwritten by 'ggplot2':
    ##   method         from 
    ##   [.quosures     rlang
    ##   c.quosures     rlang
    ##   print.quosures rlang

``` r
tx2gene <- read.csv("tx2gene.csv")
head(tx2gene)
```

    ##                     trans        ko
    ## 1 TRINITY_DN9495_c0_g1_i2 ko:K00134
    ## 2 TRINITY_DN9573_c0_g1_i1 ko:K01689
    ## 3 TRINITY_DN9485_c0_g1_i1 ko:K02111
    ## 4 TRINITY_DN8020_c0_g1_i1 ko:K04043
    ## 5 TRINITY_DN9453_c0_g1_i1 ko:K02932
    ## 6 TRINITY_DN8136_c0_g1_i1 ko:K02932

``` r
#colnames(tx2gene) <- c("trans", "ko")

samples <- read.csv("Samples.csv", header=TRUE)
head(samples)
```

    ##   Sample Menthol  Vibrio
    ## 1  Aip17 Menthol  Vibrio
    ## 2  Aip20 Control  Vibrio
    ## 3  Aip24 Menthol Control
    ## 4  Aip28 Control Control
    ## 5  Aip14 Menthol  Vibrio
    ## 6  Aip26 Control  Vibrio

``` r
files <- file.path("quant", samples$Sample, "quant.sf")
txi <- tximport(files, type="salmon", tx2gene=tx2gene)
```

    ## reading in files with read_tsv

    ## 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 
    ## removing duplicated transcript rows from tx2gene
    ## transcripts missing from tx2gene: 34247
    ## summarizing abundance
    ## summarizing counts
    ## summarizing length

``` r
dds <- DESeqDataSetFromTximport(txi, colData = samples,                                                                 design = ~ Menthol + Vibrio)
```

    ## using counts and average transcript lengths from tximport

``` r
dds$Vibrio <- relevel(dds$Vibrio, ref = "Control")
dds$Menthol <- relevel(dds$Menthol, ref = "Control")
keep <- rowSums(counts(dds)) >= 10
dds <- dds[keep,]
dds <- DESeq(dds)
```

    ## estimating size factors
    ## using 'avgTxLength' from assays(dds), correcting for library size
    ## estimating dispersions
    ## gene-wise dispersion estimates
    ## mean-dispersion relationship
    ## final dispersion estimates
    ## fitting model and testing

``` r
padj <- .05
minLog2FoldChange <- .5
dfAll <- data.frame()
# Get all DE results except Intercept, and "flatten" into a single file.
for (result in resultsNames(dds)){
    if(result != 'Intercept'){
        res <- results(dds, alpha=.05, name=result)
        dfRes <- as.data.frame(res)
        dfRes <- subset(subset(dfRes, select=c(log2FoldChange, padj)))
        dfRes$Factor <- result
        dfAll <- rbind(dfAll, dfRes)
    }
}
head(dfAll)
```

    ##           log2FoldChange      padj                     Factor
    ## ko:K00024     -0.8912784 0.9448046 Menthol_Menthol_vs_Control
    ## ko:K00031     -0.6698167 0.9448046 Menthol_Menthol_vs_Control
    ## ko:K00128     -0.2299611 0.9448046 Menthol_Menthol_vs_Control
    ## ko:K00134      1.5180968 0.7034107 Menthol_Menthol_vs_Control
    ## ko:K00140      0.1496665 0.9448046 Menthol_Menthol_vs_Control
    ## ko:K00207      0.3403610 0.9448046 Menthol_Menthol_vs_Control

``` r
# writing in csv file
write.csv(dfAll, file="dfAll.csv")

# getting path from path.txt
path1 <- read.table("path.txt", sep="\t", header=FALSE)
colnames(path1) <- c("ko", "pathway")

# getting ko from kegg orthology
getPath = read.table("ko", sep="\t", header=FALSE)
colnames(getPath) = c("pathway", "path")

# getting data from dfALL.csv
mergeko = read.csv("dfAll.csv") 
colnames(mergeko) = c("ko", "log", "padj", "factor")

# merging with column names
finalMerge1 <- merge(path1, getPath)
finalMerge <- merge(finalMerge1, mergeko)

# writing into table and file
write.table(finalMerge, file="deAnnotated.csv")

# printing output
head(finalMerge)
```

    ##          ko      pathway                                         path
    ## 1 ko:K00024 path:ko01130                  Biosynthesis of antibiotics
    ## 2 ko:K00024 path:ko01130                  Biosynthesis of antibiotics
    ## 3 ko:K00024 path:ko01120 Microbial metabolism in diverse environments
    ## 4 ko:K00024 path:ko00710  Carbon fixation in photosynthetic organisms
    ## 5 ko:K00024 path:ko00270           Cysteine and methionine metabolism
    ## 6 ko:K00024 path:ko00630      Glyoxylate and dicarboxylate metabolism
    ##          log      padj                     factor
    ## 1 -0.8912784 0.9448046 Menthol_Menthol_vs_Control
    ## 2 -0.8912784 0.9448046 Menthol_Menthol_vs_Control
    ## 3 -0.8912784 0.9448046 Menthol_Menthol_vs_Control
    ## 4 -0.8912784 0.9448046 Menthol_Menthol_vs_Control
    ## 5 -0.8912784 0.9448046 Menthol_Menthol_vs_Control
    ## 6 -0.8912784 0.9448046 Menthol_Menthol_vs_Control

``` r
# getting data from file
new_data <- read.csv("deAnnotated.csv", header=TRUE, sep=" ")

# creating filter
store <- which(new_data[5]<0.5)

# filtering values
new_data <- new_data[store,]

# writing into final csv file
write.table(new_data, file="deAnnotated.csv", col.names=TRUE, row.names=FALSE)
head(new_data)
```

    ##            ko      pathway                      path        log      padj
    ## 181 ko:K00333 path:ko01100        Metabolic pathways -0.9083072 0.4837903
    ## 182 ko:K00333 path:ko00190 Oxidative phosphorylation -0.9083072 0.4837903
    ## 183 ko:K00333 path:ko00190 Oxidative phosphorylation -0.9083072 0.4837903
    ## 184 ko:K00333 path:ko01100        Metabolic pathways -0.9083072 0.4837903
    ## 251 ko:K00522 path:ko04978        Mineral absorption -0.7372129 0.3514596
    ## 252 ko:K00522 path:ko04217               Necroptosis -0.7372129 0.3514596
    ##                         factor
    ## 181 Menthol_Menthol_vs_Control
    ## 182 Menthol_Menthol_vs_Control
    ## 183 Menthol_Menthol_vs_Control
    ## 184 Menthol_Menthol_vs_Control
    ## 251 Menthol_Menthol_vs_Control
    ## 252 Menthol_Menthol_vs_Control
