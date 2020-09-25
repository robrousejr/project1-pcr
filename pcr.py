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
    doubleStrandedDNAs = [('a','a'),('a','a')]  # get your sequence of dnas
    return doubleStrandedDNAs
