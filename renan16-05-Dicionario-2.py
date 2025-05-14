#ARQUIVO DICIONÁRIOS
#Tarefas:
#- Crie um dicionário chamado alunos
#  para armazenar o nome dos alunos e suas respectivas notas.
#- Inicialize o dicionário com os seguintes alunos e notas:
#"Ana": 8.5
#"Pedro": 7.0
#"Maria": 9.2
#Adicione o aluno "Carlos" com nota 6.5 ao dicionário alunos.
#- Atualize a nota da aluna "Ana" para 9.0.
#- Remova o aluno "Pedro" do dicionário alunos.
# Calcule a média das notas dos alunos presentes no dicionário alunos.
# Verifique se o aluno "Maria" está presente no dicionário
#  e imprima uma mensagem informando se o aluno está ou não no dicionário.
alunos = {'Ana':8.5, 'Pedro':7.0, 'Maria':9.2}
alunos['Carlos'] = 6.5
alunos['Ana'] = 9.0
del alunos['Pedro']
print(alunos)
print(alunos.get('maria', 'Maria, Esta no Dicionario!'))

import statistics 
media = statistics.mean(alunos.values())

print(f'A Media dos alunos, Ana, Maria e Carlos é: {media}')
