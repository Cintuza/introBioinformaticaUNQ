import random

# Probabilidades de estructura secundaria de los aminoácidos
estructurasSecundariasDeAminoacidos = {
"Glu" : (1.59, 0.52, 1.01),
"Ala" : (1.41, 0.72, 0.82),
"Leu" : (1.34, 1.22, 0.57),
"Met" : (1.30, 1.14, 0.54),
"Gln" : (1.27, 0.98, 0.84),
"Lys" : (1.23, 0.69, 1.07),
"Arg" : (1.21, 0.84, 0.90),
"His" : (1.05, 0.80, 0.81),

"Val" : (0.90, 1.87, 0.41),
"Ile" : (1.09, 1.67, 0.47),
"Tyr" : (0.74, 1.45, 0.76),
"Cys" : (0.66, 1.40, 0.54),
"Trp" : (1.02, 1.35, 0.65),
"Phe" : (1.16, 1.33, 0.59),
"Thr" : (0.76, 1.17, 0.90),

"Gly" : (0.43, 0.58, 1.77),
"Asn" : (0.76, 0.48, 1.34),
"Pro" : (0.34, 0.31, 1.32),
"Ser" : (0.57, 0.96, 1.22),
"Asp" : (0.99, 0.39, 1.24),
}

# Estructuras posibles
estructuras = ("H", "B", "L")

# Recibe un aminoacido codificado como la nomenclatura clasico de tres letras en string.
# Devuelve un string que representa su estructura secundaria codificada como H (hélice), B (hoja beta plegada) o
# L (bucle)
def obtenerEstructuraDeAminoacido(aminoacido):
    probabilidadesDelAminoacido = estructurasSecundariasDeAminoacidos.get(aminoacido)
    estructura = random.choices(estructuras, probabilidadesDelAminoacido)
    return estructura[0]
