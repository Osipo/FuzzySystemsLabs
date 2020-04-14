import numpy as np
ipli = list([(a,b,c,d) for a in range(0,255)
            for b in range(0,255)
            for c in range(0,255)
            for d in range(0,255)])
np.random.random(ipli)
print(ipli)