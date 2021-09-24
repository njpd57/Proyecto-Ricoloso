from distutils.core import setup 
import py2exe 
""" El profe se la come """
setup(name="Proyecto Ricoloso", 
 version="4.20", 
 description="Descarga videos de porHub", 
 author="ElEntrepiernaSudada", 
 author_email="miraLaWachas@conElMeotrasero.es", 
 url="https://www.mipicoenturaja.ong", 
 license="MIT", 
 console=['main.py'],
 options={"py2exe": {"bundle_files": 1}}, 

 zipfile=None,
)
