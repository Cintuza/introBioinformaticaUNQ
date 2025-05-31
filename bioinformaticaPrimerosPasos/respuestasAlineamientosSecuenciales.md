#### PARA PENSAR:
¿Qué tipo de información se puede extraer de la comparación de 
secuencias? ¿Cómo esperás que se vea en una comparación?

Se puede ver qué aminoácidos comparten en posiciones iguales, y 
por tanto extraer información sobre qué tanto funcionan de 
forma similar, pero además podemos extraer información sobre su 
relación evolutiva, y saber qué tan divergentes son. 
Podemos hacer esta comparación elemento a elemento de la secuencia.

#### PARA PENSAR:
¿Por qué crees que es mejor evaluar las relaciones evolutivas 
lejanas comparando proteínas?

Porque las secuencias de ácidos nucleicos tienen mayor variabilidad 
con el tiempo; sin embargo, recordando el código genético podemos 
ver que esa variabilidad puede no afectar a los aminoácidos que 
producen (es decir, distintas combinaciones de nucleótidos puede 
sintetizar el mismo aminoácido). Por lo tanto, puede que con el 
tiempo varíe la secuencia de nucleótidos, pero no tanto así la de 
aminoácidos (es decir, las proteínas), y por eso son mejores para 
evaluar relaciones evolutivas lejanas.

### DESAFIO I
Intentemos, entonces alinear estas dos palabras, para comprender 
mejor el problema. Alineá en la tabla interactiva las palabras 
"BANANA" y "MANZANA". 
¡Tomá nota de tus observaciones y de las conclusiones que se 
desprendan de estas observaciones! </br>
PREGUNTAS DISPARADORAS:</br>
¿Existe una única forma de alinearlas? 
¿Es alguno de los posibles alineamientos mejor que otro? 
Si así fuera ¿Por qué?

No existe una única forma de alinearlas. En principio con mis 
compañeros movimos las palabras enteras para hacerlas coincidir en 
lugares diferentes; luego partimos una de ellas, para que tener 
mayor número de coincidencias. Concluímos entonces que hay algunos 
alineamientos mejores que otros, y dependen del número de 
coincidencias.

### DESAFIO II
En la siguiente tabla interactiva distintos alineamientos para 
las palabras "ANA" y "ANANA". Verás que en el margen superior 
izquierdo aparece un valor de identidad calculado para cada 
alineamiento que intentes.
¡Tomá nota de los valores de identidad observados y de las 
conclusiones que se desprendan de estas observaciones!</br>
PREGUNTAS DISPARADORAS</br>
¿Son todos los valores iguales? 
¿Qué consideraciones deberían tenerse en cuenta a la hora de 
realizar el cálculo? ¿Se te ocurre, distintas formas de 
calcularlo? ¿Serán todas ellas igualmente válidas en Biología?

No todos los valores son iguales; el valor de identidad cambia 
de acuerdo a cómo alineamos las secuencias. Si las letras coinciden 
en ambas secuencias, el valor de identidad aumenta. También 
podemos hacerlas coincidir de varias maneras, cambiando de ubicación 
la palabra entera ANA al principio o al final de la secuencia
(obteniendo el mismo valor) o partiendo la palabra para que también 
coincidan (también obteniendo el mismo valor de identidad). No 
todas las formas son igualmente válidas; la validez de un alineamiento 
dependerá del contexto.

### DESAFIO III
Probá en tabla interactiva distintos alineamientos para las 
palabras "ANA" y "ANANA". Verás que en el margen superior 
izquierdo aparece un valor de identidad calculado para cada 
alineamiento que intentes y un botón para cambiar la penalidad que 
se le otorga a dicho para el cálculo de identidad.
Probá varias combinaciones, tomá nota de los valores de identidad 
observados y de las conclusiones que se desprendan de estas 
observaciones.</br>
PREGUNTAS DISPARADORAS</br>
¿Cómo se relacionan los valores de identidad obtenidos con las 
penalizaciones que se imponen al gap? ¿Qué implicancias crees que 
tiene una mayor penalización de gaps? ¿Se te ocurre alguna otra 
forma de penalización que no haya sido tenido en cuenta en este ejemplo?

