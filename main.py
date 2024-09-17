from lxml.html import fromstring
import requests
import random
import string


def mensais():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits
        while True:
            codigo = ''.join(random.choices(letras_numeros, k=8))
            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("Bem-vindo ao TBG (The Best Generators) - Links Mensais")
    print("------------------------------------------------------")
    print("░█░░░█░██░█░█░█░")
    print("░█░░░█░█░██░██░░")
    print("░███░█░█░░█░█░█░")
    print("░██░░░█░█░█████░███░░░███░░░░░░████░░████░██░░░█░")
    print("░█░█░░█░█░░░█░░░█░░█░█░░░█░░░░█░░░░░░█░░░░█░█░░█░")
    print("░█░░█░█░█░░░█░░░███░░█░░░█░░░░█░░██░░███░░█░░█░█░")
    print("░█░░█░█░█░░░█░░░█░░█░█░░░█░░░░█░░░█░░█░░░░█░░█░█░")
    print("░█░░░██░█░░░█░░░█░░█░░███░░░░░░███░░░████░█░░░██░")
    print("------------------------------------------------------")

    print("Quantos links mensais você deseja gerar?")
    quantidade = int(input("Digite a quantidade desejada: "))
    codigos_gerados = gerar_codigos(quantidade)

    dc = "https://discord.gg//"
    for codigo in codigos_gerados:
        print(dc + codigo)

    if quantidade == 1:
        print("Um link mensal foi gerado com sucesso!")
    else:
        print(f"{quantidade} links mensais foram gerados com sucesso!")

def steam():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_uppercase + string.digits
        letras = string.ascii_uppercase
        numeros = string.digits
        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=6))
            parte2 = ''.join(random.choices(letras_numeros, k=6))
            parte3 = ''.join(random.choices(letras_numeros, k=6))
            parte4 = ''.join(random.choices(letras_numeros, k=6))
            parte5 = ''.join(random.choices(letras_numeros, k=6))
            parte6 = ''.join(random.choices(numeros, k=3))
            parte7 = ''.join(random.choices(letras_numeros, k=12))
            parte8 = ''.join(random.choices(numeros, k=2))
            codigo = f"{parte1}-{parte2}-{parte3}"
            codigo2 = f"{parte1}-{parte2}-{parte3}-{parte4}-{parte5}"
            codigo3 = f"{parte6}{parte7} {parte8}"
            codigo4 = random.choice([codigo, codigo2, codigo3])
            if codigo4 not in codigos_gerados:
                return codigo4

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("Bem-vindo ao TBG (The Best Generators) - Chaves Steam")
    print("------------------------------------------------------")
    print("░█░█░███░█░█░")
    print("░██░░██░░███░")
    print("░█░█░███░░█░░")
    print("░████░█████░████░░████░██░░░██░░░░████░░░████░░██░░░█░")
    print("░█░░░░░░█░░░█░░░░░█░░█░█░█░█░█░░░█░░░░░░░█░░░░░█░█░░█░")
    print("░░██░░░░█░░░███░░░████░█░░█░░█░░░█░░██░░░███░░░█░░█░█░")
    print("░░░░█░░░█░░░█░░░░░█░░█░█░░░░░█░░░█░░░█░░░█░░░░░█░░█░█░")
    print("░████░░░█░░░████░░█░░█░█░░░░░█░░░░███░░░░████░░█░░░██░")
    print("------------------------------------------------------")

    print("Quantas keys Steam você deseja gerar?")
    quantidade = int(input("Digite a quantidade desejada: "))
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print("1 key Steam foi gerada com sucesso!")
    else:
        print(f"{quantidade} chaves Steam foram geradas com sucesso!")



