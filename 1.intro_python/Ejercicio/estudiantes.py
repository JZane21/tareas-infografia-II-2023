estudiantes = [
    {
        'nombre': 'juan',
        'apellido': 'perez',
        'notas': {
            'MAT': 30,
            'QMC': 30,
            'FIS': 30,
            'LAB': 30
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {
        'nombre': 'ana',
        'apellido': 'rivera',
        'notas': {
            'MAT': 98,
            'QMC': 98,
            'FIS': 98,
            'LAB': 98
        },
        'extras': [1],
        'asistencia': 100
    }
]


class Evaluador:
    """Esta clase implementa diversas funciones para calcular promedios
    de una lista de estudiantes y obtener otros datos adicionales, ademas,
    tambien implementa una funcion para escribir un reporte de notas"""
    def __init__(self, lista_estudiantes, min_asistencia, max_extras):
        self.lista_estudiantes = lista_estudiantes
        self.min_asistencia = min_asistencia
        self.max_extras = max_extras

    def _get_total_extras(self, estudiante) -> float:
        accum_extras = sum(estudiante["extras"]) if "extras" in estudiante else 0
        accum_extras = accum_extras if accum_extras<=self.max_extras else self.max_extras
        return accum_extras

    def _promedio_individual(self,estudiante) -> float:
        if ("notas" in estudiante) and (estudiante["asistencia"]>=self.min_asistencia):
            accum_extras = self._get_total_extras(estudiante)
            if (len(estudiante["notas"]) == 0):
                return 0
            accum = sum(estudiante["notas"].values()) / len(estudiante["notas"])
            if accum == 0:
                return 0
            return accum + accum_extras if (accum + accum_extras) <= 100 else 100
        else:
            return 0

    def _get_nombre_completo(self,estudiante):
        nombre_final = estudiante["nombre"].capitalize() + " " + estudiante["apellido"].capitalize()
        return nombre_final

    def calcular_promedios(self):
        import subprocess
        comando = "clear"
        subprocess.run(comando, shell=True, capture_output=False, text=False)
        # IMPLEMENTAR METODO
        lista_notas = []
        for estudiante in self.lista_estudiantes:
            lista_notas.append(
                {
                    "nombre completo": self._get_nombre_completo(estudiante),
                    "promedio": self._promedio_individual(estudiante)
                }
            )
        return lista_notas

    def obtener_mejor_estudiante(self):
        # IMPLEMENTAR METODO
        mejor_estudiante = {"nombre completo":"","promedio":-1}
        for estudiante in self.lista_estudiantes:
            promedio_obtenido = self._promedio_individual(estudiante)
            mejor_estudiante = {
                "nombre completo": self._get_nombre_completo(estudiante),
                "promedio": promedio_obtenido
            } if mejor_estudiante["promedio"] < promedio_obtenido else mejor_estudiante
        return mejor_estudiante

    def salvar_datos(self, nombre_archivo):
        # IMPLEMENTAR METODO
        import csv
        # Datos para este ejercicio:
        estudiantes = [
            {
                'nombre': 'juan',
                'apellido': 'perez',
                'notas': {
                    'MAT': 30,
                    'QMC': 30,
                    'FIS': 30,
                    'LAB': 30
                },
                'extras': [2, 3, 1, 1, 1],
                'asistencia': 90
            },
            {
                'nombre': 'ana',
                'apellido': 'rivera',
                'notas': {
                    'MAT': 98,
                    'QMC': 98,
                    'FIS': 98,
                    'LAB': 98
                },
                'extras': [1],
                'asistencia': 100
            },
            {
                'nombre': 'sara',
                'apellido': 'mantilla',
                'notas': {
                    'MAT': 0,
                    'QMC': 0,
                    'FIS': 0,
                    'LAB': 0
                },
                'extras': [2,2,1],
                'asistencia': 100
            },
            {
                'nombre': 'roberto',
                'apellido': 'condarco',
                'notas': {
                    'MAT': 0,
                    'QMC': 0,
                    'FIS': 0,
                    'LAB': 0
                },
                'extras': [1,1,3],
                'asistencia': 100
            },
            {
                'nombre': 'jerjes',
                'apellido': 'suarez',
                'notas': {
                    'MAT': 78,
                    'QMC': 78,
                    'FIS': 78,
                    'LAB': 78
                },
                'extras': [1,4],
                'asistencia': 60
            },
            {
                'nombre': 'arnold',
                'apellido': 'ricaldi',
                'notas': {
                    'MAT': 0,
                    'QMC': 0,
                    'FIS': 0,
                    'LAB': 0
                },
                'extras': [2],
                'asistencia': 90
            },
            {
                'nombre': 'ernesto',
                'apellido': 'massi',
                'notas': {
                    'MAT': 0,
                    'QMC': 0,
                    'FIS': 0,
                    'LAB': 0
                },
                'extras': [2,1],
                'asistencia': 90
            }
        ]
        
        
        with open(nombre_archivo,"w",newline="") as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                        quotechar=',', quoting=csv.QUOTE_MINIMAL)
            datos = ["Nombre Completo","Asistencia","MAT","FIS",
                "QMC","LAB","Total Extras","Promedio Final","Observacion"]
            informacion_estudiantes = [[] for _ in range (len(estudiantes))]
            spamwriter.writerow(datos)
            index = 0
            for i in estudiantes:
                nombre_completo = self._get_nombre_completo(i)
                informacion_estudiantes[index].append(nombre_completo)
                informacion_estudiantes[index].append(i["asistencia"] if "asistencia" in i else 0)
                if "notas" in i:
                    for j in i["notas"].values():
                        informacion_estudiantes[index].append(str(j))
                else:
                    for j in range(4):
                        informacion_estudiantes[index].append(0)
                informacion_estudiantes[index].append(self._get_total_extras(i))
                promedio_estudiante = self._promedio_individual(i)
                informacion_estudiantes[index].append(promedio_estudiante)
                informacion_estudiantes[index].append("APROBADO" if promedio_estudiante > 50  else "REPROBADO" )
                # for j in i.values():
                #     if isinstance(j,dict):
                #         for k in j.values():
                #             informacion_estudiantes[index].append(
                #             str(k)
                #         )
                #     elif isinstance(j,list):
                #         for k in j.values
                #     elif index!=1 and index!=0:
                #         informacion_estudiantes[index].append(str(j))
                index += 1
            for i in informacion_estudiantes:
                spamwriter.writerow(i)
        print('salvando datos')


# -----------------------------------------#
# ----> NO MODIFICAR DESDE AQUI! <---------#
# -----------------------------------------#
def comparar_archivo_notas(archivo):
    with open('ejemplo_notas.csv', 'r') as archivo_correcto:
        correcto_str = archivo_correcto.read()

    with open(archivo, 'r') as archivo:
        archivo_str = archivo.read()

    return correcto_str == archivo_str


if __name__ == '__main__':
    # datos iniciales
    nombre_archivo = 'notas.csv'
    notas_correcto = [{'nombre completo': 'Juan Perez', 'promedio': 35.0}, {'nombre completo': 'Ana Rivera', 'promedio': 99.0}]
    mejor_correcto = {'nombre completo': 'Ana Rivera', 'promedio': 99.0}

    # Instanciar evaluador
    evaluador = Evaluador(lista_estudiantes=estudiantes, min_asistencia=80, max_extras=5)
    # calcular promedios
    notas = evaluador.calcular_promedios()
    print(f'calcular_promedios: {notas}')
    if notas == notas_correcto:
        print('Calculo de promedios correcto!')
    else:
        print(f'ERROR, lista de promedios esperada: {notas_correcto}')
    # obtener mejor estudiante
    mejor = evaluador.obtener_mejor_estudiante()
    print(f'obtener_mejor_estudiante: {mejor}')
    if mejor == mejor_correcto:
        print('Mejor estudiante correcto!')
    else:
        print(f'ERROR, mejor estudiante esperado: {mejor_correcto}')
    # salvar datos en archivo
    evaluador.salvar_datos(nombre_archivo)
    if comparar_archivo_notas(nombre_archivo):
        print('Generacion de archivo correcta')
    else:
        print('Generacion de archivos incorrecta, ver archivo "ejemplo_notas.csv"')

'''
Su nombre es José Carrasco, tiene 20 años y actualmente estudia Ingeniería en Sistemas Computacionales en la UPB (Universidad Privada de Bolivia). Siempre le ha interesado el mundo de la tecnología y, por supuesto, formar parte de él. Es una persona amable, educada y responsable que siempre quiere ayudar a los demás, para que puedan hacer cosas que antes creían imposibles. Una de sus metas como graduado universitario con excelentes calificaciones, convertirse en Desarrollador Web FullStack, tiene un conocimiento sólido de IA, ya que cree que esta herramienta determinará el futuro progreso tecnológico y social de la humanidad. 
'''
