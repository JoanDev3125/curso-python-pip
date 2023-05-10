import matplotlib.pyplot as plt

def graficar_poblacion(item, valores, continente):
    fig, ax = plt.subplots()
    ax.pie(valores, labels=item)
    ax.axis("equal")
    plt.savefig(f"./app/{continente}.png")
    plt.close()
