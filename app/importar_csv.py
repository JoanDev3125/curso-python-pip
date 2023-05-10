import csv

def poblacion_mundial(path):
    list_general = []
    with open(path, "r") as filecsv:
        list_reader = csv.reader(filecsv, delimiter=",")
        header = next(list_reader)
        
        for row in list_reader:
            poblacion_world = zip(header, row)
            list_indv = {key:value for key, value in poblacion_world}
            list_general.append(list_indv)
    
    return list_general


def filtrar_poblacion(continente_poblacion):
    new_poblacion = []
    llave = []
    valor = []
    for item in continente_poblacion:
        list_poblacion ={
            "Pais" : item["Country/Territory"],
            "poblacion": item["2022 Population"]
        }
        new_poblacion.append(list_poblacion)
        llave.append(list_poblacion["Pais"])
        valor.append( int(list_poblacion["poblacion"]))
    return llave, valor, new_poblacion