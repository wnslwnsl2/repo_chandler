from scipy.spatial.transform import Rotation
import numpy as np
import math

rt = Rotation.from_rotvec(np.pi / 2.0 / np.sqrt(3) * np.array([1, 1, 1]))
print(rt.as_matrix())
print(1 / 3 + 1 / np.sqrt(3))
print(1 / 3 - 1 / np.sqrt(3))
