'''
Autor: Damian Safdie
Version: 1.0

Descripcion: ejercicio de profundizacion 
'''

__author__ = "Damian Safdie"
__email__ = "damiansafdie@gmail.com "
__version__ = "1.0"


import requests
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


# Crear el motor (engine) de la base de datos
engine = sqlalchemy.create_engine("sqlite:///usuarios.db")
base = declarative_base()


class Usuario(base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    userId = Column(Integer)
    title = Column(String)
    completed = Column(String)
    
    def __repr__(self):
        return f"Titulo: {self.title}"


def create_schema():   
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)


def fill():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()

    Session = sessionmaker(bind=engine)
    session = Session()

    for usuario in data:
        usu = Usuario(id = usuario["id"], userId = usuario["userId"],
                title = usuario["title"], completed = usuario["completed"])
        session.add(usu)            
    session.commit()
    

def title_completed_count(userId):
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # completed ----> 1=true 0=false
    result = session.query(Usuario).filter((Usuario.userId == userId) & (Usuario.completed == 1)).count()
    print('cantidad : ', result)
    return


if __name__ == '__main__':
    create_schema()  
    fill()   

    while True:
        id =  int(input ("Ingrese el ID a buscar [0=fin]: "))
        if id == 0:
            break
        title_completed_count(id)
    
 

 
