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

branches = (5, 10, 20, 25, 30, 50)

# Maximal number of children for three level tree
with open(path + 'report.csv','w') as report:
    csvWriter = csv.writer(report)
    csvWriter.writerow(['Option price', 
                        'Wall time', 
                        'CPU Time', 
                        'Lognormal Mean', 
                        'Lognormal Sigma', 
                        'Files', 
                        'n1', 'n2', 'n3'])
 
    # Loops for lognormal(2,1)
    for idx1, n1 in enumerate(branches):
        for idx2, n2 in enumerate(branches):
            for idx3, n3 in enumerate(branches):
    
                res = util.measurement(path, taskId = 'hw4_' + str(idx1) + str(idx2) + str(idx3) + '_1', 
                      childrenPerLevel = (n1, n2, n3), 
                      initSecPrice = [1, 100, 100, 100], 
                      logNormalMean = 2, 
                      logNormalSigma = 1) 
    
                res.append(n1)
                res.append(n2)
                res.append(n3)
                #reportLines.append(res)
                csvWriter.writerow(res)
                report.flush()
    
    
    # Loops for lognormal(1,2)
    for idx1, n1 in enumerate(branches):
        for idx2, n2 in enumerate(branches):
            for idx3, n3 in enumerate(branches):
                res = util.measurement(path, taskId = 'hw4_' + str(idx1) + str(idx2) + str(idx3) + '_2', 
                      childrenPerLevel = (n1, n2, n3), 
                      initSecPrice = [1, 100, 100, 100], 
                      logNormalMean = 1, 
                      logNormalSigma = 2) 
                res.append(n1)
                res.append(n2)
                res.append(n3)
                #reportLines.append(res)
                csvWriter.writerow(res)
                report.flush()


 