def token():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits
        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=24))
            parte2 = ''.join(random.choices(letras_numeros, k=26))
            codigo = f"{parte1}.{parte2}"
            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("Bem-vindo ao TBG (The Best Generators) - Tokens Discord")
    print("--------------------------------------------------------")
    print("░██░░███░")
    print("░█░█░█░░░")
    print("░██░░███░")
    print("░█████░░███░░█░░██░████░░██░░░█░░░░░████░░████░██░░░█░")
    print("░░░█░░░█░░░█░█░░█░░█░░░░░█░█░░█░░░░█░░░░░░█░░░░█░█░░█░")
    print("░░░█░░░█░░░█░███░░░███░░░█░░█░█░░░░█░░██░░███░░█░░█░█░")
    print("░░░█░░░█░░░█░█░░█░░█░░░░░█░░█░█░░░░█░░░█░░█░░░░█░░█░█░")
    print("░░░█░░░░███░░█░░██░████░░█░░░██░░░░░███░░░████░█░░░██░")
    print("--------------------------------------------------------")

    print("Quantos tokens Discord você deseja gerar?")
    quantidade = int(input("Digite a quantidade desejada: "))
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print("Um token Discord foi gerado com sucesso!")
    else:
        print(f"{quantidade} tokens Discord foram gerados com sucesso!")

def xbox():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits
        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=25))
            codigo = f"{parte1}"
            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("Bem-vindo ao TBG (The Best Generators) - Chaves Xbox")
    print("-----------------------------------------------------")
    print("░█░█░███░█░█░")
    print("░██░░██░░███░")
    print("░█░█░███░░█░░")
    print("░█░░░█░███░░░███░░█░░░█░░░░████░░░████░░██░░░█░")
    print("░░█░█░░█░░█░█░░░█░░█░█░░░░█░░░░░░░█░░░░░█░█░░█░")
    print("░░░█░░░███░░█░░░█░░░█░░░░░█░░██░░░███░░░█░░█░█░")
    print("░░█░█░░█░░█░█░░░█░░█░█░░░░█░░░█░░░█░░░░░█░░█░█░")
    print("░█░░░█░███░░░███░░█░░░█░░░░███░░░░████░░█░░░██░")
    print("-----------------------------------------------------")
    print("Quantas key Xbox você deseja gerar?")
    quantidade = int(input("Digite a quantidade desejada: "))
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print("1 key Xbox foi gerada com sucesso!")
    else:
        print(f"{quantidade} chaves Xbox foram geradas com sucesso!")

def trimensal():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits
        while True:
            codigo = ''.join(random.choices(letras_numeros, k=24))
            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("Bem-vindo ao TBG (The Best Generators) - Links Trimensais")
    print("---------------------------------------------------------")
    print("░█░░░█░██░█░█░█░")
    print("░█░░░█░█░██░██░░")
    print("░███░█░█░░█░█░█░")
    print("░█████░███░░█░░░░░████░░████░██░░░█░")
    print("░░░█░░░█░░█░█░░░░█░░░░░░█░░░░█░█░░█░")
    print("░░░█░░░███░░█░░░░█░░██░░███░░█░░█░█░")
    print("░░░█░░░█░░█░█░░░░█░░░█░░█░░░░█░░█░█░")
    print("░░░█░░░█░░█░█░░░░░███░░░████░█░░░██░")
    print("-----------------------------------------------------")
    print("Quantos links trimensais você deseja gerar?")
    quantidade = int(input("Digite a quantidade desejada: "))
    codigos_gerados = gerar_codigos(quantidade)

    dc = "https://promos.discord.gg/"
    for codigo in codigos_gerados:
        print(dc + codigo)

    if quantidade == 1:
        print("1 link trimensal foi gerado com sucesso!")
    else:
        print(f"{quantidade} links trimensais foram gerados com sucesso!")