Después de probar las combinaciones que habíamos realizado en el 
desafío uno, el valor de identidad bajaba si la palabra quedaba 
partida. Una mayor penalización bajará aún más el valor de identidad; 
es decir, hace que dos secuencias bajen su similitud. Se puede 
penalizar también la cantidad de gaps juntos que se insertan en la 
secuencia.

#### PARA PENSAR:
Entonces, pensando en un alineamiento de ácidos nucleicos ¿Cuáles 
te parece que son las implicancias de abrir un gap en el 
alineamiento? ¿Qué implicaría la inserción o deleción de una región 
de más de un residuo?

Abrir un gap en la secuencia puede partir un codón y por tanto 
puede alterar la secuencia de aminoácidos que produce la misma. 
Borrar o insertar una región tiene consecuencias similares, puede 
eliminar un aminoácido o insertarlo (asumiendo que la región 
incluye sólo codones), o como en el caso previo puede partir un 
codón de la cadena original, también generando cambios en el producto.

### DESAFIO IV
Probá en la tabla interactiva distintos alineamientos para las 
secuencias nucleotídicas. Podrás ver las traducciones para cada 
secuencia. Probá varias combinaciones, tomá nota de las 
observaciones y de las conclusiones que se desprendan de estas.

En las distintas alineaciones cambian efectivamente los aminoácidos 
que genera la secuencia de ácidos nucleicos. Es decir, los nucleótidos
y los gaps deben ser insertados con cuidado porque tiene esta 
consecuencia, cambia la proteína sintetizada.

#### PARA PENSAR:
¿Dá lo mismo si el gap que introducís cae en la primera, segunda 
o tercer posición del codón? ¿Cómo ponderarías las observaciones 
de este ejercicio para evaluar el parecido entre dos secuencias?

No es lo mismo, porque como vimos en el código genético, muchos 
aminoácidos comparten el primer y segundo nucleótido, variando sólo 
el tercero, por lo que variar el tercer nucleótido tiene más 
posibilidades de generar el mismo aminoácido. Por lo tanto, daría 
mayor ponderación respecto a la identidad a aquellos codones que 
varían en la tercera posición del codón.

### DESAFIO V
Te proponemos pensar los pasos a seguir en un alineamiento de dos 
secuencias cortas, teniendo en cuenta una matriz genérica de 
scoring (puntuación) que contemple las complejidades que estuvimos 
viendo, es decir que penalice de distinto modo una inserción o 
deleción, que una discordancia (mismatch) o una coincidencia 
(match). Escribilos o esquematizalos en un diagrama de flujo.

1) Armamos una matriz cuadrada de orden mxn, con una secuencia 
en la parte superior por fuera de la matriz como si fuera 
la primera fila, y la otra secuencia a la izquierda de la matriz 
como si fuera la primera columna.
2) Establecemos un valor para las coincidencias, para las 
discordancias y para los gaps.
3) En el primer espacio de la matriz a<sub>11</sub> colocamos un 0.
4) Empezamos a completar la matriz por fila de arriba hacia abajo 
y de izquierda a derecha; es decir, completaremos a<sub>12</sub>, 
a<sub>13</sub>, etc. hasta a<sub>1n</sub>, luego la fila siguiente 
desde a<sub>21</sub> hasta a<sub>2n</sub>, 
y así con todas las filas hasta a<sub>mn</sub>.
5) Para cada una de las posiciones siguientes a a<sub>11</sub> 
tomaremos las macromoléculas correspondientes a esa fila i y 
columna j y haremos el siguiente cálculo para determinar su 
valor de comparación:
- si las dos macromoléculas son iguales, se toma el valor de 
coincidencia
- si las dos macromoléculas son diferentes, se toma el valor de 
discordancia </br>
</br>
Ahora se toman los valores de las siguientes posiciones 
alrededor de la posición a<sub>ij</sub> que se está calculando, 
a saber:
- a<sub>i(j-1)</sub> si j-1 != 0 (lo que puede pasar para la primera columna)
- a<sub>(i-1)(j-1)</sub> si i-1 != 0 y j-1 != 0 (casos de primera fila y columna)
- a<sub>(i-1)j</sub> si i-1 != 0 (lo que puede pasar para la primera fila)</br>
</br>
De esos tres valores, se toma el valor mayor. Sumamos este valor 
mayor al valor de comparación calculado anteriormente. El resultado 
es el valor que se coloca en la posición a<sub>ij</sub>.

