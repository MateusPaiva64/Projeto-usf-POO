import streamlit as st
from computador import Computador

st.set_page_config(page_title="Simulador Profissional de Computador", layout="centered")
st.title("Simulador Profissional de Computador")

if "computador" not in st.session_state:
    st.session_state.computador = None

if "log_acoes" not in st.session_state:
    st.session_state.log_acoes = []

def adicionar_log(mensagem):
    st.session_state.log_acoes.append(mensagem)

def criar_computador():
    st.session_state.computador = Computador(
        marca=st.session_state.marca,
        modelo=st.session_state.modelo,
        memoria_ram=st.session_state.memoria_ram,
        armazenamento=st.session_state.armazenamento,
        sistema_operacional=st.session_state.sistema_operacional,
    )
    adicionar_log("Computador criado com sucesso!")

with st.form("form_criar_pc"):
    st.subheader("Informações do Computador")
    marca = st.text_input("Marca", key="marca")
    modelo = st.text_input("Modelo", key="modelo")
    memoria_ram = st.number_input("Memória RAM (GB)", min_value=2, max_value=128, step=2, key="memoria_ram")
    armazenamento = st.number_input("Armazenamento (GB)", min_value=128, max_value=2048, step=128, key="armazenamento")
    sistema_operacional = st.selectbox("Sistema Operacional", ["Windows", "Linux", "MacOS", "Outro"], key="sistema_operacional")
    submitted = st.form_submit_button("Criar Computador", on_click=criar_computador)

if st.session_state.computador:
    pc = st.session_state.computador

    st.markdown("---")
    st.subheader("Informações do Computador")
    st.text_area("Detalhes completos", pc.informacoes_completas(), height=180, max_chars=None, key="info_pc", disabled=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ligar Computador"):
            mensagem = pc.ligar_computador()
            adicionar_log(mensagem)
    with col2:
        if st.button("Desligar Computador"):
            mensagem = pc.desligar_computador()
            adicionar_log(mensagem)

    st.markdown("---")
    st.subheader("Gerenciamento de Programas")

    programa_para_instalar = st.text_input("Nome do Programa para Instalar")
    if st.button("Instalar Programa"):
        if programa_para_instalar.strip() == "":
            adicionar_log("Por favor, insira o nome do programa.")
        else:
            mensagem = pc.instalar_programa(programa_para_instalar.strip())
            adicionar_log(mensagem)

    if st.button("Mostrar Programas Instalados"):
        programas = pc.mostrar_programas_instalados()
        adicionar_log(f"Programas instalados: {programas}")

    st.markdown("---")
    if st.button("Formatar Disco"):
        mensagem = pc.formatar_disco()
        adicionar_log(mensagem)

    st.markdown("---")
    st.subheader("Histórico de Ações")
    for msg in st.session_state.log_acoes:
        st.write(msg)

