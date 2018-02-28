import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep

import re

stringo = 'alpha/:be>?t|||'

print re.sub('[\\/:"*?<>|]+', '', stringo)