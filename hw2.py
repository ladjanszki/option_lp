import numpy as np

import util


# Reproducible random numbers
np.random.seed(0)

# HW1
optionPrice = util.measurement(taskId = 'hw2_1', childrenPerLevel = (100, 100), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
print(optionPrice)
     
 
