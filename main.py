import re
import matplotlib.pyplot as plt
def count_bowtiedata_mutations(filename):
    "Takes a txt file from a bowtie output, returns a dict of dicts with nucleotide position as outer key, nucleotide as inner key and number of mutations as value"
    dict_of_nucleotide_positions = {}
    input_file = open(filename)
    lines = input_file.readlines()
    for line in lines:
        elements = re.split("\t|:|>",line)
        alignment_position = elements[0]
        seqread_mutation_position = elements[1]
        position = int(alignment_position)+int(seqread_mutation_position)
        if position not in dict_of_nucleotide_positions:
            dict_of_mutations = {"A":0,"T":0,"C":0,"G":0}
            dict_of_nucleotide_positions[position] = dict_of_mutations #Adds a dict with the nucleotide position as key
        outerkey = position
        innerkey = elements[3]
        dict_of_nucleotide_positions[outerkey][innerkey] += 1
    return dict_of_nucleotide_positions

def count_bowtiedata_mutations2(filename):
    "Takes a txt file from a bowtie output with alignment position as first element and mutaions listed as second element, returns a dict of dicts with nucleotide position as outer key, nucleotide as inner key and number of mutations as value"
    dict_of_nucleotide_positions = {}
    input_file = open(filename)
    lines = input_file.readlines()
    for line in lines:
        elements = re.split("\s", line)  #splits alignment position from mutations
        alignment_position = elements[0]
        mutations = elements[1]
        mutations = re.split(",", mutations) #splits mutations from one another
        for mutation in mutations:
            mutation = re.split(": | >", mutation) # splits each mutation in position and mutation
            position = int(mutation[0]) + int(alignment_position)
            if position not in dict_of_nucleotide_positions:
                dict_of_mutations = {"A": 0, "T": 0, "C": 0, "G": 0} # Creates an empty dict with nucleotides as keys
                dict_of_nucleotide_positions[position] = dict_of_mutations  # Adds a dict with the nucleotide position as key
            outerkey = position
            innerkey = mutation[2]
            dict_of_nucleotide_positions[outerkey][innerkey] += 1
    return dict_of_nucleotide_positions

def count_nucleotides(filename):
    "Takes a txt file from a bowtie output with alignment position+sequence, returns a dict of dicts with nucleotide position as outer key, nucleotide as inner key and number of nucleotides counted as value"
    dict_of_nucleotide_positions = {}
    input_file = open(filename)
    lines = input_file.readlines()
    for line in lines:
        elements = re.split("\s", line)  #splits alignment position from mutations
        alignment_position = elements[0]
        sequence = elements[1]
        for nucleotide in enumerate(sequence):
            position = int(alignment_position)+nucleotide[0]
            if position not in dict_of_nucleotide_positions:
                dict_of_mutations = {"A": 0, "T": 0, "C": 0, "G": 0}
                dict_of_nucleotide_positions[position] = dict_of_mutations  # Adds a dict with the nucleotide position as key
            outerkey = position
            innerkey = nucleotide[1]
            dict_of_nucleotide_positions[outerkey][innerkey] += 1
    return dict_of_nucleotide_positions

def calculate_mutations(dict):
    "docstring"
    dict_of_mutation_percentages = {}
    items = dict.items()
    for item in items:
        position = item[0]
        dict_of_nucleotides = item[1]
        list_of_nucleotides = dict_of_nucleotides.values()
        wt = max(list_of_nucleotides)
        mutations = sum(list_of_nucleotides)-wt
        mutation_percentage = [mutations/sum(list_of_nucleotides)]
        if position not in dict_of_mutation_percentages:
            dict_of_mutation_percentages[position] = mutation_percentage
    return dict_of_mutation_percentages

