#import numpy as np
#from Bio import SeqIo
import re
import matplotlib.pyplot as plt
import numpy as np
# Amplicon seq output: Paired end fastaQ file format
# merge paired end reads for longer reads

# bowtie - filter out bad scoring reads
# demultiplexing the reads

# make a dict of dicts, first key position, second key nucleotide, containing a number or mutations found
# Use regular expression to find the position and append the mutationdef sort_bowtiedata(filename):
def count_bowtiedata_mutations(filename):
    "Takes a txt file from a bowtie output, returns a dict of dicts with nucleotide position as outer key, nucleotide as inner key and number of mutations as value"
    dict_of_nucleotide_positions = {}
    input_file = open(filename)
    lines = input_file.readlines()
    for line in lines:
        elements = re.split("\s|:|>",line)
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
#Delete first version?

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

def plot_mutation_base_proberbility(dict):
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
    A1 = sum(A.values())
    x = ["A","T","C","G"]
    A_val = list(A.values())
    A_val.insert(0,0)
    T_val = list(T.values())
    T_val.insert(1, 0)
    C_val = list(C.values())
    C_val.insert(2, 0)
    G_val = list(G.values())
    G_val.insert(3, 0)
    bottom1 = np.add(A_val, T_val).tolist()
    bottom2 = np.add(bottom1, C_val).tolist()
    plt.bar(x, A_val)
    plt.bar(x, T_val, bottom=A_val)
    plt.bar(x, C_val, bottom=bottom1)
    plt.bar(x, G_val, bottom=bottom2)
    #y = [sum(A.values())/dict_of_wt["A"],sum(T.values())/dict_of_wt["T"],sum(C.values())/dict_of_wt["C"],sum(G.values())/dict_of_wt["G"]] # height of bar is number of substitutions divided by number of wt bases counted
    #plt.bar(x,y, color=["green","red","orange","blue"])
    #plt.bar()
    #plt.ylabel("substitution frequency")
    plt.show()
    return None

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




#def plot_subtitution_frequency(dict_of_dicts)


