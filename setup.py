from setuptools import setup, find_packages

# Cargar dependencias desde requirements.txt
with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setup(
    name="pyTask",
    version="0.1.0",
    packages=find_packages(),  # Busca paquetes en el directorio raíz
    install_requires=requirements,  # Usa las dependencias cargadas desde requirements.txt
    author="Luciano Iriarte",
    description="Library for executing concurrent tasks with threads",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Requisito de versión de Python
)