def psn():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_uppercase + string.digits
        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=4))
            parte2 = ''.join(random.choices(letras_numeros, k=4))
            parte3 = ''.join(random.choices(letras_numeros, k=4))
            parte4 = ''.join(random.choices(letras_numeros, k=4))
            codigo = f"{parte1}-{parte2}-{parte3}-{parte4}"
            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("Bem-vindo ao TBG (The Best Generators) - Chaves PSN")
    print("----------------------------------------------------")
    print("░█░█░███░█░█░")
    print("░██░░██░░███░")
    print("░█░█░███░░█░░")
    print("░████░░░████░░██░░░█░░░░░░████░░████░░██░░░█░")
    print("░█░░░█░░█░░░░░█░█░░█░░░░░█░░░░░░█░░░░░█░█░░█░")
    print("░████░░░░██░░░█░░█░█░░░░░█░░██░░███░░░█░░█░█░")
    print("░█░░░░░░░░░█░░█░░█░█░░░░░█░░░█░░█░░░░░█░░█░█░")
    print("░█░░░░░░████░░█░░░██░░░░░░███░░░████░░█░░░██░")
    print("----------------------------------------------------")

    print("Quantas keys PSN você deseja gerar?")
    quantidade = int(input("Digite a quantidade desejada: "))
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print("1 key PSN foi gerada com sucesso!")
    else:
        print(f"{quantidade} chaves PSN foram geradas com sucesso!")

def nintendo():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits
        while True:
            comprimento = random.randint(16, 24)
            codigo = ''.join(random.choices(letras_numeros, k=comprimento))
            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("Bem-vindo ao TBG (The Best Generators) - Key Nintendo")
    print("---------------------------------------------------------")
    print("░█░█░███░█░█░")
    print("░██░░██░░███░")
    print("░█░█░███░░█░░")
    print("░██░░░█░█░██░░░█░█████░████░██░░░█░████░░░████░░░░░░░████░░████░██░░░█░")
    print("░█░█░░█░█░█░█░░█░░░█░░░█░░░░█░█░░█░█░░░█░█░░░░█░░░░░█░░░░░░█░░░░█░█░░█░")
    print("░█░░█░█░█░█░░█░█░░░█░░░███░░█░░█░█░█░░░█░█░░░░█░░░░░█░░██░░███░░█░░█░█░")
    print("░█░░█░█░█░█░░█░█░░░█░░░█░░░░█░░█░█░█░░░█░█░░░░█░░░░░█░░░█░░█░░░░█░░█░█░")
    print("░█░░░██░█░█░░░██░░░█░░░████░█░░░██░████░░░████░░░░░░░███░░░████░█░░░██░")

    quantidade = int(input("Quantas chaves Nintendo você deseja gerar? "))
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
       print(codigo)

    if quantidade == 1:
        print(quantidade, "chave foi gerada com sucesso!")
    else:
        print(quantidade, "chaves foram geradas com sucesso!")

def proxies():
    def get_proxies(quantidade):
        url = 'https://sslproxies.org/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:quantidade]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        print("proxies:", proxies) 
        return proxies

    def main():
        print("Bem-vindo ao TBG (The Best Generators) - Proxie")
        print("---------------------------------------------------------")
        print("░████░░███░░░███░░█░░░█░█░░░█░░░░░████░░████░██░░░█░")
        print("░█░░░█░█░░█░█░░░█░░█░█░░█░░░█░░░░█░░░░░░█░░░░█░█░░█░")
        print("░████░░███░░█░░░█░░░█░░░░███░░░░░█░░██░░███░░█░░█░█░")
        print("░█░░░░░█░░█░█░░░█░░█░█░░░░█░░░░░░█░░░█░░█░░░░█░░█░█░")
        print("░█░░░░░█░░█░░███░░█░░░█░░░█░░░░░░░███░░░████░█░░░██░")
        quantidade = int(input("Digite a quantidade de proxies desejada: "))
        proxies = get_proxies(quantidade)

    if __name__ == "__main__":
        main()

def gerar_codigo(codigos_gerados):
    letras_numeros = string.ascii_letters + string.digits

    while True:
        parte1 = ''.join(random.choices(letras_numeros, k=4))
        parte2 = ''.join(random.choices(letras_numeros, k=4))
        parte3 = ''.join(random.choices(letras_numeros, k=4))
        parte4 = ''.join(random.choices(letras_numeros, k=4))
        codigo = f"{parte1}-{parte2}-{parte3}-{parte4}"

        if codigo not in codigos_gerados:
            return codigo


