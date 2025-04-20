import numpy as np

n = 100

for i in range(n):
    scale = round(np.random.uniform(0.1, 2.0), 2)
    x = round(np.random.uniform(-10, 10), 2)
    y = round(np.random.uniform(-10, 10), 2)
    z = 5

    text = "Rock { translation " + str(x) + " " + str(y) + " " + \
        str(z) + " scale " + str(scale) + " physics Physics {} }"
    print(text)
