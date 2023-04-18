def impostoSobreSalario(quantia):
    valor = quantia / 12
    if valor < 3000:
        return 0
    elif valor < 5000:
        return quantia * 0.1
    else:
        return quantia * 0.2

def impostoSobreServicos(quantia):
    return quantia * 0.15

def impostoSobreGC(quantia):
    return quantia * 0.2

def impostoBrutoTotal(salario, servicos, gc):
    return impostoSobreSalario(salario) + impostoSobreServicos(servicos) + impostoSobreGC(gc)

def abatimento(salario, servicos, gc, gastosMedicos, gastosEducacionais):
    impostoBruto = impostoBrutoTotal(salario, servicos, gc)
    maxAbatimento = impostoBruto * 0.3
    return min(maxAbatimento, gastosMedicos + gastosEducacionais)

salario = float(input("Renda anual com salário: "))
servicos = float(input("Renda anual com prestação de serviço: "))
gc = float(input("Renda anual com ganho de capital: "))
gastosMedicos = float(input("Gastos médicos: "))
gastosEducacionais = float(input("Gastos educacionais: "))

impostoSalario = impostoSobreSalario(salario)
impostoServicos = impostoSobreServicos(servicos)
impostoGC = impostoSobreGC(gc)
impostoTotal = impostoBrutoTotal(salario, servicos, gc)
abat = abatimento(salario, servicos, gc, gastosMedicos, gastosEducacionais)
impostoDevido = impostoTotal - abat

print("Imposto sobre salário: %.2f" % impostoSalario)
print("Imposto sobre serviços: %.2f" % impostoServicos)
print("Imposto sobre ganho de capital: %.2f" % impostoGC)
print("Imposto bruto total: %.2f" % impostoTotal)
print("Abatimento: %.2f" % abat)
print("Imposto devido: %.2f" % impostoDevido)
