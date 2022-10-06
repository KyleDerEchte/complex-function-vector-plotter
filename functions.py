import cmath

import numpy as np


def z_1(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        try:
            result[c] = ((1 / 2) * c) - (3 / (5 - c))
            if result[c] == 0:
                print(f"Zero point at {c}")
        except:
            result[c] = 0
            print(f"Defnition gap at {c}!")
            continue
    return result


def z_2(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = (c ** 2)
    return result


def z_3(z: list[complex], x: float) -> dict[complex, complex]:
    if x == 0:
        return 0
    result = {}
    for c in z:
        result[c] = ((c ** x) / x * c)
    return result


def z_4(z: list[complex], x: float) -> dict[complex, complex]:
    if x == 0:
        return 0
    result = {}
    for c in z:
        result[c] = (c / x)
    return result


def z_5(z: list[complex], x: float) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = complex(c * x)
    return result


def z_6(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = (cmath.sin(c))
    return result


def z_7(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = (cmath.cos(c))
    return result


def z_8(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        result[c] = (cmath.tan(c))
    return result


def z_9(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        if c == 0:
            continue
        result[c] = (1 / c)
    return result


def z_10(z: list[complex]) -> dict[complex, complex]:
    result = {}
    for c in z:
        try:
            result[c] = ((c ** 3) / cmath.sqrt(c)) - 3j / (5j - c)
            if result[c] == 0:
                print(f"Zero point at {c}")
        except:
            result[c] = 0
            print(f"Defnition gap at {c}!")
            continue
    return result


def of_range(start: complex, end: complex, step: float) -> list[complex]:
    complexes = []
    re = np.arange(start.real, end.real, step)
    im = np.arange(start.imag, end.imag, step)
    for r in range(len(re)):
        for i in range(len(im)):
            complexes.append(complex(re[r], im[i]))
    return complexes