def play():
    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados


    print("bem vindo ao: (welcome to:)")
    print("------------------------------------------------------")
    print("░░███░███░██░░░███░░░░")
    print("░░█░░░█_█░█_█░░█░░█░░░")
    print("░░███░█░█░█░░█░███░░░░")
    print("░█████░█░░░░█████░█░░░█░░░░░░░████░░░████░░██░░░█░")
    print("░█░░░█░█░░░░█░░░█░█░░░█░░░░░░█░░░░░░░█░░░░░█░█░░█░")
    print("░█████░█░░░░█████░█████░░░░░░█░░██░░░███░░░█░░█░█░")
    print("░█░░░░░█░░░░█░░░█░░░█░░░░░░░░█░░░█░░░█░░░░░█░░█░█░")
    print("░█░░░░░████░█░░░█░░░█░░░░░░░░░███░░░░████░░█░░░██░")
    print("------------------------------------------------------")
    print("by sr.raposo on viniciusrinaldi")
    print("--------------------------------------------------------------")

    print("How many carda do you want to generate?")
    quantidade = input("Quantos cards você gostaria de gerar? ")

    while not quantidade.isdigit():
        print("Por favor, insira apenas números.")
        quantidade = input("Quantos cards você gostaria de gerar? ")

    quantidade = int(quantidade)
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print(quantidade, "card foi gerado com sucesso!")
    else:
        print(quantidade, "cards foram gerados com sucesso!")

def apple():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits

        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=4))
            parte2 = ''.join(random.choices(letras_numeros, k=4))
            parte3 = ''.join(random.choices(letras_numeros, k=4))
            parte4 = ''.join(random.choices(letras_numeros, k=4))
            codigo = f"{parte1}-{parte2}-{parte3}-{parte4}"

            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("bem vindo ao: (welcome to:)")
    print("--------------------------------------------------------------")
    print("░░███░███░██░░░███░░░░")
    print("░░█░░░█_█░█_█░░█░░█░░░")
    print("░░███░█░█░█░░█░███░░░░")
    print("░████░████░████░█░░░░████░░░░░░████░░████░██░░░█░")
    print("░█░░█░█░░█░█░░█░█░░░░█░░░░░░░░█░░░░░░█░░░░█░█░░█░")
    print("░████░████░████░█░░░░███░░░░░░█░░██░░███░░█░░█░█░")
    print("░█░░█░█░░░░█░░░░█░░░░█░░░░░░░░█░░░█░░█░░░░█░░█░█░")
    print("░█░░█░█░░░░█░░░░████░████░░░░░░███░░░████░█░░░██░")
    print("by sr.raposo on viniciusrinaldi")
    print("--------------------------------------------------------------")

    print("How many cards do you want to generate?")
    quantidade = input("Quantos cards você gostaria de gerar? ")

    while not quantidade.isdigit():
        print("Por favor, insira apenas números.")
        quantidade = input("Quantos cards você gostaria de gerar? ")

    quantidade = int(quantidade)
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print(quantidade, "card foi gerado com sucesso!")
    else:
        print(quantidade, "cards foram gerados com sucesso!")



def microsoft():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits

        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=5))
            parte2 = ''.join(random.choices(letras_numeros, k=5))
            parte3 = ''.join(random.choices(letras_numeros, k=5))
            parte4 = ''.join(random.choices(letras_numeros, k=5))
            parte5 = ''.join(random.choices(letras_numeros, k=5))
            codigo = f"{parte1}-{parte2}-{parte3}-{parte4}-{parte5}"

            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("bem vindo ao: (welcome to:)")
    print("--------------------------------------------------------------")
    print("░░███░███░██░░░███░░░░")
    print("░░█░░░█_█░█_█░░█░░█░░░")
    print("░░███░█░█░█░░█░███░░░░")
    print("░██░░░██░█░█████░█████░░███░░░░░░░████░░████░██░░░█░")
    print("░█░█░█░█░█░█░░░░░█░░░█░█░░░█░░░░░█░░░░░░█░░░░█░█░░█░")
    print("░█░░█░░█░█░█░░░░░████░░█░░░█░░░░░█░░██░░███░░█░░█░█░")
    print("░█░░░░░█░█░█░░░░░█░░░█░█░░░█░░░░░█░░░█░░█░░░░█░░█░█░")
    print("░█░░░░░█░█░█████░█░░░█░░███░░░░░░░███░░░████░█░░░██░")
    print("by sr.raposo on viniciusrinaldi")
    print("--------------------------------------------------------------")

    print("How many cards do you want to generate?")
    quantidade = input("Quantos cards você gostaria de gerar? ")

    while not quantidade.isdigit():
        print("Por favor, insira apenas números.")
        quantidade = input("Quantos cards você gostaria de gerar? ")

    quantidade = int(quantidade)
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print(quantidade, "card foi gerado com sucesso!")
    else:
        print(quantidade, "cards foram gerados com sucesso!")

