# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define constants
H_0 = 2.3e-18  # Hubble constant in 1/s
K = 0          # Constant term in the distance modulus equation
c = 9.7e-15    # Speed of light in Mpc/s

# Density parameters
Omega_m = 0.3
Omega_Lambda = 0.7

# Define the integrand for the integral
def integrand(z_prime):
    return c / np.sqrt(Omega_m * (1 + z_prime)**3 + Omega_Lambda)

# Define the function to compute x(z) numerically
def x(z):
    integral_result, _ = quad(integrand, 0, z)  # Perform the integral from 0 to z
    return integral_result / H_0  # Return x(z)

# Define the function for angular diameter distance d_A(z)
def d_A(z):
    x_z = x(z)  # Compute x(z) for the current z
    final = x_z / (1 + z)  # Compute the final term
    return final / H_0

# Define the function for distance modulus (m-M)
def distance_modulus(d_A_z, z):
    d_L_z = d_A_z * (1 + z)**2  # Luminosity distance
    d_L_z = np.where(d_L_z > 0, d_L_z, 1e-10)  # Avoid divide-by-zero
    return 5 * np.log10(d_L_z / (10 * 1e-6)) + K  # Converting from Mpc to parsecs

# Define redshift range (z)
z_values = np.linspace(0.01, 2, 500)  # From z=0.01 to z=2

# Compute d_A for each z individually
d_A_values = np.array([d_A(z) for z in z_values])

# Compute the luminosity distance: d_L(z) = d_A(z) * (1+z)^2
d_L_values = d_A_values * ((1 + z_values) ** 2)

# Compute the distance modulus (m-M)
modulus_values = distance_modulus(d_A_values, z_values)

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 20))

# Plot the angular diameter distance on the first graph
ax1.plot(z_values, d_A_values, label=r'$d_A(z)$', color='blue')
ax1.set_xlabel('Redshift (z)')
ax1.set_ylabel(r'$d_A(z)$ (Mpc)')
ax1.set_title('Angular Diameter Distance $d_A(z)$')
ax1.grid(True)
ax1.legend()

# Plot the luminosity distance on the second graph
ax2.plot(z_values, d_L_values, label=r'$d_L(z)$', color='green')
ax2.set_xlabel('Redshift (z)')
ax2.set_ylabel(r'$d_L(z)$ (Mpc)')
ax2.set_title('Luminosity Distance $d_L(z)$')
ax2.grid(True)
ax2.legend()

# Plot the distance modulus on the third graph with logarithmic x-axis
ax3.plot(z_values, modulus_values, label=r'$(m - M)$', color='red')
ax3.set_xscale('log')  # Set x-axis to logarithmic scale
ax3.set_xlabel('Redshift (z)')
ax3.set_ylabel('Distance Modulus (m-M)')
ax3.set_title('Distance Modulus $(m - M)$')
ax3.grid(True)
ax3.legend()

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()