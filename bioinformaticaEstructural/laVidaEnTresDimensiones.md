#### PARA PENSAR:
¿Por qué una célula querría destruir sus propias 
proteínas?

Para evitar que sigan iniciándose procesos que ya 
no son necesarios.

#### PARA PENSAR:
¿Qué información nos provee esta página [PDB]?

En la primera solapa encontramos un resumen de la información 
sobre la proteína. Se presenta un identificador e identificador único 
extendido de la proteína dentro de PDB, pero también encontramos 
identificadores únicos (DOI), y del Biological Magnetic Resonance 
Data Bank. Encontramos su clasificación, el organismo al que 
pertenece, y si la secuencia sufrió mutaciones.

Se menciona cuándo fue incorporada la proteína al PDB y por quiénes, 
y datos sobre el método mediante el cual la proteína fue identificada. 
Encontramos una representación gráfica de la estructura 
secundaria de la proteína en 3D, y datos sobre su contenido molecular.

También se presentan datos sobre la publicación en la cual 
se identificó la proteína (título, responsables de la autoría, 
datos de la publicación mayor, doi, resumen, etc.). Más abajo se 
presenta una sección llamada Macromoléculas donde encontramos 
datos de entidades similares (o posibilidad de buscarlas 
dentro de la base de datos), diferentes agrupamientos de los 
que forman parte (por porcentaje de identidad) y enlaces a 
algunos de ellos en UniProt, Pharos y GTEx. Finalmente vemos 
un historial de versiones del registro de la proteína.

En una segunda solapa encontramos un gráfico mayor de la proteína, 
con varias posibilidades de manipularla para quitar elementos, 
mover o ampliar la imagen, seleccionar alguna parte de la cadena 
según diferentes criterios, etc.

En la solapa siguiente vemos la clasificación de la proteína 
según fuentes externas y otras bases de datos. En la siguiente, 
encontramos mayores datos sobre el experimento en el cual se 
identificó la proteína. En la quinta solapa vemos un gráfico 
con la secuencia de la proteína con diferentes parámetros. En la 
sexta solapa encontramos una correspondencia entre la proteína 
y el genoma. En la última solapa volvemos a encontrar datos 
sobre el historial de versiones del registro.

En todas las solapas encontramos posibilidades para descargar 
los datos que ofrece la base de datos.

#### PARA PENSAR:
¿Cómo se determinó la estructura de esta proteína? A la izquierda 
vemos una representación de la estructura de ubiquitina. 
¿Qué significan las cintas, las flechas y las regiones angostas?

La estructura de la proteína se determinó mediante defracción / 
cristalografía de rayos X. Las cintas son hélices, las flechas 
son las hojas beta plegadas.

#### PARA PENSAR:
¿Representa esa imagen a la realidad del sistema biológico?

No exactamente, ya que la imagen pone énfasis en la forma, la 
estructura secundaria de la proteína; es una abstracción.

#### PARA PENSAR:
La estructura 1UBQ fue “refinada a una resolución de 1.8 
Angstroms”. Éste es el error asociado al experimento: 
mientras mayor es la resolución, menor es la certeza al 
determinar la posición de cada átomo ¿Cuál es la utilidad 
y los condicionamientos de usar un modelo científico que 
sabemos inexacto?

#### PARA PENSAR:
¿Qué diferencias y similitudes notamos respecto de la 
representación inicial? En el menú de la izquierda hay 
opciones de distintos tipos de representación y formas de 
colorear la estructura tridimensional. ¿Para qué podría 
ser útil visualizar lo mismo de distintas maneras?

Por un lado, la imagen del sumario del registro tiene 
diferenciados con colores cada segmento de la proteína (por 
ejemplo, cada hoja beta plegada de un color diferente). Por 
otro lado, la imagen de la solapa específica para la 
representación gráfica, además de estar en un sólo color, 
tiene representadas las partículas de agua que no pudieron 
eliminarse al cristalizar la proteína. Las herramientas para 
manipular la imagen son más numerosas aquí. Visualizar la 
misma proteína de maneras distintas nos permite ver detalles 
o establecer relaciones más fácilmente.

#### PARA PENSAR:
¿Qué información esperaría encontrar como resultado un 
experimento destinado a determinar la estructura terciaria 
de una molécula biológica?

Si hablamos de representaciones gráficas, esperaríamos 
encontrar una serie de puntos en el espacio.

