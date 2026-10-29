import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base = pd.read_csv("pedidos_prontos.csv", parse_dates=["data"])
mensal = base.groupby("mes")["total"].sum()
por_categoria = base.groupby("categoria")["total"].sum().sort_values()

plt.figure(figsize=(5, 3.6))
plt.bar(por_categoria.index, por_categoria.values)
plt.savefig("canal_sem_h.png")
plt.show()