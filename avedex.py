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
    print("4 - Comparar duas aves")
    print("5 - Sobre a AveDex")
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

def selecionar_ave_por_id(catalogo):
    listar_aves(catalogo)
    id_escolhido = input("\nDigite o ID da ave: ").strip()
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)
    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)

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
        print(len(resultados)," resultados encontrados")
        escolha = input("\nDigite o ID para ver detalhes ou ENTER para voltar: ").strip()

        if escolha != "":
            ave_encontrada = buscar_ave_por_id(resultados, escolha)

            if ave_encontrada is None:
                print("ID não encontrado nos resultados.")

            else:
                exibir_detalhes_ave(ave_encontrada)

def normalizar_texto(texto):
    texto = str(texto)
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    return texto

    
def exibir_detalhes_ave(ave):
    print()
    print("=" * 50)
    print("DETALHES DA AVE")
    print("=" * 50)
    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave.get('ordem', 'Não informada')}")
    print(f"Família: {ave.get('familia', 'Não informada')}")
    print(f"Dieta: {ave.get('dieta_tipo', 'Não informada')}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave.get('curiosidade', 'Não informada')}")

def valor_ou_indisponivel(valor, unidade=""):
    if valor is None or valor == "":
        return "Não informado"

    if unidade != "":
        return f"{valor} {unidade}"

    return str(valor)

def imprimir_linha_comparacao(rotulo, valor_1, valor_2):
    print(f"{rotulo:<18} | {str(valor_1):<25} | {str(valor_2):<25}")

def exibir_comparacao_aves(ave_1, ave_2):
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)

    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print("-" * 78)

    imprimir_linha_comparacao(
        "Nome científico",
        ave_1.get("nome_cientifico"),
        ave_2.get("nome_cientifico")
    )

    imprimir_linha_comparacao(
        "Ordem",
        ave_1.get("ordem"),
        ave_2.get("ordem")
    )

    imprimir_linha_comparacao(
        "Família",
        ave_1.get("familia"),
        ave_2.get("familia")
    )

    imprimir_linha_comparacao(
        "Dieta",
        ave_1.get("dieta_tipo"),
        ave_2.get("dieta_tipo")
    )

    imprimir_linha_comparacao(
        "Habitat",
        ave_1.get("habitat"),
        ave_2.get("habitat")
    )

    imprimir_linha_comparacao(
        "Comprimento",
        valor_ou_indisponivel(ave_1.get("comprimento_cm"), "cm"),
        valor_ou_indisponivel(ave_2.get("comprimento_cm"), "cm")
    )

    imprimir_linha_comparacao(
        "Peso",
        valor_ou_indisponivel(ave_1.get("peso_g"), "g"),
        valor_ou_indisponivel(ave_2.get("peso_g"), "g")
    )

    imprimir_linha_comparacao(
        "Conservação",
        ave_1.get("status_conservacao", "Não informado"),
        ave_2.get("status_conservacao", "Não informado")
    )

    imprimir_linha_comparacao(
        "Índice",
        ave_1.get("indice_conservacao", "Não informado"),
        ave_2.get("indice_conservacao", "Não informado")
    )

    if (ave_1 == ave_2):
        print("Tente digitar ids diferentes para ver comparações entre aves diferentes")

def escolher_ave(catalogo, mensagem):
    listar_aves(catalogo)
    id_escolhido = input(f"\n{mensagem}: ").strip()
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
        return None

    return ave_encontrada

def comparar_duas_aves(catalogo):
    print()
    print("Escolha a primeira ave")
    ave_1 = escolher_ave(catalogo, "Digite o ID da primeira ave")

    if ave_1 is None:
        return

    print()
    print("Escolha a segunda ave")

    ave_2 = escolher_ave(catalogo, "Digite o ID da segunda ave")

    if ave_2 is None:
        return

    exibir_comparacao_aves(ave_1, ave_2)