def amazon():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits

        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=4))
            parte2 = ''.join(random.choices(letras_numeros, k=6))
            parte3 = ''.join(random.choices(letras_numeros, k=4))
            codigo = f"{parte1}-{parte2}-{parte3}"

            if codigo not in codigos_gerados:
              return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("bem vindo ao: (welcome to:)")
    print("--------------------------------------------------------------")
    print("░░███░███░██░░░███░░░░")
    print("░░█░░░█_█░█_█░░█░░█░░░")
    print("░░███░█░█░█░░█░███░░░░")
    print("░█████░██░░░██░█████░█████░░███░░██░░░░█░░░░░░░████░░████░██░░░█░")
    print("░█░░░█░█░█░█░█░█░░░█░░░░░█░█░░░█░█░█░░░█░░░░░░█░░░░░░█░░░░█░█░░█░")
    print("░█████░█░░█░░█░█████░░███░░█░░░█░█░░█░░█░░░░░░█░░██░░███░░█░░█░█░")
    print("░█░░░█░█░░█░░█░█░░░█░█░░░░░█░░░█░█░░░█░█░░░░░░█░░░█░░█░░░░█░░█░█░")
    print("░█░░░█░█░░░░░█░█░░░█░█████░░███░░█░░░░██░░░░░░░███░░░████░█░░░██░")
    print("by sr.raposo on viniciusrinaldi")
    print("--------------------------------------------------------------")

    print("How many cards do you want to generate?")
    quantidade = input("Quantos cards você gostaria de gerar? ")

    while not quantidade.isdigit():
        print("Por favor, insira apenas números.")
        quantidade = input("Quantos cards você gostaria de gerar? ")

    quantidade = int(quantidade)
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print(quantidade, "card foi gerado com sucesso!")
    else:
        print(quantidade, "cards foram gerados com sucesso!")



def gift():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits

        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=16))
            parte2 = ("https://discord.gift/")
            codigo = f"{parte2}{parte1}"

            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("bem vindo ao: (welcome to:)")
    print("--------------------------------------------------------------")
    print("░██░░███░")
    print("░█░█░█░░░")
    print("░██░░███░")
    print("░░████░█░████░█████░░░░░░████░░████░██░░░█░")
    print("░█░░░░░█░█░░░░░░█░░░░░░░█░░░░░░█░░░░█░█░░█░")
    print("░█░░██░█░███░░░░█░░░░░░░█░░██░░███░░█░░█░█░")
    print("░█░░░█░█░█░░░░░░█░░░░░░░█░░░█░░█░░░░█░░█░█░")
    print("░░███░░█░█░░░░░░█░░░░░░░░███░░░████░█░░░██░")
    print("by sr.raposo on viniciusrinaldi")
    print("--------------------------------------------------------------")

    print("How many Gifts do you want to generate?")
    quantidade = input("Quantos Gifts você gostaria de gerar? ")

    while not quantidade.isdigit():
        print("Por favor, insira apenas números.")
        quantidade = input("Quantos Gifts você gostaria de gerar? ")

    quantidade = int(quantidade)
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print(quantidade, "Gift foi gerado com sucesso!")
    else:
        print(quantidade, "Gifts foram gerados com sucesso!")



