# --- 1. VARIÁVEIS GLOBAIS ---
# A "prateleira" da sua biblioteca: uma lista vazia.
catalogo = []

# Variável para gerar IDs únicos automaticamente.
proximo_id = 1 

# --- 2. DEFINIÇÃO DA FUNÇÃO (Lógica) ---
def adicionar_livro(titulo, autor):
    
    # IMPORTANTE: Estas linhas devem estar identadas (4 espaços) para estarem dentro da função.
    global catalogo
    global proximo_id

    # 1. Cria o dicionario do livro
    novo_livro = {
        "id": proximo_id,
        "titulo": titulo,
        "autor": autor,
        "status": "Disponível" # Corrigido para 'Disponível' para padrão
    }

    # 2. Adicionar o novo livro ao catálogo
    catalogo.append(novo_livro)

    # 3. Atualizar ID e imprimir feedback
    print(f"Livro '{titulo}' (ID: {proximo_id}) adicionado ao catálogo.")
    proximo_id += 1 # A lógica para gerar IDs unicas


# --- 3. CHAMADAS DA FUNÇÃO (Execução e Teste) ---
adicionar_livro("Clean Code", "Robert C. Martin")
adicionar_livro("Design Patterns", "Erich Gamma")
# Note que sem estas chamadas, nada acontece, e o erro persistiria na execução!

# Imprime o catálogo final
print("\n--- Catálogo Atual ---")
print(catalogo)