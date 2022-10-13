import math


class Complex:
    def __init__(self, real, im):
        self._im = None
        self._re = None
        self.set_im(im)
        self.set_re(real)

    def get_re(self):
        return self._re

    def get_im(self):
        return self._im

    def set_re(self, real):
        self._re = real

    def set_im(self, im):
        self._im = im

    @staticmethod
    def to_alg(r, f):
        return Complex(r * math.cos(f), r * math.sin(f))

    def set_to_alg(self, r, f):
        self.set_re(r * math.cos(f))
        self.set_im(r * math.sin(f))

    def to_exp(self):
        r = math.sqrt(self._im * self._im + self._re * self._re)
        f = math.acos(self._re / r)
        if self._im < 0:
            f = 2 * math.pi - f
        return r, f

    def plus(self, other):
        return Complex(self._re + other.get_re(), self._im + other.get_im())

    def minus(self, other):
        return Complex(self._re - other.get_re(), self._im - other.get_im())

    def prod(self, other):
        return Complex(self._re * other.get_re() - self._im * other.get_im(),
                       self._re * other.get_im() + self._im * other.get_re())

    def div(self, other):
        a1 = self._re
        b1 = self._im
        a2 = other.get_re()
        b2 = other.get_im()
        re = (a1 * a2 + b1 * b2) / (a2 * a2 + b2 * b2)
        im = (a2 * b1 - a1 * b2) / (a2 * a2 + b2 * b2)
        return Complex(re, im)

    def __str__(self):
        if self._im > 0:
            return f'{self._re} + {self._im} * i'
        else:
            return f'{self._re} - {self._im * (-1)} * i'
