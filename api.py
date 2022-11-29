import flask
from flask import request
from flask.globals import g

import mysql.connector as MySQLConnector

# Iniciarlização do banco de dados
#  adicionamos o handle do conector no contexto do
#  app do flask.
def init_db():
    g.db = MySQLConnector.connect(
        host = "localhost",
        user = "root",
        password = "alunoaluno",database = "petshop"
    )
    return g.db

# Recupera o handle do banco de dados
def get_db():
    if "db" not in g:
        g.db = init_db()
    
    return g.db

# Inicialização da aplicação flask
def init_app():
    app = flask.Flask(__name__)

    with app.app_context():
        init_db()

    return app

app = init_app()

# Fechamos a conexão com o banco de dados
#  quando a aplicação se encerra.
@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# Rota raiz que diz se você conseguiu se conectar no banco de dados
@app.route("/")
def index():
    db = get_db()

    return "Is connected? %s" % ("Yes" if db.is_connected else "No")

# Implementar rota de listar todos os pets
# utilizando a conexão através do init_db()
@app.route("/pet", methods=["GET"])
def list_all_pets():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM pets")
    return c.fetchall()

# Implementar rota de listar um pet em específico
# Mostrar nome do dono/responsável ao invés do id
@app.route("/pet/<pet_id>", methods=["GET"])
def list_pet_by_id(pet_id):
    db = get_db()
    c = db.cursor()
    c.execute(f"""SELECT id_pet,nome_pet,tipo_pet,raca,(select nome from responsavel r where p.respon_fk = r.id_respon)  FROM pet p
    where id_pet = {pet_id}""")
    return c.fetchall()

# Implementar rota pra inserção de um pet
# o método padrão é POST
@app.route("/pet/cadas_pet", methods=["POST"])
def insert_pet():
    # dados recebidos através do método post
    pet_data = request.form # dicionário contendo todos os dados recebidos de um pet
    nome_pet = pet_data["nome_pet"]
    tipo_pet = pet_data["tipo_pet"]
    raca = pet_data["raca"]
    respon_fk = pet_data["respon_fk"]
    db = get_db()
    c = db.cursor()
    c.execute(f"""insert into pet (nome_pet,tipo_pet,raca,respon_fk) values ('{nome_pet}','{tipo_pet}','{raca}',{respon_fk}) """)
    db.commit()
    return "ok"
