#import numpy as np
#from Bio import SeqIo
import re
import pandas as pd
import matplotlib as plt
# Amplicon seq output: Paired end fastaQ file format
# merge paired end reads for longer reads

# bowtie - filter out bad scoring reads
# demultiplexing the reads

# make a dict of dicts, first key position, second key nucleotide, containing a number or mutations found
# Use regular expression to find the position and append the mutationdef sort_bowtiedata(filename):
def sort_bowtiedata(filename):
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
# Problem: does not add 1 but overwrites as 1

def sort_bowtiedata2(filename):
    "Takes a txt file from a bowtie output, returns a dict of dicts with nucleotide position as outer key, nucleotide as inner key and number of mutations as value"
    dict_of_nucleotide_positions = {}
    input_file = open(filename)
    lines = input_file.readlines()
    for line in lines:
        elements = re.split("\s", line)  #splits alignment position from mutations
        alignment_position = elements[0]
        mutations = elements[1]
        mutations = re.split(",", mutations)
        for mutation in mutations:
            mutation = re.split(":|>", mutation) # seperates each mutation in position and mutation
            position = int(mutation[0]) + int(alignment_position)
            if position not in dict_of_nucleotide_positions:
                dict_of_mutations = {"A": 0, "T": 0, "C": 0, "G": 0}
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

def plot_mutations_vs_position(dict_of_dicts):
    "takes a dict of dicts and plots alignment position vs number of mutations"
    matplotlib.pyplot.scatter(dict_of_dicts)

#def plot_subtitution_frequency(dict_of_dicts)


