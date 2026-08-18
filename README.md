# AveDex

A AveDex é um catálogo interativo de aves desenvolvido na disciplina de
Boas Práticas de Programação.

## Funcionalidades

- Listagem de aves
- Busca por nome, família, ordem ou dieta
- Exibição de detalhes por ID
- Comparação entre duas aves
- Dados carregados de arquivo JSON
- Validação defensiva do dataset
- Verificação de ambiente

## Como executar

```bash
python main.py
```

## Instalação das dependências opcionais

```bash
pip install -r requirements.txt
```

## Estrutura do projeto

- `main.py`: ponto de entrada.
- `src/avedex/app.py`: menu e fluxo principal.
- `src/avedex/interface.py`: abertura e menu.
- `src/avedex/catalogo.py`: listagem, busca e detalhes.
- `src/avedex/comparacao.py`: comparação entre aves.
- `src/avedex/dados.py`: carregamento e validação do JSON.
- `src/avedex/ambiente.py`: verificação de dependências.
- `src/avedex/creditos.py`: informações e fontes.
- `src/avedex/utils.py`: funções auxiliares.
- `data/avedex_dataset_midias.json`: dados das aves.

## Testes

Os testes manuais estão documentados em:
`docs/testes_manuais.md`

## Testes defensivos realizados
- [x] JSON carregado corretamente
- [x] Arquivo JSON ausente
- [x] JSON mal formatado
- [x] Campo obrigatório ausente
- [x] ID duplicado
- [x] Campo numérico inválido
- [x] Entrada inválida no ID
- [x] Verificação de ambiente
