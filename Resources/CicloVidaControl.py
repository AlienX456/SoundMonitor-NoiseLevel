from NivelDeRuido.NivelRuido import NivelRuido
from Resources.AwsS3Resource import AwsS3Resource
import os

class CicloVidaControl:

    def __init__(self):
        self.__nivelDeRuido = NivelRuido()
        self.__awsS3Resource = AwsS3Resource()

    def processAudio(self, nombreArchivo):
        self.__awsS3Resource.download_object(nombreArchivo)
        Leq = self.__nivelDeRuido.calculardB(nombreArchivo)
        os.remove(nombreArchivo)
        return Leq


