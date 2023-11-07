


from generation_algorithms.wilson_algo import generate_wilson
from generation_algorithms.aldous_broder import generate_aldous_broder
from generation_algorithms.recursive import generate_recursive
from utilities import display_maze

import datetime
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline




def benchmark(func, num_tests, size):
	records = []

	for x in range(num_tests):

		start = datetime.datetime.now()

		func((size,size), verbose=False)

		end = datetime.datetime.now()
		delta = end - start
		time = round(delta.total_seconds(), 4)
		records.append(time)

		print(f"{size}x{size} mazes: {x}/{num_tests: <5}", end='\r')
	
	return records



# Conducts tests to benchmark the speed of each maze generation algorithm

# inputs
num_tests = 10
maze_sizes = np.array([10, 20, 30, 40, 50, 75, 100])
# maze_sizes = np.array([10, 20, 30, 40])


# test wilson
wilson_timings = []
for size in maze_sizes:
	current_size_timeings = benchmark(generate_wilson, num_tests, size)

	current_size_timeings.insert(0, round(statistics.mean(current_size_timeings), 3))
	# current_size_timeings.insert(0, str(size))
	wilson_timings.append(current_size_timeings)


for i, size_times in enumerate(wilson_timings):
	print(f"Wilson-{maze_sizes[i]} avg: {size_times[0]}") 



wilson_timings_array = np.array(wilson_timings)
wilson_averages_list = wilson_timings_array[:,0]

# plot wilson
# smooth line look good
xnew = np.linspace(maze_sizes.min(), maze_sizes.max(), 300)
spl = make_interp_spline(maze_sizes, wilson_averages_list, k=3)
average_smooth = spl(xnew)

plt.plot(xnew, average_smooth, color="blue", label="Wilson")
plt.scatter(maze_sizes, wilson_averages_list, color='blue', marker='o')





# test aldous-broder
aldous_timings = []
for size in maze_sizes:
	current_size_timeings = benchmark(generate_aldous_broder, num_tests, size)

	current_size_timeings.insert(0, round(statistics.mean(current_size_timeings), 3))
	# current_size_timeings.insert(0, str(size))
	aldous_timings.append(current_size_timeings)


for i, size_times in enumerate(aldous_timings):
	print(f"Aldous-{maze_sizes[i]} avg: {size_times[0]}") 



aldous_timings_array = np.array(aldous_timings)
aldous_averages_list = aldous_timings_array[:,0]

# plot aldous-broder
# smooth line look good
xnew = np.linspace(maze_sizes.min(), maze_sizes.max(), 300)
spl = make_interp_spline(maze_sizes, aldous_averages_list, k=3)
average_smooth = spl(xnew)

plt.plot(xnew, average_smooth, color="red", label="Aldous-Broder")
plt.scatter(maze_sizes, aldous_averages_list, color='red', marker='o')





plt.xlabel("Maze Size²")
plt.ylabel("Averge Seconds Taken")

plt.title(f"Average Algorithm Timings {num_tests}x")
plt.legend()
plt.savefig('benchmarks/average_' + str(num_tests) + 'x_benchmark.png')
plt.show()




# %%
