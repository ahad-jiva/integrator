import random
import math
from functions import main_f

if __name__ == "__main__":
    lower_bound = float(input("Lower bound of integration: "))
    upper_bound = float(input("Upper bound of integration: "))

    subintervals = (upper_bound - lower_bound)/1000

    i_max = main_f(lower_bound)
    x = lower_bound
    for i in range(0, 1001):
        test = main_f(x)
        x += subintervals
        if test > i_max:
            i_max = test
        else:
            continue
    r_width = upper_bound - lower_bound
    r_height = math.ceil(i_max)
    r_area = r_width * r_height

    below = 0
    total = 0
    resolution = int(input("Number of points to sample: "))
    print("Computing...")
    for i in range(0, resolution):
        rand_x = random.uniform(lower_bound, upper_bound)
        rand_y = random.uniform(0, r_height)

        if rand_y <= main_f(rand_x):
            below += 1
        total += 1

    a_ratio = (below / total) * r_area
    print(f'Approximate area = {a_ratio}')



