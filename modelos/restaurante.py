class Restaurante:
    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha
        self.avaliacoes = []
        self.ativo = True


    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def exibir_avaliacoes(self):
        if not self.avaliacoes:
            print("Sem avaliações.")
        for avaliacao in self.avaliacoes:
            print(avaliacao)

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def __str__(self):
        estado = "Ativo" if self.ativo else "Inativo"
        return f"Restaurante: {self.nome} - Tipo de Cozinha: {self.tipo_cozinha} - Estado: {estado}"

