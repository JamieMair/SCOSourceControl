from nearestneighbour import *
import numpy as np


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
        assert find_nearest_neighbour_from_point(point_cloud, point)==answer

def test_simple_math():
    assert 2+2==4