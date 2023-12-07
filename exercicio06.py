"""
vamos supor que precisamos criar um programa
para cadastrar alunos em uma escola,
armazenando informaçoes como nome, idade e
nota. podemos utilizar um dicionario para
representar cada aluno, onde a chave sera o 
numero de matricula e o valor sera outro
dicionario contendo as informaçoes do aluno.
"""
alunos = {}

def cadastrar_aluno(matricula, nome, idade, nota):
    # verifica se a matrícula já está em uso
    if matricula in alunos:
        print("Matrícula já em uso. Escolha outra.")
    else:
        # cria um dicionário com as informações do aluno
        aluno_info = {'Nome': nome, 'Idade': idade, 'Nota': nota}
        
        # adiciona o aluno ao dicionário de alunos
        alunos[matricula] = aluno_info
        print(f"Aluno cadastrado com sucesso. Matrícula: {matricula}")

def exibir_alunos():
    # exibe a lista de alunos cadastrados
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de Alunos:")
        for matricula, info in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {info['Nome']}, Idade: {info['Idade']}, Nota: {info['Nota']}")

# exemplo de uso
cadastrar_aluno(1, "João", 15, 8.5)
cadastrar_aluno(2, "Maria", 16, 9.0)

exibir_alunos()
