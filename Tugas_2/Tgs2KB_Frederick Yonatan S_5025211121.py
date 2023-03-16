import random

# Mendefinisikan jarak antara dua kota
def distance(city1, city2):
    x_distance = abs(city1[0] - city2[0])
    y_distance = abs(city1[1] - city2[1])
    distance = (x_distance ** 2 + y_distance ** 2) ** 0.5
    return distance

# Menghitung total jarak rute
def total_distance(route, cities):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distance(cities[route[i]], cities[route[(i + 1) % len(route)]])
    return total_distance

# Membuat populasi awal dengan jumlah individu yang diinginkan
def create_population(num_individuals, city_list):
    population = []
    for i in range(num_individuals):
        individual = list(range(len(city_list)))
        random.shuffle(individual)
        population.append(individual)
    return population

# Seleksi orangtua dengan menggunakan turnamen
def selection_tournament(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    best = tournament[0]
    for individual in tournament:
        if total_distance(individual, city_list) < total_distance(best, city_list):
            best = individual
    return best

# Crossover dengan menggunakan metode order crossover (OX)
def crossover(parent1, parent2):
    child = [-1] * len(parent1)
    gene_a = random.randint(0, len(parent1) - 1)
    gene_b = random.randint(0, len(parent1) - 1)
    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)
    for i in range(start_gene, end_gene + 1):
        child[i] = parent1[i]
    for i in range(len(parent2)):
        if parent2[i] not in child:
            for j in range(len(child)):
                if child[j] == -1:
                    child[j] = parent2[i]
                    break
    return child

# Mutasi dengan menggunakan metode swap mutation
def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]
    return individual

# Implementasi algoritma genetika
def genetic_algorithm(city_list, population_size, num_generations, tournament_size, crossover_rate, mutation_rate):
    population = create_population(population_size, city_list)
    for i in range(num_generations):
        new_population = []
        for j in range(population_size):
            parent1 = selection_tournament(population, tournament_size)
            parent2 = selection_tournament(population, tournament_size)
            child = crossover(parent1, parent2)
            child = mutation(child, mutation_rate)
            new_population.append(child)
        population = new_population
        best_individual = population[0]
        for individual in population:
            if total_distance(individual, city_list) < total_distance(best_individual, city_list):
                best_individual = individual
        print("Generation:", i+1, "- Best Distance:", total_distance(best_individual, city_list), "- Best Route:", best_individual)
    return best_individual

# Input data kota
city_list = []
num_cities = int(input("Enter the number of cities: "))
for i in range(num_cities):
    city = (float(input("Enter the x coordinate of city " + str(i + 1) + ": ")), 
            float(input("Enter the y coordinate of city " + str(i + 1) + ": ")))
    city_list.append(city)

# Input parameter algoritma genetika
population_size = int(input("Enter the population size: "))
num_generations = int(input("Enter the number of generations: "))
tournament_size = int(input("Enter the tournament size: "))
crossover_rate = float(input("Enter the crossover rate: "))
mutation_rate = float(input("Enter the mutation rate: "))

# Menjalankan algoritma genetika dan mencetak hasil
best_route = genetic_algorithm(city_list, population_size, num_generations, tournament_size, crossover_rate, mutation_rate)
print("Best Distance:", total_distance(best_route, city_list))
print("Best Route:", best_route)

