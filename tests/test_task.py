import time
import pytest
from pyTask import Task

def test_task_execution():
    """Prueba la ejecución de una tarea básica."""
    def sample_task(a, b):
        return a + b

    task = Task(sample_task, 5, 3)
    task.start()
    result = task.wait()
    assert result == 8, "La tarea debería retornar 8 como resultado de 5 + 3"

def test_task_with_exception():
    """Prueba la gestión de excepciones dentro de una tarea."""
    def sample_task(a, b):
        return a / b  # Esta operación generará una excepción si b es 0

    task = Task(sample_task, 5, 0)
    task.start()
    with pytest.raises(ZeroDivisionError):
        task.wait()

def test_task_with_callback():
    """Prueba el callback de una tarea."""
    def sample_task(a, b):
        return a + b

    callback_result = []

    def callback(result):
        callback_result.append(result)

    task = Task(sample_task, 10, 20, callback=callback)
    task.start()
    task.wait()

    assert callback_result == [30], "El callback debería recibir el resultado 30"

def test_task_is_completed():
    """Verifica si is_completed funciona correctamente."""
    def sample_task():
        time.sleep(1)
        return "done"

    task = Task(sample_task)
    task.start()
    assert not task.is_completed(), "La tarea no debería estar completada inmediatamente después de iniciar"
    task.wait()
    assert task.is_completed(), "La tarea debería estar completada después de esperar su finalización"

def test_task_cancel():
    """Prueba la función de cancelación de una tarea."""
    def sample_task():
        time.sleep(5)
        return "done"

    task = Task(sample_task)
    task.start()
    task.cancel()
    assert task.is_completed(), "La tarea debería estar marcada como completada después de cancelarla"
