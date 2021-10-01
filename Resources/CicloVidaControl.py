from datetime import datetime
from NivelDeRuido.NivelRuido import NivelRuido
from Resources.AwsS3Resource import AwsS3Resource
import os

class CicloVidaControl:

    def __init__(self):
        self.__nivel_ruido = NivelRuido()
        self.__aws_s3_resource = AwsS3Resource()

    def process_audio(self, nombre_archivo):
        metadata = self.__aws_s3_resource.download_object(nombre_archivo)
        start_time = datetime.now()
        leq = self.__nivel_ruido.calcular_db(nombre_archivo)
        finish_time = datetime.now()
        duration = finish_time - start_time
        os.remove(nombre_archivo)
        return leq, metadata, duration.total_seconds()


