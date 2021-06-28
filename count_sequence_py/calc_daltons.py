"""
This Program calculates the weight of protein based on protein length and average weight of
each amino acid
"""


def calc_weight(sequence):
    """
    This function is returning the weight of the protein sequence given based on average weight
    given for each amino acid in given protein
    """
    return len(sequence) * AVG_WEIGHT


if __name__ == '__main__':
    PROTEIN_SEQUENCE = ('MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQVC'
                        'CFVVHKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVH'
                        'KRCVMNVPSLCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKSESKQ'
                        'KTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSLSFGISELQKAGVDGWFKLLSQ'
                        'EEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDFNFLMVLGK'
                        'GSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVM'
                        'EYVNGGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGHIKIADFGMCKE'
                        'NIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEMLAGQAPFEGEDEDELFQSIMEHNVAY'
                        'PKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQPPYKPKARDKRDTSNF'
                        'DKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV')

    # average weight of each amino acid
    AVG_WEIGHT = 110
    WEIGHT_IN_KD = calc_weight(PROTEIN_SEQUENCE)

    # printing the final output
    print('The length of "Protein kinase C beta type" is:', len(PROTEIN_SEQUENCE))
    print('The average weight of this protein sequence in kilodaltons is:', (WEIGHT_IN_KD / 1000))
