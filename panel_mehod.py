import numpy as np


def camber(x):
    z = np.zeros(np.size(x))
    for i in range(len(x)):
        if x[i] <= 0.4:
            z[i] = 0.25 * (0.8 * x[i] - x[i] ** 2)
        else:
            z[i] = 0.111 * (0.2 + 0.8 * x[i] - x[i] ** 2)
    return z


def make_panels(func, n, c):
    panels_x = np.linspace(0, c, n + 1)
    panels_z = func(panels_x)
    circ_x = panels_x[:-1] + 1 / 4 * c / n
    colloc_x = panels_x[:-1] + 3 / 4 * c / n
    circ_z = np.interp(circ_x, panels_x, panels_z)
    colloc_z = np.interp(colloc_x, panels_x, panels_z)
    alpha_i = -np.arctan2(panels_z[1:] - panels_z[:-1], panels_x[1:] - panels_x[:-1])
    return panels_x, panels_z, circ_x, circ_z, colloc_x, colloc_z, alpha_i


def calc_coeff(circ_x, circ_z, colloc_x, colloc_z, alpha_i, Q, alpha):
    n = np.size(circ_x)
    n_i = np.array([np.sin(alpha_i), np.cos(alpha_i)])
    a = np.zeros((n, n))
    M = np.array([[0, 1], [-1, 0]])

    for j in range(n):
        aj = (M @ np.array([(colloc_x - circ_x[j]), (colloc_z - circ_z[j])])) * (
                    1 / (2 * np.pi) * 1 / ((colloc_x - circ_x[j]) ** 2 + (colloc_z - circ_z[j]) ** 2))
        a[:, j] = np.array([a @ n for a, n in zip(aj.T, n_i.T)])

    b = -Q**2 * np.sin(alpha + alpha_i)
    return a, b

def stream(x, z, Q, alpha, gamma, circ_x, circ_z):
    p = Q * (z * np.cos(alpha) - x * np.sin(alpha))  # uniform flow
    for g, x0, z0 in zip(gamma, circ_x, circ_z):
        p += g / (2 * np.pi) * np.log(np.sqrt((x - x0) ** 2 + (z - z0) ** 2))  # Vortex elements
    return p

