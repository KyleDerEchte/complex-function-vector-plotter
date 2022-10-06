import matplotlib.pyplot as plt
import numpy as np

import functions as fn


def main():
    data: dict[complex] = fn.z_squared(fn.of_range(-10 - 10j, 10 + 10j, 1))
    x: list[float] = []
    y: list[float] = []
    u: list[float] = []
    v: list[float] = []
    for val in data.keys():
        x_to_insert = val.real
        y_to_insert = val.imag

        u_to_insert = data.get(val).real
        v_to_insert = data.get(val).imag

        n = np.sqrt(u_to_insert ** 2 + v_to_insert ** 2)
        if n != 0:
            u_to_insert = u_to_insert / n * 0.5
            v_to_insert = v_to_insert / n * 0.5

        x.append(x_to_insert)
        y.append(y_to_insert)
        u.append(u_to_insert)
        v.append(v_to_insert)

    color = []
    for i in range(len(x)):
        div = np.sqrt(x[i] ** 2 + y[i] ** 2)
        color.append(div)
    print(f"Generated {len(x)} vectors.")
    plt.quiver(x, y, u, v, color, cmap="jet")
    plt.colorbar()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
