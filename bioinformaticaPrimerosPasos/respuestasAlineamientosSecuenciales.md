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

### DESAFIO VII
Calculá el E-value y % identidad utilizando el programa
Blast de la siguiente secuencia input usando 20000 hits, un e-value 
de 100 y tomando aquellos hits con un mínimo de 70% cobertura. 
Observe y discuta el comportamiento de : E-value vs. % id, 
Score vs % id, Score vs E-value:

VVGGLGGYMLGSAMSRPIIHFGSDYEDRYYRENMHRYPNQVYYRPMDEYSNQNNFVHDCVNITIKQHTVTTTTKGENFTETDVKMMERVVEQMCITQYERESQAYYQRGSSMVLFSSPPVILLISFLIFLIVG

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