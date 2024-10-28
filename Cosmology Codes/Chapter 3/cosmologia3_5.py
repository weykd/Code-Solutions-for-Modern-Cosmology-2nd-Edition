import sympy as sp
from einsteinpy.symbolic import *
import numpy as np
sp.init_printing()

# Define the time variable and scale factor
t = sp.symbols('t')  # Time coordinate
a = sp.Function('a')(t)  # Scale factor as a function of time
dot_a = sp.diff(a, t)  # Define the derivative of a as dot_a
r, theta, phi = sp.symbols('r theta phi')  # Spatial coordinates
o = sp.symbols('{omega_k*H0^2}')

# Define the FLRW metric
# Here, we assume k = 0 for simplicity (flat universe)
metric = [
    [-1, 0, 0, 0],                              # g_{tt} = -1
    [0, a**2 / (1 + o * r**2), 0, 0],           # g_{rr} = a(t)^2/(1-kr^2)
    [0, 0, a**2 * r**2, 0],                     # g_{\theta \theta} = a(t)^2 * r^2
    [0, 0, 0, a**2 * r**2 * sp.sin(theta)**2]   # g_{\phi \phi} = a(t)^2 * r^2 * sin^2(theta)
]

# Create the MetricTensor object
flrw_metric = MetricTensor(metric, [t, r, theta, phi])
flrw_metric.tensor()  # Print the metric tensor

ch=ChristoffelSymbols.from_metric(flrw_metric)
ch.tensor()
ch.simplify()
print('-----------------------------------------------------------------------------------')
print('Letra a)')
print('-----------------------------------------------------------------------------------')
print('-> Componentes (i, 0, j):')
print('(1, 0, 1):', ch[1,0,1])
print('(1, 0, 2):', ch[1,0,2])
print('(1, 0, 3):', ch[1,0,3])
print('(2, 0, 1):', ch[2,0,1])
print('(2, 0, 2):', ch[2,0,2])
print('(2, 0, 3):', ch[2,0,3])
print('(3, 0, 1):', ch[3,0,1])
print('(3, 0, 2):', ch[3,0,2])
print('(3, 0, 3):', ch[3,0,3])
print('Logo os componentes não nulos são o Parâmetro de Hubble H apenas nas componentes que tem índice i=j, e podemos escrever isso como sendo H*delta de kronecker (i,j).')
print('')
print('-> Componentes (0, i, j):')
print('(0, 1, 1):', ch[0,1,1])
print('(0, 1, 2):', ch[0,1,2])
print('(0, 1, 3):', ch[0,1,3])
print('(0, 2, 3):', ch[0,2,3])
print('(0, 2, 2):', ch[0,2,2])
print('(0, 3, 3):', ch[0,3,3])
print('Vemos que as componentes com i=j são as únicas não nulas, e nessas, os fatores que multiplicam o Parâmetro de Hubble são justamente os fatores da métrica. Isso nos permite escrever estes componentes da maneira do enunciado.')
print('')
print('-> Componentes (i, j, k): Vem diretamente da aplicação da fórmula para os Símbolos de Christoffel.')
print('-----------------------------------------------------------------------------------')
print('Letra b)')
print('-----------------------------------------------------------------------------------')

Ric = RicciTensor.from_metric(flrw_metric)
Ric.tensor()
Ric.simplify()
print('Componentes R_00:', Ric[0,0])
print('')
print('Componentes R_ij:')
print('(1,1):', Ric[1,1])
print('(1,2):', Ric[1,2])
print('(1,3):', Ric[1,3])
print('(2,2):', Ric[2,2])
print('(2,3):', Ric[2,3])
print('(3,3):', Ric[3,3])

print('Por esses valores, podemos identificar a relação descrita no enunciado')
print('-----------------------------------------------------------------------------------')
print('Letra c)')
print('-----------------------------------------------------------------------------------')

#Ricci Scalar
R = RicciScalar.from_riccitensor(Ric)
R.simplify()
# Einstein Tensor
einst = EinsteinTensor.from_metric(flrw_metric)
einst.tensor()

print('\nEscalar de Ricci:', R)
print('Componente G_00 do Tensor de Einstein:', einst[0,0],'= 8πG*rho')