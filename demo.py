import numpy as np
from matplotlib import pyplot as plt
from noise_robust_differentiator import derivative_n2


def sin_demo():
    t = np.linspace(0, 4 * np.pi, 100)
    dt = t[1] - t[0]
    x = np.sin(t)

    deriv = derivative_n2(x, dt=dt)
    true_deriv = np.cos(t)

    plt.plot(
        t, deriv,
        color='tab:blue', label='Numerical')
    plt.plot(
        t, true_deriv,
        color='black', label='True', linestyle='--')
    plt.xlabel('$t$')
    plt.ylabel('$df / dt$')
    plt.legend()


def noisy_sin_demo():
    t = np.linspace(0, 4 * np.pi, 100)
    dt = t[1] - t[0]
    x = np.sin(t)
    x_noisy = x + np.random.normal(scale=0.05, size=len(x))

    deriv = derivative_n2(
        x_noisy, dt=dt, filter_length=11)
    true_deriv = np.cos(t)

    fig, axes = plt.subplots(
        figsize=(6, 7), nrows=2, ncols=1)
    axes[0].plot(
        t, x,
        color='black', label='True', linestyle='--')
    axes[0].plot(
        t, x_noisy,
        color='grey', label='Noisy')
    axes[0].set_xlabel('$t$')
    axes[0].set_ylabel('$f$')
    axes[0].legend()

    axes[1].plot(
        t, deriv,
        color='tab:blue', label='Numerical on noisy')
    axes[1].plot(
        t, true_deriv,
        color='black', label='True', linestyle='--')
    axes[1].set_xlabel('$t$')
    axes[1].set_ylabel('$df / dt$')
    axes[1].legend()


if __name__ == '__main__':
    # sin_demo()
    noisy_sin_demo()
    plt.show()
