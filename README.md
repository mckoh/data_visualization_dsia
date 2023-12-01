# Hands-on Datenvisualisierung

In diesem Repo habe ich euch unsere Code-Files aus der zweiten ILV zusammengestellt. Unseren Code findet ihr in den folgenden Notebook-Dateien:

* [datenvisualisierung_bokeh.ipynb](datenvisualisierung_bokeh.ipynb)
* [datenvisualisierung_matplotlib.ipynb](datenvisualisierung_matplotlib.ipynb)
* [datenvisualisierung_plotly.ipynb](datenvisualisierung_plotly.ipynb)
* [datenvisualisierung_seaborn.ipynb](datenvisualisierung_seaborn.ipynb)

## Matplotlib (`matplotlib`)

Hier gibt es einige **[Anregungen](https://matplotlib.org/2.0.2/gallery.html)** zur Visualisierung mit `matplotlib`, und das sind die wichtigsten Funktionen:

```python
from matplotlib import pyplot as plt

plt.hist()
plt.scatter()
plt.boxplot()
plt.bar()
plt.barh()
plt.pie()
```

## Seaborn (`seaborn`)

Hier gibt es einige **[Anregungen](https://seaborn.pydata.org/examples/index.html)** zur Visualisierung mit `seaborn`, und das sind die wichtigsten Funktionen:

```python
import seaborn as sns

sns.heatmap()
sns.clustermap()
sns.pairplot()
```

## Bokeh (`bokeh`)

Hier gibt es einige **[Anregungen](https://seaborn.pydata.org/examples/index.html)** zur Visualisierung mit `bokeh`, und das sind die wichtigsten Funktionen:

```python
from bokeh.plotting import figure, show

figure()
show()
```

## Plotly (`plotly`)

Hier gibt es einige **[Anregungen](https://plotly.com/python/)** zur Visualisierung mit `plotly`, und das sind die wichtigsten Funktionen:

```python
from plotly import express as px

px.histogram()
px.bar()
px.scatter()
px.pie()
```
