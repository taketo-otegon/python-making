import numpy as np
import matplotlib.pyplot as plt


def plot_easily(history,name,analytical_f):
    plt.scatter(history[:,0],history[:,1],label=name)
    plt.plot(history[:,0],analytical_f(history[:,0]),"r",label="Analytical solution")
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(name)
    plt.legend()
    plt.show()


def plot_error(history,analytical_f):
    error = analytical_f(history[:,0]) - history[:,1]
    plt.scatter(history[:,0],error,label="Error")
    plt.xlabel('t')
    plt.ylabel('Error')
    plt.title('Error')
    plt.legend()
    plt.show()




