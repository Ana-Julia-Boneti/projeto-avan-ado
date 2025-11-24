def calcular_idade(idade):
     return idade.strip().title()            

def calcular_idade():
    idade = input("Digite a sua idade: ")
    preco = float(input("Digite o preço do produto: "))
    categoria = input("Digite a categoria do produto: ")
    return (calcular_idade(idade), preco, categoria)

def salvar_produto(produto):
    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[0]};{produto[1]};{produto[2]}\n"
        arquivo.write(linha)

def listar_produtos():
    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                idade, preco, categoria = linha.strip().split(";")
                preco, categoria = linha.strip().split(";")
                print(f"Produto: {idade} | Preço: R${preco} | Categoria: {categoria}")
    except FileNotFoundError:
        print("Nenhum produto cadastrado ainda.")
while True:
    print("\n1 - Calcular idade")
    print("2 - Listar produtos")
    print ("0 - sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        produto = calcular_idade()
        salvar_produto(produto)
    elif opcao == "2":
        listar_produtos()
    elif opcao == "0":
        break