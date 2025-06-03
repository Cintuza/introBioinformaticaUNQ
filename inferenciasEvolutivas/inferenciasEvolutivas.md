Hemos estado trabajando sobre algunos casos concretos de estudio en el trabajo práctico anterior. En particular trabajamos sobre alineamientos de secuencias de Cyt P450 de distintos organismos (podés descargar las secuencias con las que trabajamos desde aquí). En esta ocasión trabajaremos sobre un gran misterio de la biología molecular: el caso del Humanomosca o Moscahumano. Seguramente vieron en la tele el resonado caso del niño con cabeza de mosca de fruta y como bien sabemos la tele nunca miente ¿no? Aún cuando se han realizado múltiples estudios que intentan darle una respuesta kafkiana a los padres, aún no se ha podido determinar cuánto de esta criatura conserva las características del niño. Para ello se secuenció el Cyt P450 del niño_mosca y se obtuvo la siguiente resultado:
> bartmosca 
> MGSGDAENGKKIFVQKCAQCHTYEVGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE

### DESAFÍO I
Detalla las tácticas y/o metodologías que deberían utilizarse 
para darles una respuesta a los padres del niño. Dadas las 
secuencias de Mosca, humano y Moscahumano ¿Qué criterios se 
les ocurren para comparar las secuencias? ¿Qué resultados 
obtienen del análisis anterior? ¿Qué resultado esperaría 
obtener si utilizara el resto de las secuencias en el análisis? 
¿Por qué?

Para saber cuánto queda en el bartmosca del niño, hacemos un 
alineamiento entre la secuencia dada y las de la mosca y una 
persona humana. Podemos comparar las secuencias contando el 
número de inserciones/deleciones que encontramos en la secuencia 
problema y las otras; aunque este método ignora los cambios 
intermedios que se podrían haber producido, si fue una mutación 
directa quizás podemos asumir que no hubo cambios intermedios. 
Sin embargo, para resultados más precisos de inferencias 
evolutivas se acude a modelos estadísticos de reconstrucción 
filogenética que permitan aproximar 
mejor los cambios evolutivos, y a partir de los cuales se puedan 
realizar árboles.

Del análisis anterior esperaría tener regiones que provengan de 
la secuencia de la mosca, regiones que provengan de una persona 
humana, pero también regiones en común, ya que debido a estudios 
evolutivos podemos asumir que hay ancestros en común. Si agregamos 
al análisis el resto de las secuencias, de acuerdo a qué tan 
cercanas o divergentes sean las especies de las mismas, podemos 
encontrar mayor o menor similitud en tal o cual región.


### DESAFÍO II
Como vimos anteriormente existen algunos softwares optimizados 
para confeccionar alineamientos de secuencias. En particular 
hemos trabajado con Clustal (Larkin et al. 2007). Confecciona 
el alineamiento para el punto I.

Puede verse el alineamiento múltiple realizado con Clustal en [secuenciasCytocromoCAlineadasClustal.fa](secuenciasCytocromoCAlineadasClustal.fa)

### DESAFÍO III
Mediante el uso del servidor de IQtree (Trifinopoulos et al. 2016), 
confecciona los árboles filogenéticos para los alineamientos 
obtenidos en el punto II. Como vemos, el servidor nos permite 
elegir el modelo de sustitución ¿A qué se refiere? ¿Qué es el 
Bootstrap? ¿De qué manera nos habla de la calidad de nuestro árbol? 
¿Cómo influye el número de Bootstraps en el resultado? 
Interpreten los resultados obtenidos, mediante la visualización 
de los árboles con la herramienta FigTree. ¿Es necesario realizar 
algún paso extra, previo a la interpretación del árbol? ¿Por qué?

Los modelos de sustitución se utilizan para calcular la verosimilitud 
de los árboles filogenéticos. Se usan para calcular el número de 
sustituciones que ocurrieron desde que un par de secuencias se 
hicieron divergentes de un ancestro común, es decir para estudiar 
distancias evolutivas.

Bootstrap es un método que consiste en, a partir de un alineamiento 
múltiple y su correspondiente árbol, generar alineamientos y 
árboles al azar usando las mismas secuencias. La diferencia entre 
el árbol original y los construídos al azar sirve para determinar 
qué tan confiable es el árbol original obtenido. Cuantas más 
corridas de bootstrap, son mayores las posibilidades contra las 
cuales comparar si nuestro árbol original es confiable.

Realizar un alineamiento confiable, con métodos de sustitución y 
cálculo de la verosimilitud diferente del azar, es indispensable 
para tener un árbol confiable.

Puede ver el archivo con el análisis y árbol obtenido de IQtree en [analisisArbolConBootstrapIQtree.iqtree](analisisArbolConBootstrapIQtree.iqtree). 
Puede además verse el árbol en formato NEWICK en el siguiente archivo: [arbolConBootstrapIQtree.treefile](arbolConBootstrapIQtree.treefile)

Puede verse la representación gráfica del árbol obtenida de FigTree en [representacionGraficaArbolBootstrapFigTree.jpg](representacionGraficaArbolBootstrapFigTree.jpg)