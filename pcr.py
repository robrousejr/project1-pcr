import random

# Returns CDNA from RNA
def getCDNA(rna):
    cdna = rna.upper() # Ensure all caps to prevent errors
    cdna = cdna.replace("A", "X")
    cdna = cdna.replace("T", "A")
    cdna = cdna.replace("X", "T")
    cdna = cdna.replace("C", "X")
    cdna = cdna.replace("G", "C")
    cdna = cdna.replace("X", "G")
    cdna = cdna[::-1]  # reverse complementary strand
    return cdna

# param: a double strand dna, a tuple of 2 strings, representing 2 segments of dna from 5" to 3"
# return: a tuple of 2 strs representing the pair of primers (5" -> 3", GC content > 40%, bases btw the 2 primers: ~200)
def getPrimers():
    # Primer pair 7 (Sequence, GC, start, end)
    forwardPrimer = ("CATTCGTTTCGGAAGAGACAGG", 0.5, 7, 28)
    reversePrimer = ("ATTGCAGCAGTACGCACACA", 0.5, 134, 115)
    primers = (forwardPrimer, reversePrimer)
    return primers

# param: a list of tuples of 2 strs, representing double stranded dna segments
# return: a list of single strand dna segments
def denaturation(dna_segments):
    single_strands_DNA = []
    for item in dna_segments:
        single_strands_DNA.append(item[0])
        single_strands_DNA.append(item[1])
    return single_strands_DNA

# param: a list of single strand dna segments, each segment is from 5" to 3"
# return: a list of tuples of 2 strs (2 dna segments from 5" to 3")
def annealing_elongation(singleStrandDNAs, primers, fall_of_rate = 50):
    # ...
    f_primer = primers[0]
    r_primer = primers[1]

    # calculate the rate for cycle
    f_rate = (f_primer[3] - f_primer[2]) + random.randint(-fall_of_rate, fall_of_rate)
    r_rate = (r_primer[3] - r_primer[2]) + random.randint(-fall_of_rate, fall_of_rate)





    doubleStrandedDNAs = [('a','a'),('a','a')]  # get your sequence of dnas
    return doubleStrandedDNAs


# param: gene to be copied (a tuple of 2 strs), fall of rate of DNA polymerase (int), and num_cycles to run PCR (int)
# return: a list of double stranded dna segments
def PCR(dna_segment_to_be_copied, fall_of_rate, num_cycles):
    # ....
    primers = getPrimers()
    cycles = 0
    PCRproducts = [dna_segment_to_be_copied]
    while cycles < num_cycles:
        singleStrandDNAs = denaturation(PCRproducts)
        PCRproducts = annealing_elongation(singleStrandDNAs, primers, fall_of_rate)

    return PCRproducts