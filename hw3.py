import numpy as np
import csv
import os

import util


# Reproducible random numbers
np.random.seed(0)

# Prefix
path = 'results/hw3/'

if not os.path.exists(path):
    os.mkdir(path) 

reportLines = []
 
# Maximal number of children for three level tree
#for n in (10, 20, 50, 100, 200):
for n in (5, 10, 20):
    res = util.measurement(path, taskId = 'hw3_' + str(n), childrenPerLevel = (n, n, n), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
    res.append(n)
    reportLines.append(res)

# csv report
with open(path + 'report.csv','w') as report:
    csvWriter = csv.writer(report)
    csvWriter.writerow(['Option price', 'Wall time', 'CPU Time', 'n branch'])
    for row in reportLines:
        csvWriter.writerow(row)
 

 
 
 
