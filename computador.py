class Computador:
    def __init__(self, marca, modelo, memoria_ram, armazenamento, sistema_operacional):
        self.__marca = marca
        self.__modelo = modelo
        self.__memoria_ram = memoria_ram  # GB
        self.__armazenamento = armazenamento  # GB
        self.__sistema_operacional = sistema_operacional
        self.__ligado = False
        self.__programas_instalados = []

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_memoria_ram(self):
        return self.__memoria_ram

    def get_armazenamento(self):
        return self.__armazenamento

    def get_sistema_operacional(self):
        return self.__sistema_operacional

    def is_ligado(self):
        return self.__ligado

    def get_programas_instalados(self):
        return self.__programas_instalados.copy()

    # Setters
    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def set_memoria_ram(self, nova_memoria_ram):
        self.__memoria_ram = nova_memoria_ram

    def set_armazenamento(self, novo_armazenamento):
        self.__armazenamento = novo_armazenamento

    def set_sistema_operacional(self, novo_so):
        self.__sistema_operacional = novo_so

    # Métodos de ação
    def ligar_computador(self):
        if not self.__ligado:
            self.__ligado = True
            return f"O computador {self.__marca} {self.__modelo} foi ligado com sucesso."
        else:
            return "O computador já está ligado."

    def desligar_computador(self):
        if self.__ligado:
            self.__ligado = False
            return f"O computador {self.__marca} {self.__modelo} foi desligado."
        else:
            return "O computador já está desligado."

    def instalar_programa(self, nome_programa):
        if not self.__ligado:
            return "Ligue o computador antes de instalar programas."
        if nome_programa in self.__programas_instalados:
            return f"O programa '{nome_programa}' já está instalado."
        self.__programas_instalados.append(nome_programa)
        return f"Programa '{nome_programa}' instalado com sucesso."

    def mostrar_programas_instalados(self):
        if not self.__programas_instalados:
            return "Nenhum programa instalado."
        return ", ".join(self.__programas_instalados)

    def formatar_disco(self):
        if not self.__ligado:
            return "Ligue o computador antes de formatar."
        self.__programas_instalados = []
        return "Disco formatado com sucesso. Todos os programas foram removidos."

    def informacoes_completas(self):
        status = "Ligado" if self.__ligado else "Desligado"
        programas = self.mostrar_programas_instalados()
        return (f"Marca: {self.__marca}\n"
                f"Modelo: {self.__modelo}\n"
                f"Memória RAM: {self.__memoria_ram} GB\n"
                f"Armazenamento: {self.__armazenamento} GB\n"
                f"Sistema Operacional: {self.__sistema_operacional}\n"
                f"Status: {status}\n"
                f"Programas Instalados: {programas}")
