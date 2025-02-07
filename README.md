# Lattes HTML Parser

Programa que extraí todas as informações contidas dentro do currículo Lattes e as transforma em um arquivo JSON.

## Requisitos
- Python >= 3.11
- Pip >= 24

## Antes de executar
1. Baixe a página HTML do currículo.
2. Modifique no arquivo main.py a variavel CAMINHO_HTML e coloque o caminho do HTML baixado.

## Como executar
```bash
pip install -r requirements.txt
python main.py
```

## TODO
- [x] Extrair informações principais
- [x] Extrair aba Identificação
- [x] Extrair aba Formação acadêmica/titulação
- [x] Extrair aba Formação Complementar
- [ ] Extrair aba Atuação Profissional
- [ ] Extrair aba Projetos de pesquisa
- [ ] Extrair aba Projetos de extensão
- [ ] Extrair aba Revisor de periódico
- [ ] Extrair aba Áreas de atuação
- [ ] Extrair aba Idiomas
- [ ] Extrair aba Prêmios e títulos
- [ ] Extrair aba Produções
- [ ] Extrair aba Patentes e registros
- [ ] Extrair aba Bancas
- [ ] Extrair aba Eventos
- [ ] Extrair aba Orientações
- [ ] Extrair aba Inovação
- [ ] Extrair aba Educação e Popularização de C & T
- [ ] Extrair aba Outras informações relevantes