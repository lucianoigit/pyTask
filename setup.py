from setuptools import setup, find_packages

setup(
    name="tasklib",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Tu Nombre",
    description="Librería para ejecutar tareas concurrentes con hilos",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)