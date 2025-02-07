import re
import json
from bs4 import BeautifulSoup
from utils import select_and_format_text, transform_elm_in_text

CAMINHO_HTML = './html/Rafael.html' # Modifique aqui o arquivo de entrada.
CAMINHO_JSON = CAMINHO_HTML.replace('.html', '.json')

with open(CAMINHO_HTML, 'r', encoding='utf-8') as filehandle:
    soup = BeautifulSoup(filehandle, 'html.parser')

result = {}

# Extrair aba Identificação
elm_identificao = soup.select_one('.layout-cell-pad-main .title-wrapper:nth-child(6) > div')

result['Nome em citações bibliográficas'] = select_and_format_text(elm_identificao, '.layout-cell.layout-cell-9:nth-child(4) > div')
result['Lattes ID'] = select_and_format_text(elm_identificao, '.layout-cell.layout-cell-9:nth-child(6) > div')
result['Orcid ID'] = select_and_format_text(elm_identificao, '.layout-cell.layout-cell-9:nth-child(8) > div').replace('?', '')
result['Nacionalidade'] = select_and_format_text(elm_identificao, '.layout-cell.layout-cell-9:nth-child(10) > div')

# Extrair aba Formação acadêmica/titulação
elm_formacoes_academicas = soup.select('.layout-cell-pad-main .title-wrapper:nth-child(8) > .data-cell > div.layout-cell-3')
formacoes_academicas = {}

for elm in elm_formacoes_academicas:
    formacoes_academicas[select_and_format_text(elm, 'b')] = transform_elm_in_text(elm.find_next_sibling())

result['Formacoes Academicas'] = formacoes_academicas

# Extrair aba Formação Complementar
elm_formacoes_complementares = soup.select('.layout-cell-pad-main .title-wrapper:nth-child(12) > .data-cell > div.layout-cell-3')
formacoes_complementares = {}

for elm in elm_formacoes_complementares:
    formacoes_complementares[select_and_format_text(elm, 'b')] = transform_elm_in_text(elm.find_next_sibling())

result['Formacoes Complementares'] = formacoes_complementares

# Extrair aba Atuação Profissional
elm_atuacao_profissional = soup.select('.layout-cell-pad-main .title-wrapper:nth-child(14) > .data-cell')
atuacao_profissional = {}

for elm in elm_atuacao_profissional:
    atuacao_profissional[transform_elm_in_text(elm.select_one('.inst_back'))] = []
    # break

result['Atuação Profissional'] = atuacao_profissional

with open(CAMINHO_JSON, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)