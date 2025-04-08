### DESAFÍO I
¿Podrías buscar un ejemplo de macromoléculas que almacenen información sobre la ‘identidad’ de un organismo dado?

Un ejemplo de macromolécula que almacena dicha información es el ADN (ácido desoxirribonucleico). El mismo es uno 
de los dos tipos de ácidos nucleicos existentes. Contienen material genético y por tanto información sobre la 
identidad de un determinado organismo.

### DESAFÍO II
Proponé una forma de expresar la información contenida en la estructura primaria de las proteínas usando tipos de 
datos de los lenguajes de programación que conocés.

Si la estructura primaria contiene sólo la cadena/secuencia de aminoácidos, creo que la misma podría expresarse 
como una cadena de strings; cada string sería un aminoácido. Con una lista, podrían contenerse los elementos 
repetidos y en el orden dado. Sin embargo, de esta forma se perderían enlaces extras entre elementos de la cadena 
que no sean consecutivos. 

### DESAFÍO III
¿En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?

La estructura terciaria, si entendí bien, tendría representados los átomos y moléculas y su ubicación en el espacio. 
Sería una representación mucho más detallada que sólo tener los aminoácidos, ya que se indica la conformación de cada 
uno de ellos. Es decir, cada elemento debería definirse por su tipo propio, su relación/enlaces posibles con los otros 
elementos, y su relación con el espacio. Por lo que creo que deberían crearse objetos específicos para definirlos.

### DESAFÍO IV
Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. ¿Cuáles fueron sus 
contribuciones en este campo? ¿Qué nos cuenta su historia acerca del mundo de la ciencia?

Su contribución fue la obtención de imágenes que llevaron a la identificación del ADN.

Durante su estadía en Francia, aprendió la técnica de difracción de rayos X y se convirtió una experta en la misma. 
De nuevo en Inglaterra, en la institución en la que se desarrollaba sus investigaciones, obtuvo las fotografías más 
nítidas hasta el momento de la molécula de ADN, mejorando el aparato que se utilizaba y el método para el mismo.

Sin embargo, Rosalind Franklin no llegó a publicar sus hipótesis sobre la estructura del ADN de forma inédita. Un 
colega suyo le mostró las imágenes a dos otros investigadores, quienes en base a ellas publicaron el artículo en el que 
se define por primera vez la estructura del ADN como la conocemos hoy. Ambos ganaron el Premio Nobel por dicho 
descubrimiento. El verdadero mérito de Rosalind en el mismo no fue reconocido ampliamente hasta varios años después.

Este hecho es una muestra más del machismo en la sociedad, en este caso en el ámbito científico. Las mujeres y 
diversidades no contamos, aún hoy en día, con igualdad de oportunidades. Y aún sucede en ámbitos laborales la 
apropiación del trabajo de las mujeres y diversidades por parte de los varones, sin darle ningún mérito. Reconocer esta 
realidad de desigualdad es la única forma de encontrar soluciones reales en la sociedad patriarcal en la que nos 
desarrollamos.

### DESAFÍO V
Escribí un scrip en Python que prediga la estructura secundaria que adoptará cada residuo (aminoácido) de la secuencia 
proteica dada, especificandola como H (si es una hélice), B (si es una hoja beta plegada) y L (si es un bucle o loop).

[Resuelto en estructuraSecundariaAminoacido.py](estructuraSecundariaAminoacido.py)

#### PREGUNTAS DISPARADORAS: 
¿Qué inputs tendría tu programa? ¿De qué modo se te ocurre configurar el output? ¡Guardate esta idea, la vamos a usar 
más adelante!

El input debería ser una representación del aminoácido; podría ser un string con el código del mismo. Si el output debe 
ser algo similar a una imagen o una representación gráfica de la estructura, podría ser una imagen hecha con caracteres.

#### PARA PENSAR: 
¿Cuántas proteínas puede sintetizar un organismo? ¿De qué depende la cantidad y la característica de las proteínas que 
puede sintetizar un organismo?

La síntesis de proteínas y su cantidad depende de las proteínas que pueda construir el ADN con la ayuda del ARN.

### DESAFÍO VI
¿Qué hace distintos a dos individuos de una especie? Propone una forma de corroborar tu respuesta realizando un 
diagrama de un posible método computacional para dicho fin.

Lo que hace diferentes a dos individuos son cadenas de ADN diferentes. Teniendo en cuenta la estructura primaria del 
ADN, que sería la secuencia de nucléotidos de una sola de las hebras o cadenas, se me ocurre que tomando 
desde el inicio ambas secuencias haría una comparación elemento por elemento (es decir, nucleótido por nucleótido) 
en orden; si en algún momento los dos elementos son diferentes, entonces los individuos son distintos.

#### PREGUNTAS DISPARADORAS: 
¿Qué información deberías tener? ¿De qué modo deberías expresar dicha información para el análisis?

Debería tener la secuencia de nucleótidos de una cadena de ADN. La forma de representar estos elementos depende de 
la profundidad de la información que se quiera obtener; a un nivel muy básico, una lista de strings donde cada 
cadena de caracteres represente un nucleótido quizás alcance.

### Desafío VII
Dado: Un máximo de 15 identificadores de la base de datos de proteínas UniProt; 
Retornar: Para cada proteína que posea el motivo de N-glicosilación, imprimir su identificador de acceso seguido de 
una lista de posiciones en la secuencia de la proteína donde se encuentra el motivo.

[Resuelto en posicionesDeMotivos.py](posicionesDeMotivos.py)

[Testeado en posicionesDeMotivosTest.py](posicionesDeMotivosTest.py)

### Desafío VIII
Dada la siguiente lista de sequencias, realizar el una representación Logo.

[`MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV`, 
`MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV`, 
`MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV`]

[Resuelto en representarListaDeSecuencias.ipynb](representarListaDeSecuencias.ipynb)

