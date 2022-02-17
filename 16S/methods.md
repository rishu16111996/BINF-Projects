Methods- 16s Sequencing Analysis using QIIME2

QIIME2 \[1\] is an extensible and decentralised microbiome analysis
package. It offers a variety of plugins for microbiome analysis. It
provides a platform to start DNA sequence analysis from scratch and
finish with publication grade statistics and other significant results.
QIIME produces data in the form of artifacts. An artifact produced as a
result of any analysis carried out by QIIME is stored as a .qza file.
QIIME follows the following steps during analysis-

1.  Importing sequences into an activated QIIME environment.

2.  Demultiplexing data by scanning and attaching relevant barcodes back
    to the sequences.

3.  Removal of parts not needed for analysis of sequences (for example
    primers)

4.  QC or Quality Control which involves-
    1.  Denoising using DADA2 or deblur and/or
    2.  Quality filtering, trimming and clustering with VSEARCH or dbOTU
5.  Taxonomy assignment

6.  Data analysis and further insights.

The tutorials include multiple samples being analysed for insights.

1.  QIIME 2 to perform an analysis of human microbiome samples from two
    individuals at four body sites at five timepoints, the first of
    which immediately followed antibiotic usage. This study \[2\] is
    analysed, the sequencer used is Illumina HiSeq using the Earth
    Microbiome Project \[3\] hypervariable region 4 (V4) 16S rRNA
    sequencing protocol. A TSV file containing metadata is obtained
    using the wget or curl command. This file is then used throughout
    the analysis. The sequence and barcode are downloaded after the
    metadata using either curl or wget command. The next process is to
    import sequences into QIIME which is done using the import function.
    A .qza output is obtained as a result. The next step involves
    demultiplexing the sequences (the qza file in this case) which are
    single end reads. qiime demux emp single function is used which
    demultiplexes single ended reads. A summary file is then generated
    and is a qzv file which can be visualised in the browser or using
    command line interface. The next step involves quality control, and
    there are two options or tools available for this. One is DADA2 and
    the other one is deblur. DADA2 will detect and get rid of amplicon
    sequences if any. DADA2 is used in this case and the results are
    then formulated which is a qzv file ready for visualisation.
    Further, all this data can be summarised using feature table
    summarise and feature table tablulate. The next step involves
    phylogenetic analysis which will mark the differences and
    similarities between the sequences and individual sequences itself.
    A phylogenetic tree is generated using MAFFT algorithm for multiple
    sequence alignment. Alpha and beta diversity analysis is then
    carried out using q2-diversity tool in QIIME. Emperor tool is used
    to generate and explore the principal coordinate plots. Alpha
    diversity can be further explored using alpha rarefaction lotting.
    Machine learning methods are then used for taxonomic analysis,
    particularly using a pre-trained Naive Bayes classifier
    (q2-feature-classifier plugin). The next step involves ANCOM which
    can be applied to identify features that are differentially abundant
    (i.e. present in different abundances) across sample groups.

2.  Fecal Microbiota Transplant (FMT) Study This data \[4\] is involves
    a study where children under the age of 18 with autism and
    gastrointestinal disorders, as measured by the Autism Diagnostic
    Interview-Revised (ADI-R) and Gastrointestinal Symptom Rating Scale
    (GSRS), respectively, were treated with fecal microbiota transplant
    in attempt to reduce the severity of their behavioral and
    gastrointestinal symptoms. Changes are then tracked in their
    microbiome, several metrics of the severity of autism including the
    Parent Global Impressions-III (PGI-III) and the Childhood Autism
    Rating Scale (CARS), and the severity of their gastrointestinal
    symptoms through their GSRS score over an eighteen week period. The
    microbiome was tracked through collection of weekly fecal swab
    samples (collected by swabbing used toilet paper) and less frequent
    stool samples (collected as whole stool). In the full study, which
    was a phase 1 clinical trial designed to test safety of the
    treatment, eighteen individuals received the treatment, and twenty
    individuals were followed as controls. The controls did not receive
    the treatment, but were monitored to track normal temporal variation
    in the gut microbiome. The fecal material that was transplanted
    during treatment was also sequenced in this study. This dataset
    includes data from five individuals who received treatment and five
    controls. Between six and sixteen samples are included per
    individual, including stool and fecal swab samples for each
    individual, and samples before and after FMT treatment. Five samples
    of the transplanted fecal material are also included. Data was
    sequenced on two Illumina MiSeq sequencing runs. In this exercise,
    QC or quality control is performed first using DADA2 to generate
    Feature Table and Feature Data. Either 10% subsample or 1% subsample
    is chosen for analysis. The demux command for demultiplexing is run
    individually on sequences individually using same values for
    truncating length and trimming the sequences individually. The
    summary is obtained using the demux summarize function and the
    demultiplexing using DADA2 is then run. Since demultiplexing is run
    individually on both sequences, these sequences then have to be
    merged. This denoised data is then merged using feature-table merge
    and feature table-merge seqs which will merge the sequences into
    one. The statistics for this particular run is then obtained using
    feature-table summarise. Diversity analysis is then carried out on
    this sample. Alpha and beta diversity can be plotted, taxonomic and
    phylogenetic analysis can then be done. ANCOM can give further
    insights into the data.

