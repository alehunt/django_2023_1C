from setuptools import setup
setup(
    name="paquete",
    version="0.1",
    description="Este es un paquete de ejemplo",
    author="Codo a Codo",
    author_email="io.codoacodo@bue.edu.ar",
    url="https://www.buenosaires.gob.ar/educacion/codo-codo",
    packages=['paquete','paquete.hola','paquete.adios'],
    scripts=[]
)
