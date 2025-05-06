from app import app, db
from models import ImagenesScala
import ast
import json

with app.app_context():
    registros = ImagenesScala.query.all()
    for r in registros:
        if isinstance(r.colors, str):
            try:
                # Intenta convertir el string a dict
                dict_color = ast.literal_eval(r.colors)
                r.colors = dict_color
                print(f"Corrigiendo registro {r.id}")
            except Exception as e:
                print(f"Error en registro {r.id}: {e}")
    db.session.commit()
