

from pyTask import Task


def mi_funcion(a, b):
    return a + b

def mi_callback(resultado):
    print(f"Resultado obtenido: {resultado}")

task = Task(mi_funcion, 5, 10, callback=mi_callback)
task.start()
