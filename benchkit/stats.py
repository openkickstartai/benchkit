"""Statistics."""
import math
from typing import List, Tuple

def mean(v): return sum(v)/len(v) if v else 0.0

def stdev(v):
    if len(v)<2: return 0.0
    m = mean(v); return math.sqrt(sum((x-m)**2 for x in v)/(len(v)-1))

def ci(v, conf=0.95):
    n = len(v)
    if n<2: m=mean(v); return (m,m)
    m=mean(v); se=stdev(v)/math.sqrt(n)
    t = 1.96 if n>30 else 2.0+4.0/n
    return (m-t*se, m+t*se)

def significant(a, b, conf=0.95):
    ca, cb = ci(a,conf), ci(b,conf)
    overlap = ca[1]>=cb[0] and cb[1]>=ca[0]
    diff = (mean(b)-mean(a))/mean(a)*100 if mean(a) else 0
    return (not overlap, diff)

def remove_outliers(v, f=1.5):
    if len(v)<4: return v
    s = sorted(v); q1,q3 = s[len(s)//4], s[3*len(s)//4]; iqr=q3-q1
    return [x for x in v if q1-f*iqr <= x <= q3+f*iqr]
