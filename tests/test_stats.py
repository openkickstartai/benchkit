"""Tests."""
from benchkit.stats import mean, stdev, ci, significant, remove_outliers

def test_mean(): assert mean([1,2,3,4,5])==3.0
def test_stdev(): assert stdev([1,1,1])==0.0; assert stdev([1,2,3])>0
def test_ci():
    lo,hi = ci([10.0]*100); assert lo==hi==10.0
    lo,hi = ci(list(range(100))); assert lo < mean(list(range(100))) < hi
def test_sig():
    a=[10+i*0.01 for i in range(50)]; b=[20+i*0.01 for i in range(50)]
    s,d = significant(a,b); assert s; assert d>50
def test_not_sig():
    a=[10+i*0.001 for i in range(50)]; b=[10+i*0.001 for i in range(50)]
    s,d = significant(a,b); assert not s
def test_outliers():
    v=[10,10,10,10,10,10,100]; c=remove_outliers(v); assert 100 not in c
