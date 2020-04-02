import numpy as np

import util


# Reproducible random numbers
np.random.seed(0)

# HW1
optionPrice = util.measurement(taskId = 'hw1_1', childrenPerLevel = (100, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
print(optionPrice)
     
# HW2
optionPrice = util.measurement(taskId = 'hw1_2', childrenPerLevel = (1000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
print(optionPrice)

# HW3
optionPrice = util.measurement(taskId = 'hw1_3', childrenPerLevel = (10000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
print(optionPrice)

# HW4
optionPrice = util.measurement(taskId = 'hw1_4', childrenPerLevel = (100000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
print(optionPrice)

 
 
 
