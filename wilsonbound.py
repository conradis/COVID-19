"""
Implementation of the Wilson Bound formula to improve sorting of positive/negative rated items
"""

# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import norm
import pandas as pd

# Default confidence level
CONFIDENCE = 0.95

def ci_lower_bound(pos, ntot, confidence = CONFIDENCE):
    if ntot == 0:
        return 0
    z = norm.ppf(1-(1-confidence)/2) #for confidence 95%, z = 1.96
    phat = 1.0*pos/ntot
    return (phat + z*z/(2*ntot) - z * np.sqrt((phat*(1-phat)+z*z/(4*ntot))/ntot))/(1+z*z/ntot)


if __name__ == '__main__':

    #test sample list: (num of positive rating, total number of ratings)
    test_sample = [(2,2), (0,2), (51,100), (30,100), (70,100), (50001,100000)]
    df = pd.DataFrame(columns=('N_positive', 'N_total', '%_positive', 'positive_WilsonBound'))
    
    #print the wilson bound for the test samples
    for i in range(len(test_sample)):
        (p,n) = test_sample[i]
        df.loc[i] = [p,n,100.0*p/n,ci_lower_bound(p,n)]

    print df.to_string()
   


    



    