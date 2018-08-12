import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class Mandelbrot:

    def __init__(self, x_min, x_max, x_len, y_min, y_max, y_len, num_iters):
        """
        :param num_iters: Number of iterations of the z <- z^2 + c map.
        """
        self.x_min = x_min
        self.x_max = x_max
        self.x_len = x_len
        self.y_min = y_min
        self.y_max = y_max
        self.y_len = y_len
        self.num_iters = num_iters
        self.x = np.linspace(x_min, x_max, x_len)
        self.y = np.linspace(y_min, y_max, y_len)

    @abstractmethod
    def is_mandelbrot(self, c):
        pass

    @abstractmethod
    def generate(self):
        pass


class MandelbrotScalar(Mandelbrot):

    def is_mandelbrot(self, c):
        z = 0
        for i in range(self.num_iters):
            z = z * z + c
            if z.real * z.real + z.imag * z.imag > 4:
                return False
        return True

    def generate(self):
        z = np.empty((self.y_len, self.x_len))
        for j in range(self.y_len):
            for i in range(self.x_len):
                a = self.x[i]
                b = self.y[j]
                z[j, i] = self.is_mandelbrot(a + b * 1j)
        plt.contourf(self.x, self.y, z)
        plt.show()


class MandelbrotVector(Mandelbrot):

    def is_mandelbrot(self, c):
        z = np.zeros((self.y_len, self.x_len)) + np.zeros(
            (self.y_len, self.x_len)) * 1j
        not_mandelbrot = np.full(z.shape, False)
        for i in range(self.num_iters):
            z = np.multiply(z, z) + c
            not_mandelbrot |= (abs(z) > 2)
            z[not_mandelbrot] = 0
        return ~not_mandelbrot

    def generate(self):
        xx, yy = np.meshgrid(self.x, self.y, sparse=True)
        z = self.is_mandelbrot(xx + yy * 1j)
        plt.contourf(self.x, self.y, z)
        plt.show()
