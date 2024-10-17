from setuptools import setup, find_packages

setup(
    name="pyTask",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Luciano Iriarte",
    description="Librería para ejecutar tareas concurrentes con hilos",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
