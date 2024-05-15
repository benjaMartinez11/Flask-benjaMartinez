from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'boca!'

@app.route('/Yo')
def Yo():
    return '💛💙BOCA BOCA BOCA💛💙'

@app.reoute('actor')
def actor():
    consulta = """
        SELECT name FROM genres
        ORDER BY name;
    """
    con =db.get_db()
    res = con.execute(consulta)
    lista_actor = res.fetchall()
    pagina = render_template('actor.html',
                            generos=lista_actor)
    return pagina
