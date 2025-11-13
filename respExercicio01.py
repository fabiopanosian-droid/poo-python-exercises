class Aluno:
    def __init__(self, nome: str, matricula: str, curso: str):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        return f"Nome: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}"


class Disciplina:
    def __init__(self, nome: str, codigo: str, carga_horaria: int):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"Nome: {self.nome} | Código: {self.codigo} | Carga horária: {self.carga_horaria}h"


if __name__ == "__main__":
    # Dois alunos
    a1 = Aluno("Maria Silva", "2021001", "Engenharia de software")
    a2 = Aluno("João Pereira", "2021002", "Internet das Coisas")

    # Duas disciplinas
    d1 = Disciplina("Engenharia de Software", "eng101", 60)
    d2 = Disciplina("Internet das Coisas", "iot101", 45)

    print("Alunos:")
    print(a1)
    print(a2)

    print("\nDisciplinas:")
    print(d1)
    print(d2)