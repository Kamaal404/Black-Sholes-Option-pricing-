import math
from scipy.stats import norm
import numpy as np
import plotly.graph_objects as go
import streamlit as st

# Black-Scholes functions for call and put option pricing
def black_scholes_call(S, K, T, Vol, r):
    d1 = (math.log(S / K) + (r + Vol**2 / 2) * T) / (Vol * math.sqrt(T))
    d2 = d1 - (Vol * math.sqrt(T))
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    C = S * Nd1 - K * math.exp(-r * T) * Nd2
    return C

def black_scholes_put(S, K, T, Vol, r):
    d1 = (math.log(S / K) + (r + Vol**2 / 2) * T) / (Vol * math.sqrt(T))
    d2 = d1 - (Vol * math.sqrt(T))
    Nd1 = norm.cdf(-d1)
    Nd2 = norm.cdf(-d2)
    P = K * math.exp(-r * T) * Nd2 - S * Nd1
    return P


st.set_page_config(layout="wide", page_title="Black-Scholes Option Pricing", page_icon=":chart_with_upwards_trend:")
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    .stSidebar, .css-1aumxhk, .css-hxt7ib {
        background-color: black !important;
        color: white !important;
    }
    .css-10trblm { color: white !important; }
    </style>
""", unsafe_allow_html=True)

st.title("Black-Scholes Option Pricing")

# Add LinkedIn profile link
st.markdown("[Connect with me on LinkedIn Kamal Saalaoui](https://www.linkedin.com/in/kamal-saalaoui-69400b297/)")

# Input section
st.sidebar.header("Input Parameters")
S = st.sidebar.number_input("Spot Price (S)", value=100.0, step=1.0, format="%.2f")
K = st.sidebar.number_input("Strike Price (K)", value=110.0, step=1.0, format="%.2f")
T = st.sidebar.number_input("Time to Maturity (T in years)", value=1.0, step=0.1, format="%.2f")
Vol = st.sidebar.number_input("Volatility (σ)", value=0.2, step=0.01, format="%.2f")
r = st.sidebar.number_input("Risk-Free Rate (r)", value=0.05, step=0.01, format="%.2f")

# Calculate option prices
call_price = black_scholes_call(S, K, T, Vol, r)
put_price = black_scholes_put(S, K, T, Vol, r)

st.sidebar.markdown(f"**Call Option Price:** {call_price:.2f}")
st.sidebar.markdown(f"**Put Option Price:** {put_price:.2f}")

# 3D Surface Plot parameters
x_data = np.linspace(0.1, 0.5, 50)  # Volatility range
y_data = np.linspace(0.01, 0.2, 50)  # Risk-free rate range
X, Y = np.meshgrid(x_data, y_data)

# Calculate Z for call and put prices
Z_call = np.array([[black_scholes_call(S, K, T, x, y) for x, y in zip(row_x, row_y)] for row_x, row_y in zip(X, Y)])
Z_put = np.array([[black_scholes_put(S, K, T, x, y) for x, y in zip(row_x, row_y)] for row_x, row_y in zip(X, Y)])

# Create 3D Surface Plots
fig_call = go.Figure(
    data=[go.Surface(z=Z_call, x=x_data, y=y_data, colorscale="Viridis")],
    layout=go.Layout(
        title="Call Option Price",
        scene=dict(
            xaxis_title="Volatility (σ)",
            yaxis_title="Risk-Free Rate (r)",
            zaxis_title="Option Price",
            bgcolor="black"
        ),
    )
)
fig_call.update_layout(scene_camera=dict(eye=dict(x=-2, y=-2, z=1)))  # Rotate call graph 180 degrees

fig_put = go.Figure(
    data=[go.Surface(z=Z_put, x=x_data, y=y_data, colorscale="Viridis")],
    layout=go.Layout(
        title="Put Option Price",
        scene=dict(
            xaxis_title="Volatility (σ)",
            yaxis_title="Risk-Free Rate (r)",
            zaxis_title="Option Price",
            bgcolor="black"
        ),
    )
)
fig_put.update_layout(scene_camera=dict(eye=dict(x=-2, y=2, z=1)))  


col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_call, use_container_width=True)
with col2:
    st.plotly_chart(fig_put, use_container_width=True)
