#Introduction to bioinformatics
#Project 1
#PCR Simulation with Python
#Genome E
#26245-26472
#protein_id="YP_009724392.1"

import os
import numpy

# Returns CDNA from RNA
def getCDNA(rna):
    cdna = rna.upper() # Ensure all caps to prevent errors
    cdna = cdna.replace("A", "X")
    cdna = cdna.replace("T", "A")
    cdna = cdna.replace("X", "T")
    cdna = cdna.replace("C", "X")
    cdna = cdna.replace("G", "C")
    cdna = cdna.replace("X", "G")
    return cdna

file = "sequence.fasta"

#print lines retrieving

comments = file.readline()

SARS_COV2_genome = file.read()

file.close()

SARS_COV2_genome = SARS_COV2_genome.replace('\n','')

# extract E gene from 26245:26472
E_gene = SARS_COV2_genome[26245:26472]   # rna sequence


