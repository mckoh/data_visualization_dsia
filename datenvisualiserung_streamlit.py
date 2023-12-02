
import streamlit as st
from numpy.random import normal
from matplotlib import pyplot as plt
from seaborn import kdeplot

st.header("Überschrift")
st.write("Hallo Welt")

avg_gr = st.slider(max_value=210, min_value=140, value=165, label="Mittelwert Körpergröße")
avg_gew = st.slider(max_value=150, min_value=40, value=80, label="Mittelwert Gewicht")

std_gr = st.slider(max_value=25, min_value=0, value=12, label="Standardabweichung Körpergröße")
std_gew = st.slider(max_value=10, min_value=0, value=5, label="Standardabweichung Gewicht")

n = st.number_input(step=100, label="Anzahl Sportlern", min_value=100, max_value=10000)

sample_gr = normal(loc=avg_gr, scale=std_gr, size=n)
sample_gew = normal(loc=avg_gew, scale=std_gew, size=n)

fig, ax = plt.subplots()
ax.scatter(
    x=sample_gr,
    y=sample_gew,
    color="k",
    label="Test",
    alpha=0.3
)
kdeplot(sample_gr, sample_gew)
ax.legend()
st.pyplot(fig)