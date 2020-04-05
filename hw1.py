import numpy as np
import csv
import os

import util


# Reproducible random numbers
np.random.seed(0)

# Prefix
path = 'results/hw1/'

if not os.path.exists(path):
    os.mkdir(path) 

reportLines = []


# 100 children
res = util.measurement(path, taskId = 'hw1_1', childrenPerLevel = (100, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
reportLines.append(res)
     
# 1000 children
res = util.measurement(path, taskId = 'hw1_2', childrenPerLevel = (1000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
reportLines.append(res)

# 10'000 children
res = util.measurement(path, taskId = 'hw1_3', childrenPerLevel = (10000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
reportLines.append(res)

# 100'000 children
res = util.measurement(path, taskId = 'hw1_4', childrenPerLevel = (100000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
reportLines.append(res)

# 100 children
res = util.measurement(path, taskId = 'hw1_5', childrenPerLevel = (100, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 0, logNormalSigma = 2) 
reportLines.append(res)
     
# 1000 children
res = util.measurement(path, taskId = 'hw1_6', childrenPerLevel = (1000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 0, logNormalSigma = 2) 
reportLines.append(res)

# 10'000 children
res = util.measurement(path, taskId = 'hw1_7', childrenPerLevel = (10000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 0, logNormalSigma = 2) 
reportLines.append(res)

# 100'000 children
res = util.measurement(path, taskId = 'hw1_8', childrenPerLevel = (100000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 0, logNormalSigma = 2) 
reportLines.append(res)
 

# csv report
with open(path + 'report.csv','w') as report:
    csvWriter = csv.writer(report)
    csvWriter.writerow(['Option price', 'Wall time', 'CPU Time', 'Lognormal Mean', 'Lognormal Sigma', 'Files'])
    for row in reportLines:
        csvWriter.writerow(row)
 

 
 
 