def epic():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits

        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=5))
            parte2 = ''.join(random.choices(letras_numeros, k=5))
            parte3 = ''.join(random.choices(letras_numeros, k=5))
            parte4 = ''.join(random.choices(letras_numeros, k=5))
            codigo = f"{parte1}-{parte2}-{parte3}-{parte4}"

            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("bem vindo ao: (welcome to:)")
    print("--------------------------------------------------------------")
    print("░░█░█░███░█░█░░")
    print("░░██░░██░░███░░")
    print("░░█░█░███░░█░░░")
    print("░████░████░█░████░░░░░████░░████░██░░░█░")
    print("░█░░░░█░░█░█░█░░░░░░░█░░░░░░█░░░░█░█░░█░")
    print("░███░░████░█░█░░░░░░░█░░██░░███░░█░░█░█░")
    print("░█░░░░█░░░░█░█░░░░░░░█░░░█░░█░░░░█░░█░█░")
    print("░████░█░░░░█░████░░░░░███░░░████░█░░░██░")
    print("by sr.raposo on viniciusrinaldi")
    print("--------------------------------------------------------------")

    print("How many keys do you want to generate?")
    quantidade = input("Quantos keys você gostaria de gerar? ")

    while not quantidade.isdigit():
        print("Por favor, insira apenas números.")
        quantidade = input("Quantos keys você gostaria de gerar? ")

    quantidade = int(quantidade)
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print(quantidade, "key foi gerado com sucesso!")
    else:
        print(quantidade, "keys foram gerados com sucesso!")


def Roblox():
    def gerar_codigo(codigos_gerados):
        letras_numeros = string.ascii_letters + string.digits

        while True:
            parte1 = ''.join(random.choices(letras_numeros, k=12))
            codigo = f"{parte1}"

            if codigo not in codigos_gerados:
                return codigo

    def gerar_codigos(quantidade):
        codigos_gerados = set()
        while len(codigos_gerados) < quantidade:
            codigos_gerados.add(gerar_codigo(codigos_gerados))
        return codigos_gerados

    print("bem vindo ao: (welcome to:)")
    print("--------------------------------------------------------------")
    print("░░███░███░██░░░███░░░░")
    print("░░█░░░█_█░█_█░░█░░█░░░")
    print("░░███░█░█░█░░█░███░░░░")
    print("░███░░░███░░████░░█░░░░░░███░░█░░░█░░░░░░████░░████░██░░░█░")
    print("░█░░█░█░░░█░█░░░█░█░░░░░█░░░█░░█░█░░░░░░█░░░░░░█░░░░█░█░░█░")
    print("░███░░█░░░█░████░░█░░░░░█░░░█░░░█░░░░░░░█░░██░░███░░█░░█░█░")
    print("░█░░█░█░░░█░█░░░█░█░░░░░█░░░█░░█░█░░░░░░█░░░█░░█░░░░█░░█░█░")
    print("░█░░█░░███░░████░░█████░░███░░█░░░█░░░░░░███░░░████░█░░░██░")
    print("by sr.raposo on viniciusrinaldi")
    print("--------------------------------------------------------------")

    print("How many cards do you want to generate?")
    quantidade = input("Quantos cards você gostaria de gerar? ")

    while not quantidade.isdigit():
        print("Por favor, insira apenas números.")
        quantidade = input("Quantos cards você gostaria de gerar? ")

    quantidade = int(quantidade)
    codigos_gerados = gerar_codigos(quantidade)

    for codigo in codigos_gerados:
        print(codigo)

    if quantidade == 1:
        print(quantidade, "card foi gerado com sucesso!")
    else:
        print(quantidade, "cards foram gerados com sucesso!")



def password():
    while True:
        print("--------------------------------------------------------------")
        print("Digite a senha para acessar o gerador:")
        print("--------------------------------------------------------------")

        senha = input("ㅤ")

        if senha == '7845':
            main()

        else:
            print("senha errada, a senha só inclui numeros, insira novamente")
            
    

def keys_consoles():
    while True:
        print("--------------------------------------------------------------")
        print("Bem-vindo ao TBG (The Best Generators) - Keys de Consoles")
        print("Escolha o console:")
        print("1. Xbox")
        print("2. Nintendo")
        print("3. PlayStation (PSN)")
        print("4. Voltar ao menu principal")

        resposta = input("Digite o número da opção desejada: ")

        if resposta == '1':
            xbox()
        elif resposta == '2':
            nintendo()
        elif resposta == '3':
            psn()
        elif resposta == '4':
            print("Voltando ao menu principal...")
            break
        else:
            print("Por favor, escolha uma opção válida.")



