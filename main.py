import panel_mehod as pm
import numpy as np
from matplotlib import pyplot as plt


def main():
    # Initialize variables
    Q = 1
    n = 100
    alpha_deg = 5
    # alpha_deg = -4.09625
    alpha_rad = alpha_deg * np.pi / 180

    # Constructing panels
    panels_x, panels_z, circ_x, circ_z, colloc_x, colloc_z, alpha_i = pm.make_panels(pm.camber, n, 1)
    # Calculating coefficients
    A, b = pm.calc_coeff(circ_x, circ_z, colloc_x, colloc_z, alpha_i, 1, alpha_rad)

    # Solving linear system for gamma (I have a rouge Q that has to be included for program to work for Q != 1).
    gamma = np.linalg.solve(A, b * Q)

    # Solving streamfunction for plotting
    X = np.linspace(-0.5, 1.5, 100)
    Z = np.linspace(-1, 1, 100)
    xg, zg = np.meshgrid(X, Z)
    psi = pm.stream(xg, zg, Q, alpha_rad, gamma, circ_x, circ_z)

    # Plotting stream function
    plt.plot(panels_x, panels_z, linewidth=3, color='k')
    plt.scatter(circ_x, circ_z, color='r')
    plt.scatter(colloc_x, colloc_z, color='g')
    plt.contour(xg, zg, psi, 50)

    # Calculating lift coeff. The rouge Q from earlier is back! This time to scale coefficients for when Q != 0.
    gamma_tot = sum(gamma)
    Cl = 2 * gamma_tot / Q
    print(f'Cl = {Cl}')

    # Calculate moment by multiplying lift from vorticies by the distance from courter-chord.
    Cm_c4 = 0
    for i in range(n):
        Cm_c4 += 2 * gamma[i] / Q * -(circ_x[i] - 0.25)
        # Cm_c4 += 2*gamma[i] * -(circ_x[i]-0.355528)
    print(f'Cm_c4 = {Cm_c4}')

    plt.show()
    return 0


if __name__ == '__main__':
    main()
