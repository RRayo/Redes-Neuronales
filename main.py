from fitness.bits_fitness import BitFitness
from fitness.nqueens_fit import NQueensFit
from genetic_algorithm import GeneticAlgorithm
from population.pop_nqueens import PopNQueens
from population.population import Population
from reproduction.reproduction import Reproduction
from selection.selection import Selection


def main():  # TODO hacer clase/función que reciba los parámetros mutacion_rate, pop_size
    # BITS

    len_genes = 5
    genes = [0, 1]
    pop_size = len_genes * 2
    mutation_rate = 0.1
    max_fit = 5  # todos son iguales al individuo original
    ga_bits = GeneticAlgorithm(len_genes, genes, pop_size, mutation_rate, max_fit)
    fitness_max_history, fitness_mean_history, counter, time = ga_bits.run(Population, BitFitness, Selection,
                                                                           Reproduction, ref_individual=True)

    print(fitness_max_history, fitness_mean_history, counter, time)

    # STRING

    len_genes = 5
    genes = list("qwertyuiopasdfghjklzxcvbnm")
    pop_size = len_genes * 10
    mutation_rate = 0.1
    max_fit = 5  # todos son iguales al individuo original
    ga_string = GeneticAlgorithm(len_genes, genes, pop_size, mutation_rate, max_fit)
    fitness_max_history, fitness_mean_history, counter, time = ga_string.run(Population, BitFitness, Selection,
                                                                             Reproduction, ref_individual=True)

    print(fitness_max_history, fitness_mean_history, counter, time)

    # N-Queens

    len_genes = 8
    genes = [i for i in range(len_genes)]
    pop_size = len_genes * 10
    mutation_rate = 0.1
    max_fit = 1.0  # minimo numero de errores
    ga_string = GeneticAlgorithm(len_genes, genes, pop_size, mutation_rate, max_fit)
    fitness_max_history, fitness_mean_history, counter, time = ga_string.run(PopNQueens, NQueensFit, Selection,
                                                                             Reproduction, ref_individual=False)

    print(fitness_max_history, counter, time)


main()
