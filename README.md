![GitHub language count](https://img.shields.io/github/languages/count/CodeXfull/Projeto-Piscina) ![GitHub top language](https://img.shields.io/github/languages/top/CodeXfull/Projeto-Piscina) 

# Projeto-Piscina
Esse projeto é para automatizar uma piscina, isto é, ligar o motor e as luzes com um sonoff por meio de integração Python e banco de dados SQLite. Esse é o primeiro escopo do projeto e teste com o Python. 

## Sou iniciante em programação em Python, com certeza existem maneiras melhores de fazer essa manipulaçao com o sqlite. Foi o jeito que encontrei e esse é meu 1º projeto.

### 1º importe o sqlite no Python. Lembrando que ele é built-in.
![Importando Banco](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/importar.png)

### 2º salvar o banco de dados em uma pasta dentro do seu pc
Ela vai servir para que o banco de dados gerado seja criado dentro de uma pasta do seu pc e seus dados ficarem armazenados. No meu caso coloquei dentro do Google Drive pq já faz a sincronização com a nuvem.

![criando a conexão](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/python.gif)

### 3º criar cursor
Em python para criar uma tabela precisamos de um cursor e um execute:
   * cursor: é um interador que permite navegar e manipular os registros no banco de dados.
   * execute: lê e executa comandos SQL puro diretamente no banco de dados. 
   
![cursor](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/cursor.png)

### 4º Criando uma tabela

Sintaxe:
CREATE TABLE nome_da_tabela{}

![criando](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/criar%20tabela.png)

### 5º Cadastrar algo na tabela

Sintaxe: 
INSERT INTO nome_da_tabela{} 

Lembrando que esse método que está apresentado abaixo é se vc quer pegar entradas do usuário, senão só coloque cursor.execute... e precisa do con.commit() tbm pq ele serve para gravar as alterações no banco de dados 

 ![cadastro](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/cadastra_usuario.png)
 
 ### 6º Imprimir o que está cadastrado 
 Aqui estou colocando um imprimir da parte que está dentro da função imprimir_agendamento
 
 Sintaxe:
 SELECT *FROM nome_da_tabela
 
 ![Imprimir](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/imprimir.png)
 
 ### 7º Alterando dados de uma tabela
 
 ![Alterar Dados](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/alterar_dados.png)
 
 ### 8º Excluir algo da tabela 
 
 ![excluir](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/excluir_algo_da_tabela.png)
 
 ### 9º Pegar o último dado cadastrado
 
 ![](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/pega_ultimo_dado_cadastrado.png)
 
 ### 10º Login
 Essa é uma parte mto importante porque a pessoa precisa fazer login e senha para acessar o sistema, além disso, conforme o tipo de user que é vai abrir determinadas possibilidades de uso.
 
 ![login](https://github.com/CodeXfull/Projeto-Piscina/blob/master/arquivos/fazer_login.png)
 
 ### Dica de ouro: para abrir o banco de dados online e ver se tudo esta funcionando [SQL online](https://sqliteonline.com/)
