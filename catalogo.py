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
# --- 3. CHAMADAS DA FUNÇÃO (Execução e Teste) ---
adicionar_livro("Clean Code", "Robert C. Martin")
adicionar_livro("Design Patterns", "Erich Gamma")
adicionar_livro("A Startup Enxuta", "Eric Reis")
# Note que sem estas chamadas, nada acontece, e o erro persistiria na execução!
listar_livros()
