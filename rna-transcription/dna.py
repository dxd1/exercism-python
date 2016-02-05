def to_rna(dna):
    dictionary = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna = ''
    for char in dna:
        rna += dictionary[char]
    return rna
