class Avaliacao:
    def __init__(self, nota, comentario):
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        return f"Avaliação: {self.nota} - Comentário: {self.comentario}"
