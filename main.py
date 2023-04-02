import panel_mehod as pm
import numpy as np
from matplotlib import pyplot as plt

def main():
    print('Hello')
    Q = 1
    alpha_deg = 15
    alpha_rad = alpha_deg*np.pi/180
    panels_x, panels_z, circ_x, circ_z, colloc_x, colloc_z, alpha_i = pm.make_panels(pm.camber, 5, 1)
    A, b = pm.calc_coeff(panels_x, panels_z, circ_x, circ_z, colloc_x, colloc_z, alpha_i, 1, alpha_rad)

    gamma = np.linalg.solve(A, b)
    print(gamma)

    def vortex(gamma0, x, z, x0, z0):
        return gamma0/(2*np.pi) * np.log(np.sqrt((x-x0)**2 + (z-z0)**2))
        #return gamma0/(2*np.pi) * np.arctan2(z-z0, x-x0)

    def stream(x, z, Q, alpha):
        p = np.zeros(shape=np.shape(x))
        p = Q * (z*np.cos(alpha) - x*np.sin(alpha))
        for g, x0, z0 in zip(gamma, circ_x, circ_z):
            p += vortex(g, x, z, x0, z0)
        return p

    X = np.linspace(-0.5, 1.5)
    Z = np.linspace(-1, 1)
    xg, zg = np.meshgrid(X, Z)

    psi = stream(xg, zg, Q, alpha_rad)

    x_foil = np.linspace(0,1)
    z_foil = pm.camber(x_foil)
    #plt.plot(x_foil, z_foil, linewidth=5, color='k')
    plt.scatter(panels_x, panels_z)
    plt.scatter(circ_x, circ_z, color='r')
    plt.scatter(colloc_x, colloc_z, color='g')

    plt.contour(xg, zg, psi, 30)
    plt.show()



if __name__ == '__main__':
    main()
