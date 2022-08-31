import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

t = np.linspace(0, 0.05, 1000)
v = 220*np.sqrt(2)*np.sin(2*np.pi*60*t)

fig1 = go.Figure(data=go.Scatter(x=t, y=v))
fig2, ax = plt.subplots()
ax.plot(t, v)

st.markdown("# Título 1")
st.markdown("Simples")
st.pyplot(fig2)
st.markdown("Bonito Igual a Josh")
st.plotly_chart(fig1)
st.markdown("## Título 2")
st.markdown("### Título 3")