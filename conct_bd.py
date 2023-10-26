#TESTE DE CONECÇÃO BD

import mysql.connector
#config ={
#    "host":"127.0.0.1",
#    "password":"root",}
#try:
#    con = mysql.connector.connect(**config)
#    if con.is_connected():
#        print("Deu certo!")
#except mysql.connector.Error as erro:
#    print(erro)

#CONECTAR BD

config = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "root",
    database = "mydb"
)

cursor = config.cursor()

def criar_cliente(nome,email,telefone):
    sql = "INSERT INTO pessoa (nome,email,telefone) VALUES (%s,%s, %s)"
    val = (nome, email, telefone)
    cursor.execute(sql,val)
    config.commit()
    print("Cliente iserido com sucesso!")

def listar_cliente():
    cursor.execute("SELECT * FROM pessoa")
    pessoas = cursor.fetchall()
    for pessoa in pessoas:
        print(pessoa)

def atualizar_cliente(idpessoa, nome, email, telefone):
    sql = "UPDATE pessoa SET nome = %s, email = %s, telefone = %s WHERE idpessoa = %s"
    val = (nome, email, telefone, idpessoa)
    cursor.execute(sql,val)
    config.commit()

def deletar_cliente(idpessoa):
    sql = "DELETE FROM pessoa WHERE idpessoa = %s"
    val = (idpessoa,)
    cursor.execute(sql, val)
    config.commit
    print("Cliente deletado com sucesso!")

while True:

    print("\n")
    print("--------------- MENU ---------------")
    print("1. Adicionar pessoa.")
    print("2. Listar pessoas.")
    print("3. Atualizar pessoa.")
    print("4. Deletar pessoa.")
    print("5. Sair.")
    print("\n")
    op = str(input("Escolha uma opção: "))

    if op == "1":
        nome = str(input("Digite o nome da pessoa: "))
        email = str(input("Digite o e-mail da pessoa: "))
        telefone = float(input("Digite o telefone da pessoa: "))
        criar_cliente(nome,email,telefone)

    if op == "2":
        listar_cliente()

    if op == "3":
        idpessoa = int(input("Digite o ID da pessoa: "))
        nome = str(input("Digite o nome da pessoa: "))
        email = str(input("Digite o e-mail da pessoa: "))
        telefone = float(input("Digite o telefone da pessoa: "))
        atualizar_cliente(idpessoa, nome, email, telefone)
    if op == "4":
        idpessoa = int(input("Digite o ID da pessoa: "))
        deletar_cliente(idpessoa)
    
    if op == "5":
        break 