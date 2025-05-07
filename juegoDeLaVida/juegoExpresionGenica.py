import proteina2
"""
Juego muy simple donde quien juega sigue el camino de la ARN polimerasa y del ARN mensajero para explicar el proceso
de expresión génica, es decir, la síntesis de una proteína.
Para ello se deben responder preguntas con dos opciones de respuesta, A o B.
Para comenzar, ejecutar main().
Para salir del juego, ingresar una S.
"""

def main():
    nuevoJuego = JuegoExpresionGenica()
    nuevoJuego.iniciarJuego()

class JuegoExpresionGenica:
    def __init__(self):
        self.ultimaRespuestaEsCorrecta = True
        self.cantidadTotalPreguntas = 8
        self.respuestasCorrectas = 0

    @property
    def ultimaRespuestaEsCorrecta(self):
        return self._ultimaRespuestaEsCorrecta

    @ultimaRespuestaEsCorrecta.setter
    def ultimaRespuestaEsCorrecta(self, valor):
       self._ultimaRespuestaEsCorrecta = valor

    @property
    def respuestasCorrectas(self):
        return self._respuestasCorrectas

    @respuestasCorrectas.setter
    def respuestasCorrectas(self, respuestas):
        self._respuestasCorrectas = respuestas

    def getCantidadTotalPreguntas(self):
        return self.cantidadTotalPreguntas


    def iniciarJuego(self):
        print(
            "\nBienvenide! En este juego vas a llevar adelante la expresión génica de una célula eucariota, es decir, "
            "el proceso de sintetizar una proteína a partir de un gen. Para ello vas a tener que decidir qué es lo que "
            "tienen que hacer les diferentes actores involucrados en este proceso, y conseguir así la deseada proteína. "
            "Buena suerte!!\n")
        respuesta = input("\033[1;35mIngresa cualquier tecla para iniciar el juego o S para salir: \033[0m\n")
        self.chequearSalida(respuesta)
        print(
            "\nVamos a comenzar! Recordá, en cualquier momento podes salir del juego ingresando S. \n\nSos una ARN "
            "polimerasa que iniciará el proceso de expresión génica en el núcleo de la célula. Para ello, debés "
            "encontrar el gen dentro de la cadena de ADN que sintetiza la proteína de tu interés. ¿Qué harías primero?")
        self.acoplarseAlADN()


    def acoplarseAlADN(self):
        respuesta = input(
            "\n\033[1;35mIngresá A para ir directo a copiar una hebra de ADN, o ingresá B si crees que hay que "
            "hacer un paso previo: \033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                self.actualizarContadorConRespuestaIncorrecta()
                respuesta = input(
                    "Oh no! El ADN se encuentra tan enrrollado en las proteínas histonas que es imposible realizar "
                    "la transcripción. ¿Qué harías?\n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Ingresá A para ir directo a copiar una hebra de ADN, "
                    "o ingresá B para hacer algún paso previo\n")
        self.encontrarGen()


    def encontrarGen(self):
        self.actualizarContadorConRespuestaCorrecta()
        respuesta = input(
            "\nBien! Ahora que la hélice está extendida, debes encontrar el gen dentro de la cadena de ADN que "
            "te dará la información necesaria para la proteína que querés sintetizar. ¿Por dónde empezar? "
            "\033[1;35mIngresá A para buscar la región promotora, o ingresa B para buscar desde el inicio "
            "de la cadena de ADN.\033[0m\n")
        while respuesta != "A":
            self.chequearSalida(respuesta)
            if respuesta == "B":
                self.actualizarContadorConRespuestaIncorrecta()
                respuesta = input(
                    "Parece que la suerte no logrará la expresión génica! Ingresá A para buscar la región promotora que "
                    "da inicio al gen que estás buscando, o ingresa B para buscar desde el inicio de la "
                    "cadena de ADN \n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Ingresá A para buscar la región promotora que da inicio "
                    "al gen que estás buscando, o ingresa B para buscar desde el inicio de la cadena de ADN\n")
        self.corroborarCorrespondenciaNucleotidos()


    def corroborarCorrespondenciaNucleotidos(self):
        self.actualizarContadorConRespuestaCorrecta()
        respuesta = input(
            "\nGenial, encontraste la región promotora y por lo tanto el inicio del gen cuyos nucleótidos debes "
            "transcribir. Antes de seguir, corroboramos que sepas cómo vas a hacer la transcripción! \033[1;35mPor ejemplo, si una "
            "secuencia de la hebra molde del ADN a transcribir es 'ACCATCAG', ¿cuál de las siguientes secuencias de ARN "
            "es correcta? A: 'TGGTAGTC' o B: 'UGGUAGUC'\033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                self.actualizarContadorConRespuestaIncorrecta()
                respuesta = input(
                    "Dale una revisión a tus conocimientos sobre transcripción e intentalo de nuevo! Si la secuencia de "
                    "la hebra molde del ADN a transcribir es 'ACCATCAG', ¿cuál de las siguientes secuencias de ARN es "
                    "correcta? A: 'TGGTAGTC' o B: 'UGGUAGUC' \n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Si la secuencia de la hebra molde del ADN a transcribir "
                    "es 'ACCATCAG', ¿cuál de las siguientes secuencias de ARN es correcta? A: 'TGGTAGTC' o B: 'UGGUAGUC' \n")
        self.iniciarTranscripcion()


    def iniciarTranscripcion(self):
        self.actualizarContadorConRespuestaCorrecta()
        respuesta = input(
            "\nExcelente! Los nucleótidos timina de ADN deben ser sustituídos por nucleótidos uracilo de ARN. ¿Dónde "
            "transcribís la información para que llegue al próximo paso? "
            "\033[1;35mEscribí A si decidis si transcribís la información en un ARN de traducción; o B, si "
            "transcribís la información en un ARN mensajero\033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                self.actualizarContadorConRespuestaIncorrecta()
                respuesta = input(
                    "¡Parece que no existe lo que buscás! ¿Querés buscar un ARN de traducción (opción A) o preferís "
                    "sintentizar una cadena de ARN mensajero y transcribir allí la información (opción B)?\n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! ¿Querés buscar un ARN de traducción (opción A) o "
                    "preferís sintentizar una cadena de ARN mensajero y transcribir allí la información (opción B)? \n")

        print(
            "\nLa transcripción ha sido realizada con éxito: la cadena de ARN mensajero está lista, tu trabajo como "
            "ARN polimerasa ha terminado! Pero el ARN mensajero debe seguir trabajando, así que te proponemos seguir "
            "sus pasos! \033[0m\n")
        self.encontrarRibosoma()

    def encontrarRibosoma(self):
        self.actualizarContadorConRespuestaCorrecta()
        respuesta = input(
            "\nComo ARN mensajero, salís del núcleo para buscar la organela que construirá la proteína en base "
            "a la información que llevás. \033[1;35mEscribí A si crees que debés buscar un ribosoma para realizar "
            "esta tarea, o B si crees que debés buscar una mitocontria.\033[0m\n")
        while respuesta != "A":
            self.chequearSalida(respuesta)
            if respuesta == "B":
                self.actualizarContadorConRespuestaIncorrecta()
                respuesta = input(
                    "¡La mitocondria no parece preparada para esta tarea! Escribí A para buscar un ribosoma, o B "
                    "para seguir probando con una mitocondria.\n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Escribí A para buscar un ribosoma, o B "
                    "para seguir probando con una mitocondria.\n")
        self.ingresarAlRibosoma()


    def ingresarAlRibosoma(self):
        self.actualizarContadorConRespuestaCorrecta()
        respuesta = input(
            "\nEn el ribosoma transcurrirá la traducción y síntesis de la proteína. "
            "El ribosoma posee una subunidad grande y una subunidad pequeña entre las cuales irás avanzando para que se "
            "pueda leer toda tu secuencia de a tres nucleótidos a la vez (lo que se denomina codón). \033[1;35mPero momento, ¿cómo "
            "sabrá en qué codón de tu secuencia debe empezar a traducir? Escribí A para que el ribosoma arranque al "
            "principio de tu cadena, o B para que busque un codón de inicio dentro de tu cadena: \033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                self.actualizarContadorConRespuestaIncorrecta()
                respuesta = input(
                    "¡Empezar al inicio de tu cadena sin revisar antes genera un error! Escribí A para que el ribosoma "
                    "siga intentando arrancar al principio de tu cadena, o B para que busque un codón de inicio dentro "
                    "de tu cadena: \n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Escribí A para que el ribosoma arranque al principio de "
                    "tu cadena, o B para que busque un codón de inicio dentro de tu cadena: \n")
        self.buscarARNDeTraduccion()


    def buscarARNDeTraduccion(self):
        self.actualizarContadorConRespuestaCorrecta()
        respuesta = input(
            "\n¡Así es! Existe un codón de inicio que indica dónde iniciará la secuencia peptídica. Pero "
            "alguien debe unirse a tus codones para interpretarlos y traer el aminoácido correspondiente a cada uno "
            "(lo que denominamos traducción). \033[1;35m¿Quién hará esta tarea? Indica A si crees que será otro ARN mensajero, o B "
            "si crees que será un ARN de transferencia: \033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                self.actualizarContadorConRespuestaIncorrecta()
                respuesta = input(
                    "¡Ninguna otra organela parece querer hacer el trabajo! Indica A si quieres seguir buscando otro "
                    "ARN mensajero, o B si crees que será el ARN de transferencia:  \n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Indica A si crees que será otro ARN mensajero, o B si crees "
                    "que será el ARN de transferencia:  \n")
        self.finalizarTraduccion()


    def finalizarTraduccion(self):
        self.actualizarContadorConRespuestaCorrecta()
        respuesta = input(
            "\nExacto! El ARN de transferencia posee por un lado un anticodón que se complementa con uno de tus codones, "
            "y en el extremo opuesto el aminoácido que corresponde a dicho codón. Mientras la subunidad pequeña del "
            "ribosoma atrae a cada ARN de transferencia correspondiente y lo une a tus codones, la subunidad más grande "
            "separa el aminoácido y comienza a armar la cadena protéica. Una vez que el ARN de transferencia dejó su "
            "aminoácido, se libera y deja lugar al ARN de transferencia siguiente, mientras tu cadena se mueve a su vez "
            "al siguiente codón. \033[1;35m¿Cuándo termina este proceso? Ingresá A si crees que el ARN de transferencia "
            "da la señal de fin, o ingresá B si crees que vos como cadena de ARN mensajero das la señal de fin: \033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                self.actualizarContadorConRespuestaIncorrecta()
                respuesta = input(
                    "¡Parece que el ribosoma no encuentra forma de indicar el fin de la traducción! Ingresá A para que "
                    "el ARN de transferencia siga intentando dar la señal de fin, o ingresá B si crees que vos como cadena de "
                    "ARN mensajero debés dar la señal: \n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Ingresá A si crees que el ARN de transferencia da la señal de fin, "
                    "o ingresá B si crees que vos como cadena de ARN mensajero das la señal de fin:  \n")
        self.actualizarContadorConRespuestaCorrecta()
        proteina2.imprimirProteinaFinal()
        print((
                  "\n\033[1;35mFelicitaciones!! Al dar la señal de fin de la traducción con un codón de finalización, haz logrado "
                  "terminar el proceso de sintetizar la proteína :) Te esperamos para la próxima expresión génica!!\033[0m"))
        quit()

    def chequearSalida(self, respuesta: str):
        if respuesta == "S":
            print("¡Hasta la próxima!")
            quit()

    def mostrarContadorDeRespuestas(self):
        respuestas = '\033[1;42m'
        for valor in range(self.respuestasCorrectas):
            respuestas += ' ' + str(8 - valor)
        if self.ultimaRespuestaEsCorrecta == False:
            respuestas += '\033[1;41m ' + str(self.getCantidadTotalPreguntas() - self.respuestasCorrectas)
        print('\nRespuestas correctas: ' + respuestas + '\033[0m')

    def actualizarContadorConRespuestaCorrecta(self):
        self.ultimaRespuestaEsCorrecta = True
        self.respuestasCorrectas += 1
        self.mostrarContadorDeRespuestas()

    def actualizarContadorConRespuestaIncorrecta(self):
        self.ultimaRespuestaEsCorrecta = False
        self.mostrarContadorDeRespuestas()