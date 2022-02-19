"""
System object, containing all bodies in the simulation
"""
from typing import List, Dict, Callable
from dataclasses import dataclass


import numpy as np
import numpy.typing as npt


from .body import Body


ForceDict = Dict[Body, npt.NDArray[np.float64]]
ForceFunction = Callable[[List[Body]], ForceDict]

@dataclass
class System:
    """ Contains all the bodies in the simulation
    """
    bodies: List[Body]
    force_functions: List[ForceFunction]

    def run_force_functions(self) -> ForceDict:
        """Runs all force functions.

        Parameters
        ----------
        None

        Returns
        -------
        forces
            Dictionary with Body as keys and ndarray[float] as values
        """


def two_by_two_runner(function: Callable[[Body, Body], npt.NDArray[np.float64]],
    bodies: List[Body]) -> Dict[Body, np.float64]:
    """Runs function on all combinations of length 2 from bodies.

    Parameters
    ----------
    function
        Callable that takes two Body objects and returns a ndarray[float].
    bodies
        The second parameter.

    Returns
    -------
    forces
        Dictionary with Body as keys and ndarray[float] as values
    """
