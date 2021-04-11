class Facultate():
    '''Clasa Facultate'''

    finantare_per_student = 230

    def __init__(self, nume, acronim, studenti):
        self.nume = nume
        self.acronim = acronim
        self.studenti = studenti

    @property
    def nume_facultate(self):
        return 'Facultatea de {}'.format(self.nume)

    @property
    def numar_studenti(self):
        return 'Numar studenti {} la facultatea {}'.format(self.studenti, self.acronim)

    @property
    def finantare(self):
        return self.finantare_per_student * self.studenti


if __name__ == "__main__":
    f1 = Facultate('Tehnologii Informationale', 'ti', 3720)
    print(f1.nume_facultate)
    print(f1.finantare)
