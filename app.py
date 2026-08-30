import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set up the web page title
st.set_page_config(page_title="Break-Even Dashboard", layout="centered")
st.title("Dynamic Break-Even Analysis")

# 1. Create interactive sliders in a sidebar
st.sidebar.header("Set Parameters")
fixed_cost = st.sidebar.slider("Fixed Cost ($):", min_value=1000, max_value=50000, step=1000, value=10000)
variable_cost = st.sidebar.slider("Var. Cost ($):", min_value=1.0, max_value=100.0, step=0.5, value=10.0)
price = st.sidebar.slider("Price ($):", min_value=5.0, max_value=200.0, step=1.0, value=25.0)

# 2. Calculations (using your original logic)
denom = max(price - variable_cost, 0.1) 
be_units = int(fixed_cost / denom)
max_units = max(be_units * 2, 100)

x = np.linspace(0, max_units, 1000)
total_revenue = price * x
total_cost = fixed_cost + (variable_cost * x)
fixed_cost_line = np.full_like(x, fixed_cost)

# 3. Plotting using Matplotlib's object-oriented API (safer for web apps)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, total_revenue, label='Total Revenue', color='green', lw=2)
ax.plot(x, total_cost, label='Total Cost', color='red', lw=2)
ax.plot(x, fixed_cost_line, label='Fixed Cost', color='blue', linestyle='--')

# Mark Break-Even Point
if price > variable_cost:
    ax.scatter(be_units, price * be_units, color='black', s=100, zorder=5, 
               label=f'Break-Even: {be_units} units')
    ax.axvline(x=be_units, color='gray', linestyle=':', alpha=0.7)
    ax.axhline(y=price * be_units, color='gray', linestyle=':', alpha=0.7)

# Chart Styling
ax.set_title('Break-Even Point Visualization', fontsize=14, fontweight='bold')
ax.set_xlabel('Units Sold', fontsize=12)
ax.set_ylabel('Money ($)', fontsize=12)
ax.set_xlim(0, max_units)
ax.set_ylim(0, max(total_revenue[-1], total_cost[-1]) * 1.1)
ax.grid(True, which='both', linestyle='--', alpha=0.5)
ax.legend(loc='upper left', fontsize=10)

# 4. Render the plot in the web app
st.pyplot(fig)