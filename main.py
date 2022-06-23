import re
import matplotlib.pyplot as plt

def count_nucleotides(m_reads):
    "Takes a txt file from a bowtie output with alignment position followed by the sequence seperated by a blank space, returns a dict of dicts with nucleotide position as outer key, nucleotide as inner key and number of nucleotides counted as value"
    dict_of_nucleotide_positions = {}
    input_file = open(m_reads)
    lines = input_file.readlines()
    for line in lines:
        elements = re.split("\s", line)  #splits alignment position from mutations
        alignment_position = elements[0]
        sequence = elements[1]
        for nucleotide in enumerate(sequence): #enumerate to keep track of the alignment position
            position = int(alignment_position)+nucleotide[0]
            if position not in dict_of_nucleotide_positions:
                dict_of_mutations = {"A": 0, "T": 0, "C": 0, "G": 0, "N":0}
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
        mutations = sum(list_of_nucleotides)-wt-dict_of_nucleotides["N"]
        mutation_percentage = [mutations/sum(list_of_nucleotides)]
        if position not in dict_of_mutation_percentages:
            dict_of_mutation_percentages[position] = mutation_percentage
    return dict_of_mutation_percentages

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
    ax2 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)
    ax3 = plt.subplot2grid((3, 3), (1, 1))
    ax4 = plt.subplot2grid((3, 3), (1, 2))
    ax5 = plt.subplot2grid((3, 3), (2, 1))
    ax6 = plt.subplot2grid((3, 3), (2, 2))
    ax1.scatter(x, y)
    ax1.set_title('Mutation Distribution')
    ax2.bar(x1, y1, color = ["blue","green","orange","red"])
    ax2.set_title('%WT mutated')
    ax3.bar(AX, A.values(), color = ["blue"])
    ax3.set_title('A')
    ax4.bar(TX, T.values(),color="green")
    ax4.set_title('T')
    ax5.bar(CX, C.values(),color="orange")
    ax5.set_title('C')
    ax6.bar(GX, G.values(),color="red")
    ax6.set_title('G')
    plt.tight_layout()
    return