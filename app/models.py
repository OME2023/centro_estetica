from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime  # Agregamos la importación para obtener la fecha actual

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dni = Column(String(20))
    nombre_apellido = Column(String(100))
    edad = Column(Integer)
    antecedentes_personales = Column(String)
    antecedentes_hereditarios = Column(String)
    alergia = Column(String)
    medicacion = Column(String)
    fecha_alta = Column(DateTime, default=datetime.now)  # Añadimos el campo de fecha de alta

    def serialize(self):
        return {
            'id': self.id,
            'dni': self.dni,
            'nombre_apellido': self.nombre_apellido,
            'edad': self.edad,
            'antecedentes_personales': self.antecedentes_personales,
            'antecedentes_hereditarios': self.antecedentes_hereditarios,
            'alergia': self.alergia,
            'medicacion': self.medicacion,
            'fecha_alta': self.fecha_alta.strftime("%Y-%m-%d %H:%M:%S")  # Convertimos la fecha a string para serializar
        }

    @staticmethod
    def inicializar_base_datos(url):
        engine = create_engine(url)
        Base.metadata.create_all(bind=engine)
