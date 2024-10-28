import sympy as sp
from einsteinpy.symbolic import *
from einsteinpy.geodesic import Geodesic, Timelike, Nulllike
import numpy as np
sp.init_printing()

# Define the time variable and scale factor
t = sp.symbols('t')  # Time coordinate
a = sp.Function('a')(t)  # Scale factor as a function of time
dot_a = sp.diff(a, t)  # Define the derivative of a as dot_a
r, theta, phi = sp.symbols('r theta phi')  # Spatial coordinates

# Define the FLRW metric
# Here, we assume k = 0 for simplicity (flat universe)
metric = [
    [-1, 0, 0, 0],  # g_{tt} = -1
    [0, a**2 / (1 - 0 * r**2), 0, 0],  # g_{rr} = a(t)^2/(1-kr^2)
    [0, 0, a**2 * r**2, 0],  # g_{\theta \theta} = a(t)^2 * r^2
    [0, 0, 0, a**2 * r**2 * sp.sin(theta)**2]  # g_{\phi \phi} = a(t)^2 * r^2 * sin^2(theta)
]

# Create the MetricTensor object
flrw_metric = MetricTensor(metric, [t, r, theta, phi])
flrw_metric.tensor()  # Print the metric tensor

# Optional: You can calculate Christoffel symbols or other properties
ch = ChristoffelSymbols.from_metric(flrw_metric)
ch.tensor()
print('-----------------------------------------------------------------------------------------------')
print("\nLetra a):")
print('-----------------------------------------------------------------------------------------------')
print('Índice Covariante 0:',ch[0])
print('')
print('Índice Covariante 1:',ch[1])
print('')
print('Índice Covariante 2:',ch[2])
print('')
print('Índice Covariante 3:',ch[3])
# Calculate the Ricci tensor and scalar
Ric = RicciTensor.from_metric(flrw_metric)
Ric.tensor()
print('-----------------------------------------------------------------------------------------------')
print('Letra b)')
print('-----------------------------------------------------------------------------------------------')
print('Índices Espaciais do Tensor de Ricci com i=1,2,3:')
print('Componente i=1 do Tensor de Ricci:', Ric[1])
print('Componente i=2 do Tensor de Ricci:', Ric[2])
print('Componente i=3 do Tensor de Ricci:', Ric[3])
print('')
print('Índices Espaciais do Tensor de Ricci com i=1,2,3 e j=0:')
print('Componente i=1 j=0 do Tensor de Ricci:', Ric[1,0])
print('Componente i=2 j=0 do Tensor de Ricci:', Ric[2,0])
print('Componente i=3 j=0 do Tensor de Ricci:', Ric[3,0])
print('')

R = RicciScalar.from_riccitensor(Ric)