6) Una vez recorrida toda la matriz y habiendo llegado a la posición 
a<sub>mn</sub>, desde allí haremos el camino inverso hasta llegar 
a a<sub>11</sub> evaluando los valores de las posiciones que 
recorramos. Arrancamos el puntaje del alineamiento, que 
por ahora es cero, sumando el valor de a<sub>mn</sub>.
7) Creamos dos conjuntos ordenados, uno para cada secuencia, y 
agregamos el valor de la macromolécula correspondiente a la fila m 
y a la columna n a su lista correspondiente.
8) Evaluamos las posiciones adyacentes a<sub>m(n-1)</sub>, 
a<sub>(m-1)(n-1)</sub> y a<sub>(m-1)n</sub>. Si hay tres valores 
diferentes:
- si la posición con mayor valor es a<sub>(m-1)(n-1)</sub> 
(es decir en diagonal), se agregan las dos macromoléculas a sus 
correspondientes conjuntos en la posición que les corresponde 
en la secuencia. Nos movemos a dicha posición, sumamos el valor 
de la misma al puntaje del alineamiento y volvemos a efectuar este 
paso hasta llegar a a<sub>11</sub>.
- si la posición con mayor valor es a<sub>m(n-1)</sub>, se agrega 
un gap en la secuencia vertical, y se resta el valor de penalización 
de gap al puntaje del alineamiento. Nos movemos a dicha posición, 
sumamos el valor de la misma al puntaje del alineamiento y volvemos 
a efectuar este paso hasta llegar a a<sub>11</sub>.
- si la posición con mayor valor es a<sub>(m-1)n</sub>, se agrega 
un gap en la secuencia horizontal, y se resta el valor de 
penalización de gap al puntaje del alineamiento. Nos movemos a 
dicha posición, sumamos el valor de la misma al puntaje del 
alineamiento y volvemos a efectuar este paso hasta llegar a a<sub>11</sub>.
9) En caso de que haya empate entre los valores de las posiciones 
adyacentes evaluadas en el paso 8), deben hacerse dicho paso para 
cada una de ellas siguiendo todos los caminos, es decir, todos los 
alineamientos posibles y sus puntajes.
10) El mejor alineamiento, en el caso de que haya más de uno, será 
el que tenga el mejor puntaje.

#### PARA PENSAR: ¿En qué consiste la programación dinámica? ¿Por qué crees que es útil en este caso?

La programación dinámica sirve para optimizar algoritmos, 
reduciendo su tiempo de ejecución. Esto es útil en estos casos 
debido al volumen masivo de datos que puede implicar analizar 
secuencias y sus mejores alineamientos.

### DESAFIO VI
Utilizando la herramienta interactiva desarrolladas por el Grupo 
de Bioinformática de Freiburg probá distintos Gap penalties para 
el ejemplo propuesto y observá lo que ocurre. Interpretando la 
recursión, explicá con tus palabras de dónde salen los valores 
de la matriz que se construye. ¡Esquematiza tus conclusiones!

Las secuencias utilizadas fueron:</br>
AHC-NIRVS</br>
AICIN-RCK

Y fueron analizadas en https://needleman-wunsch.vercel.app/

Dejando valores de coincidencia = 1, de discordancia = -1, y de 
gap = -1, el porcentaje de identidad que calcula el sitio es 
del 44%, y el puntaje de alineamiento es -1. 
Este valor no cambiar al aumentar la penalización por gaps; es 
decir, llevarla por ejemplo a -2 o a -3. Sin embargo, dejar la 
penalización por gap igual a cero, hace que el puntaje de 
alineamiento sea 4.

