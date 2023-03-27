import pytest
from exercitiu_student import Student

class TestStudent:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.nume = 'Alex'
        self.prenume = 'Ionescu'
        self.varsta = 22
        self.note = [10, 8, 9]
        self.student = Student(
            self.nume,
            self.prenume,
            self.varsta,
            self.note,
        )

    def test_creare_obiect_student(self):
        assert self.student.nume == self.nume
        assert self.student.prenume == self.prenume
        assert self.student.varsta == self.varsta
        assert self.student.note == self.note
        assert self.student.medie == sum(self.note)/len(self.note)

    def test_verificare_medie_promovare_student_adevarata(self):
        assert self.student.promovat() is True

    def test_verificare_medie_nepromovare_student(self):
        nume = 'Elvis'
        prenume = 'Munteanu'
        varsta = 35
        note = [6, 3, 2, 4]
        student_elvis = Student(nume, prenume, varsta, note)
        assert student_elvis.promovat() is False

    def test_prezentare_student(self):
        format_prezentare_student = f"{self.student.nume} {self.student.prenume}, {self.student.varsta} ani, media: {self.student.medie}."
        assert self.student.prezentare() == format_prezentare_student

    def test_adaugare_note_student(self):
        nr_note_curent = len(self.student.note)
        self.student.adauga_nota(10)
        rezultat_asteptat = nr_note_curent + 1
        assert len(self.student.note) == rezultat_asteptat

    def test_scadere_nota_student_daca_nota_exista(self):
        nota = 8
        nr_note_curent = len(self.student.note)
        self.student.scade_nota(nota)
        rezultatul_asteptat = nr_note_curent - 1
        assert len(self.student.note) == rezultatul_asteptat

    def test_scadere_nota_student_daca_nota_nu_exista(self):
        nota = 5
        nr_note_curent = len(self.student.note)
        self.student.scade_nota(nota)
        assert len(self.student.note) == nr_note_curent

