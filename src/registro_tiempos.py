import pandas
import time

class RegistrodeTiempos:

    def __init__(self,nombre_estructura,nombre_funcionalidad,n_datos):
        self.registro = list()
        self.nombre_estructura = nombre_estructura
        self.nombre_funcionalidad = nombre_funcionalidad
        self.n_datos = n_datos

        self.tiempo_inicio = 0
        self.tiempo_fin = 0
    
    def iniciar_conteo(self):
        self.tiempo_inicio = time.time()

    def finalizar_conteo(self):
        self.tiempo_fin = time.time()
        self.registro.append(self.tiempo_inicio-self.tiempo_fin)

    def retornar_registro(self):
        datos = pandas.DataFrame(data=self.registro,index=range(1,len(self.registro)+1))
        datos.to_csv("{}_{}_{}_datos.csv".format(self.nombre_funcionalidad,self.nombre_estructura,self.n_datos),index=range(0,len(self.registro)+1))