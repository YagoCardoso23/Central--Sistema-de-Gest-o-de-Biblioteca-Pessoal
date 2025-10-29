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

    catalogo.append(novo_livro)
    proximo_id += 1 


def listar_livros():
    print("\n======== Catálogo da Biblioteca ========")

    #verifica se ha livros para evitar erros e dar um bom feedback
    if not catalogo:
        print("O catalogo está vazio")
        return #Termina a função aqui se não houver livros 
    
    #2. laço de repetição (for loop ):
    #Percorre cada item (que chamaremos de 'livros') dentro da lista 'catalogo'.
    for livro in catalogo:
        # 3. Formatação da Saída:
        # Usamos F-string para formatar os dados do dicionário 'livro'
        # e apresentá-los de forma amigável.
        print(f"ID: {livro['id']} | Título: {livro['titulo']:<30} | Autor: {livro['autor']:<20} | Status: {livro['status']}")
    
    print("========================================")

def buscar_livros(id_livros):
    # Percorre cada livro no catalogo 
    for livro in catalogo:
        #estruturar de 
        if livro['id'] == id_livros:

            return livro 
    return None


def devolver_livro(id_livro):
    livro = buscar_livros(id_livro)

    if livro:
        # A devolução SÓ ocorre se o status for 'Emprestado'
        if livro['status'] == "Emprestado":
            livro['status'] = "Disponível" 
            print(f"\nSUCESSO: Livro '{livro['titulo']}' devolvido.")
        else:
            # ERRO: Não pode devolver algo que não está emprestado
            print(f"\nERRO: Livro '{livro['titulo']}' já está {livro['status'].lower()}.")
    else:
        print(f"\nERRO: Livro com ID {id_livro} não encontrado.")


def emprestar_livro(id_livro):
    livro = buscar_livros(id_livro)

    if livro:
        # CONDIÇÃO DE SUCESSO: SÓ EMPRESTA se o status for "Disponível"
        if livro['status'] == "Disponível": 
            livro['status'] = "Emprestado" # MUDANÇA DE ESTADO
            print(f"\nSUCESSO: Livro '{livro['titulo']}' emprestado.")
        else:
            # CONDIÇÃO DE ERRO: Já está em outro estado (Emprestado)
            print(f"\nERRO: Livro '{livro['titulo']}' já está {livro['status'].lower()}.")
    else:
        print(f"\nERRO: Livro com ID {id_livro} não encontrado.")


# --- 3. CHAMADAS DA FUNÇÃO (Execução e Teste) ---
# --- 4. CHAMADAS DE TESTE (Execução) ---
print("\n--- INICIANDO O SISTEMA ---")
adicionar_livro("Clean Code", "Robert C. Martin") # ID 1
adicionar_livro("Design Patterns", "Erich Gamma")  # ID 2
adicionar_livro("A Startup Enxuta", "Eric Ries")    # ID 3

print("\n--- TESTE 1: Estado Inicial ---")
listar_livros() 

# --- AÇÃO 1: Emprestar um livro disponível (ID 1)
emprestar_livro(1)

# --- AÇÃO 2: Tentar emprestar o mesmo livro (ID 1) novamente (DEVE DAR ERRO)
emprestar_livro(1)

# --- AÇÃO 3: Tentar devolver um livro disponível (ID 2) (DEVE DAR ERRO)
devolver_livro(2)

# --- AÇÃO 4: Devolver o livro emprestado (ID 1)
devolver_livro(1)

# --- AÇÃO 5: Listar novamente para ver a mudança de status
print("\n--- TESTE 2: Estado Final ---")
listar_livros()