La idea de ponderar en el valor de una posición de la matriz 
no sólo la coincidencia o no de esa posición en la cadena, 
sino también a sus posiciones adyacentes, tiene que ver con 
que varias posiciones coincidentes juntas arman una región 
conservada, es menos posible que esa coincidencia sea azarosa, 
y en términos evolutivos tiene mucho más valor para ver si dos 
secuencias son homólogas.

#### PARA PENSAR:
¿En qué casos serán de utilidad uno u otro tipo de alineamientos? 
¿Qué limitaciones tendrá cada uno?

La pregunta hace referencia a los alineamientos a pares de 
secuencias y a los alineamientos múltiples. Los primeros 
sirven para ver qué tan similares o divergentes son dos 
secuencias. Los alineamientos múltiples, por otro lado, sirven 
cuando tenemos una secuencia que no sabemos bien a qué es 
homóloga, por lo que alinearla con otras muchas secuencias 
permite encontrar secuencias similares que nos orientes en 
cuanto a su origen.

### DESAFIO VII
Calculá el E-value y % identidad utilizando el programa
Blast de la siguiente secuencia input usando 20000 hits, un e-value 
de 100 y tomando aquellos hits con un mínimo de 70% cobertura. 
Observe y discuta el comportamiento de : E-value vs. % id, 
Score vs % id, Score vs E-value:

VVGGLGGYMLGSAMSRPIIHFGSDYEDRYYRENMHRYPNQVYYRPMDEYSNQNNFVHDCVNITIKQHTVTTTTKGENFTETDVKMMERVVEQMCITQYERESQAYYQRGSSMVLFSSPPVILLISFLIFLIVG

Para esta búsqueda se utilizó la base curada de UNIPROT (SwissProt). 
La secuencia presentada pertenece a la especie humana, y al introducirla 
en el programa BLAST nos dice que el porcentaje de identidad es del 100%
(lo que tiene sentido, ya que el porcentaje de identidad representa la 
cantidad de matches de la secuencia con la original, que en este caso es 
ella misma) y un E-value de 3e-97 (valor que cuanto más bajo, más significante 
es el match, por lo que también tiene sentido).

Ajustando los parámetros como lo indica el enunciado del ejercicio, se 
obtuvieron 51 secuencias que produjeron alineamientos significativos con 
la secuencia original. La tabla resultante se muestra en principio ordenada 
por el E-value de cada resultado, de menor a mayor. 

Allí podemos observar que a medida que el E-Value aumenta, el porcentaje de 
identidad disminuye. Sin embargo, no se puede asegurar que esto sea estricto 
y se cumpla para todos los casos; por ejemplo, la secuencia correspondiente 
al mono araña (P51446) tiene un E-value mayor a las correspondientes al 
bovino híbrido (B5SY89) y al panda (Q6EH52) (a saber, E- value de 8e-86 vs 
7e-86), pero tiene un porcentaje de identidad también mayor (94.44% vs 92.06%).

Algo similar pasa en la relación entre el E-value y el score; mientras aumenta 
el E-value, disminuye el score, pero hay excepciones (véase el caso de las 
secuencias correspondientes al mandril y al nilgó). Es decir, BLAST 
penaliza un E-value alto, ya que considera que las similitides encontradas entre 
las secuencias no son probabilísticamente significativas sino más bien azarosas.

Si cambiamos el orden de la tabla y ahora la ordenamos por el score total 
de las secuencias de forma descendente, podemos comparar más fácilmente 
dicho valor con el porcentaje de identidad. Ambos valores disminuyen en 
paralelo, pero otra vez hay excepciones (la secuencia de la proteína del 
bovino híbrido, por ejemplo, tiene mayor score total que la correspondiente 
al mangabey, pero menor porcentaje de identidad). Es decir, la cantidad de 
matches entre dos secuencias en general hace que aumente el score total.

