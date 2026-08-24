aluno = {
    "nome": "Leandro ",
    "idade": 20,
    "notas": [8.5, 7.0, 9.0]
}

print("--- DADOS DO ALUNO ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Notas: {aluno['notas']}")


media = sum(aluno['notas']) / len(aluno['notas'])
print(f"Média das notas: {media:.2f}")