import random
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('tkagg')


# param: a DNA strand
# Returns complement from given strand
def getComp(strand):
    comp = strand.upper()  # Ensure all caps to prevent errors
    comp = comp.replace("A", "X")
    comp = comp.replace("T", "A")
    comp = comp.replace("X", "T")
    comp = comp.replace("C", "X")
    comp = comp.replace("G", "C")
    comp = comp.replace("X", "G")
    return comp


# param: null
# return: a tuple of two tuples where each tuple contain primers sequence, GC, start, and end position.
def getPrimers():
    # Primer pair 7 (Sequence, GC, start, end)
    forwardPrimer = ("TGTACTCATTCGTTTCGGAA", 0.5, 7, 28)
    reversePrimer = ("AAGGACTAGAAGACCAGATT", 0.5, 134, 115)
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
def annealing_elongation(singleStrandDNAs, primers, fall_of_rate=50, prim_distance=200):
    DNA = []
    # ...
    f_primer = primers[0][0]
    c_f_primer = getComp(f_primer)
    r_primer = primers[1][0]
    c_r_primer = getComp(r_primer)
    c_r_primer = c_r_primer[::-1]

    # use any primer to get the length of a primer
    f_prim_length = 22  # len(f_primer)
    r_prim_length = 20  # len(r_primer)
    # print("prim_lenght")
    # print(f_prim_length)
    # print(r_prim_length)
    # print()

    # calculate the rate for cycle
    # rate = prim_distance + random.randint(-fall_of_rate, fall_of_rate)
    # print("\nrate:" + str(rate))

    for item in singleStrandDNAs:

        rate = prim_distance + random.randint(-fall_of_rate, fall_of_rate)
        # print("\nrate:")
        # print(rate)

        # print("item: ")
        # print(item)
        # first strand of the tuple DNA for the list is the initial single strand
        first = item
        second = ""

        if first == "":
            continue

        # if this is true then we are dealing with a reverse primer for the second
        if first.find(c_r_primer) != -1:
            # easier to work with coding strands in 5->3
            second = first

            # we need the complement to the r_primer to find the end index to get the strand we want the complement of
            check = c_r_primer

            # get the end index
            end = second.index(check)

            # use end to get the strand we need the complement of and get the complement
            second = second[end:end + r_prim_length + rate]

            second = getComp(second)
            second = second[::-1]

        elif first.find(c_f_primer) != -1:
            # no need to reverse since easier to work in 3->5
            second = first

            # need the complement of the primer to find start index on the strand
            check = c_f_primer

            # use the complement to get the start index and find the part of the strand we want
            start = second.index(check)
            second = second[start: start + f_prim_length + rate]

            # get the complement and reverse the strand so we have 3->5 uniformly in every strand
            second = getComp(second)
            second = second[::-1]

        DNA.append((first, second))

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
        # print(singleStrandDNAs)
        # for item in singleStrandDNAs:
        #    print(item)
        PCRproducts = annealing_elongation(singleStrandDNAs, primers, fall_of_rate)
        print("\n cycle " + str(cycles + 1) + " completed")
        # for item in PCRproducts:
        # print(item)
        cycles += 1
    # print("Total cyles:" + str(cycles))

    return PCRproducts


def stats(rep_dna):
    """
    Find statistics on replicated DNA. Finds strands, max strand length, min strand length, and average strand length.
    Finds average GC content of strands. Plots distributions of strands
    :param replicated_dna:
    :return:
    """

    segment_lengths = []
    gc_contents = []
    for pair in rep_dna:
        for strand in pair:
            if strand != '':
                segment_lengths.append(len(strand))

                # Find GC contents of both strands
                num_of_c = strand.count('C')
                num_of_g = strand.count('G')
                gc_content = num_of_c + num_of_g
                gc_contents.append(gc_content)

    num_of_strands = len(segment_lengths)

    max_length = max(segment_lengths)
    min_length = min(segment_lengths)
    avg_length = sum(segment_lengths) / len(segment_lengths)
    avg_gc_content = (sum(gc_contents) / len(gc_contents)) / avg_length

    hist = plt.hist(segment_lengths)
    plt.xlabel('Strand Lengths')
    plt.ylabel('Frequency')
    plt.title('Distribution of Strand Lengths')
    print(f'Total Strands found:{num_of_strands}')
    print(f'Average GC Content:{avg_gc_content}%', )
    print(f'Max Length:{max_length}')
    print(f'Min Length:{min_length}')
    print(f'Average Length:{avg_length}')
    plt.show()

    return