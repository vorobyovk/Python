import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as pc
import scipy.optimize as opt

alpha = np.pi / 4
speed = 35
x = np.linspace(0, 120, 1000)
y = x * np.tan(alpha) - (pc.g * x**2)/(2 * speed**2 * np.cos(alpha) ** 2)

plt.grid()
plt.plot(x, y)
plt.show()

alpha = np.pi / 4
speed = 35
def angle_flight(x, alpha, speed):
  return x * np.tan(alpha) - (pc.g * x**2)/(2 * speed**2 * np.cos(alpha) ** 2)
result = opt.minimize_scalar(lambda x, alpha, speed: -angle_flight(x, alpha, speed), bracket=(40, 60, 80), args=(alpha, speed))
print(result)
print("=========================================")
print(angle_flight(result.x, alpha, speed))
