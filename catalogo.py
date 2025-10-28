# A "prateleira" da sua biblioteca: uma lista vazia.
# Ela armazenará dicionários (que são os livros).
catalogo = []

# Variável para gerar IDs únicos automaticamente.
# Como é o primeiro livro, o próximo ID será 1.
proximo_id = 1 

# Funções (def) são blocos de código que fazem uma tarefa específica.
def adicionar_livro(titulo, autor):
  
# Precisamos avisar que vamos alterar as variáveis globais 'catalogo' e 'proximo_id'
    # 'global' é usado quando modificamos variáveis definidas fora da função
  global catalogo
  global proximo_id



