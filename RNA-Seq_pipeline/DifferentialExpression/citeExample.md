## Overview

The two main steps in performing differential expression analysis are to
estimate the relative abundance of transcripts, and to apply statistical
models to test for differential expression between treatment groups.
Estimating relative abundance is basically determining how many NGS
reads match a given gene within a genome. In this module you’ll use
Salmon (Minniti et al. 2019) to estimate relative abundance, tximport
(Soneson, Love, and Robinson 2015) to import the Salmon abundance
estimates, and DESeq2 (Love, Huber, and Anders 2014) to perform
statistical tests to identify differentially expressed genes.

## References

<div id="refs" class="references">

<div id="ref-Love">

Love, Michael I., Wolfgang Huber, and Simon Anders. 2014. “Moderated
Estimation of Fold Change and Dispersion for RNA-Seq Data with DESeq2.”
*Genome Biology* 15 (12): 550–50.
<https://doi.org/10.1186/s13059-014-0550-8>.

</div>

<div id="ref-Patro">

Minniti, Giusi, Simen Rød Sandve, János Tamás Padra, Live Heldal Hagen,
Sara Lindén, Phillip B. Pope, Magnus Ø Arntzen, and Gustav
Vaaje-Kolstad. 2019. “The Farmed Atlantic Salmon (Salmo Salar)
Skin-Mucus Proteome and Its Nutrient Potential for the Resident
Bacterial Community.” *Genes* 10 (7): 515.
<https://doi.org/10.3390/genes10070515>.

</div>

<div id="ref-Soneson">

Soneson, Charlotte, Michael I. Love, and Mark D. Robinson. 2015.
“Differential Analyses for RNA-Seq: Transcript-Level Estimates Improve
Gene-Level Inferences.” *F1000Research* 4 (December): 1521–1.
<https://www.ncbi.nlm.nih.gov/pubmed/26925227>.

</div>

</div>
