import numpy as np
freq = np.zeros(256)
freq[ord('a')] += 1
print(freq[ord('a')])
