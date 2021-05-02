# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:06:27 2020

@author: Oscar
"""

import numpy as np
import wavio
import logging
from NivelDeRuido.Audio import Audio
from Resources.AwsS3Resource import AwsS3Resource

class NivelRuido:
    """Calcula el nivel de ruido en dB luego de importar un archivo
        de audio en formato .wav.
        Grafica la forma de onda del audio.
        @vrsión: 1.0 30/05/2020
        @autor: Óscar Acosta, Universidad Distrital/Universidad de San Buenaventura
    """

    def carga_audio(self, nombreArchivo):
        w = wavio.read(nombreArchivo)
        t = np.linspace(0, len(w.data) / w.rate, num=len(w.data))
        return Audio(data=w.data, t=t, fs=w.rate)


    def calcular_db(self, nombreArchivo):
        audio = self.carga_audio(nombreArchivo)
        audio_64 = np.int64(audio.data)    # Los datos de audio se pasan a 64 bits para poder realizar los cálculos
        N = len(audio_64)
        square = np.int64(np.zeros(N))
        for i in range(len(audio_64)):
            square[i] = (audio_64[i]**2)
        square_sum = sum(square)
        mean = (square_sum /N)
        rms = np.sqrt(mean)
        dBFS = 20 * np.log10(rms/(np.iinfo(np.int16).max))
        Leq = 122.7 - abs(dBFS)
        return Leq