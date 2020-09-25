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

# Primer pair 7 (Sequence, GC, start, end)
forwardPrimer = ("CATTCGTTTCGGAAGAGACAGG", 0.5, 7, 28)
reversePrimer = ("ATTGCAGCAGTACGCACACA", 0.5, 134, 115)
primers = [forwardPrimer, reversePrimer]

print(E_gene)
print
print(len(E_gene))
print
print(primers[1])
