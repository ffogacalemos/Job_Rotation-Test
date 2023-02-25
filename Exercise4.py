def soma():
    estados = {'SP': 67836.43,
           'RJ': 36678.66,
           'MG': 29229.88,
           'ES': 27165.48,
           'outros': 9849.53}

    soma = sum(estados.values())

    for i, j in estados.items():
        print(i, ": ", ((j*100)/soma), "%")