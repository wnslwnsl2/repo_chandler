from scipy.spatial.transform import Rotation
import numpy as np
import math

r_12 = Rotation.from_matrix([[1, 0, 0], [0, 0.5, -math.sqrt(3) / 2],
                             [0, math.sqrt(3) / 2, 0.5]])
r_13 = Rotation.from_matrix([[0, 0, -1], [0, 1, 0], [1, 0, 0]])
r_23 = r_12.inv() * r_13
print(r_23.as_matrix())