def cards():
    while True:
        print("--------------------------------------------------------------")
        print("Bem-vindo ao TBG (The Best Generators) - Cards")
        print("Escolha a opção desejada:")
        print("1. Play store")
        print("2. Apple")
        print("3. Microsoft")
        print("4. Amazon")
        print("5. Voltar ao menu principal")

        resposta = input("Digite o número da opção desejada: ")

        if resposta == '1':
            play()
        elif resposta == '2':
            apple() 
        elif resposta == '3':
            microsoft()
        elif resposta == '4':
            amazon()
        elif resposta == '5':
            print("Voltando ao menu principal...")
            break
        else:
            print("Por favor, escolha uma opção válida.")





def discord():
    while True:
        print("--------------------------------------------------------------")
        print("Bem-vindo ao TBG (The Best Generators) - Discord")
        print("Escolha a opção desejada:")
        print("1. Nitro Gift")
        print("2. Links Mensais")
        print("3. Tokens Discord")
        print("4. Links Trimensais")
        print("5. Voltar ao menu principal")

        resposta = input("Digite o número da opção desejada: ")


        if resposta == '1':
            gift()
        elif resposta == '2':
            mensais()
        elif resposta == '3':
            token()
        elif resposta == '4':
            trimensal()
        elif resposta == '5':
            print("Voltando ao menu principal...")
            break
        else:
            print("Por favor, escolha uma opção válida.")

def online():
    while True:
        print("--------------------------------------------------------------")
        print("Bem-vindo ao TBG (The Best Generators) - Online")
        print("Escolha a opção desejada:")
        print("1. Key Steam")
        print("2. Key Epic Games")
        print("3. Voltar ao menu principal")

        resposta = input("Digite o número da opção desejada: ")

        if resposta == '1':
            steam()
        elif resposta == '2':
            epic()
        elif resposta == '3':
            print("Voltando ao menu principal...")
            break
        else:
            print("Por favor, escolha uma opção válida.")




def outros():
    while True:
        print("--------------------------------------------------------------")
        print("Bem-vindo ao TBG (The Best Generators) - Outros")
        print("Escolha a opção desejada:")
        print("1. Proxies")
        print("2. Card Roblox")
        print("3. Voltar ao menu principal")

        resposta = input("Digite o número da opção desejada: ")

        if resposta == '1':
            proxies()
        elif resposta == '2':
            Roblox()
        elif resposta == '3':
            print("Voltando ao menu principal...")
            break
        else:
            print("Por favor, escolha uma opção válida.")




def main():
    while True:
        print("⌌____________________⌍")
        print(" |░█████░███░░░████░░|")
        print(" |░░░█░░░█░░█░█░░░░░░|")
        print(" |░░░█░░░███░░█░░██░░|")
        print(" |░░░█░░░█░░█░█░░░█░░|")
        print(" |░░░█░░░███░░░███░░░|")
        print("by vini.rinaldi")
        print("Bem-vindo ao TBG (The Best Generators), escolha uma categoria:")
        print("1. Discord")
        print("2. Keys de Consoles")
        print("3. Cards")
        print("4. Online games")
        print("5. Outros")
        print("6. Sair")

        resposta = input("Digite o número do módulo desejado: ")

        if resposta == '1':
            discord()
        elif resposta == '2':
            keys_consoles()
        elif resposta == '3':
            cards()
        elif resposta == '4':
            online()
        elif resposta == '5':
            outros()
        elif resposta == '6':
            print("Saindo... Obrigado por usar o TBG!")
            break
        else:
            print("Por favor, escolha um número válido.")


        voltar = input("Deseja voltar ao início? (s/n): ").strip().lower()
        if voltar != 's':
            print("Saindo... Obrigado por usar o TBG!")
            break


if __name__ == "__main__":
    password()
