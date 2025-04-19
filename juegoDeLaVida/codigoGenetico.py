import random

# Codigo genetico para ARN expresado como diccionario; la clave corresponde a los aminoacidos
# expresados en la nomenclatura de una sola letra y el valor a sus valores posibles
# de codones expresados como una lista de strings
codigoGenetico = {
"E" : ["GAA", "GAG"],
"A" : ["GCU", "GCC", "GCA", "GCG"],
"L" : ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
"M" : ["AUG"],
"Q" : ["CAA", "CAG"],
"K" : ["AAA", "AAG"],
"R" : ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
"H" : ["CAU", "CAC"],

"V" : ["GUU", "GUC", "GUA", "GUG"],
"I" : ["AUU", "AUC", "AUA"],
"Y" : ["UAU", "UAC"],
"C" : ["UGU", "UGC"],
"W" : ["UGG"],
"F" : ["UUU", "UUC"],
"T" : ["ACU", "ACC", "ACA", "ACG"],

"G" : ["GGU", "GGC", "GGA", "GGG"],
"N" : ["AAU", "AAC"],
"P" : ["CCU", "CCC", "CCA", "CCG"],
"S" : ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
"D" : ["GAU", "GAC"],
}

# Recibe un aminoacido expresado en la nomenclatura de una sola letra, y devuelve al azar
# un posible codon de nucleotidos de ARN que produzca dicho aminoacido, según el codigo genetico.
# Tanto el aminoacido como el codon se expresan en strings.
def obtenerCodonParaAminoacido(aminoacido : str):
    codonesPosibles = codigoGenetico.get(aminoacido)
    codon = random.choices(codonesPosibles)
    return codon[0]

# Recibe una secuencia proteica representada como un string donde cada letra representa un
# aminoacido, y retorna una cadena de ARN que codifica para dicha secuencia.
def obtenerCadenaDeARNCodificante(secuenciaProteica : str):
    cadenaDeARN = ""
    for aminoacido in secuenciaProteica:
        codonParaAminoacido = obtenerCodonParaAminoacido(aminoacido)
        cadenaDeARN = cadenaDeARN + codonParaAminoacido
    return cadenaDeARN
