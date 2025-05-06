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
    cantidadTotalPreguntas = 8

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
            "\n\033[1;35mIngresá A para ir directo a copiar una hebra de ADN, o ingresá B para deshacer la hélice de ADN: \033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                respuesta = input(
                    "Oh no! El ADN se encuentra tan enrrollado en las proteínas histonas que es imposible realizar "
                    "la transcripción. ¿Qué harías?\n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Ingresá A para ir directo a copiar una hebra de ADN, "
                    "o ingresá B para deshacer la hélice de ADN\n")
        self.encontrarGen()


    def encontrarGen(self):
        respuesta = input(
            "\nBien! Ahora que la hélice está extendida, debes encontrar dentro de la hebra molde del ADN el gen que "
            "te dará la información necesaria para la proteína que querés sintetizar. ¿Qué hacés a continuación? "
            "\033[1;35mIngresá A para buscar la región promotora que da inicio al gen que estás buscando, o ingresa B para "
            "intentar plegarte en cualquier lugar de la cadena de ADN (hoy te sentís con suerte!) \033[0m\n")
        while respuesta != "A":
            self.chequearSalida(respuesta)
            if respuesta == "B":
                respuesta = input(
                    "Parece que la suerte no logrará la expresión génica! Ingresá A para buscar la región promotora que "
                    "da inicio al gen que estás buscando, o ingresa B para intentar plegarte en cualquier lugar de la "
                    "cadena de ADN \n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Ingresá A para buscar la región promotora que da inicio "
                    "al gen que estás buscando, o ingresa B para intentar plegarte en cualquier lugar de la cadena de ADN\n")
        self.corroborarCorrespondenciaNucleotidos()


    def corroborarCorrespondenciaNucleotidos(self):
        respuesta = input(
            "\nGenial, encontraste la región promotora y por lo tanto el inicio del gen cuyos nucleótidos debes "
            "transcribir. Antes de seguir, corroboramos que sepas cómo vas a hacer la transcripción! \033[1;35mPor ejemplo, si una "
            "secuencia de la hebra molde del ADN a transcribir es 'ACCATCAG', ¿cuál de las siguientes secuencias de ARN "
            "es correcta? A: 'TGGTAGTC' o B: 'UGGUAGUC'\033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
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
        respuesta = input(
            "\nExcelente! Los nucleótidos timina de ADN deben ser sustituídos por nucleótidos uracilo de ARN. Entonces, "
            "sabes cómo transcribir los nucléotidos, y encontraste la región promotora para empezar la transcripción. "
            "\033[1;35mUna vez allí: A, decidis llevar vos misma la información del gen hasta la próxima etapa (no confiás en nadie "
            "más para este trabajo!); o B, sintentizás una cadena de ARN mensajero y transcribís allí la información "
            "(que viva el trabajo en equipo!) \033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                respuesta = input(
                    "Parece que el intento de guardar vos misma los nucleótidos no funciona! Intentá de nuevo, ¿querés "
                    "llevar vos misma la información del gen hasta la próxima etapa (opción A) o preferís sintentizar una "
                    "cadena de ARN mensajero y transcribir allí la información (opción B)?\n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! ¿Querés llevar vos misma la información del gen hasta "
                    "la próxima etapa (opción A) o preferís sintentizar una cadena de ARN mensajero y transcribir allí "
                    "la información (opción B)? \n")

        print(
            "\nLa transcripción ha sido realizada con éxito: la cadena de ARN mensajero está lista, tu trabajo como "
            "ARN polimerasa ha terminado! Pero el ARN mensajero debe seguir trabajando, así que te proponemos seguir "
            "sus pasos! \033[0m\n")
        self.encontrarRibosoma()


    def encontrarRibosoma(self):
        respuesta = input(
            "\nComo ARN mensajero, debes encontrar un ribosoma, que construirá la proteína en base a la información "
            "que llevás. \033[1;35mEscribí A para salir del núcleo celular, o B para buscar un ribosoma dentro del núcleo. \033[0m\n")
        while respuesta != "A":
            self.chequearSalida(respuesta)
            if respuesta == "B":
                respuesta = input(
                    "¡Encontrar un ribosoma en el núcleo está difícil! Escribí A para salir del núcleo celular, o B "
                    "para seguir busando un ribosoma dentro del núcleo. \n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Escribí A para salir del núcleo celular, o B para buscar "
                    "un ribosoma dentro del núcleo.  \n")
        self.ingresarAlRibosoma()


    def ingresarAlRibosoma(self):
        respuesta = input(
            "\nSaliste del núcleo y encontraste un ribosoma! Allí transcurrirá la traducción y síntesis de la proteína. "
            "El ribosoma posee una subunidad grande y una subunidad pequeña entre las cuales irás avanzando para que se "
            "pueda leer toda tu secuencia de a tres nucleótidos a la vez (lo que se denomina codón). \033[1;35mPero momento, ¿cómo "
            "sabrá en qué codón de tu secuencia debe empezar a traducir? Escribí A para que el ribosoma arranque al "
            "principio de tu cadena, o B para que busque un codón de inicio dentro de tu cadena: \033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
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
        respuesta = input(
            "\n¡Así es! Existe un codón de inicio, generalmente el primer triplete de nucleótidos AUG, que indica dónde "
            "iniciará la secuencia peptídica; al ser AUG, el primer aminoácido especificado es la metionina. Pero "
            "alguien debe unirse a tus codones para interpretarlos y traer el aminoácido correspondiente a cada uno "
            "(lo que denominamos traducción). \033[1;35m¿Quién hará esta tarea? Indica A si crees que será otra organela, o B "
            "si crees que será el ARN de transferencia: \033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                respuesta = input(
                    "¡Ninguna otra organela parece querer hacer el trabajo! Indica A si quieres seguir buscando otra "
                    "organela, o B si crees que será el ARN de transferencia:  \n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Indica A si crees que será otra organela, o B si crees "
                    "que será el ARN de transferencia:  \n")
        self.finalizarTraduccion()


    def finalizarTraduccion(self):
        respuesta = input(
            "\nExacto! El ARN de transferencia posee por un lado un anticodón que se complementa con uno de tus codones, "
            "y en el extremo opuesto el aminoácido que corresponde a dicho codón. Mientras la subunidad pequeña del "
            "ribosoma atrae a cada ARN de transferencia correspondiente y lo une a tus codones, la subunidad más grande "
            "separa el aminoácido y comienza a armar la cadena protéica. Una vez que el ARN de transferencia dejó su "
            "aminoácido, se libera y deja lugar al ARN de transferencia siguiente, mientras tu cadena se mueve a su vez "
            "al siguiente codón. \033[1;35m¿Cuándo termina este proceso? Ingresá A si crees que el ribosoma da la señal de fin, "
            "o ingresá B si crees que vos como cadena de ARN mensajero das la señal de fin: \033[0m\n")
        while respuesta != "B":
            self.chequearSalida(respuesta)
            if respuesta == "A":
                respuesta = input(
                    "¡Parece que el ribosoma no encuentra forma de indicar el fin de la traducción! Ingresá A para que "
                    "el ribosoma siga intentando dar la señal de fin, o ingresá B si crees que vos como cadena de "
                    "ARN mensajero debés dar la señal: \n")
            else:
                respuesta = input(
                    "Lo siento, no existe la opción indicada! Ingresá A si crees que el ribosoma da la señal de fin, "
                    "o ingresá B si crees que vos como cadena de ARN mensajero das la señal de fin:  \n")
        proteina2.imprimirProteinaFinal()
        print((
                  "\n\033[1;35mFelicitaciones!! Al dar la señal de fin de la traducción con un codón de finalización, haz logrado "
                  "terminar el proceso de sintetizar la proteína :) Te esperamos para la próxima expresión génica!!\033[0m"))
        quit()


    def chequearSalida(self, respuesta: str):
        if respuesta == "S":
            print("¡Hasta la próxima!")
            quit()
