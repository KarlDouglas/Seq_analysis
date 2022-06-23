import main
import matplotlib.pyplot as plt

BC1 = main.count_nucleotides("BC1.F.map")

BC1_mutations = main.calculate_mutations((BC1))

BC1_plot = main.plot_mutation_base_proberbility(BC1, BC1_mutations)
plt.savefig("BC1.png")


