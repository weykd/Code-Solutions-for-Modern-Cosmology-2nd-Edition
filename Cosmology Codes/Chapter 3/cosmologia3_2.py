import sympy as sp
from einsteinpy.symbolic import *
from einsteinpy.geodesic import Geodesic, Timelike, Nulllike
import numpy as np
sp.init_printing()

# Define the symbols
r = sp.symbols('r')
syms = sp.symbols('t theta phi')

# Define the metric for 3D spherical coordinates
metric = [[0 for i in range(3)] for i in range(3)]
metric[0][0] = -1  # g_tt
metric[1][1] = r**2  # g_rr
metric[2][2] = (r**2) * (sp.sin(syms[1])**2)  # g_theta_theta

# Creating the metric object
m_obj = MetricTensor(metric, syms)
m_obj.tensor()

# Calculate the Christoffel symbols
ch = ChristoffelSymbols.from_metric(m_obj)

# Print the Christoffel symbols
print('------------------------------------------------')
print('Letra a)')
print('------------------------------------------------')
print('Componentes Tempo')
print('Componente (t,t,t):', ch.tensor()[0,0,0])
print('Componente (t,theta,t):', ch.tensor()[0,1,0])
print('Componente (t,phi,t):', ch.tensor()[0,2,0])
print('Componente (t,theta,theta):', ch.tensor()[0,1,1])
print('Componente (t,phi,phi):', ch.tensor()[0,2,2])
print('Componente (t,phi,theta):', ch.tensor()[0,2,1])
print('Componentes Theta')
print('Componente (theta,t,t):', ch.tensor()[1,0,0])
print('Componente (theta,theta,t):', ch.tensor()[1,1,0])
print('Componente (theta,phi,t):', ch.tensor()[1,2,0])
print('Componente (theta,theta,theta):', ch.tensor()[1,1,1])
print('Componente (theta,phi,phi):', ch.tensor()[1,2,2])
print('Componente (theta,phi,theta):', ch.tensor()[1,2,1])
print('Componentes Phi')
print('Componente (phi,t,t):', ch.tensor()[2,0,0])
print('Componente (phi,theta,t):', ch.tensor()[2,1,0])
print('Componente (phi,phi,t):', ch.tensor()[2,2,0])
print('Componente (phi,theta,theta):', ch.tensor()[2,1,1])
print('Componente (phi,phi,phi):', ch.tensor()[2,2,2])
print('Componente (phi,phi,theta):', ch.tensor()[2,2,1])

# Letra b --------------------------------------------------------------------------
print('------------------------------------------------')
print('Letra b)')
print('------------------------------------------------')
print('Equação de Movimento 1:')
print('d^2(theta)/dt^2', ch.tensor()[1,2,2], '[d(phi)/dt]^2 = 0')

print('Equação de Movimento 2:')
print('d^2(phi)/dt^2 +2*', ch.tensor()[2,2,1], '[d (theta)/dt]^2 = 0')

print('------------------------------------------------')
print('Letra c)')
print('------------------------------------------------')
# Calculate the Ricci tensor and scalar
Ric = RicciTensor.from_metric(m_obj)
R = RicciScalar.from_riccitensor(Ric)
print('Escalar de Ricci:', R.simplify())
