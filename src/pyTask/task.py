import threading
import queue
import time
from functools import wraps

class Task:
    """
    Implementación de una clase Task basada en hilos (threads).
    Permite ejecutar tareas de manera concurrente y opcionalmente usar un callback al finalizar.
    """

    def __init__(self, target, *args, callback=None, **kwargs):
        self.target = target  # Función a ejecutar como tarea
        self.args = args      # Argumentos posicionales para la tarea
        self.kwargs = kwargs  # Argumentos nombrados para la tarea
        self.callback = callback  # Callback opcional para ejecutar cuando termine la tarea
        self.result = None    # Resultado de la tarea
        self.exception = None # Excepción ocurrida durante la ejecución (si existe)
        self._queue = queue.Queue()  # Cola para manejo de resultado
        self._thread = threading.Thread(target=self._run)  # Hilo dedicado a la tarea
        self._completed = threading.Event()  # Evento para señalizar completitud

    def _run(self):
        """Método privado para ejecutar la tarea dentro del hilo."""
        try:
            self.result = self.target(*self.args, **self.kwargs)  # Ejecuta la tarea
        except Exception as e:
            self.exception = e  # Captura excepciones si ocurren
        finally:
            self._queue.put(self.result)  # Inserta el resultado en la cola
            self._completed.set()  # Marca la tarea como completada

            # Ejecutar callback si está definido
            if self.callback:
                self.callback(self.result)

    def start(self):
        """Inicia la tarea en un hilo separado."""
        self._thread.start()  # Inicia el hilo

    def wait(self, timeout=None):
        """
        Espera a que la tarea finalice.
        Puede aceptar un timeout opcional en segundos.
        """
        self._completed.wait(timeout)  # Espera a que la tarea se complete
        if self.exception:
            raise self.exception  # Si hubo excepción, la lanza
        return self.result  # Retorna el resultado final de la tarea

    def is_completed(self):
        """Verifica si la tarea ya ha sido completada."""
        return self._completed.is_set()

    def cancel(self):
        """Cancela la tarea si está en ejecución."""
        if not self.is_completed():
            self._completed.set()  # Marca como completada para "cancelarla"

    @staticmethod
    def task_decorator(func):
        """
        Decorador para convertir una función en una Task automáticamente.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            task = Task(func, *args, **kwargs)
            task.start()  # Inicia la tarea automáticamente
            return task  # Retorna la instancia de Task
        return wrapper

# Ejemplo de uso con callback
def suma(a, b):
    time.sleep(2)  # Simula un proceso de larga duración
    return a + b

def resultado_callback(resultado):
    print(f"Callback recibido: El resultado de la suma es {resultado}")

# Crear una tarea con callback
task = Task(suma, 5, 10, callback=resultado_callback)
task.start()  # Iniciar la tarea

# Esperar la tarea para obtener el resultado (opcional)
resultado = task.wait()
print(f"Resultado final: {resultado}")

# Ejemplo de uso con decorador
@Task.task_decorator
def multiplicacion(a, b):
    time.sleep(2)
    return a * b

# Crear tarea automáticamente con el decorador
task_multiplicacion = multiplicacion(5, 3)
resultado_multiplicacion = task_multiplicacion.wait()
print(f"Resultado de la multiplicación: {resultado_multiplicacion}")
