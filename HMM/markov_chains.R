#!/usr/bin/env Rcsript
# markov_chains.R

#install.packages("plyr")
#install.packages("seqinr")
#install.packages("ggplot2")
#install.packages("gridExtra")

library(plyr)
library(seqinr)
library(ggplot2)
library(gridExtra)

plotData <- function(seq,
                     nucleotides,
                     title){

  freqNucleotide <- count(seq,1,alphabet=nucleotides,freq=TRUE)

  freqDiNucleotide <- count(seq,2,alphabet=nucleotides,freq=TRUE)
  
  freqTriNucleotide <- count(seq,3,alphabet=nucleotides,freq=TRUE)
  
  df <- as.data.frame(freqNucleotide)
  colnames(df) <- c("Base", "Base_Proportion")
  p1 <- ggplot(df, aes(x = Base, y = Base_Proportion, fill=Base )) +
    geom_bar(stat = "identity")
  p1 <- p1 + theme(legend.position="none") +
    ggtitle("Compositional bias of each nucleotide")
  
  df <- as.data.frame(freqDiNucleotide)
  colnames(df) <- c("Base", "Base_Proportion")
  p2 <- ggplot(df, aes(x = Base, y = Base_Proportion, fill=Base )) +
    geom_bar(stat = "identity")
  p2 <- p2 + theme(legend.position="none") +
    ggtitle("Compositional bias of each dinucleotide")
  
  df <- as.data.frame(freqTriNucleotide)
  colnames(df) <- c("Base", "Base_Proportion")
  p3 <- ggplot(df, aes(x = Base, y = Base_Proportion, fill=Base )) +
    geom_bar(stat = "identity")
  p3 <- p3 + theme(legend.position="none") +
    ggtitle("Compositional bias of each trinucleotide") +
    theme(axis.text.x  = element_text(angle=90, vjust=0.5, size=8) )
  
 
  grid.arrange(p1, p2, p3, nrow=3, top=title)
}


generateFirstOrderSeq <- function(lengthSeq,
                                  nucleotides,
                                  initialProb,
                                  firstOrderMatrix){

  outputSeq <- character()
  firstnucleotide <- sample(nucleotides, 1, rep=TRUE, prob=initialProb)
  
  outputSeq[1]    <- firstnucleotide
  
  for(i in 2:lengthSeq){
    prevNuc <- outputSeq[i-1]
    currentProb <- firstOrderMatrix[prevNuc,]
  
    outputSeq[i] <- sample(nucleotides,1,prob=currentProb)
  }
  return(outputSeq)
}

generateFirstOrderhmmseq <- function(lengthSeq, nucleotides, initialProb, states, transitionmatrix, emissionmatrix){
  
  outputSeq      <- character()     
  mystates        <- character()             

  firststate      <- sample(states, 1, rep=TRUE, prob=initialProb)

  probabilities   <- emissionmatrix[firststate,]

  firstnucleotide <- sample(nucleotides, 1, rep=TRUE, prob=probabilities)
  outputSeq[1]   <- firstnucleotide       
  mystates[1]     <- firststate         
  
  for (i in 2:lengthSeq){
    prevstate    <- mystates[i-1]  
    stateprobs   <- transitionmatrix[prevstate,]
    state        <- sample(states, 1, rep=TRUE, prob=stateprobs)
    probabilities <- emissionmatrix[state,]

    nucleotide   <- sample(nucleotides, 1, rep=TRUE, prob=probabilities)
    outputSeq[i] <- nucleotide      
    mystates[i]  <- state             
  }
  
  for (i in 1:lengthSeq){
    nucleotide   <- outputSeq[i]
    state        <- mystates[i]
    print(paste("Position", i, ", State", state, ", Nucleotide = ", nucleotide))
  }
  return(outputSeq)
}

