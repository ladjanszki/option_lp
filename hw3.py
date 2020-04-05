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

# csv report
with open(path + 'report.csv','w') as report:
    csvWriter = csv.writer(report)
    csvWriter.writerow(['Option price', 'Wall time', 'CPU Time', 'Lognormal Mean', 'Lognormal Sigma', 'Files', 'n branch'])

    # Maximal number of children for three level tree
    for idx, n in enumerate((5, 10, 20, 30, 50, 70, 100, 120, 135)):
        res = util.measurement(path, taskId = 'hw3_' + str(idx) + '_1', childrenPerLevel = (n, n, n), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
        res.append(n)
        csvWriter.writerow(res)
        report.flush()
 
