import sympy as sp
from einsteinpy.symbolic import *
sp.init_printing()

syms = sp.symbols('r theta')
# define the metric for 3d spherical coordinates
metric = [[0 for i in range(2)] for i in range(2)]
metric[0][0] = 1
metric[1][1] = syms[0]**2
# creating metric object
m_obj = MetricTensor(metric, syms)
m_obj.tensor()

ch = ChristoffelSymbols.from_metric(m_obj)
ch.tensor()

print(ch.tensor()[0,1,1])

Ric = RicciTensor.from_metric(m_obj)
Ric.tensor()

R = RicciScalar.from_riccitensor(Ric)
R.simplify()
R.expr

print(R)