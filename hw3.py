import numpy as np

import util


# Reproducible random numbers
np.random.seed(0)

for n in (10, 20, 50, 100, 200):
    measRes = util.measurement(taskId = 'hw3_1', childrenPerLevel = (n, n, n), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
    print(measRes)
 
