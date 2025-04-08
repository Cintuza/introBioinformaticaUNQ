import unittest
import pytest
from posicionesDeMotivos import obtenerIdentificadoresConSusMotivos

class PosicionesDeMotivosTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    # Prueba de la funcion obtenerIdentificadoresConSusMotivos() con una lista de identificadores
    # de proteina
    def test_obtenerIdentificadoresConSusMotivos(self):
        identificadores = ['Q9GJS9', 'B5ZC00', 'Q727N0', 'Q38HX2']
        obtenerIdentificadoresConSusMotivos(identificadores)
        captured = self.capsys.readouterr()
        self.assertEqual('Q9GJS9\n[53, 241]\nB5ZC00\n[84, 117, 141, 305, 394]\nQ38HX2\n[235]\n', captured.out)

if __name__ == '__main__':
    unittest.main()