En ambos dos órdenes de la tabla, por E-value y por porcentaje 
de identidad, es interesante notar que los primeros diez resultados, es decir 
aquellos cuyos alineamientos son "más similares" a la secuencia humana, son primates. 
También podemos concluir que un bajo E-value (es decir, baja probabilidad de que 
las similitudes encontradas entre secuencias sea por azar) o un alto porcentaje 
de identidad (es decir la cantidad de matches del alineamiento de una secuencia 
contra la secuencia original) no definen por sí mismos la similitud entre 
dos secuencias (el score total), sino que es una combinación de ambas junto 
con otros factores.

### DESAFIO VIII
Realizá nuevas búsquedas usando la mitad de la secuencia problema 
y para un cuarto de la secuencia original. Compará los gráficos 
obtenidos. ¿Qué conclusiones puede sacas?

Para poder comparar, se realizó la búsqueda con los mismos 
parámetros que la búsqueda anterior (base de datos Swiss-Prot, 
un e-value de 100 y tomando aquellos hits con un mínimo de 
70% cobertura). La secuencia entera tiene 133 aminoácidos, la segunda 66 y la 
tercera 35, y los cortes se realizaron comenzando siempre por el 
principio de la cadena.

Lo primero que podemos notar es que la segunda y tercera 
secuencia traen más resultados, pero no muchos más (51, 53 y 57 
secuencias respectivamente), ya que reducir la cantidad de 
elementos de la secuencia puede hacer que se reduzcan las 
coincidencias pero también las discordancias y los gaps.

Los gráficos obtenidos permiten observar más fácilmente que, 
por ejemplo, la mayor parte de las secuencias se alinean con la 
secuencia original a partir del octavo elemento de la cadena
(la primera y segunda cadena tienen menos de cinco coincidencias 
a partir del primer elemento, mientras que la tercera tiene diez). 
A pesar de eso, en el gráfico de la tercera cadena (que recordemos 
es la más corta) podemos ver también que esos diez primeros 
alineamientos tienen muchas más discordancias que los primeros 
alineamientos de las otras dos secuencias.

### DESAFIO IX
Utilizando BLAST utilice búsquedas de similitud secuencial 
para identificar a la siguiente proteína:

MIDKSAFVHPTAIVEEGASIGANAHIGPFCIVGPHVEIGEGTVLKSHVVVNGHTKIGRDNEIYQ
FASIGEVNQDLKYAGEPTRVEIGDRNRIRESVTIHRGTVQGGGLTKVGSDNLLMINAHIAHDCT
VGNRCILANNATLAGHVSVDDFAIIGGMTAVHQFCIIGAHVMVGGCSGVAQDVPPYVIAQGNHA
TPFGVNIEGLKRRGFSREAITAIRNAYKLIYRSGKTLDEVKPEIAELAETYPEVKAFTDFFARS
TRGLIR

PARA PENSAR: ¿Cuál es la función de la proteína? 
¿A qué grupo taxonómico pertenece? 
A un nivel de significancia estadística adecuado, 
¿cuántas secuencias similares se encuentran?

La proteína es la Acyl-[acyl-carrier-protein]--UDP-N-
acetylglucosamine O-acyltransferase, y pertenece a la 
Escherichia coli APEC O1, una enterobacteria. 

Buscando con un e-value de 100 y una cobertura de mínimo 70% en 
la base de datos Swiss-Prot de UNIPROT, obtenemos 232 
secuencias. Sin embargo, si bien todas las secuencias tienen un 
e-value bajo, también tienen un bajo porcentaje de identidad. 
Si filtramos la búsqueda por aquellos alineamientos que tengan 
más de un 70% de identidad respecto de la secuencia problema, 
obtenemos 29 secuencias.

Finalmente, consultando la página de la proteína en UNIPROT 
(https://www.uniprot.org/uniprotkb/A1A7M5/entry) podemos rescatar 
que la proteína cumple funciones en la biosíntesis del lípido A, 
un glicolípido fosforilado que ancla el lipopolisacárido a la 
membrana externa de la célula (es decir cataliza una reacción química).