# Nome: João Pedro Neigri Heleno - 2270323
# Matéria: Teoria da Computação - Profº Lucio Agostinho Rocha

def converteAFND2AFD(estados, alfabeto, estadoInicial, estados_finais, transicoes):
    
    # Mapeia conjunto de estados para os estados do AFD
    mapeamento_estados = {}

    # Cria e inicializa a fila de estados como vazia
    filaEstados = []

    
    # Pega o estado inicial do AFD
    estadoInicialAFD = frozenset([estadoInicial])
    mapeamento_estados[estadoInicialAFD] = 'A'
    filaEstados.append(estadoInicialAFD)

    # Armazena as transições do AFD
    transicoes_afd = {}

    # Verifica os estados até a fila estar vazia
    while filaEstados:
        estado_atual_afnd = filaEstados.pop(0)

        # Manuseia as transições para cada simbolo do alfabeto
        for simbolo in alfabeto:
            estado_destino_afnd = set()

            # Pega conjunto de estados possiveis partindo do estado atual com o símbolo atual
            for estado in estado_atual_afnd:
                if (estado, simbolo) in transicoes:
                    estado_destino_afnd.update(transicoes[(estado, simbolo)])

            estado_destino_afd = frozenset(estado_destino_afnd)

            if estado_destino_afd not in mapeamento_estados:
                novoEstadoAFD = chr(ord(max(mapeamento_estados.values())) + 1)
                mapeamento_estados[estado_destino_afd] = novoEstadoAFD
                filaEstados.append(estado_destino_afd)

            transicoes_afd[(mapeamento_estados[estado_atual_afnd], simbolo)] = mapeamento_estados[estado_destino_afd]

    # Pega o conjunto de estados finais do AFD
    estados_finais_afd = set()
    for estado_afd, estado_afnd in mapeamento_estados.items():
        for estado_final_afnd in estados_finais:
            if estado_final_afnd in estado_afd:
                estados_finais_afd.add(estado_afnd)

    # Cria o novo AFD
    afd = {
        'estados': set(mapeamento_estados.values()),
        'alfabeto': alfabeto,
        'estadoInicial': 'A',
        'estados_finais': estados_finais_afd,
        'transicoes': transicoes_afd
    }

    return afd

# Recebe do usuário as informações do AFND e o inicializa
def inputAFND():

    estados = input("Insira os estados do AFND desejado sepado por virgula (estado1,estado): ").split(',')
    estadoInicial = input("Insira o estado inicial do AFND: ")
    estados_finais = input("Insira os estados finais do AFND: ").split(',')
    alfabeto = input("Insira o alfabeto do AFND ").split(',')
   
    # Recebe as transições do AFD
    transicoes = {}
    print("Insira as transições do AFND no formato 'estado, símbolo, estado_destino'")
    print("Digite 'fim' para obter o AFD")
    
    while True:
        entrada = input("Transição: ")
        if entrada == 'fim':
            break

        estado, simbolo, *estados_destino = entrada.split(',')
        if (estado, simbolo) in transicoes:
            transicoes[(estado, simbolo)].extend(estados_destino)
        else:
            transicoes[(estado, simbolo)] = estados_destino

    afnd = {
        'estados': estados,
        'estadoInicial': estadoInicial,
        'estados_finais': estados_finais,
        'alfabeto': alfabeto,
        'transicoes': transicoes
    }

    return afnd


# Exemplo de utilização
afnd = inputAFND()
afd = converteAFND2AFD(**afnd)

print("\n-----------------------------\n")

print('Estados do AFD:', afd['estados'])
print('Alfabeto do AFD:', afd['alfabeto'])
print('Estado inicial do AFD:', afd['estadoInicial'])
print('Estados finais do AFD:', afd['estados_finais'])
print('Transições do AFD:', afd['transicoes'])