#### PARA PENSAR: 
¿En qué consiste un archivo PDB?

https://files.rcsb.org/view/1UBQ.pdb

Consiste en información estructurada sobre la proteína, 
datos básicos que se encuentran en la primera solapa del 
registro de la proteína y describimos en puntos anteriores. 
Encontramos por ejemplo los residuos y la estructura que 
forman en el espacio (hélice, hoja beta, etc), la secuencia 
de residuos, etc.

#### PARA PENSAR:
Desplacémonos por el archivo hasta encontrar las líneas 
que comienzan con la palabra ATOM. ¿Qué tipo de información 
brinda esta sección?

Nos brinda información sobre la representación en 3D de 
la proteína: el número de átomo, el elemento químico, el 
aminoácido al que pertenece, la cadena, el número de aminoácido 
sus coordenadas en el espacio.

#### PARA PENSAR:
¿Podríamos extraer de este archivo información sobre la 
estructura primaria de la proteína en cuestión? ¿Cómo se 
presenta dicha información y qué significa la representación? 
Desde el punto de vista computacional: ¿de qué tipo de dato 
se trata esta información?

Sí, podemos extraerla de las líneas SEQRES (secuencia de 
residuos). Cada línea tiene el número de línea, la cantidad 
total de elementos que conforman la cadena, y los aminoácidos 
codificados en su clasificación de 3 letras. Se trata de un 
tipo de dato string.

#### PARA PENSAR:
¿Considera que el formato PDB es útil para presentar los 
resultados del experimento?

No, ya que es información que no se encuentra estructurada 
en campos propios, sino que usa campos generales. Sin 
metadatos que indiquen específicamente lo que significa 
cada dato, la información es más difícil de manipular.

#### PARA PENSAR: 
Observamos que la información respeta cierta estructura 
interna. ¿Cuáles son los beneficios y las limitaciones 
de imponer una estructura para comunicar los resultados 
de un experimento? Hemos visto que las proteínas tienen 
estructura tridimensional y hemos podido observar algunas 
características de las mismas. ¿Será igual con los ácidos 
nucléicos? Rosalind Franklin es una científica muy 
relevante, que tuvo menos reconocimiento del merecido. 
Contanos sobre los procedimientos que puso Rosalind.

La ventaja de tener los datos estructurados es que podemos 
manipular gran cantidad de registros e identificar en todos 
ellos un dato específico de forma automatizada. La desventaja 
es que estructurar los resultados es laborioso, y por otro 
lado implica la normalización de información que quizás 
es bastante diferente entre sí.

Sí, Rosalind Franklin fue quien propuso la técnica de 
difracción de rayos X y lo hizo para identificar la 
molécula de ADN.



### DESAFÍO I
Un caso de estudio interesante es el EGFR es uno de los 
principales marcadores de cáncer de pulmón. Para estudiar 
esta proteína, utilizaremos CaviDB, una base de datos en 
línea gratuita que provee información sobre las cavidades 
proteicas y sus propiedades. Sabemos que la estructura 
1M14 se corresponde con un confórmero activo, es decir 
una estructura con actividad, mientras que la estructura 
3W32 se corresponde con una conformación inactiva.

Compará el sitio activo de ambos confórmeros (posición 837) 
así como también los tamaños de los pockets. ¿Qué observás?

En el caso de la proteína 3W32, la posición 837 es un 
ácido aspártico (D) y en la proteína 1M14 dicha posición 
es en cambio una leucina. Ambos aminoácidos forman parte 
de un pocket o cavidad en sus correspondientes cadenas 
protéicas; las mismas parecen tener forma similar, pero 
la cavidad perteneciente a la proteína 
1M14 parece ser más grande, lo que se corrobora en su 
longitud (0.733 contra 0.56 de la cavidad perteneciente 
a la proteína 3W32).

### DESAFÍO II
Las variantes de AKR1C4 están asociadas con el trastorno 
bipolar y otros trastornos del estado de ánimo y la 
resistencia a los medicamentos.
Investigá la proteína usando la base de datos Uniprot 
y anotá los sitios relevantes biológicamente.

Se recogieron los datos de dicha proteína del siguiente 
registro:
https://www.uniprot.org/uniprotkb/P17516/feature-viewer#structure </br>
donde se encontraron sitios relevantes en las siguientes 
posiciones: 
- sitios (sin especificar): 54 y 84
- sitios de enlace: 20-24, 50, 117, 166-167, 190, 216-221 y 270-280
- sitios activos: 55

