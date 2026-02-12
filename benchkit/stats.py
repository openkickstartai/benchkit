"""Statistics."""
import math
from typing import List, Tuple

def mean(v): 
    if not v or not isinstance(v, (list, tuple)):
        return 0.0
    return sum(v)/len(v)

def stdev(v):
    if not v or not isinstance(v, (list, tuple)) or len(v)<2: 
        return 0.0
    m = mean(v)
    return math.sqrt(sum((x-m)**2 for x in v)/(len(v)-1))

def ci(v, conf=0.95):
    if not v or not isinstance(v, (list, tuple)):
        return (0.0, 0.0)
    n = len(v)
    if n<2: 
        m=mean(v)
        return (m,m)
    m=mean(v)
    se=stdev(v)/math.sqrt(n)
    t = 1.96 if n>30 else 2.0+4.0/n
    return (m-t*se, m+t*se)

def significant(a, b, conf=0.95):
    if not a or not b or not isinstance(a, (list, tuple)) or not isinstance(b, (list, tuple)):
        return (False, 0.0)
    ca, cb = ci(a,conf), ci(b,conf)
    overlap = ca[1]>=cb[0] and cb[1]>=ca[0]
    mean_a = mean(a)
    diff = (mean(b)-mean_a)/mean_a*100 if mean_a != 0 else 0
    return (not overlap, diff)

def remove_outliers(v, f=1.5):
    if not v or not isinstance(v, (list, tuple)) or len(v)<4: 
        return v if v else []
    s = sorted(v)
    n = len(s)
    q1_idx = max(0, n//4 - 1) if n >= 4 else 0
    q3_idx = min(n-1, 3*n//4) if n >= 4 else n-1
    q1, q3 = s[q1_idx], s[q3_idx]
    iqr = q3 - q1
    return [x for x in v if q1-f*iqr <= x <= q3+f*iqr]
