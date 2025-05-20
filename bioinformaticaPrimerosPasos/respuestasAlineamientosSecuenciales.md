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