import json

# 1) Cálculo do somatório
def calcular_somatorio():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K

    return SOMA

# 2) Verificar se o número pertence à sequência de Fibonacci
def pertence_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

# 3) Cálculo do menor, maior faturamento e dias com faturamento acima da média
def calcular_faturamento(faturamentos):
    faturamentos_validos = [f for f in faturamentos if f > 0]
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)
    media_faturamento = sum(faturamentos_validos) / len(faturamentos_validos)
    dias_acima_da_media = len([f for f in faturamentos_validos if f > media_faturamento])
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# 4) Cálculo do percentual de faturamento por estado
def calcular_percentual_faturamento(faturamento_estados):
    total_faturamento = sum(faturamento_estados.values())
    percentuais = {}

    for estado, valor in faturamento_estados.items():
        percentual = (valor / total_faturamento) * 100
        percentuais[estado] = percentual
    
    return percentuais

# 5) Função para inverter uma string sem usar funções prontas
def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

# Main program
if __name__ == "__main__":
    # 1) Cálculo do somatório
    somatorio = calcular_somatorio()
    print(f"1) O valor de SOMA ao final do processamento é: {somatorio}")
    
    # 2) Verificar se um número pertence à sequência de Fibonacci
    numero = int(input("2) Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    
    # 3) Cálculo do faturamento diário (usando JSON como exemplo)
    faturamentos_json = '''
    {
      "faturamento": [0, 1500, 1000, 2000, 0, 500, 3000, 2500, 0, 0, 700, 800, 100, 0, 0, 1600, 1200, 1700, 0, 1800]
    }
    '''
    dados = json.loads(faturamentos_json)
    faturamentos = dados['faturamento']

    menor, maior, dias_acima_media = calcular_faturamento(faturamentos)
    print(f"3) Menor faturamento: {menor}")
    print(f"Maior faturamento: {maior}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")

    # 4) Cálculo do percentual de faturamento por estado
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    percentuais = calcular_percentual_faturamento(faturamento_estados)
    print("4) Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}% do faturamento total")
    
    # 5) Inversão de uma string
    string = input("5) Informe uma string para inverter: ")
    resultado_invertido = inverter_string(string)
    print(f"A string invertida é: {resultado_invertido}")