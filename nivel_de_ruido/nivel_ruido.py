# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:06:27 2020

@author: Oscar
"""

import numpy as np
import wavio
from nivel_de_ruido.audio import Audio

class NivelRuido:
    """Calcula el nivel de ruido en dB luego de importar un archivo
        de audio en formato .wav.
        Grafica la forma de onda del audio.
        @vrsión: 1.0 30/05/2020
        @autor: Óscar Acosta, Universidad Distrital/Universidad de San Buenaventura
    """

    @staticmethod
    def carga_audio(nombre_archivo):
        audio_file = wavio.read(nombre_archivo)
        linsp = np.linspace(0, len(audio_file.data) / audio_file.rate, num=len(audio_file.data))
        return Audio(data=audio_file.data, linsp=linsp, rate=audio_file.rate)


    def calcular_db(self, nombre_archivo):
        audio = self.carga_audio(nombre_archivo)
        audio_64 = np.int64(audio.data)
        audio_len = len(audio_64)
        square = np.int64(np.zeros(audio_len))
        for i in range(len(audio_64)):
            square[i] = (audio_64[i]**2)
        square_sum = sum(square)
        mean = (square_sum /audio_len)
        rms = np.sqrt(mean)
        dbfs = 20 * np.log10(rms/(np.iinfo(np.int16).max))
        leq = 122.7 - abs(dbfs)
        return leq