### DESAFÍO III
Analizá la estructura PDB 2FVLB ¿Cuántas cavidades fueron 
predichas para dicha estructura? ¿Hay alguna cavidad 
drogable? ¿Coincide con algún sitio de relavancia biológica?

Para la estructura de 2FVLB se predicen 17 cavidades, pero 
solo una es drogable. Y sí coincide con varios sitios de 
relevancia biológica anotados en el desafío anterior.

#### Para investigar
Investigá en qué consiste el docking, en qué ideas basa su 
funcionamiento ¿Cómo podría aprovecharse este método para 
tratar esta patología?

El docking es un método computacional utilizado para 
predecir la mejor orientación (generalmente aquella que 
requiera menor energía de unión) en la que una proteína 
se puede acoplar con otro elemento. Basa sus ideas en la 
estructura tercearia de las proteínas.

La idea es que los fármacos serán más efectivos cuanto 
mejor puedan acoplarse a las proteínas que producen una 
patología, y el docking puede ayudar a predecir cuál 
será el mejor lugar, el mejor pocket, para que ese 
acoplamiento suceda.

### DESAFÍO IV
Investigá en CaviDB las características estructurales 
de la Albúmina Humana sobre la estructura 1AO6A:
- ¿Cuántas cavidades fueron predichas para dicha estructura? 
¿Cuáles son las pricipales cavidades en tanto a tamaño 
de la proteína? ¿Existen cavidades que se solapen con 
los residuos descritos como relavantes para la actividad 
enzimática de la albúmina?

Se predicen 26 cavidades para dicha estructura. En cuanto 
a tamaño, podemos observar que las cavidades principales son 
la cavidad 1 (65 residuos), la 23 (28 residuos) y la 26 
(44 residuos). Todos los residuos mencionados para la 
actividad catalítica de la proteína forman parte de alguna 
cavidad excepto la Cys 34.

- ¿Alguna de las cavidades catalíticamente activas se 
encuentran activadas? ¿Qué rangos de pKa se observan en 
dichas cavidades?

Todas las cavidades se muestran activadas en un rango 
de 0 a 10.

### DESAFÍO V
Se sabe que en la albúmina bovina el sitio activo se 
encuentra corrido respecto del humano, aunque también 
involucra un aminoácido cargado (Lys 221). Investigá 
en CaviDB las características estructurales de la 
estructura de albúmina bovina 4JK4A y compará las 
características de su sitio activo con las características 
del sitio activo de la albúmina humana (Lys 199).

Según podemos ver en CaviDB, la albúmina bovina 4JK4A 
tiene 583 aminoácidos en su cadena, y su estructura 
secundaria predominante es en hélice. Para ella se han 
predicho 36 cavidades, de las cuales 4 se consideran 
drogables.

El sitio activo Lys 199 en la albúmina humana forma 
parte de una de las cavidades más grandes que presenta 
la proteína, mientras que el mismo sitio en la albúmina 
bovina (Lys 221) forma parte de dos cavidades más bien 
pequeñas.

#### Para investigar
Leé más sobre los hallazgos hechos por l@s investigadores/as 
de la Universidad Nacional de Quilmes sobre la evolución 
de albúminas y contrastalo con lo que pudiste observar.

El artículo menciona que las regiones conservadas entre 
ambas cadenas proteínicas también conservaron las 
cavidades y túneles que forman. Esto se corrobora con lo 
observado en el punto anterior.

### DESAFÍO VI
En el campo sequence query ingresá la siguiente secuencia 
colab, usando num_relax = 1 y template_mode = pdb100:</br>
sp|P03129|VE7_HPV16 Protein E7 OS=Human papillomavirus type 16 OX=333760 GN=E7 PE=1 SV=1 
MHGDTPTLHEYMLDLQPETTDLYCYEQLNDSSEEEDEIDGPAGQAEPDRAHYNIVTFCCKCDSTLRLCVQSTHVDIRTLEDLLMGTLGIVCPICSQKP

La corrida se ejecuta desde el Runtime --> Run all
- ¿Qué el campo template_mode? ¿Qué opciones pueden ser utilizadas?

Es un formato que podemos dar como guía para que AlphaFold 
estructure los resultados.

- ¿Qué regiones de la estructura resultante tienen una mayor confianza? Desarrollar un script que permita graficar los pLDDT por posición
