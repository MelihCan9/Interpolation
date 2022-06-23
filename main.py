import matplotlib.pyplot as plt
import numpy as np

def direct(x, y, data_point):

    from scipy.interpolate import interp1d

    f = interp1d(x, y)
    y_point = f(data_point)  # use interpolation function returned by `interp1d`

    plt.plot(x, y)
    plt.plot(23, y_point, 'ro')
    plt.title('Direct Method Interpolation')
    plt.scatter(x, y, color='blue', marker='o', label='Given data points')
    plt.scatter(data_point, y_point, color='red', marker='o',
                label='Interpolation point \n x = {} , y = {}'.format(data_point, round(float(y_point), 3)))
    plt.xlabel('Day')
    plt.ylabel('Number of deaths')
    plt.legend()
    plt.show()

def lagrange(x, y, data_point):
    # Lagrange Interpolation

    m = len(x)  # Data points
    n = m - 1  # Degree of polynomial

    # Interpolate output
    yp = 0

    # To plot as a polynomial graph
    poly_plot = np.polyfit(x, y, n)
    x_pol = np.linspace(x[0], x[-1])
    y_pol = np.polyval(poly_plot, x_pol)

    # Executing the Lagrange formula
    for i in range(n + 1):
        p = 1
        for j in range(n + 1):
            # Here is important, we are not taking the index that we are currently with to the respect to the formula
            if i != j:
                p *= (data_point - x[j]) / (x[i] - x[j])
        yp += y[i] * p

    print("For t = {}, y = {}".format(data_point, yp))

    # Plotting all in one
    plt.plot(x_pol, y_pol, '')
    plt.title('Lagrange Interpolation')
    plt.scatter(x, y, color='blue', marker='o', label='Given data points')
    plt.scatter(data_point, yp, color='red', marker='o',
                label='Interpolation point \n x = {} , y = {}'.format(data_point, round(yp, 3)))
    plt.xlabel('Day')
    plt.ylabel('Number of deaths')
    plt.legend()
    plt.show()


def nddp(x, y, data_point):

    def get_coeff(x, y):
        n = np.shape(y)[0]
        pyramid = np.zeros([n, n])
        pyramid[::, 0] = y

        for j in range(1, n):
            for i in range(n - j):
                pyramid[i][j] = (pyramid[i + 1][j - 1] - pyramid[i][j - 1]) / (x[i + j] - (x[i]))

        return pyramid[0]

    coeff_vector = get_coeff(x, y)

    final_pol = np.polynomial.Polynomial([0.])
    n = coeff_vector.shape[0]

    for i in range(n):
        p = np.polynomial.Polynomial([1.])
        for j in range(i):
            p_temp = np.polynomial.Polynomial([-x[j], 1.0])
            p = np.polymul(p, p_temp)

        p *= coeff_vector[i]
        final_pol = np.polyadd(final_pol, p)

    p = np.flip(final_pol[0].coef, axis=0)

    m = len(x)  # Data points
    n = m - 1  # Degree of polynomial

    poly_plot = np.polyfit(x, y, n)
    x_pol = np.linspace(x[0], x[-1])
    y_pol = np.polyval(poly_plot, x_pol)
    plt.plot(x_pol, y_pol, '')
    plt.title('NDDP Interpolation')
    plt.scatter(x, y, color='blue', marker='o', label='Given data points')
    plt.scatter(data_point, np.polyval(p,23), color='red', marker='o',
                label='Interpolation point \n x = {} , y = {}'.format(data_point, round(np.polyval(p,23), 3)))
    plt.xlabel('Day')
    plt.ylabel('Number of deaths')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    x = np.array([20, 21, 24, 26, 27, 28])
    y = np.array([18, 17, 15, 14, 16, 15])

    # Interpolate input
    data_point = int(input("Please enter the x value to interpolate: "))

    #lagrange(x,y, data_point)
    nddp(x, y, data_point)

    #direct(x, y, data_point)