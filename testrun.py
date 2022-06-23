import main
import matplotlib.pyplot as plt

main.merge_txt_files("BC1.F.map", "BC1.R.map","BC1.M.map", "BC1.map")
BC1 = main.count_nucleotides("BC1_merged.txt")
BC1_mutations = main.calculate_mutations((BC1))
BC1_plot = main.plot_mutation_base_proberbility(BC1, BC1_mutations)
plt.savefig("BC1.png")

main.merge_txt_files("BC2.F.map", "BC2.R.map","BC2.M.map", "BC2.map")
BC2 = main.count_nucleotides("BC2_merged.txt")
BC2_mutations = main.calculate_mutations((BC2))
BC2_plot = main.plot_mutation_base_proberbility(BC2, BC2_mutations)
plt.savefig("BC2.png")

main.merge_txt_files("BC3.F.map", "BC3.R.map","BC3.M.map", "BC3.map")
BC3 = main.count_nucleotides("BC3_merged.txt")
BC3_mutations = main.calculate_mutations((BC3))
BC3_plot = main.plot_mutation_base_proberbility(BC3, BC3_mutations)
plt.savefig("BC3.png")

main.merge_txt_files("BC4.F.map", "BC4.R.map","BC4.M.map", "BC4.map")
BC4 = main.count_nucleotides("BC4_merged.txt")
BC4_mutations = main.calculate_mutations((BC4))
BC4_plot = main.plot_mutation_base_proberbility(BC4, BC4_mutations)
plt.savefig("BC4.png")

main.merge_txt_files("BC5.F.map", "BC5.R.map","BC5.M.map", "BC5.map")
BC5 = main.count_nucleotides("BC5_merged.txt")
BC5_mutations = main.calculate_mutations((BC5))
BC5_plot = main.plot_mutation_base_proberbility(BC5, BC5_mutations)
plt.savefig("BC5.png")

main.merge_txt_files("BC6.F.map", "BC6.R.map","BC6.M.map", "BC6.map")
BC6 = main.count_nucleotides("BC6_merged.txt")
BC6_mutations = main.calculate_mutations((BC6))
BC6_plot = main.plot_mutation_base_proberbility(BC6, BC6_mutations)
plt.savefig("BC6.png")

main.merge_txt_files("BC7.F.map", "BC7.R.map","BC7.M.map", "BC7.map")
BC7 = main.count_nucleotides("BC7_merged.txt")
BC7_mutations = main.calculate_mutations((BC7))
BC7_plot = main.plot_mutation_base_proberbility(BC7, BC7_mutations)
plt.savefig("BC7.png")

main.merge_txt_files("BC8.F.map", "BC8.R.map","BC8.M.map", "BC8.map")
BC8 = main.count_nucleotides("BC8_merged.txt")
BC8_mutations = main.calculate_mutations((BC8))
BC8_plot = main.plot_mutation_base_proberbility(BC8, BC8_mutations)
plt.savefig("BC8.png")

main.merge_txt_files("BC9.F.map", "BC9.R.map","BC9.M.map", "BC9.map")
BC9 = main.count_nucleotides("BC9_merged.txt")
BC9_mutations = main.calculate_mutations((BC9))
BC9_plot = main.plot_mutation_base_proberbility(BC9, BC9_mutations)
plt.savefig("BC9.png")

main.merge_txt_files("BC10.F.map", "BC10.R.map","BC10.M.map", "BC10.map")
BC10 = main.count_nucleotides("BC10_merged.txt")
BC10_mutations = main.calculate_mutations((BC10))
BC10_plot = main.plot_mutation_base_proberbility(BC10, BC10_mutations)
plt.savefig("BC10.png")
