import unittest


import numpy as np


from orbitalmechanics.body import Body
from orbitalmechanics.geometry import distance


class DistanceTest(unittest.TestCase):
    def test_distance_1(self):
        body1 = Body(mass=1, initial_position=np.array([0, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
        body2 = Body(mass=1, initial_position=np.array([1, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
    
        self.assertEqual(distance(body1, body2), 1.0)


    def test_distance_2(self):
        body1 = Body(mass=1, initial_position=np.array([1, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
        body2 = Body(mass=1, initial_position=np.array([1, 2, 0]),
            initial_velocity=np.array([0, 0, 0]))
    
        self.assertEqual(distance(body1, body2), 2.0)


    def test_distance_3(self):
        body1 = Body(mass=1, initial_position=np.array([1, 2, 0]),
            initial_velocity=np.array([0, 0, 0]))
        body2 = Body(mass=1, initial_position=np.array([1, 2, 3]),
            initial_velocity=np.array([0, 0, 0]))
    
        self.assertEqual(distance(body1, body2), 3.0)


    def test_distance_4(self):
        body1 = Body(mass=1, initial_position=np.array([0, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
        body2 = Body(mass=1, initial_position=np.array([3, 4, 0]),
            initial_velocity=np.array([0, 0, 0]))
    
        self.assertEqual(distance(body1, body2), 5.0)


    def test_distance_5(self):
        body1 = Body(mass=1, initial_position=np.array([0, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
        body2 = Body(mass=1, initial_position=np.array([0, 5, 12]),
            initial_velocity=np.array([0, 0, 0]))
    
        self.assertEqual(distance(body1, body2), 13.0)