def calculate_substitutions(dict):
    "docstring"
    dict_of_substitution_frequencies = {}
    for key, value in dict.items():
        position = key
        list = value.values()
        wt = max(list)
        mutations = sum(list) - wt
        for nucleotide, number in value.items():
            substitution_frequency = number/sum(list)
            if position not in dict_of_substitution_frequencies:
                dict_of_substitutions = {"A": 0, "T": 0, "C": 0, "G": 0}
                dict_of_substitution_frequencies[position] = dict_of_substitutions  # Adds a dict with the nucleotide position as key
            outerkey = position
            innerkey = nucleotide
            dict_of_substitution_frequencies[outerkey][innerkey] += substitution_frequency
    return dict_of_substitution_frequencies

def plot_mutation_base_proberbility(dict, dict_of_mutation_percentages):
    "Docstring"
    dict_of_wt = {"A": 0, "T": 0, "C": 0, "G": 0}
    A = { "T": 0, "C": 0, "G": 0}
    T = {"A": 0, "C": 0, "G": 0}
    G = {"T": 0, "C": 0, "A": 0}
    C = {"T": 0, "A": 0, "G": 0}
    for key, value in dict.items():
        wt = max(value, key=value.get)
        count = max(value.values())
        dict_of_wt[wt] += count
        if "A" == wt:
            substitution = list(value.values())
            A["T"] += substitution[1]
            A["C"] += substitution[2]
            A["G"] += substitution[3]
        if "T" == wt:
            substitution = list(value.values())
            T["A"] += substitution[0]
            T["C"] += substitution[2]
            T["G"] += substitution[3]
        if "C" == wt:
            substitution = list(value.values())
            C["A"] += substitution[0]
            C["G"] += substitution[3]
            C["T"] += substitution[1]
        if "G" == wt:
            substitution = list(value.values())
            G["A"] += substitution[0]
            G["T"] += substitution[1]
            G["C"] += substitution[2]
    x1 = ["A","T","C","G"]
    AX = ["T","C","G"]
    TX = ["A","C","G"]
    CX = ["A","G","T"]
    GX = ["A","T","C"]
    y1 = [sum(A.values())/dict_of_wt["A"],sum(T.values())/dict_of_wt["T"],sum(C.values())/dict_of_wt["C"],sum(G.values())/dict_of_wt["G"]] # height of bar is number of substitutions divided by number of wt bases counted
    lists = sorted(dict_of_mutation_percentages.items())
    x, y = zip(*lists)
    ax = plt.subplot2grid((2, 2), (0, 0))
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
    ax2 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    ax3 = plt.subplot2grid((3, 3), (1, 0))
    ax4 = plt.subplot2grid((3, 3), (1, 1))
    ax5 = plt.subplot2grid((3, 3), (2, 0))
    ax6 = plt.subplot2grid((3, 3), (2, 1))
    ax1.scatter(x, y)
    ax1.set_title('Mutation Distribution')
    ax2.bar(x1, y1)
    ax2.set_title('%WT mutated')
    ax3.bar(AX, A.values())
    ax3.set_title('A')
    ax4.bar(TX, T.values(),color="green")
    ax4.set_title('T')
    ax5.bar(CX, C.values(),color="orange")
    ax5.set_title('C')
    ax6.bar(GX, G.values(),color="red")
    ax6.set_title('G')
    plt.tight_layout()
    plot = plt.show()
    return plot

def plot_mutations_vs_position(dict_of_mutation_percentages):
    "takes a dict of dicts and plots alignment position vs number of mutations"
    lists = sorted(dict_of_mutation_percentages.items())
    x, y = zip(*lists)
    plt.scatter(x,y)
    plt.xlabel("Base position")
    plt.ylabel("mutational frequency")
    plot = plt.show()
    return plot

#why does it not return A?

#plot 4 bars with each base representing each WT base that has been mutated. Eg. 40% of the mutated bases being a G
#Plot within each base 3 bars of the possible substitutions that represent the frequency.


def demultiplex_seqreads(filename, adapter):
    "sorts seqreads by barcode"
    seq = adapter
    lines = filename.readlines()
    return lines

def merge_paired_end_reads(filename1,filename2):
    "takes two files and merges pared end reads from seq"
    F_reads = filename1.open()
    R_reads = filename2.open()
    return