3.  Analysis on Soil Samples from Atacama Desert in Northern Chile The
    main motive of this tutorial was to process and understand steps of
    paired-end read analysis, up to the point where the analysis steps
    are identical to single-end read analysis which includes importing,
    demultiplexing and denoising. The Atacama Desert is one of the most
    arid locations on Earth, with some areas receiving less than a
    millimeter of rain per decade. Despite this extreme aridity, there
    are microbes living in the soil. The soil microbiomes profiled in
    this study follow two east-west transects, Baquedano and Yungay,
    across which average soil relative humidity is positively correlated
    with elevation (higher elevations are less arid and thus have higher
    average soil relative humidity). Along these transects, pits were
    dug at each site and soil samples were collected from three depths
    in each pit \[5\]. A similar protocol is follwed wherein the TSV
    file is downloaded, and either 1 or 10% subsample containing the
    barcode and paired end sequences are retrieved using wget or curl.
    In this data set, the barcode reads are the reverse complement of
    those included in the sample metadata file, so we additionally
    include the –p-rev-comp-mapping-barcodes parameter. After
    demultiplexing, we can generate and view a summary of how many
    sequences were obtained per sample. After demultiplexing reads, we
    looked at the sequence quality based on ten-thousand randomly
    selected reads, and then denoise the data. In this example we have
    150-base forward and reverse reads. Since we need the reads to be
    long enough to overlap when joining paired ends, the first thirteen
    bases of the forward and reverse reads are being trimmed, but no
    trimming is being applied to the ends of the sequences to avoid
    reducing the read length by too much. In this example, the same
    values are being provided for –p-trim-left-f and –p-trim-left-r and
    for –p-trunc-len-f and –p-trunc-len-r, but that is not a
    requirement. This data is then summarised and put in a feature
    table. Further, alpha beta diversity analysis, taxonomic and
    phylogenetic analysis can also be carried out.

References-

1.  Bolyen E, Rideout JR, Dillon MR, Bokulich NA, Abnet CC, Al-Ghalith
    GA, Alexander H, Alm EJ, Arumugam M, Asnicar F, Bai Y, Bisanz JE,
    Bittinger K, Brejnrod A, Brislawn CJ, Brown CT, Callahan BJ,
    Caraballo-Rodríguez AM, Chase J, Cope EK, Da Silva R, Diener C,
    Dorrestein PC, Douglas GM, Durall DM, Duvallet C, Edwardson CF,
    Ernst M, Estaki M, Fouquier J, Gauglitz JM, Gibbons SM, Gibson DL,
    Gonzalez A, Gorlick K, Guo J, Hillmann B, Holmes S, Holste H,
    Huttenhower C, Huttley GA, Janssen S, Jarmusch AK, Jiang L, Kaehler
    BD, Kang KB, Keefe CR, Keim P, Kelley ST, Knights D, Koester I,
    Kosciolek T, Kreps J, Langille MGI, Lee J, Ley R, Liu YX, Loftfield
    E, Lozupone C, Maher M, Marotz C, Martin BD, McDonald D, McIver LJ,
    Melnik AV, Metcalf JL, Morgan SC, Morton JT, Naimey AT, Navas-Molina
    JA, Nothias LF, Orchanian SB, Pearson T, Peoples SL, Petras D,
    Preuss ML, Pruesse E, Rasmussen LB, Rivers A, Robeson MS, Rosenthal
    P, Segata N, Shaffer M, Shiffer A, Sinha R, Song SJ, Spear JR,
    Swafford AD, Thompson LR, Torres PJ, Trinh P, Tripathi A, Turnbaugh
    PJ, Ul-Hasan S, van der Hooft JJJ, Vargas F, Vázquez-Baeza Y,
    Vogtmann E, von Hippel M, Walters W, Wan Y, Wang M, Warren J, Weber
    KC, Williamson CHD, Willis AD, Xu ZZ, Zaneveld JR, Zhang Y, Zhu Q,
    Knight R, and Caporaso JG. 2019. Reproducible, interactive, scalable
    and extensible microbiome data science using QIIME 2. Nature
    Biotechnology 37: 852–857.
    <a href="https://doi.org/10.1038/s41587-019-0209-9" class="uri">https://doi.org/10.1038/s41587-019-0209-9</a>

2.  Caporaso JG, Lauber CL, Costello EK, Berg-Lyons D, Gonzalez A,
    Stombaugh J, Knights D, Gajer P, Ravel J, Fierer N, Gordon JI,
    Knight R. Moving pictures of the human microbiome. Genome Biol.
    2011;12(5):R50. doi: 10.1186/gb-2011-12-5-r50. PMID: 21624126;
    PMCID: PMC3271711.

3.  Sample processing, sequencing, and core amplicon data analysis were
    performed by the Earth Microbiome Project (www.earthmicrobiome.org),
    and all amplicon sequence data and metadata have been made public
    through the EMP data portal (qiita.microbio.me/emp).

4.  Kang, D., Adams, J.B., Gregory, A.C. et al. Microbiota Transfer
    Therapy alters gut ecosystem and improves gastrointestinal and
    autism symptoms: an open-label study. Microbiome 5, 10 (2017).
    <a href="https://doi.org/10.1186/s40168-016-0225-7" class="uri">https://doi.org/10.1186/s40168-016-0225-7</a>

5.  Significant Impacts of Increasing Aridity on the Arid Soil
    Microbiome. Julia W. Neilson, Katy Califf, Cesar Cardona, Audrey
    Copeland, Will van Treuren, Karen L. Josephson, Rob Knight, Jack A.
    Gilbert, Jay Quade, J. Gregory Caporaso, and Raina M. Maier.
    mSystems May 2017, 2 (3) e00195-16; DOI: 10.1128/mSystems.00195-16.
