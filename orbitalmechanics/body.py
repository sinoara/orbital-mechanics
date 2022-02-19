"""Body object
Contains information regarding the body object.
"""
from dataclasses import dataclass


import numpy as np
import numpy.typing as npt


@dataclass
class Body:
    """Holds body data

    Parameters
    ----------
    mass : float
        The body's mass
    initia_position : array
        (3,) array containing the body's initial position
    initia_position : array
        (3,) array containing the body's initial velocity
    """
    mass: float
    initial_position: npt.NDArray[np.float64]
    initial_velocity: npt.NDArray[np.float64]

    def __post_init__(self) -> None:
        self.current_position : npt.NDArray[np.float64] = self.initial_position
        self.current_velocity : npt.NDArray[np.float64] = self.initial_velocity
