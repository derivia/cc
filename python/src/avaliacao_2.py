from typing import List, Tuple
import re
from datetime import datetime

def validar_matricula(matricula: str) -> bool:
    return len(matricula) == 8 and matricula.isnumeric()

def validar_objetivo(objetivo: str) -> bool:
    return objetivo.lower() in ["ganhar", "emagrecimento"]

def parse_data(data: str) -> datetime:
    # recebe a string no formato DD/MM/AAAA e retorna uma data no formato AAAA/MM/DD
    # útil para associações de funções que recebem o tipo datetime;
    # Também é compatível com o meio de sinais como >, <, ==, etc.
    dia, mes, ano = map(int, data.split("/"))
    return datetime(ano, mes, dia)

def validar_formatacao_peso(peso: str) -> bool:
    # um padrão regex para verificar se a string recebida (o peso) está no formato DKdg
    # onde D é um sequência de números decimais
    pattern = r"^\d+(\.\d+)?g$"
    if re.search(pattern, peso) is not None:
        return True
    else:
        return False

def validar_data_peso(data_peso_matriz: List[Tuple[datetime, str]]) -> bool:
    # valida se o formato (data, peso) (10/2024 56kg200g, por exemplo) está correto
    # verifica se as datas inseridas posteriormente não ocorrem antes das anteriores
    # verifica se está entre o intervalo 01/01/2024-31/10/2024
    data_inicio = datetime(2024, 1, 1)
    data_fim = datetime(2024, 10, 31)

    max_data = None
    for data, peso in data_peso_matriz:
        if not isinstance(data, datetime) or not validar_formatacao_peso(peso):
            return False
        if data < data_inicio or data > data_fim:
            return False
        if max_data is not None and data < max_data:
            return False
        max_data = data
    return True

def parse_data_peso(datas_pesos: List[str]) -> List[Tuple[datetime, str]]:
    # transforma as datas e pesos em uma lista de strings no formato DD/MM/AAAA DKdg, onde D é um número decimal
    # e o peso é separado
    matriz_datas_pesos = []
    for data_peso in datas_pesos:
        data, peso = data_peso.strip().split(" ")
        data_formatada = parse_data(data)
        matriz_datas_pesos.append((data_formatada, peso))
    return matriz_datas_pesos

def validar_entrada(entrada: List[str]) -> bool:
    # função de validação
    # verificação utilizando AND
    # se todas as funções retornam True
    matricula = entrada[1]
    objetivo = entrada[2]
    datas_pesos = entrada[3:]
    if len(datas_pesos) % 2 != 0:
        print("Número ímpar de elementos para datas e pesos inseridos.")
        return False
    pares_datas_pesos = []
    for i in range(0, len(datas_pesos), 2):
        pares_datas_pesos.append((datas_pesos[i], datas_pesos[i + 1]))
    return (validar_matricula(matricula) and validar_objetivo(objetivo) and validar_data_peso(parse_data_peso(pares_datas_pesos)))

def iniciar_entrada():
    usuarios = {}
    print("Insira os dados do paciente.")
    print("Insira 'parar' para finalizar a inserção.")
    recebendo_entrada = True
    while recebendo_entrada:
        entrada = input()
        if entrada.lower() == "parar":
            recebendo_entrada = False
        else:
            dados = entrada.split()
            if validar_entrada(dados):
                chave = dados[0] # nome, matricula e objetivo
                datas_pesos = []
                for i in range(3, len(dados), 2):
                    datas_pesos.append((dados[i], dados[i + 1])) # converte as duplas data_peso em uma lista para inserir na matriz
                usuarios[chave] = datas_pesos + datas_pesos
            else:
                print("Entrada inválida. Usuário não cadastrado.")
    print(usuarios)

iniciar_entrada()

