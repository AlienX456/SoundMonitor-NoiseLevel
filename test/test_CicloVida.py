from unittest import TestCase, mock
from Resources.CicloVidaControl import CicloVidaControl
import os

class test_CicloVida(TestCase):

    @mock.patch('Resources.CicloVidaControl.AwsS3Resource')
    @mock.patch('Resources.CicloVidaControl.NivelRuido.calcular_db')
    def test_cicloDeVida(self, calcular_db, awsS3Resource):
        open("./test/test_file", 'a').close()
        assert os.path.isfile('./test/test_file')
        test_leq = 95.7
        calcular_db.return_value = test_leq
        cicloVidaControl = CicloVidaControl()
        Leq = cicloVidaControl.process_audio("./test/test_file")
        assert not os.path.isfile('test_file"')
        assert test_leq == Leq
