# Luke Fetchko
# CSCI U236
# Prof. Dan Wooster
# Hours Spent: 7-8 hours
# Probelms enountered: It took me very long to figure out how to correctly write to the output file,
# I kept getting only the last sequences information when using a context manager with 'w' mode in my get results function,
# but I figured out that my main problem was not manually closing the files at the end of the program since we manually opened them.

# This program reads and processes input files containing DNA sequence names and the DNA sequences themself,
# it calculates the number of each individual nucelotide present, the total mass of a given sequence, the mass percentages of each nucleotide in a sequence, determines the codons present in the sequence,
# and finally writes to an output file the results calculated of each sequence with a name, nucleotide list, a list with the number of each nucleotide in the sequence and mass percentage list in
# ACGT order,a list containing all codons,
# and lastly determines if a given sequence encodes for a protein.

# Program runs as expected and output file matches content and format exactly as expected on GitHub


# Also I noticed on CodePost that check contents ecoli test 2 is using dna.txt for its input file

# needed constants
MIN_NUM_OF_CODONS_FOR_PROTEIN = 5
PCT_OF_CANDG_FOR_PROTEIN = 30
NUM_OF_NTIDES = 4
NTIDES_PER_CODON = 3
MASSES = [135.128, 111.103, 151.128, 125.107]

# function to traverse the given string and count the number of each individual nucleotides and return number of each nucleotide in a list of [A,C,G,T] order
def get_count(s):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for char in s:
        if char == 'A':
            a_count += 1
        elif char == 'C':
            c_count += 1
        elif char == 'G':
            g_count += 1
        elif char == 'T':
            t_count += 1
    return [a_count, c_count, g_count, t_count]

# function to calculate the total mass of a specific sequence including junk characters, mass values come from MASSES constant list in order by index
def get_mass(counts_list, j_count):
    total = 0
    i = 0
    while i < len(counts_list):
        total += (counts_list[i] * MASSES[i])
        i += 1
    total += j_count * 100.000
    return total

# function to calculate mass percentage of each nucleotide of a sequence given list of counts of nucleotide and total mass, returns list of mass percentages in A,C,G,T order
def get_percentages(counts_list, total_mass):
    i = 0
    list1 = []
    while i < NUM_OF_NTIDES:
        pct = ((counts_list[i] * MASSES[i]) / total_mass) * 100
        list1.append(round(pct,1))
        i += 1
    return list1

# function to return list of codons given modified sequence without junk characters, appends to list and removes newline character if present in list
def get_codons(seq):
    list1 = []
    while seq:
        list1.append(seq[:NTIDES_PER_CODON])
        seq = seq[NTIDES_PER_CODON:]
    if '\n' in list1:
        list1.remove('\n')
    return list1

# function to generate string containing all necessary output to file, checks that given sequence with counts list, mass total, percentages list, and codons list is a protein based on predefined specifications
def get_results(name, seq, counts, mass_total, percentages, codons):
    line1= 'Region Name: ' + name.rstrip('\n')
    line2 = 'Nucleotides: ' + seq.rstrip('\n')
    line3 = 'Nuc. Counts: ' + str(counts)
    line4 = "Total Mass%: " + str(percentages)+ ' of '+ str(round(mass_total,1))
    line5 = 'Codons List: ' + str(codons)
    is_protein = True

    if codons[0] != 'ATG':
        is_protein = False
    elif codons[-1] != 'TAA' and codons[-1] != 'TAG' and codons[-1] != 'TGA':
        is_protein = False
    elif len(codons) < MIN_NUM_OF_CODONS_FOR_PROTEIN:
        is_protein = False
    elif percentages[1] + percentages[2] < PCT_OF_CANDG_FOR_PROTEIN:
        is_protein = False

    if is_protein:
        line6 ='Is Protein?: ' + 'YES'
    else:
        line6 ='Is Protein?: ' + 'NO'

    results_str = '{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6)

    return results_str

# function to calculate number of junk characters in a given sequence
def get_junk_count(seq):
    junk_count1 = 0
    for char in seq:
        if char == '-':
            junk_count1 +=1
    return junk_count1

# main function
def main():
# breifly explain what program does
    print('This program reports information about DNA\nnucleotide sequences that may encode proteins.')

# get the file names and open needed files
    input_f = open(input('Input file name? '))
    output_f = open(input('Output file name? '), 'w')
# read all lines of the input
    lines = input_f.readlines()
# traverse all lines of input
    # initialize index/counter variable for while loop
    i = 0
    while i < len(lines):
        #get sequence name
        name_seq =lines[i]
        # get original sequnce in all upper case
        seq = lines[i + 1].upper()
        # count number of junk characters
        junk_count = get_junk_count(seq)
        # generate modified sequence without junk chars
        modified = seq.replace("-","")
        #call get_count function and store results in list
        counts = get_count(modified)
        #call get_mass function and store value
        mass_total = get_mass(counts, junk_count)
        #call get_percentage function and store results in list
        percentages = get_percentages(counts, mass_total)
        #call get_codons function and store results in list
        codons = get_codons(modified)
        # write needed output to output file
        if i + 1 == len(lines) - 1:
            output_f.write(get_results(name_seq, seq,counts,mass_total, percentages, codons))
        else:
            output_f.write(get_results(name_seq, seq,counts,mass_total, percentages, codons) + '\n')
        # update index or counter by 2 since 2 lines have already been processed
        i += 2
    # close files
    output_f.close()
    input_f.close()
#call main
main()
