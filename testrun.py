import main

#test1 = main.count_bowtiedata_mutations2("Bowtie_data_coordinate+mutation.txt")
#print(test1)

test2 = main.count_nucleotides("test.map")
#print(test2)

test_calculator = main.calculate_mutations((test2))
#print(test_calculator)

test_calculator2 = main.calculate_substitutions(test2)
#print(test_calculator2)

#test_plot = main.plot_mutations_vs_position(test_calculator)

test_plot2 = main.plot_mutation_base_proberbility(test2, test_calculator)
print(test_plot2)

#test_demultiplex = main.demultiplex_seqreads("test_data2.fastaq", "GACTAGCTACGTCAGTTCAAGTCC")