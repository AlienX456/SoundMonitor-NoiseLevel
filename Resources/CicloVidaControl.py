from NivelDeRuido.NivelRuido import NivelRuido
from Resources.AwsS3Resource import AwsS3Resource
import os

class CicloVidaControl:

    def __init__(self):
        self.__nivel_ruido = NivelRuido()
        self.__aws_s3_resource = AwsS3Resource()

    def process_audio(self, nombreArchivo):
        self.__aws_s3_resource.download_object(nombreArchivo)
        Leq = self.__nivel_ruido.calcular_db(nombreArchivo)
        os.remove(nombreArchivo)
        return Leq


