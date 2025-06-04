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