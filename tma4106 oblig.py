import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# #oppgave 1
# def f(x):
#     return np.exp(x)

# def df(f,x,h):
#     return (f(x+h) - f(x))/h

# print(df(f,1.5,1e-8)) #1-8 gir best resultat, lavere gir mer feil

# #oppg2 
# def derivert(f,x,h):
#     return (f(x+h)-f(x-h))/(2*h)
# print(derivert(f,1.5,1e-5)) # 1e-5 gir best resultat.

#oppg3

# def der(f,x,h):
#     return (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)

# print(derivert(f,1.5,1e-6)) # 1e-5 gir best resultat

#oppg4, oppg 5, oppg 6
m = 2000
n = 10
k = 0.0005
h = 0.1
r = k / h**2

u = np.zeros((n+1,m+1))
x = np.linspace(0,1,n+1)
u[:,0] = np.sin(x)
u[0, :] = u[n, :] = 0 


# for j in range(m): #oppg 4
#     for i in range(1, n):  # rom (hopp over kantene) da disse er kjent, lik 0
#         u[i][j+1] = u[i][j] + (k/h**2) * (u[i+1][j] - 2*u[i][j] + u[i-1][j]) 

#implisitt metode, fikspunktiterasjon oppg 5
for j in range(m):
    u_old = u[:, j].copy()
    u_new = u_old.copy()
    
    #fikspunktiterasjon
    for _ in range(50): #burde være nok iterasjoner
        u_prev = u_new.copy()
        for i in range(1, n):
            #u_new[i] = (u_old[i] + r * (u_prev[i-1] + u_prev[i+1])) / (1 + 2*r) #oppg5
            rhs = r * (u_old[i-1] + u_old[i+1]) + (1 - 2*r) * u_old[i] #oppg6
            u_new[i] = (rhs + r * (u_prev[i-1] + u_prev[i+1])) / (1 + 2*r) #oppg6
        if max(abs(u_new - u_prev)) < 1e-6: #trenger ikke å kjøre hele løkka hvis den har konvergert.
            break
    
    u[:, j+1] = u_new
        
fig, ax = plt.subplots()
line, = ax.plot(x, u[:, 0])


def update(j):
    line.set_ydata(u[:, j])
    ax.set_title(f"t = {j*k:.3f}")
    return line,

ani = animation.FuncAnimation(fig, update, frames=m+1, interval=0.0003)
plt.show() 














