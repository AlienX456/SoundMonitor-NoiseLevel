from NivelDeRuido.NivelRuido import NivelRuido
from unittest import TestCase


class TestCalculoNivelRuido(TestCase):

    def test_nivel(self):
        nivelRuido = NivelRuido()
        Leq = nivelRuido.calculardB("test/97.5DbAudio.wav")
        assert round(Leq, 1) == 97.5



