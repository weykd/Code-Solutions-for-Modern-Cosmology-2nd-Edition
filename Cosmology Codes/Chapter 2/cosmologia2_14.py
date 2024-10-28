# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import quad

# Define the function to integrate
def integrand(a, omega_m, omega_r, omega_lambda, H_0):
    return (a / H_0) * (1 / np.sqrt(omega_m * a + omega_r + omega_lambda * a**4))

# Define the parameters
omega_m = 0.3106       # Example value for matter density parameter
omega_r = 0      # Example value for radiation density parameter (can be very small)
omega_lambda = 0.6894  # Example value for dark energy density parameter
H_0 = 7.2532782 * 10**(-2)          # Example value for Hubble constant in 1/Gyr

# Perform the integration from a = 0 to a = 0.767
result, error = quad(integrand, 0, 0.767, args=(omega_m, omega_r, omega_lambda, H_0))

print("Numerical integration result:", result)
print("Estimated error:", error)