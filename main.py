from NivelDeRuido.NivelRuido import NivelRuido

def main():
    """Prueba unitaria"""
    medicion = NivelRuido()
    print("\n El nivel de ruido en dB es: {:.1f} decibeles \n ".format(medicion.calculardB("test/00_010346.wav")))


if __name__ == "__main__":
    main()