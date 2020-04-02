import numpy as np
import csv
import os

import util


# Reproducible random numbers
np.random.seed(0)

# Prefix
path = 'results/hw2/'

if not os.path.exists(path):
    os.mkdir(path) 

reportLines = []
 

# 100 x 100 children
res = util.measurement(path, taskId = 'hw2_1', childrenPerLevel = (100, 100), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
reportLines.append(res)

# csv report
with open(path + 'report.csv','w') as report:
    csvWriter = csv.writer(report)
    csvWriter.writerow(['Option price', 'Wall time', 'CPU Time'])
    for row in reportLines:
        csvWriter.writerow(row)
 

 
 
