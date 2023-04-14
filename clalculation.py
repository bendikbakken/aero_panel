from numpy import pi, sin


def alpha0():
    a = (0.25 * 0.5 * (1.369 + 0.5 * sin(2 * 1.369)) - 0.3 * sin(1.369)) + 0.05 * 1.369
    b = 0
    c = (0.111 * 0.5 * (pi + 0.5 * sin(2 * pi)) - (0.111 + 0.0222) * sin(pi)) + 0.0222 * pi
    d = (0.111 * 0.5 * (1.369 + 0.5 * sin(2 * 1.369)) - (0.111 + 0.0222) * sin(1.369)) + 0.0222 * 1.369
    return -1 / pi * (a - b + c - d)


th1 = 1.369


def A1_1(th): return 2 / pi * (0.25 * 0.5 * (th + 0.5 * sin(2 * th)) - 0.05 * sin(th))


def A1_2(th): return 2 / pi * (0.111 * 0.5 * (th + 0.5 * sin(2 * th)) - 0.0222 * sin(th))


A0 = 5 * pi / 180 - (
            1 / pi * (0.25 * sin(th1) - 0.05 * th1) + 1 / pi * (-0.0222 * pi - 0.111 * sin(th1) + 0.0222 * th1))
A1 = A1_1(th1) - A1_1(0) + A1_2(pi) - A1_2(th1)


def A2_func(a, th):
    return a * (1 / 6 * (3 * sin(th) + sin(3 * th)) - 1 / 10 * sin(2 * th))


A2 = A2_func(0.5 / pi, 1.369) - A2_func(0.5 / pi, 0) + A2_func(0.222 / pi, pi) - A2_func(0.222 / pi, 1.369)

print(A0)
print(A1)
print(A2)
print(f'alpha_L=0 = {alpha0() * 180 / pi}')

Cl = pi * (2 * A0 + A1)
CmLE = -(Cl / 4 + pi / 4 * (A1 + A2))
CmC4 = pi / 4 * (A2 - A1)
print(f'Cl = {Cl}')
print(f'Cm,LE = {CmLE}')
print(f'Cm,C4 = {CmC4}')
print(f'x_cp/c = {1 / 4 * (1 + pi / Cl * (A1 - A2))}')
