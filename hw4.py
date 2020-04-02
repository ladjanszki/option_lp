import numpy as np
import csv
import os

import util


# Reproducible random numbers
np.random.seed(0)

# Prefix
path = 'results/hw4/'

if not os.path.exists(path):
    os.mkdir(path) 

reportLines = []
 
# Maximal number of children for three level tree
for idx1, n1 in enumerate((5, 10, 20)):
    for idx2, n2 in enumerate((5, 10, 20)):
        for idx3, n3 in enumerate((5, 10, 20)):

            res = util.measurement(path, taskId = 'hw4_' + str(idx1) + str(idx2) + str(idx3) + '_1', 
                  childrenPerLevel = (n1, n2, n3), 
                  initSecPrice = [1, 100, 100, 100], 
                  logNormalMean = 2, 
                  logNormalSigma = 1) 

            res.append(n1)
            res.append(n2)
            res.append(n3)
            reportLines.append(res)

            res = util.measurement(path, taskId = 'hw4_' + str(idx1) + str(idx2) + str(idx3) + '_2', 
                  childrenPerLevel = (n1, n2, n3), 
                  initSecPrice = [1, 100, 100, 100], 
                  logNormalMean = 0, 
                  logNormalSigma = 2) 
            res.append(n1)
            res.append(n2)
            res.append(n3)
            reportLines.append(res)

# csv report
with open(path + 'report.csv','w') as report:
    csvWriter = csv.writer(report)
    csvWriter.writerow(['Option price', 
                        'Wall time', 
                        'CPU Time', 
                        'Lognormal Mean', 
                        'Lognormal Sigma', 
                        'Files', 
                        'n1', 'n2', 'n3'])
    for row in reportLines:
        csvWriter.writerow(row)
 

 
