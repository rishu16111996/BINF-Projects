## Title :

### Methods used in module Described

## Methods :

Differential Expression is mainly used for gene level inference, and the
results can be further deployed for other analyses. Differential
Expression involves two main steps-

1.  estimating the relative abundance of transcript, and to apply
    statistical models to test for differential expression between
    treatment groups. In this particular module, the same steps were
    followed by using tools like Salmon and then R packages like DESeq2.

2.  Initially, Salmon is used to quantify the transcripts in a given
    file of your RNASeq experiment. It runs in 2 phases- Indexing and
    Quantification. Indexing phase involves creating a mapping based
    index on the auxiliary Kmer hash over of length 31. After this step,
    quantification is done and –validate mappings flag is used to enable
    selective alignment.

3.  These transcripts are then put in the form of a table. A R script
    called mergeKo.r is written and Kable is used to put it in a
    presentable form. Hereafter, the first filtering is done using
    Swissprot coverage. Then KEGG IDs are matched to these Swissprot
    IDs, and then BLAST results are merged to this KEGG-Swissprot table.
    This is done so that analysis using tximport and then DESeq2 can be
    carried out.

4.  Scripts are written to further import the data into DESeq2 and carry
    out analysis. DESeq2 helps carry out RNASeq analysis by using
    shrinkage estimation, for dispersions and fold changes to improve
    stability and interpretability of estimates. This enables a more
    quantitative analysis focused on the strength rather than the mere
    presence of differential expression.The two conditions used in this
    analysis was Menthol vs Vibrio in Aitapsia. Here on, the filtering
    is done using padj or p-adjacent value less than 0.05. This gives us
    a list of both upregulated and down regulated genes in 2 different
    scenarios (with KEGG Orthology IDs, pathway and Swissprot
    references).

5.  We used get\_path.py script to get pathway from KO ID for each gene
    and then downloaded the kegg pathway file using wget command in
    linux and the merged KO Id with pathway and paths then filtered out
    padj to 0.5.

### Refrence :

Love, Michael I., Wolfgang Huber, and Simon Anders. 2014. “Moderated
Estimation of Fold Change and Dispersion for RNA-Seq Data with DESeq2.”
*Genome Biol* 15 (12): 550–50..

Patro, Rob, Geet Duggal, Michael I. Love, Rafael A. Irizarry, and Carl
Kingsford. 2017. “Salmon Provides Fast and Bias-Aware Quantification of
Transcript Expression.” *Nat Methods* 14 (4): 417–19..

Soneson, Charlotte, Michael I. Love, and Mark D. Robinson. 2016.
“Differential Analyses for RNA-Seq: Transcript-Level Estimates Improve
Gene-Level Inferences.” *F1000Res* 4 (February):
1521–1..

## Results :

| ko        | pathway      | path                      |         log |      padj | factor                        |
| :-------- | :----------- | :------------------------ | ----------: | --------: | :---------------------------- |
| ko:K00333 | path:ko01100 | Metabolic pathways        | \-0.9083072 | 0.4837903 | Menthol\_Menthol\_vs\_Control |
| ko:K00333 | path:ko00190 | Oxidative phosphorylation | \-0.9083072 | 0.4837903 | Menthol\_Menthol\_vs\_Control |
| ko:K00333 | path:ko00190 | Oxidative phosphorylation | \-0.9083072 | 0.4837903 | Menthol\_Menthol\_vs\_Control |
| ko:K00333 | path:ko01100 | Metabolic pathways        | \-0.9083072 | 0.4837903 | Menthol\_Menthol\_vs\_Control |
| ko:K00522 | path:ko04978 | Mineral absorption        | \-0.7372129 | 0.3514596 | Menthol\_Menthol\_vs\_Control |
| ko:K00522 | path:ko04217 | Necroptosis               | \-0.7372129 | 0.3514596 | Menthol\_Menthol\_vs\_Control |
