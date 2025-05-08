from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy.dialects.postgresql import JSON

from app import db

# CLASE
class ImagenesScala(db.Model):
    """
    Modelo de base de datos que representa un registro de análisis de una imagen BMP
    enviado desde una aplicación externa, como un programa Scala.

    Atributos:
        id (int): Identificador único del registro (clave primaria).
        filename (str): Nombre del archivo BMP analizado (sin ruta).
        username (str): Nombre del usuario que realizó el análisis.
        colors (JSON): Diccionario JSON que contiene el conteo de píxeles por color.
        timestamp (datetime): Fecha y hora en que se generó el análisis.

    Este modelo se utiliza para almacenar resultados enviados a través de la API `/upload`,
    y es visualizado desde la interfaz web mediante la ruta `/analisis`.

    Métodos:
        __str__(): Devuelve una representación legible del registro, combinando
                   nombre de archivo, usuario y fecha.
    """
    __tablename__ = 'imagenes_scala'
    id = Column(Integer, primary_key=True)
    filename = Column(String(100))
    username = Column(String(50))
    colors = Column(JSON)
    timestamp = Column(DateTime)

    def __str__(self):
        return f"{self.filename} - {self.username} - {self.timestamp}"

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    street_address = Column(String(50))
    description = Column(String(250))

    def __str__(self):
        return self.name

class Review(db.Model):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    restaurant = Column(Integer, ForeignKey('restaurant.id', ondelete="CASCADE"))
    user_name = Column(String(30))
    rating = Column(Integer)
    review_text = Column(String(500))
    review_date = Column(DateTime)

    @validates('rating')
    def validate_rating(self, key, value):
        assert value is None or (1 <= value <= 5)
        return value

    def __str__(self):
        return f"{self.user_name}: {self.review_date:%x}"
