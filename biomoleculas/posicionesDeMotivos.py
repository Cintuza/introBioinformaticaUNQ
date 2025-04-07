import requests

"""
Dada una lista de identificadores de proteina, tomados de UniProt, obtiene la secuencia de la proteina 
y busca las posiciones donde se encuentra el motivo de N-glicosilación dentro de la secuencia. 
Imprime el identificador junto con la lista de posiciones.
"""
def obtenerIdentificadoresConSusMotivos(listaDeIdentificadores : list):
    for identificador in listaDeIdentificadores:
        secuencia = obtenerSecuenciaAPartirDeIdentificador(identificador)
        posicionesDeMotivos = encontrarMotivos(secuencia)
        if posicionesDeMotivos:
            print(identificador)
            print(posicionesDeMotivos)

# Dado un identificador string tomado de UniProt, consulta en la api de dicha base de datos y devuelve
# tambien como string solo la secuencia de la proteina correspondiente al identificador pasado como argumento.
def obtenerSecuenciaAPartirDeIdentificador(identificador : str):
    url = 'https://rest.uniprot.org/uniprotkb/' + identificador + '.fasta'
    respuesta = requests.get(url)
    secuencia = extraerSecuenciaDeRequest(respuesta)
    return secuencia

# Dada una response de un request a la api de UniProst a partir de un identificador de proteina,
# devuelve solo la secuencia que corresponde a la proteina.
def extraerSecuenciaDeRequest(respuesta):
    primerOcurrencia = respuesta.text.find('\n')
    soloSecuencia = respuesta.text[primerOcurrencia:]
    soloSecuenciaSinEnter = soloSecuencia.replace('\n', '')
    return soloSecuenciaSinEnter

# Dada una secuencia representada en string, devuelve True si corresponde al motivo de N-glicosilación,
# y False en caso contrario.
def esMotivo(subSecuencia : str):
    if subSecuencia[1] == 'P':
        return False
    if (subSecuencia[2] != 'S') and (subSecuencia[2] != 'T'):
        return False
    if subSecuencia[3] == 'P':
        return False
    return True

# Dada la secuencia de una proteina representada como un string, devuelve la lista de posiciones
# donde se encuentra el motivo de N-glicosilación, donde cada posición es la posicion del primer
# aminoacido del motivo. Si el motivo no se encuentra en la secuencia, devuelve una lista vacia.
def encontrarMotivos(secuencia : str):
    posicionAminoacido = 0
    posicionesDeMotivos = []
    motivos = []
    for aminoacido in secuencia:
        if aminoacido == 'N':
            posibleMotivo = secuencia[posicionAminoacido:posicionAminoacido+4]
            if esMotivo(posibleMotivo):
                posicionesDeMotivos.append(posicionAminoacido)
                motivos.append(posibleMotivo)
        posicionAminoacido += 1
    return posicionesDeMotivos