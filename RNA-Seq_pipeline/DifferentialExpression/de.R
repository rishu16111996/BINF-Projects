#!/usr/bin/env Rscript
# de.R
library(tximport)
library(readr)
library(DESeq2)
tx2gene <- read.csv("tx2gene.csv")
head(tx2gene)

#colnames(tx2gene) <- c("trans", "ko")

samples <- read.csv("Samples.csv", header=TRUE)
head(samples)

files <- file.path("quant", samples$Sample, "quant.sf")
txi <- tximport(files, type="salmon", tx2gene=tx2gene)

dds <- DESeqDataSetFromTximport(txi, colData = samples,                                                                 design = ~ Menthol + Vibrio)

dds$Vibrio <- relevel(dds$Vibrio, ref = "Control")
dds$Menthol <- relevel(dds$Menthol, ref = "Control")
keep <- rowSums(counts(dds)) >= 10
dds <- dds[keep,]
dds <- DESeq(dds)

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

# getting data from file
new_data <- read.csv("deAnnotated.csv", header=TRUE, sep=" ")

# creating filter
store <- which(new_data[5]<0.5)

# filtering values
new_data <- new_data[store,]

# writing into final csv file
write.table(new_data, file="deAnnotated.csv", col.names=TRUE, row.names=FALSE)
head(new_data)
