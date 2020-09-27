import random

# Returns complement from given strand
def getComp(strand):
    comp = strand.upper() # Ensure all caps to prevent errors
    comp = comp.replace("A", "X")
    comp = comp.replace("T", "A")
    comp = comp.replace("X", "T")
    comp = comp.replace("C", "X")
    comp = comp.replace("G", "C")
    comp = comp.replace("X", "G")
    return comp

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
def annealing_elongation(singleStrandDNAs, primers, fall_of_rate = 50, prim_distance = 150):
    DNA = []
    # ...
    f_primer = primers[0][0]
    r_primer = primers[1][0]
     
    # use any primer to get the length of a primer
    prim_length = len(f_primer)

    # calculate the rate for cycle
    rate = prim_distance + random.randint(-fall_of_rate, fall_of_rate)


    for item in singleStrandDNAs:

        # first strand of the tuple DNA for the list is the initial single strand
        first = item
        second = ""

        if first == "":
            continue

        # if this is true then we are dealing with a reverse primer for the second
        first_r = first[::-1]
        if first_r.count(getComp(r_primer)) == 1:
            # easier to work with coding strands in 5->3
            second = first[::-1]

            # we need the complement to the r_primer to find the end index to get the strand we want the complement of
            check = getComp(r_primer)

            # get the end index
            end = second.index(check)

            # use end to get the strand we need the complement of and get the complement
            second = second[end - rate:end + prim_length]

            second = getComp(second)

        elif first.count(getComp(f_primer)) == 1:
            # no need to reverse since easier to work in 3->5
            second = first

            # need the complement of the primer to find start index on the strand
            check = getComp(f_primer)

            # use the complement to get the start index and find the part of the strand we want
            start = second.index(check)
            second = second[start: start + prim_length + rate]

            # get the complement and reverse the strand so we have 3->5 uniformly in every strand
            second = getComp(second)
            second = second[::-1]

        DNA.append((first,second))

    return DNA

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
        cycles += 1

    return PCRproducts