catalogo_aves = [
    {
        "id": "1",
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "comprimento_cm": 23,
        "peso_g": 68,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto lembra a expressão bem-te-vi."
    },
    {
        "id": "2",
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "comprimento_cm": 20,
        "peso_g": 49,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Insetos e outros pequenos invertebrados",
        "curiosidade": "Constrói um ninho de barro característico."
    },
    {
        "id": "3",
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos, áreas abertas e ambientes rurais",
        "comprimento_cm": 13,
        "peso_g": 20,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "O macho possui plumagem amarela intensa."
    },
    {
        "id": "4",
        "nome_popular": "Patola-de-pés-azuis",
        "nome_cientifico": "Sula nebouxii",
        "ordem": "Suliformes",
        "familia": "Sulidae",
        "dieta_tipo": "Piscívora",
        "habitat": "Ilhas tropicais",
        "comprimento_cm": 81,
        "peso_g": 1500,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Diversos peixes",
        "curiosidade": "Possuem pés azuis"
    },
    {
        "id": "5",
        "nome_popular": "secretária",
        "nome_cientifico": "Sagittarius serpentarius",
        "ordem": "Accipitriformes",
        "familia": "Sagittariidae",
        "dieta_tipo": "Carnivora",
        "habitat": "Planices e savanas",
        "comprimento_cm": 130,
        "peso_g": 4000,
        "status_conservacao": "Ameaçado",
        "indice_conservacao": 3,
        "alimentacao": "Insetos e pequenos vertebrados",
        "curiosidade": "Pisoteiam suas presas, são conhecidas por caçarem cobras."
    },
    {
        "id": "6",
        "nome_popular": "Pinguim-imperador",
        "nome_cientifico": "Aptenodytes forsteri",
        "ordem": "Sphenisciformes",
        "familia": "Spheniscidae",
        "dieta_tipo": "Piscívora",
        "habitat": "Antartica",
        "comprimento_cm": 115,
        "peso_g": 3000,
        "status_conservacao": "Ameaçado",
        "indice_conservacao": 3,
        "alimentacao": "Peixes e crustáceos",
        "curiosidade": "As fêmeas passam o inverno no mar enquanto os machos incubam os ovos."
    },
    {
        "id": "7",
        "nome_popular": "cucaburra-grande",
        "nome_cientifico": "Dacelo novaeguineae",
        "ordem": "Coraciiformes",
        "familia": "Alcedinidae",
        "dieta_tipo": "Carnivora",
        "habitat": "Leste australiano",
        "comprimento_cm": 44,
        "peso_g": 333,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 2,
        "alimentacao": "pequenos mamíferos e répteis",
        "curiosidade": "Seu canto parece uma risada."
    },
    {
        "id": "8",
        "nome_popular": "Coruja-buraqueira",
        "nome_cientifico": "Athene cunicularia",
        "ordem": "Strigiformes",
        "familia": "Strigidae",
        "dieta_tipo": "Carnivora",
        "habitat": "Florestas sul e norte americanas",
        "comprimento_cm": 25,
        "peso_g": 190,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "insetos e pequenos vertebrados",
        "curiosidade": "O nome científico vem da deusa grega Athena."
    },
    {
        "id": "9",
        "nome_popular": "Noitibó-orelhudo",
        "nome_cientifico": "Lyncornis macrotis",
        "ordem": "Caprimulgiformes",
        "familia": "Caprimulgidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Florestas tropicais do sul da Asia",
        "comprimento_cm": 36,
        "peso_g": 141,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Insetos e pequenos repteis",
        "curiosidade": "São noturnos."
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
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "4":
        comparar_duas_aves(catalogo_aves)

    elif opcao_menu == "5":
        print("A AveDex é um catálogo interativo de aves.")
        print("Em breve, teremos comparação, imagens, sons e dados em arquivo JSON.")
    
    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    else:
        print("Opção inválida. Digite apenas 0, 1, 2, 3, 4 ou 5.")

    if opcao_menu != "0":
        pausar()