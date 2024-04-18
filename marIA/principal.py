import random

def selecao_natural(populacao, fitness, tamanho_populacao):
    # Calcula a probabilidade de seleção proporcional ao fitness de cada indivíduo
    probabilidades = [fit / sum(fitness) for fit in fitness]
    
    # Seleciona indivíduos para a próxima geração com base nas probabilidades calculadas
    nova_geracao = random.choices(populacao, weights=probabilidades, k=tamanho_populacao)
    
    return nova_geracao
