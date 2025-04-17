import sympy as sp

def verificar_causalidade(expr_str):
    # Define variáveis simbólicas
    n = sp.Symbol('n', integer=True)
    x = sp.Function('x')

    # Converte a string da expressão para simbólica
    expr = eval(expr_str)

    # Encontra todos os termos do tipo x[n + k]
    dependencias = expr.atoms(sp.Function)
    
    # Calculo causal
    causality_ok = True
    for term in dependencias:
        if isinstance(term, sp.Function) and term.func == x:
            indice = term.args[0]
            # Calcula diferença em relação a 'n'
            diff = sp.simplify(indice - n)
            if diff.is_number and diff > 0:
                causality_ok = False
                break

    if causality_ok:
        print(f"A expressão '{expr_str}' é ✅ Causal")
    else:
        print(f"A expressão '{expr_str}' é ❌ Não Causal")

    return causality_ok

def verificar_memoria(expr_str):
    # Define variáveis simbólicas
    n = sp.Symbol('n', integer=True)
    x = sp.Function('x')

    # Converte a string para expressão simbólica
    expr = eval(expr_str)

    # Pega todos os termos do tipo x[...]
    dependencias = expr.atoms(sp.Function)

    # Calculo da memória
    tem_memoria = False
    for term in dependencias:
        if isinstance(term, sp.Function) and term.func == x:
            indice = term.args[0]
            # Compara se é diferente de x[n]
            if not sp.simplify(indice - n) == 0:
                tem_memoria = True
                break

    if tem_memoria:
        print(f"A expressão '{expr_str}' ✅ TEM memória")
    else:
        print(f"A expressão '{expr_str}' ❌ NÃO TEM memória (é sem memória)")

    return tem_memoria

expressao = "x(n) - x(n)"
resultadoCausal = verificar_causalidade(expressao)
resultadoMemoria = verificar_memoria(expressao)
print(resultadoCausal)
print(resultadoMemoria)