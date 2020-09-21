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