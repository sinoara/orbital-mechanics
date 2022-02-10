# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring, missing-class-docstring
import unittest


import numpy as np

from scipy.constants import gravitational_constant as g_const


from orbitalmechanics.body import Body
from orbitalmechanics.physics import gravity_force


class DistanceTest(unittest.TestCase):
    def test_grav_force1(self):
        body1 = Body(mass=1, initial_position=np.array([0, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
        body2 = Body(mass=1, initial_position=np.array([1, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
        self.assertEqual(gravity_force(body1, body2), g_const)


    def test_grav_force2(self):
        body1 = Body(mass=3, initial_position=np.array([1, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
        body2 = Body(mass=1, initial_position=np.array([1, 2, 0]),
            initial_velocity=np.array([0, 0, 0]))
        self.assertEqual(gravity_force(body1, body2), g_const*3/4)

    def test_grav_force3(self):
        body1 = Body(mass=1, initial_position=np.array([0, 1, 0]),
            initial_velocity=np.array([0, 0, 0]))
        body2 = Body(mass=5, initial_position=np.array([3, 1, 4]),
            initial_velocity=np.array([0, 0, 0]))
        self.assertEqual(gravity_force(body1, body2), g_const)
