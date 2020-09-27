#Introduction to bioinformatics
#Project 1
#PCR Simulation with Python
#Genome E
#26245-26472
#protein_id="YP_009724392.1"
#"""
#Rob Rouse
#Yuvraj Subedi
#Jaron Smith
#"""

import os
import numpy
import pcr as pcr

with open('sequence.fasta') as file:
    comments = file.readline()
    SARS_COV2_genome = file.read()

file.close()

SARS_COV2_genome = SARS_COV2_genome.replace('\n','')

# extract E gene from 26245:26472
E_gene = SARS_COV2_genome[26245:26472]   # rna sequence

#get complementary DNA
cDNA_c = pcr.getComp(E_gene)
cDNA = cDNA_c[::-1]

#double stranded DNA
DNA = (E_gene, cDNA)

forwardPrimer = pcr.getPrimers()[0]
reversePrimer = pcr.getPrimers()[1]

# Sequences
print(DNA[0][forwardPrimer[2]:reversePrimer[2]])
print(DNA[1][forwardPrimer[2]:reversePrimer[2]])

PCR_products = pcr.PCR(DNA, 30, 20)
pcr.stats(PCR_products)


