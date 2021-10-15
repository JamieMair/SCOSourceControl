from nearestneighbour import *
import numpy as np
from time import time


def test_point_cloud_generation():
    # Test size of array
    n = 256
    d = 2
    cloud = generate_point_cloud(n, d=d)
    assert np.size(cloud) == n*d
    assert np.shape(cloud) == (n, d)

    # Check that the same cloud is generated on each call
    second_cloud = generate_point_cloud(n, d=d)
    assert np.all(cloud == second_cloud) 
    
    # Check that the same cloud is generated on each call (again)
    third_cloud = generate_point_cloud(n, d=d)
    assert np.all(cloud == third_cloud) 
    assert np.all(second_cloud == third_cloud) 


def test_nearest_neighbour():
    point_cloud = generate_point_cloud(256, d=2, seed=1234)

    test_points = [5, 10, 20, 100, 150, 250]
    test_answers = [24, 112, 140, 4, 231, 143]
    
    for (point, answer) in zip(test_points, test_answers):
        calculated_nn = find_nearest_neighbour_from_point(point_cloud, point)
        assert calculated_nn==answer, f"The nearest neighbour of point {point} was expected to be {answer}, but was calculated to be {calculated_nn}."


def test_all_nearest_neighbours():
    n = 256
    point_cloud = generate_point_cloud(256, d=3, seed=1234)

    nearest_neighbour_indices = find_all_nearest_neighbours(point_cloud)
    for i in range(n):
        nearest_neighbour_idx = find_nearest_neighbour_from_point(point_cloud, i)
        assert nearest_neighbour_idx == nearest_neighbour_indices[i], f"Failed on the index {i}. Actual: {nearest_neighbour_idx}, Calculated: {nearest_neighbour_indices[i]}"

""" Uncomment this code for the speed test.
def test_all_nearest_neighbours_speed():
    n = 8096
    repeats = 3
    point_cloud = generate_point_cloud(n, d=3, seed=1234)

    times = []
    for r in range(repeats):
        start_t = time()
        nearest_neighbour_indices = find_all_nearest_neighbours(point_cloud)
        end_t = time()
        if nearest_neighbour_indices is None:
            raise Exception("The find_all_nearest_neighbours function is not implemented properly, returned a None object.")
        times.append(end_t-start_t)

    min_time = np.min(times)
    print(f"Minimum NN calculation time for n={n} is {min_time*1000:.3f}ms.\n")
    threshold = 2.5
    assert min_time < threshold, f"NN calculation for n={n} must be below {threshold*1000:.1f}ms"
"""