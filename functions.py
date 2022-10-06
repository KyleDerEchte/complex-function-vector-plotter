import cmath

import numpy as np


def z_squared(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = (c ** 2)
    return result


def z_squared_x_div_x_times_z(z: list[complex], x: float) -> dict[complex, complex]:
    if x == 0:
        return 0
    result = {}
    for c in z:
        result[c] = ((c ** x) / x * c)
    return result


def z_div_x(z: list[complex], x: float) -> dict[complex, complex]:
    if x == 0:
        return 0
    result = {}
    for c in z:
        result[c] = (c / x)
    return result


def z_mul_x(z: list[complex], x: float) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = complex(c * x)
    return result


def sin_of_z(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = (cmath.sin(c))
    return result


def cos_of_z(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = (cmath.cos(c))
    return result


def tan_of_z(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = (cmath.tan(c))
    return result


def one_div_z(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        if c == 0:
            continue
        result[c] = (1 / c)
    return result


def of_range(start: complex, end: complex, step: float) -> list[complex]:
    complexes = []
    re = np.arange(start.real, end.real, step)
    im = np.arange(start.imag, end.imag, step)
    for r in range(len(re)):
        for i in range(len(im)):
            complexes.append(complex(re[r], im[i]))
    return complexes
