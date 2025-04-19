import re

"""
Encuentra, si existen, regiones promotoras con la caja TATA.
El metodo solicita un archivo en txt donde se encuentra almacenada la secuencia de ADN a analizar.
Si la caja TATAAA existe, devuelve la lista de posiciones donde se encuentra la misma dentro de la 
secuencia de ADN.
Si la caja no existe, imprime un mensaje en consola diciendolo.
"""
def encontrarRegionesPromotoras() :
    nombreDelDocumentoConSecuenciaDeADN = input("Ingrese el nombre del documento con la secuencia de ADN en formato txt: ")
    documentoConSecuenciaDeADN = open(nombreDelDocumentoConSecuenciaDeADN, "r")
    secuenciaDeADN = documentoConSecuenciaDeADN.read()
    regionesPromotoras = [match.start() for match in re.finditer("TATAAA", secuenciaDeADN)]
    if regionesPromotoras:
        return regionesPromotoras
    else:
        print("No existen regiones promotoras con la caja TATA")