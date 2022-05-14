import main

BC1 = main.count_nucleotides("BC1.map")
BC2 = main.count_nucleotides("BC2.map")
BC3 = main.count_nucleotides("BC3.map")
BC4 = main.count_nucleotides("BC4.map")
BC5 = main.count_nucleotides("BC5.map")
BC6 = main.count_nucleotides("BC6.map")
BC7 = main.count_nucleotides("BC7.map")

BC1_mutations = main.calculate_mutations((BC1))
BC2_mutations = main.calculate_mutations((BC2))
BC3_mutations = main.calculate_mutations((BC3))
BC4_mutations = main.calculate_mutations((BC4))
BC5_mutations = main.calculate_mutations((BC5))
BC6_mutations = main.calculate_mutations((BC6))
BC7_mutations = main.calculate_mutations((BC7))

BC1_plot = main.plot_mutation_base_proberbility(BC1, BC1_mutations)
BC2_plot = main.plot_mutation_base_proberbility(BC2, BC2_mutations)
BC3_plot = main.plot_mutation_base_proberbility(BC3, BC3_mutations)
BC4_plot = main.plot_mutation_base_proberbility(BC4, BC5_mutations)
BC5_plot = main.plot_mutation_base_proberbility(BC5, BC5_mutations)
BC6_plot = main.plot_mutation_base_proberbility(BC6, BC6_mutations)
BC7_plot = main.plot_mutation_base_proberbility(BC7, BC7_mutations)

print(BC1_plot)
