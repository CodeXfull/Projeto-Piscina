"""
Banco de Dados - Eng. De Software
Programador: Éverton 
Data: 15/04/2020
Alteração 
"""
import sqlite3  # importar o banco de dados em python
import random as r

"""
Obs: Para criar o banco de dados a coisa mais importante é estabelecer
a conexão em: conn = sqlite3.connect ('C:/Users/Thundertronics/Documents/sqllite/banco_dados.db')
    - Crie uma pasta em um local dentro de seu PC
    - Copie o local
    - Cole em:  conn = sqlite3.connect('COLE AQUI/ nome_banco_de_dados.db')
    ATENÇÃO: Barra deve estar assim / e não assim \

Para abrir o banco de dados utilize: https://sqliteonline.com/
"""

conn = sqlite3.connect('C:/Users/Developer/Google Drive/banco.db')

"""
Criar uma tabela no banco de dados precisa:
    - cursor: é um interador que permite navegar e manipular os registros do bd.
    - execute: lê e executa comandos SQL puro diretamente no bd.
"""

cursor = conn.cursor()


def criar_tabela_usuario():
    """
    Função que cria a tabela usuários dentro do banco de dados
    """
    try:
        cursor.execute("""
        CREATE TABLE usuario(
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT NOT NULL,
                senha TEXT NOT NULL, 
                user TEXT DEFAULT 'Monitor'                
        );
        """)

        cursor.execute("""
                    INSERT INTO usuario ( login, senha, user)
                    VALUES (?,?,?)
                    """, ('admin', 'admin', 'administrador'))

        conn.commit()

    except sqlite3.OperationalError:
        print('Voce já criou o banco de dados usuário e não pode criar novamente ')


def criar_tabela_agendamento():
    """
        Função que cria a tabela usuários dentro do banco de dados
    """
    try:
        cursor.execute("""
        CREATE TABLE agendamento(
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE NOT NULL,
                hora TIME NOT NULL   
        );
        """)

    except sqlite3.OperationalError:
        print('Voce já criou o banco de dados agendamento e não pode criar novamente')


def criar_tabela_sonoff():
    """
    Função para registrar das leituras do sonoff (Ligado/Desligado) em relação
    ao estado do motor e das luzes
    """
    try:
        cursor.execute("""
        CREATE TABLE sonoff(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            motor TEXT NOT NULL,
            luzes TEXT NOT NULL
        );
        """)

    except sqlite3.OperationalError:
        print('Voce já criou o banco de dados sobre a leitura do sonoff')


def cadastrar_usuario():
    try:
        # solicitando os dados ao usuário
        print('\nCadastre um usuário')
        p_login = input('Login: ')
        p_senha = input('Senha: ')
        p_user = input('Usuário ("Administrador","Gerente","Monitor"): ')

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO usuario ( login, senha, user)
        VALUES (?,?,?)
        """, (p_login, p_senha, p_user))

        conn.commit()

    except sqlite3.OperationalError:
        print('Você cometeu algo de errado ao colocar os dados')
    else:
        print('Cadastro realizado com sucesso')


def imprimir_usuarios_cadastrados():
    try:
        print('-='*40)
        print("Usuários Cadastrados".center(80))
        print('-=' * 40)

        # lendo os dados
        cursor.execute("""
        SELECT * FROM usuario;
        """)

        for linha in cursor.fetchall():
            print(linha)

        print('-' * 80)

    except sqlite3.OperationalError:
        print('Ocorreu um erro de comunição com o banco de dados')


def excluir_usuario():
    try:
        id_cliente = input('Digite o id da pessoa que deseja excluir: ')

        cursor.execute("""
        DELETE FROM usuario
        WHERE id = ? AND id != 1
        """, (id_cliente,))

        conn.commit()

    except sqlite3.OperationalError:
        print('Esse id não existe')
    else:
        print('Usuário excluído com sucesso')


def cadastrar_agendamento():
    try:
        # solicitando os dados ao usuário
        p_data = input('data (yyyy/mm/dd): ')
        p_hora = input('Hora (HH:MM): ')

        # inserindo dados na tabela
        cursor.execute("""
            INSERT INTO agendamento (data, hora)
            VALUES (?,?)
        """, (p_data, p_hora))

        conn.commit()
        print('Cadastro realizado com sucesso')

    except sqlite3.OperationalError:
        print('Você cometeu algo de errado ao colocar os dados')


def imprimir_agendamento():
    try:
        print('-=' * 20)
        print("Agendamento".center(40))
        print('-=' * 20)
        print(' ID     DATA       HORA')
        cursor.execute("""
        SELECT * FROM agendamento;
        """)

        for linha in cursor.fetchall():
            print(linha)

    except sqlite3.OperationalError:
        print('Ocorreu um erro de comunição com o banco de dados')
        print('-'*30)


def alterar_agendamento():
    # essa função imprimir agendamento só faz sentido a fins de testes pra consulta
    imprimir_agendamento()

    # solicitando os dados ao usuário
    print('\nDigite o ID de qual data deseja modificar')
    id_cliente = input('ID : ')
    p_data = input('data (yyyy/mm/dd): ')
    p_hora = input('Hora (HH:MM): ')

    cursor.execute("""
    UPDATE agendamento
    SET data = ?, hora = ?
    WHERE id = ?
    """, (p_data, p_hora, id_cliente))

    conn.commit()


def excluir_agendamento():
    try:
        imprimir_agendamento()
        print('\nDigite qual é o ID da data que deseja excluir')
        id_cliente = input('ID exluir: ')

        cursor.execute("""
        DELETE FROM agendamento
        WHERE id = ?
        """, (id_cliente,))

        conn.commit()

    except sqlite3.OperationalError:
        print('Esse id não existe')
    else:
        print('Agendamento excluído com sucesso')


def aquisicao_dados_sonoff():
    """
    Nessa função é inserido o estado de forma aleatória
    Porém é onde entra o estado do Sonoff em relação ao motor (Ligado/Desligado)
    Teria que criar essa implementação de leitura, ou seja, uma váriavel para receber
    """
    try:
        motor = r.choice(['Desligado','Ligado'])
        luzes = r.choice(['Desligado','Ligado'])

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO sonoff(motor, luzes)
        VALUES (?,?)
        """, (motor, luzes))

        conn.commit()

    except sqlite3.OperationalError:
        print('Você cometeu algo de errado ao colocar os dados')


