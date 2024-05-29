from flask import Blueprint, render_template
from . import db

bp = Blueprint('actor', __name__, url_prefix='/actores')

@bp. route('/')
def actor():
    consulta = """
     SELECT first_name,last_name FROM actor
     ORDER BY first_name ;
 """
    con = db.get_db()
    res = con.execute(consulta)
    lista_actores = res.fetchall()
    pagina = render_template('actor.html',
                            actores=lista_actores)
    return pagina

