import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


m = 2000
n = 10
k = 0.0005
h = 0.1
r = k / h**2
r_cn = k / (2 * h**2)

x = np.linspace(0, 1, n+1)



u_exp = np.zeros((n+1, m+1))
u_imp = np.zeros((n+1, m+1))
u_cn  = np.zeros((n+1, m+1))

#initialkrav
for u in [u_exp, u_imp, u_cn]:
    u[:, 0] = np.sin(x)
    u[0, :] = u[n, :] = 0

#eksplisitt euler
for j in range(m):
    for i in range(1, n):
        u_exp[i, j+1] = u_exp[i, j] + r * (u_exp[i+1, j] - 2*u_exp[i, j] + u_exp[i-1, j])

#imp euler
for j in range(m):
    u_old = u_imp[:, j].copy()
    u_new = u_old.copy()
    for _ in range(50):
        u_prev = u_new.copy()
        for i in range(1, n):
            u_new[i] = (u_old[i] + r * (u_prev[i-1] + u_prev[i+1])) / (1 + 2*r)
        if max(abs(u_new - u_prev)) < 1e-6:
            break
    u_new[0] = 0
    u_new[n] = 0
    u_imp[:, j+1] = u_new

#Crank-Nicholson
for j in range(m):
    u_old = u_cn[:, j].copy()
    u_new = u_old.copy()
    for _ in range(50):
        u_prev = u_new.copy()
        for i in range(1, n):
            rhs = r_cn * (u_old[i-1] + u_old[i+1]) + (1 - 2*r_cn) * u_old[i]
            u_new[i] = (rhs + r_cn * (u_prev[i-1] + u_prev[i+1])) / (1 + 2*r_cn)
        if max(abs(u_new - u_prev)) < 1e-6:
            break
    u_new[0] = 0
    u_new[n] = 0
    u_cn[:, j+1] = u_new


fig, ax = plt.subplots()
line1, = ax.plot(x, u_exp[:, 0], label="Eksplisitt")
line2, = ax.plot(x, u_imp[:, 0], label="Implisitt")
line3, = ax.plot(x, u_cn[:, 0],  label="Crank-Nicolson")
ax.set_ylim(0, 1)
ax.legend()

def update(j):
    line1.set_ydata(u_exp[:, j])
    line2.set_ydata(u_imp[:, j])
    line3.set_ydata(u_cn[:, j])
    ax.set_title(f"t = {j * k:.3f}")
    return line1, line2, line3

ani = animation.FuncAnimation(fig, update, frames=m+1, interval=0.0003)
plt.show()
