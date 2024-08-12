from scipy.spatial.transform import Rotation
import numpy as np
import math

rt = Rotation.from_euler('zyx', np.pi * np.array([0.25, 0, 0.5]))
print(rt.as_matrix())
