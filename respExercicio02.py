class Aluno:
    def __init__(self, nome: str, matricula: str, curso: str, notas=None):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = [] if notas is None else list(notas)

    def adicionar_nota(self, nota):
        try:
            self.notas.append(float(nota))
        except (TypeError, ValueError):
            raise ValueError("Nota. Use um número.")

    def calcular_media(self) -> float:
        if not self.notas:
            return 0.0
        return round(sum(self.notas) / len(self.notas), 2)

    def status(self):
        media = self.calcular_media()
        print("Aprovado" if media >= 7.0 else "Reprovado")