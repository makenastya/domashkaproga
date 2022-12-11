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
        if isinstance(other, Complex):
            real = other.get_re()
            imag = other.get_im()
        else:
            real = other
            imag = 0
        return Complex(self._re + real, self._im + imag)

    def minus(self, other):
        if isinstance(other, Complex):
            real = other.get_re()
            imag = other.get_im()
        else:
            real = other
            imag = 0
        return Complex(self._re - real, self._im - imag)

    def prod(self, other):
        if isinstance(other, Complex):
            real = other.get_re()
            imag = other.get_im()
        else:
            real = other
            imag = 0
        return Complex(self._re * real - self._im * imag,
                       self._re * imag + self._im * real)

    def div(self, other):
        a1 = self._re
        b1 = self._im
        if isinstance(other, Complex):
            a2 = other.get_re()
            b2 = other.get_im()
        else:
            a2 = other
            b2 = 0
        re = (a1 * a2 + b1 * b2) / (a2 * a2 + b2 * b2)
        im = (a2 * b1 - a1 * b2) / (a2 * a2 + b2 * b2)
        return Complex(re, im)

    def __abs__(self):
        real = self.get_re()
        imag = self.get_im()
        return (real * real) + (imag * imag)

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.get_re() == other.get_re() and self.get_im() == other.get_im()
        elif self.get_im() == 0:
            return self.get_re() == other
        else:
            return False

    def __add__(self, other):
        return self.plus(other)

    def __radd__(self, other):
        return self.plus(other)

    def __sub__(self, other):
        return self.minus(other)

    def __rsub__(self, other):
        return self.minus(other)

    def __mul__(self, other):
        return self.prod(other)

    def __rmul__(self, other):
        return self.prod(other)

    def __truediv__(self, other):
        return self.div(other)

    def __rtruediv__(self, other):
        # Other is not a complex number, otherwise __truediv__ is used
        return Complex(other, 0).div(self)

    def __getitem__(self, i):
        if i == 0:
            return self.get_re()
        elif i == 1:
            return self.get_im()
        else:
            return None

    def __setitem__(self, i, value):
        if i == 0:
            self.set_re(value)
        elif i == 1:
            self.set_im(value)

    def __iter__(self):
        return iter([self._re, self._im])

    def __str__(self):
        if self._im > 0:
            return f'{self._re} + {self._im} * i'
        else:
            return f'{self._re} - {self._im * (-1)} * i'