viterbi <- function(sequence, transitionmatrix, emissionmatrix){

  states <- rownames(emissionmatrix)
  
  v <- makeViterbimat(sequence, transitionmatrix, emissionmatrix)
  
  mostprobablestatepath <- apply(v, 1, function(x) which.max(x))
  
  prevnucleotide            <- sequence[1]
  prevmostprobablestate     <- mostprobablestatepath[1]
  prevmostprobablestatename <- states[prevmostprobablestate]
  startpos <- 1
  for (i in 2:length(sequence)){
    nucleotide            <- sequence[i]
    mostprobablestate     <- mostprobablestatepath[i]
    mostprobablestatename <- states[mostprobablestate]
    if (mostprobablestatename != prevmostprobablestatename){
      print(paste("Positions",startpos,"-",(i-1),
                  "Most probable state = ", prevmostprobablestatename))
      startpos <- i
    }
    prevnucleotide <- nucleotide
    prevmostprobablestatename <- mostprobablestatename
  }
  print(paste("Positions",startpos,"-",i,
              "Most probable state = ", prevmostprobablestatename))
}

makeViterbimat <- function(sequence, transitionmatrix, emissionmatrix) {
  
  sequence <- toupper(sequence)

  numstates <- dim(transitionmatrix)[1]
  
  v <- matrix(NA, nrow = length(sequence), ncol = dim(transitionmatrix)[1])

  v[1, ] <- 0
 
  v[1,1] <- 1
 
  for (i in 2:length(sequence)) { 
    for (l in 1:numstates) { 
 
      statelprobnucleotidei <- emissionmatrix[l,sequence[i]]

      v[i,l] <-  statelprobnucleotidei * max(v[(i-1),] * transitionmatrix[,l])
    }
  }
  return(v)
}


pdf("markov_plots.pdf")

nucleotides <- c("A","C","G","T")

zeroOrderProbablities <- c(0.2,0.3,0.3,0.2)
 
names(zeroOrderProbablities) <- nucleotides

zeroOrderSeq <- sample(nucleotides,1000,rep=T,prob=zeroOrderProbablities)

plotData(zeroOrderSeq, nucleotides, "Multinomial Model of DNA Evoloution")

afterAprobs <- c(0.2,0.3,0.3,0.2) 
afterCprobs <- c(0.1,0.41,0.39,0.1)  
afterGprobs <- c(0.25,0.25,0.25,0.25)
afterTprobs <- c(0.5,0.17,0.17,0.17)

mytransitionmatrix <- matrix(c(afterAprobs, afterCprobs, afterGprobs, afterTprobs), 4, 4, byrow = TRUE) 


colnames(mytransitionmatrix) <- nucleotides
rownames(mytransitionmatrix) <- nucleotides


inProb <- c(0.4,0.1,0.1,0.4)
names(inProb) <- nucleotides

firstOrderSeq <- generateFirstOrderSeq(1000,nucleotides,inProb,mytransitionmatrix)

plotData(firstOrderSeq, nucleotides, "Markov Chain of first order")

states              <- c("AT-rich", "GC-rich")
ATrichprobs         <- c(0.7, 0.3)             
GCrichprobs         <- c(0.1, 0.9)            
theTransitionMatrix <- matrix(c(ATrichprobs, GCrichprobs), 2, 2, byrow = TRUE) 
rownames(theTransitionMatrix) <- states
colnames(theTransitionMatrix) <- states

ATrichstateprobs    <- c(0.39, 0.1, 0.1, 0.41)
GCrichstateprobs    <- c(0.1, 0.41, 0.39, 0.1) 
theEmissionMatrix   <- matrix(c(ATrichstateprobs, GCrichstateprobs), 2, 4, byrow = TRUE)
rownames(theEmissionMatrix) <- states
colnames(theEmissionMatrix) <- nucleotides


initialProb <- c(0.5, 0.5)
hmmfirstOrderSeq = generateFirstOrderhmmseq(10000, nucleotides, initialProb, states, theTransitionMatrix, theEmissionMatrix)
plotData(hmmfirstOrderSeq, nucleotides,  "Hidden Markov Model of first order")


myseq <- c("A", "A", "G", "C", "G", "T", "G", "G", "G", "G", "C", "C", "C", "C",
           "G", "G", "C", "G", "A", "C", "A", "T", "G", "G", "G", "G", "T", "G",
           "T", "C")
viterbi(myseq, theTransitionMatrix, theEmissionMatrix)

dev.off()
