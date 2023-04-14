import panel_mehod as pm
import numpy as np
from matplotlib import pyplot as plt


def main():
    Q = 1
    n = 100
    alpha_deg = 5
    # alpha_deg = -4.09625
    alpha_rad = alpha_deg * np.pi / 180
    panels_x, panels_z, circ_x, circ_z, colloc_x, colloc_z, alpha_i = pm.make_panels(pm.camber, n, 1)
    A, b = pm.calc_coeff(circ_x, circ_z, colloc_x, colloc_z, alpha_i, 1, alpha_rad)

    gamma = np.linalg.solve(A, b)


    X = np.linspace(-0.5, 1.5, 100)
    Z = np.linspace(-1, 1, 100)
    xg, zg = np.meshgrid(X, Z)

    psi = pm.stream(xg, zg, Q, alpha_rad, gamma, circ_x, circ_z)

    plt.plot(panels_x, panels_z, linewidth=3, color='k')
    plt.scatter(circ_x, circ_z, color='r')
    plt.scatter(colloc_x, colloc_z, color='g')

    gamma_tot = sum(gamma)
    Cl = 2*gamma_tot
    print(f'Cl = {Cl}')

    #calculate moment
    Cm_c4 = 0
    for i in range(n):
        Cm_c4 += 2 * gamma[i] * -(circ_x[i] - 0.25)
        # Cm_c4 += 2*gamma[i] * -(circ_x[i]-0.355528)

    print(f'Cm_c4 = {Cm_c4}')
    plt.contour(xg, zg, psi, 50)
    plt.show()


if __name__ == '__main__':
    main()
