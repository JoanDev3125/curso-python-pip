import matplotlib.pyplot as plt

def generar_pie_chart():
    labels =["A", "B", "C"]
    values = [200, 34, 150]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("./img/pie.png")
    plt.close()