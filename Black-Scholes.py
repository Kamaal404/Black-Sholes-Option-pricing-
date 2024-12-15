import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.colors import LinearSegmentedColormap


C=0
S=110
K=100
T=1
Vol=0.2
r=0.05

# Create a custom colormap: red to green
colors = ["red", "green"]  # Define the colors from low to high
cmap = LinearSegmentedColormap.from_list("red_to_green", colors)


def black_scholes_call(S,K,T,Vol,r):
    d1=(math.log(S/K)+(r + Vol**2 / 2)*T)/(Vol*math.sqrt(T))
    d2= d1-(Vol*math.sqrt(T))
    Nd1=norm.cdf(d1)#Standard normal CDF
    Nd2=norm.cdf(d2) # Standard normal CDF
    C=S*Nd1 - K*np.exp(-r*T)*Nd2
    return C

def black_scholes_put(S,K,T,Vol,r):
    d1=(math.log(S/K)+(r + Vol**2 / 2)*T)/(Vol*math.sqrt(T))
    d2= d1-(Vol*math.sqrt(T))
    Nd1=norm.cdf(-d1)#Standard normal CDF
    Nd2=norm.cdf(-d2) # Standard normal CDF
    C=  K*np.exp(-r*T)*Nd2 -S*Nd1
    return C

print(black_scholes_call(S,K,T,Vol,r))
print(black_scholes_put (S,K,T,Vol,r))


fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection = "3d")

# Set black background for the figure and the plot
fig.patch.set_facecolor('black')  # Background color of the figure
ax.set_facecolor('black')         # Background color of the 3D plot

x_data = np.arange(0.1,0.5,0.02)
y_data = np.arange(0.05,0.25,0.02)

X , Y= np.meshgrid(x_data,y_data)

Z= black_scholes_put(S,K,T,X,Y)
ax.plot_surface(X,Y,Z, cmap=cmap)
ax.xaxis.set_tick_params(color='white', labelcolor='white')
ax.yaxis.set_tick_params(color='white', labelcolor='white')
ax.zaxis.set_tick_params(color='white', labelcolor='white')
ax.set_xlabel('X Axis', color='white')
ax.set_ylabel('Y Axis', color='white')
ax.set_zlabel('Z Axis', color='white')

ax.set_xlabel('Volatility', fontsize=12, color='white')

# Add labels for Y and Z for context
ax.set_ylabel('Risk-Free Rate', fontsize=12, color='white')
ax.set_zlabel('Option price', fontsize=12, color='white')

ax.grid(color='gray')

ax.view_init(elev=15, azim=128) #for the put 15 128 and for the call option 15 -128
plt.title('Surface Plot with Custom Red-to-Green Colormap')
plt.savefig('3D_Plot_put.png', dpi=300, bbox_inches='tight')



#############################################################
# Set black background for the figure and the plot
ax1 = plt.axes(projection = "3d")
fig.patch.set_facecolor('black')  # Background color of the figure
ax1.set_facecolor('black')         # Background color of the 3D plot

x_data = np.arange(0.1,0.5,0.02)
y_data = np.arange(0.05,0.25,0.02)

X , Y= np.meshgrid(x_data,y_data)

Z= black_scholes_call(S,K,T,X,Y)
ax1.plot_surface(X,Y,Z, cmap=cmap)
ax1.xaxis.set_tick_params(color='white', labelcolor='white')
ax1.yaxis.set_tick_params(color='white', labelcolor='white')
ax1.zaxis.set_tick_params(color='white', labelcolor='white')
ax1.set_xlabel('X Axis', color='white')
ax1.set_ylabel('Y Axis', color='white')
ax1.set_zlabel('Z Axis', color='white')

ax1.set_xlabel('Volatility', fontsize=12, color='white')

# Add labels for Y and Z for context
ax1.set_ylabel('Risk-Free Rate', fontsize=12, color='white')
ax1.set_zlabel('Option price', fontsize=12, color='white')

ax1.grid(color='gray')

ax1.view_init(elev=15, azim=-128) #for the put 15 128 and for the call option 15 -128
plt.title('Surface Plot with Custom Red-to-Green Colormap')
plt.savefig('3D_Plot_call.png', dpi=300, bbox_inches='tight')
