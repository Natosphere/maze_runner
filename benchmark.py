
from generation_algorithms.wilson_algo import generate_wilson
from generation_algorithms.aldous_broder import generate_aldous_broder
from generation_algorithms.recursive import generate_recursive
from utilities import display_maze

import datetime
import statistics




def benchmark(func, num_tests, size):
	records = []

	for x in range(num_tests):

		start = datetime.datetime.now()

		func(size, verbose=False)

		end = datetime.datetime.now()
		delta = end - start
		time = round(delta.total_seconds(), 4)
		records.append(time)

		print(f"{size} mazes: {x}/{num_tests: <5}", end='\r')
	
	return records



# Conducts tests to benchmark the speed of each maze generation algorithm

# inputs
num_tests = 20
maze_sizes = [(10,10), (20,20), (30,30), (40,40), (50,50), (75,75), (100,100)]
maze_sizes = [(10,10), (20,20), (30,30), (40,40)]





wilson_timings = []
for size in maze_sizes:
	current_size_timeings = benchmark(generate_aldous_broder, num_tests, size)

	current_size_timeings.insert(0, statistics.mean(current_size_timeings))
	current_size_timeings.insert(0, str(size))
	wilson_timings.append(current_size_timeings)


for size_times in wilson_timings:
	print(f"Wilson-{size_times[0]} avg: {size_times[1]}") 







