import unicodedata

print("=" * 40)
print(" AVEDEX")
print("=" * 40)

nome_usuario = input("Digite seu nome: ").strip()
opcao_menu = ""

def exibir_linha():
    print("=" * 40)

def exibir_menu():
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Sobre a AveDex")
    print("0 - Sair")

def mostrar_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")
    print("Aqui vamos conhecer aves e praticar boas práticas.")
    
def listar_aves(catalogo):
    print()
    exibir_linha()
    print("AVES CADASTRADAS")
    exibir_linha()

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")
    
def mostrar_curiosidade():
    print("Curiosidade:")
    print("Muitas aves ajudam no equilíbrio ambiental ao dispersar sementes.")
    
def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex será um catálogo interativo de aves.")
    
def pausar():
    input("\nPressione ENTER para voltar ao menu...")

def buscar_ave_por_id(catalogo, codigo_procurado):
    for ave in catalogo:
        if ave["id"] == codigo_procurado:
            return ave
    return None

def buscar_aves(catalogo, termo_busca):
    resultados = []

    termo = normalizar_texto(termo_busca)

    for ave in catalogo:
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        texto_busca = " ".join(campos_busca)
        texto_busca = normalizar_texto(texto_busca)

        if termo in texto_busca:
            resultados.append(ave)
    return resultados

def exibir_resultados_busca(resultados):
    print()
    print("=" * 50)
    print("RESULTADOS DA BUSCA")
    print("=" * 50)

    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        for ave in resultados:
            print(
            f"{ave['id']} - {ave['nome_popular']} "
            f"({ave['familia']}, {ave['dieta_tipo']})"
            )

def tela_busca(catalogo):

    termo = input("Digite parte do nome, família, ordem ou dieta: ").strip()

    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return

    resultados = buscar_aves(catalogo, termo)
    exibir_resultados_busca(resultados)

    if len(resultados) > 0:
        
        escolha = input("\nDigite o ID para ver detalhes ou ENTER para voltar: ").strip()

        if escolha != "":
            ave_encontrada = buscar_ave_por_id(resultados, escolha)

        if ave_encontrada is None:
            print("ID não encontrado nos resultados.")

        else:
            exibir_detalhes(ave_encontrada)

def normalizar_texto(texto):
    texto = str(texto)
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    return texto

    
def exibir_detalhes(ave):
    print()
    exibir_linha()
    print("DETALHES DA AVE")
    exibir_linha()
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave['curiosidade']}")

catalogo_aves = [
    {
        "id": "1",
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto lembra a expressão bem-te-vi."
    },
    {
        "id": "2",
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos, áreas abertas e ambientes rurais",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "O macho possui plumagem amarela intensa."
    },
    {
        "id": "3",
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e outros pequenos invertebrados",
        "curiosidade": "Constrói um ninho de barro característico."
    },
    {
        "id": "4",
        "nome_popular": "Patola-de-pés-azuis",
        "nome_cientifico": "Sula nebouxii",
        "ordem": "Suliformes",
        "familia": "Sulidae",
        "dieta_tipo": "piscívora",
        "habitat": "Ilhas tropicais",
        "alimentacao": "Diversos peixes",
        "curiosidade": "Possuem pés azuis"
    },
    {
        "id": "5",
        "nome_popular": "secretária",
        "nome_cientifico": "Sagittarius serpentarius",
        "ordem": "Accipitriformes",
        "familia": "Sagittariidae",
        "dieta_tipo": "carnivora",
        "habitat": "Planices e savanas",
        "alimentacao": "Insetos e pequenos vertebrados",
        "curiosidade": "Pisoteiam suas presas, são conhecidas por caçarem cobras."
    }
]

while opcao_menu != "0":
    exibir_menu()
    opcao_menu = input("Escolha uma opção: ").strip()
    
    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        tela_busca(catalogo_aves)

    elif opcao_menu == "3":
        listar_aves(catalogo_aves)
        id = input("Digite o id da ave: ")
        selecionar_ave_por_id(catalogo_aves, id)

    elif opcao_menu == "4":
        print("A AveDex é um catálogo interativo de aves.")
        print("Em breve, teremos comparação, imagens, sons e dados em arquivo JSON.")
    
    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    else:
        print("Opção inválida. Digite apenas 0, 1, 2, 3 ou 4.")