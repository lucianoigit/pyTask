# pyTask/__init__.py

# Importa la clase Task desde task.py
from .task import Task

# Exponer solo Task y su decorador si es necesario
__all__ = ['Task']
