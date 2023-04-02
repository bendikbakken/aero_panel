import numpy as np


def camber(x):
    if x <= 0.4:
        z = 0.25 * (0.8 * x - x ** 2)
    else:
        z = 0.111 * (0.2 + 0.8 * x - x ** 2)


def make_panels(func, n, c):
    panels_x = np.linspace(0, c, n+1)
    panels_z = camber(panels_x)
    circ_points = np.interp(panels_x, panels_z, panels_x[:-1] + 1 / 4 * c / n)
    colloc_points = np.interp(panels_x, panels_z, panels_x[:-1] + 3 / 4 * c / n)
    alpha_i = np.arctan2(panels_z[1:]-panels_z[0:-1], panels_x[1:]-panels_x[0:-1])


def calc_freestream(Q, alpha):
    return [Q*np.cos(alpha), Q*np.sin(alpha)]



def calc_coeff(panels_x, panels_y, circ_points, colloc_points, alpha_i):
    n = np.size(circ_points)
    n_i = np.array([np.sin(alpha_i), np.cos(alpha_i)])
    t_i = np.array([np.cos(alpha_i), -np.sin(alpha_i)])
    a = np.zeros((n,n))

    uw = 1/(2*np.pi*()) * np

    def q(,)
    for i in range(n):
        for j in range(n):
            a[i,j] = -1/(2*np.pi) * 1/r
