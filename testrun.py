import main

#test1 = main.sort_bowtiedata2("Bowtie_data_coordinate+mutation.txt")
#print(test1)

test2 = main.count_nucleotides("Bowtie_data_coordinate+sequence.txt")
print(test2)

test_calculator = main.calculate_mutations((test2))
print(test_calculator)

test_calculator2 = main.calculate_substitutions(test2)
print(test_calculator2)