def imprimir_estado_sonoff():
    aquisicao_dados_sonoff()
    print('-=' * 20)
    print("Sonoff".center(40))
    print('-=' * 20)
    print(' ID    MOTOR     LUZES')
    cursor.execute("""
            SELECT *FROM sonoff
            WHERE id = (SELECT MAX( id ) FROM sonoff)
        """)

    for linha in cursor.fetchall():
        print(linha)


def monitorar():
    imprimir_agendamento()
    imprimir_estado_sonoff()


def selecionar():
        teste = ''
        p_login = input('Login: ')
        p_senha = input('Senha: ')

        cursor.execute("""
        SELECT DISTINCT user
        FROM usuario
        WHERE login = ? AND senha = ? 
        """, (p_login, p_senha))

        try:
            for linha in cursor.fetchone():
                teste = linha
        except TypeError:
            print('Erro')
        else:
            return teste


criar_tabela_usuario()
criar_tabela_agendamento()
criar_tabela_sonoff()

while True:
    print('=' * 50)
    print("BANCO DE DADOS PISCINA".center(50))
    print('=' * 50)
    print('Faça LOGIN para continuar')
    res = selecionar()

    x = True
    while x:
        try:
            if res.lower() == 'gerente':
                print('\nDigite o que você deseja fazer: ')
                print('1 - Cadastrar Agendamento')
                print('2 - Imprimir Agendamento')
                print('3 - Editar horário/data de Agendamento')
                print('4 - Excluir Agendametno')
                print('5 - Ver Status')
                print('6 - Sair')
                num = int(input('Digite um número: '))

                if num == 1:
                    cadastrar_agendamento()
                elif num == 2:
                    imprimir_agendamento()
                elif num == 3:
                    alterar_agendamento()
                elif num == 4:
                    excluir_agendamento()
                elif num == 5:
                    monitorar()
                elif num == 6:
                    x = False
                else:
                    print('Número digitado inválido')

            elif res.lower() == 'administrador':
                print('\nDigite o que você deseja fazer: ')
                print('1 - Cadastrar Usuário')
                print('2 - Excluir Usuário')
                print('3-  imprimir usuários cadastrados')
                print('4 - Sair')
                num = int(input('Digite um número: '))

                if num == 1:
                    cadastrar_usuario()
                elif num == 2:
                    excluir_usuario()
                elif num == 3:
                    imprimir_usuarios_cadastrados()
                elif num == 4:
                    x = False
                else:
                    print('Número digitado inválido')

            elif res.lower() == 'monitor':
                print('\nDigite o que você deseja fazer: ')
                print('1 - Ver Status')
                print('2 - Saim')
                num = int(input('Digite um número: '))

                if num == 1:
                    monitorar()
                elif num == 2:
                    x = False
                else:
                    print('Número digitado inválido')
            else:
                print('User_Case Incorreto, peça para o administrados atualizar seu cadastro')

        except AttributeError:
            print('Você digitou usuário ou senha inválido')
            x = False
