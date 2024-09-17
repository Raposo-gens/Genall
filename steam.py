import streamlit as st
import random
import string

def gerar_codigo(codigos_gerados, partes=4, tamanho_parte=5):
    letras_numeros = string.ascii_letters + string.digits
    while True:
        partes_codigo = [''.join(random.choices(letras_numeros, k=tamanho_parte)) for _ in range(partes)]
        codigo = '-'.join(partes_codigo)
        if codigo not in codigos_gerados:
            return codigo

def gerar_codigos(quantidade):
    codigos_gerados = set()
    while len(codigos_gerados) < quantidade:
        codigos_gerados.add(gerar_codigo(codigos_gerados))
    return codigos_gerados

st.title('TBG (The Best Generators)')
st.write('Escolha a categoria:')

categoria = st.selectbox(
    'Selecione uma opção',
    ['Discord', 'Keys de Consoles', 'Cards', 'Online games', 'Outros']
)

if categoria == 'Discord':
    st.header('Gerador de Nitro Gifts')
    quantidade = st.number_input('Quantos Gifts você gostaria de gerar?', min_value=1, value=1)
    if st.button('Gerar'):
        codigos_gerados = gerar_codigos(quantidade)
        for codigo in codigos_gerados:
            st.write(codigo)

elif categoria == 'Keys de Consoles':
    st.header('Gerador de Keys de Consoles')
    quantidade = st.number_input('Quantas keys você gostaria de gerar?', min_value=1, value=1)
    if st.button('Gerar'):
        codigos_gerados = gerar_codigos(quantidade)
        for codigo in codigos_gerados:
            st.write(codigo)

elif categoria == 'Cards':
    st.header('Gerador de Cards')
    quantidade = st.number_input('Quantos cards você gostaria de gerar?', min_value=1, value=1)
    if st.button('Gerar'):
        codigos_gerados = gerar_codigos(quantidade)
        for codigo in codigos_gerados:
            st.write(codigo)

elif categoria == 'Online games':
    st.header('Gerador de Keys para Jogos Online')
    quantidade = st.number_input('Quantas keys você gostaria de gerar?', min_value=1, value=1)
    if st.button('Gerar'):
        codigos_gerados = gerar_codigos(quantidade)
        for codigo in codigos_gerados:
            st.write(codigo)

elif categoria == 'Outros':
    st.header('Outros Geradores')
    st.write('Funcionalidade não implementada ainda.')
