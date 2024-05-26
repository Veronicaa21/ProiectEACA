import cmath
import matplotlib.pyplot as plt
import numpy as np


a=complex(input("Dati valoarea coeficientului a: "))
b=complex(input("Dati valoarea coeficientului b: "))
c=complex(input("Dati valoarea coeficientului c: "))
d=complex(input("Dati valoarea coeficientului d: "))

h = b / (3 * a)
p = (3 * a * h ** 2 - 2 * b * h + c) / a
q = (-a * h ** 3 + b * h ** 2 - c * h + d) / a

if p == 0:
    if q == p:
        x = -h
        print(x)

delta = 4 * p ** 3 + 27 * q ** 2
alfa = cmath.sqrt(p / (-3))
omega = complex((-1) / 2, cmath.sqrt(3) / 2)

if delta == 0:
    x0 = -h + 2 * alfa
    x1 = alfa - h
    x2 = -alfa - h
    print(x0, x1, x2)
else:
    x0 = alfa - (p / (3 * alfa)) - (b / (3 * a))
    x1 = omega * alfa - ((p * omega ** 2) / (3 * alfa)) - (b / (3 * a))
    x2 = alfa * omega ** 2 - ((p * omega) / (3 * alfa)) - (b / (3 * a))
    print(x0, x1, x2)


def f(x):
    return a * x ** 3 + b * x ** 2 + c*x + d


x_gf = np.linspace(-10, 10, 400)
y_gf = [f(x) for x in x_gf]


plt.plot(x_gf, y_gf, label='f(x)', color='purple')

plt.scatter([x0.real, x1.real, x2.real], [f(x0).real, f(x1).real, f(x2).real], color='blue', label='Radacini')
plt.scatter([x0.imag, x1.imag, x2.imag], [f(x0).imag, f(x1).imag, f(x2).imag], color='blue')

plt.legend()
plt.title('Graficul ecuației de gradul trei')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.9)
plt.axvline(0, color='black', linewidth=0.9)


plt.grid(color='gray', linestyle='--', linewidth=0.9)
plt.legend()


plt.show()