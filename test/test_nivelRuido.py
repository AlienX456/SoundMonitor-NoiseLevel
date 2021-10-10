from nivel_de_ruido.nivel_ruido import NivelRuido
from unittest import TestCase


class TestCalculoNivelRuido(TestCase):

    def test_nivel(self):
        nivel_ruido = NivelRuido()
        leq = nivel_ruido.calcular_db("test/97.5DbAudio.wav")
        assert round(leq, 1) == 97.5



