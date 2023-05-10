
import importar_csv
import charts as ch

def run():
   
    poblacion_mundial = importar_csv.poblacion_mundial("./app/world_population.csv")
    

    continente = input("Ingresa un continente: ")
    continente_poblacion = list(filter(lambda item: item["Continent"] == continente, poblacion_mundial)) 
    
    #print(poblacion_mundial)

    llave, valor, filtrar_poblacion = importar_csv.filtrar_poblacion(continente_poblacion)

    ch.graficar_poblacion(llave, valor, continente)

if __name__ == "__main__":
    run()