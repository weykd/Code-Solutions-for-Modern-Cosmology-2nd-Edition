import sympy as sp
from einsteinpy.symbolic import *
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
    [-1, 0, 0, 0],                              # g_{tt} = -1
    [0, a**2 / (1 - 0 * r**2), 0, 0],           # g_{rr} = a(t)^2/(1-kr^2)
    [0, 0, a**2 * r**2, 0],                     # g_{\theta \theta} = a(t)^2 * r^2
    [0, 0, 0, a**2 * r**2 * sp.sin(theta)**2]   # g_{\phi \phi} = a(t)^2 * r^2 * sin^2(theta)
]

# Create the MetricTensor object
flrw_metric = MetricTensor(metric, [t, r, theta, phi])
flrw_metric.tensor()  # Print the metric tensor

# Einstein Tensor
einst = EinsteinTensor.from_metric(flrw_metric)
einst.tensor()

print('A componente espaço-espaço (g_rr) do Tensor de Einstein é:', einst.tensor()[1,1],' enquanto a componente T_rr do Tensor de Energia Momento é T_rr = P. Logo teremos',einst.tensor()[1,1],'=8πGP')
print('')
print('Contudo, temos também que a componente G_tt é: 3*Derivative(a(t), t)**2)/a(t)**2 e isso é igual a componente T_tt = rho. Portanto, temos que Derivative(a(t), t)**2)/a(t)**2 = 8πG*rho')
print('')
print('Manipulando isso, encontramos que [Derivative(a(t), t)/a(t)]**2 = (8πG/3)*rho, e então substituindo isso na relação anterior obtemos a Segunda Equação de Friedmann.')