# ctes.py

# ------------------------------
# Cosmological Parameters (Planck 2018)
# ------------------------------

# Baryon density parameter
Omega_b_h2 = 0.022447  # ±0.00027
Omega_b_h2_upper = 0.022717
Omega_b_h2_lower = 0.022177

# CDM density parameter
Omega_c_h2 = 0.11928  # ±0.0018
Omega_c_h2_upper = 0.12108
Omega_c_h2_lower = 0.11748

# Optical depth due to reionization
tau_rei = 0.0568  # ±0.014
tau_rei_upper = 0.0708
tau_rei_lower = 0.0428

# Hubble parameter
h = 0.6770  # ±0.0081
h_upper = 0.6851
h_lower = 0.6689

# Scalar spectral index
n_s = 0.96682  # +0.0076/-0.0073
n_s_upper = 0.97442
n_s_lower = 0.95952

# Scalar power spectrum amplitude
ln_1010_A_s = 3.0480  # ±0.028
ln_1010_A_s_upper = 3.0760
ln_1010_A_s_lower = 3.0200

# Cosmological constant parameter
Omega_Lambda = 0.6894  # ±0.011
Omega_Lambda_upper = 0.7004
Omega_Lambda_lower = 0.6784

# Matter density parameter
Omega_m = 0.3106  # ±0.011
Omega_m_upper = 0.3216
Omega_m_lower = 0.2996

# Matter power spectrum normalization
sigma_8 = 0.8110  # ±0.012
sigma_8_upper = 0.8230
sigma_8_lower = 0.7990

# Age of the universe
t_0 = 13.784  # Gyr, +0.040/-0.037
t_0_upper = 13.824  # Gyr
t_0_lower = 13.747  # Gyr

# ------------------------------
# B.1 Physical Constants
# ------------------------------

# Basics
pi = 3.141592653589793

# Speed of light
c = 2.99792458e10  # cm/s

# Reduced Planck's constant
hbar = 6.58211889e-16  # eV s
hbar_alt1 = 1.973269602e-5  # eV cm/c

# Newton's constant
G = 6.673e-8  # cm^3 g^-1 s^-2

# Planck mass
m_pl = 1.221e19  # GeV/c^2
m_pl_alt1 = 1.094e-38  # M☉

# Boltzmann constant
k_B = 8.617342e-5  # eV/K
k_B_alt1 = 1.380649e-23  # J/K

# Fine structure constant
alpha = 1 / 137.03599976

# Electron mass
m_e = 0.510998902  # MeV/c^2
m_e_alt1 = 9.1093837e-28  # g

# Ground-state energy of hydrogen (Rydberg's constant)
epsilon_0 = 13.60569172  # eV

# Thomson cross-section
sigma_T = 0.665245854e-24  # cm^2

# Neutron mass
m_n = 939.565330  # MeV/c^2
m_n_alt1 = 1.67492749804e-24  # g

# Proton mass
m_p = 938.271998  # MeV/c^2
m_p_alt1 = 1.67262158e-24  # g

# Neutron–proton mass difference
Q = 1.2933  # MeV/c^2

# Neutron lifetime
tau_n = 885.7  # s

# Fermi constant
G_F = 1.16639e-5  # GeV^-2 (ℏc)^3

# ------------------------------
# B.2 Astrophysical Constants
# ------------------------------

# Hubble constant
H0 = 100*h  # h km s^-1 Mpc^-1
H0_alt1 = 2.1331e-42 * h # GeV/ħ
H0_alt2 = 1.023e-10 * h # yr^-1

# Solar mass
M_sun = 1.989e33  # g
M_sun_alt1 = 1.116e57  # GeV/c^2

# Parsec
pc = 3.0856e18  # cm

# Critical density
rho_crit = 1.879e-29 * h**2  # g cm^-3
rho_crit_alt1 = 2.775e11 * h**2  # M☉ Mpc^-3
rho_crit_alt2 = 8.098e-11 * h**2  # eV^4/(ℏc)^3
rho_crit_alt3 = 1.879e-32 * h**2 * c**2 # J cm^-3

# Cosmic microwave background temperature
T = 1000000 # Temperature at Time of Interest

T0 = 2.726  # Today (K)
T0_alt1 = 2.349e-4  # Today (eV/k_B)

# Cosmic microwave background energy density
rho_gamma = (pi**2)*(k_B**4)*(T**4) / (15*(hbar*c)**3)
rho_gamma_alt1 = 2.474e-5 * h**(-2)*(T/T0)**4 * rho_crit_alt3  # J cm^-3

# Neutrino density parameter today
m_nu = 0.06 # eV - Verify each time used
Omega_nu_h2 = m_nu / (94)

# Scale factor at equality
a_eq = 4.15e-5  / (Omega_m * h**2)

# Inverse comoving horizon at equality
k_eq = 0.073 * Omega_m * h**2  # Mpc^-1