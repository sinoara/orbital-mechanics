# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring, missing-class-docstring
import unittest


import numpy as np


from orbitalmechanics.system import System
from orbitalmechanics.body import Body


class FunctionRunTest(unittest.TestCase):
    def test_grav_force1(self):
        body1 = Body(mass=1, initial_position=np.array([0, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
        body2 = Body(mass=1, initial_position=np.array([1, 0, 0]),
            initial_velocity=np.array([0, 0, 0]))
        
        bodies_list = [body1, body2]
        
        system = System(bodies_list, [])
        
        
        self.assertEqual(0, 1)
