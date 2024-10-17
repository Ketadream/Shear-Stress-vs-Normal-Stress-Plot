import matplotlib.pyplot as plt
import numpy as np

# Data for the point
normal_stress = 77.65
shear_stress = 54.91

# Mohr-Coulomb failure envelope parameters
cohesion = 0  # kPa
friction_angle = 35.2659  # degrees
phi_radians = np.radians(friction_angle)

# Normal stress range for plotting the failure envelope
sigma_values = np.linspace(0, 90, 100)
tau_values = cohesion + sigma_values * np.tan(phi_radians)

# Create figure and axis with a larger size and high DPI for better quality
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)

# Plot the point
ax.scatter(normal_stress, shear_stress, color='#1f77b4', edgecolor='black', s=200, zorder=5, label='Stress Point')

# Plot the Mohr-Coulomb failure envelope
ax.plot(sigma_values, tau_values, color='#ff7f0e', linestyle='-', linewidth=2, label='Mohr-Coulomb Failure Envelope')

# Plot dashed lines (guidelines) to the axes for the stress point
ax.axhline(y=shear_stress, color='gray', linestyle='--', linewidth=1.5, alpha=0.8)
ax.axvline(x=normal_stress, color='gray', linestyle='--', linewidth=1.5, alpha=0.8)

# Draw a subtle, semi-transparent circle around the point
circle = plt.Circle((normal_stress, shear_stress), 5, color='#ff7f0e', fill=False, linestyle='--', linewidth=2, alpha=0.8)
ax.add_patch(circle)

# Set axis limits with some padding for aesthetics
ax.set_xlim(0, 90)
ax.set_ylim(0, 60)

# Set axis labels with a modern font and larger size
ax.set_xlabel('Normal Stress (kPa)', fontsize=14, fontweight='bold', labelpad=10)
ax.set_ylabel('Shear Stress (kPa)', fontsize=14, fontweight='bold', labelpad=10)

# Add title with a professional look
ax.set_title('Shear Stress vs Normal Stress with Mohr-Coulomb Failure Envelope', fontsize=16, fontweight='bold', pad=20)

# Add grid with improved styling for readability
ax.grid(True, which='both', color='gray', linestyle=':', linewidth=0.5, alpha=0.7)

# Customize tick labels for a clean appearance
ax.tick_params(axis='both', which='major', labelsize=12)

# Hide top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a legend for the point and Mohr-Coulomb envelope
ax.legend(loc='upper left', fontsize=12)

# Show plot
plt.tight_layout()
plt.show()
