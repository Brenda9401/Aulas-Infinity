# def mensagem():
#     return "Olá mundo!"
# print (mensagem())

# def calcular_area(largura, altura):
#     area = largura * altura
#     return f'o valor da area é {area}'

# print(calcular_area(50,20))


# def info(**dados):
#     for chave,valor in dados.items():
#         print(f'a chave é {chave} e o valor é {valor}')

# info(nome= 'Marcos',idade=26, cidade = 'Belo Horizonte')

# def media(n1,n2,n3):
#     return f'a media dos numeros é {(n1 + n2 + n3)/3}'

# resultado = media(10,50,90)

# print(resultado)

def calcularDesconto(precoOriginal):
    taxaDesconto = 0.10 
    precoDesconto = precoOriginal * taxaDesconto 
    precoFinal = precoOriginal - precoDesconto 
    return f'o preço com desconto é {precoFinal}'

produto1 = calcularDesconto(500)

print(produto1)