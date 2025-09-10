# Taller de fundamentos de PNL de D-Lab Python

[![Datahub](https://img.shields.io/badge/launch-datahub-blue)](https://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdlab-berkeley%2FPython-Text-Analysis&urlpath=lab%2Ftree%2FPython-Text-Analysis%2F&branch=main)
[![Binder](https://img.shields.io/badge/launch-binder-579aca.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/dlab-berkeley/Python-Text-Analysis/HEAD)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Este repositorio contiene los materiales para D-Lab Python NLP Fundamentals
taller. 

## Prerequisitos

* Recomendamos asistir a Fundamentos de Python, Organización de datos de Python y
* Fundamentos de Python Machine Learning antes de este taller.

Consulte el [Catálogo de talleres] (https://dlab-berkeley.github.io/dlab-workshops/) de D-Lab para explorar todos los talleres, ver lo que se está ejecutando ahora y revisar los requisitos previos.

## Objetivos del taller

Este taller de 3 partes preparará a los participantes para avanzar con la investigación utilizando el procesamiento del lenguaje natural (NL), con un enfoque especial en las aplicaciones de las ciencias sociales. Exploramos enfoques fundamentales para aplicar métodos computacionales al texto en Python. Cubrimos algunos de los principales paquetes utilizados en NLP, incluidos scikit-learn, NLTK, spaCy y Gensim.

1. **Parte 1: Preprocesamiento.** ¿Cómo estandarizamos y limpiamos el texto?
¿Documentos? Los datos de texto son ruidosos y, a menudo, necesitamos desarrollar una canalización en
Con el fin de estandarizar los datos para facilitar mejor el modelado computacional. Aprenderá operaciones de preprocesamiento comunes y específicas de la tarea, 
familiarizarse con los paquetes de NLP de uso común y de lo que son capaces. También aprenderá sobre tokenizadores,
y cómo han cambiado desde el advenimiento de los grandes modelos de lenguaje.
2. **Parte 2: Bolsa de palabras.** Para realizar cualquier análisis computacional de datos de texto, necesitamos idear enfoques para convertir el texto en un 
representación numérica. Aprenderá cómo convertir datos de texto en una matriz de frecuencia y cómo TF-IDF complementa la representación de la bolsa de palabras.
También aprenderá sobre la configuración de parámetros de un vectorizador y aplicará la clasificación de opiniones a los datos de texto vectorizados.
3. **Parte 3: Incrustaciones de palabras.** Las incrustaciones de palabras sustentan casi todos los modelos de lenguaje modernos. En este taller, aprenderás las diferencias 
entre una representación de bolsa de palabras e incrustaciones de palabras. Se le presentará el cálculo de la similitud del coseno entre palabras y aprenderá cómo 
Las incrustaciones de palabras pueden sufrir sesgos.

Los materiales para esta serie de talleres están diseñados para complementarse unos con otros. La Parte 2 asume familiaridad con el contenido de la Parte 1, y la Parte 3 requiere de manera similar la comprensión de las dos partes anteriores.

## Instrucciones de instalación

Anaconda es un útil software de gestión de paquetes que permite ejecutar Python
y cuadernos Jupyter fácilmente. Instalar Anaconda es la forma más fácil de hacer
Seguro que tienes todo el software necesario para ejecutar los materiales para este taller.
Si desea ejecutar Python en su propia computadora, complete lo siguiente
Pasos previos al taller:

1. [Descargue e instale Anaconda (Python 3.9
distribución)](https://www.anaconda.com/products/individual). Haga clic en el icono
Botón "Descargar".

2. Descargue el [taller] Análisis de texto de Python
materiales](https://github.com/dlab-berkeley/Python-Text-Analysis):

- Haga clic en el botón verde "Código" en la parte superior derecha del repositorio
información.
- Haga clic en "Descargar Zip".
- Extraiga este archivo a una carpeta en su computadora donde pueda fácilmente
acceder a él (recomendamos Escritorio).

3. Opcional: si estás familiarizado con 'git', puedes clonarlo
repositorio abriendo una terminal e ingresando el comando 'git clone
git@github.com:dlab-berkeley/Python-Text-Analysis.git'.

## ¿Python no funciona en su computadora portátil? 

Si no tiene Anaconda instalada y los materiales cargados en su taller
para cuando comience,  recomendamos *encarecidamente* usar el centro de datos de D-Lab para
Ejecute los materiales para estas lecciones. Para acceder al DataHub, haga clic en el botón
siguiente botón:

[![Datahub](https://img.shields.io/badge/launch-datahub-blue)](https://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdlab-berkeley%2FPython-Text-Analysis&urlpath=lab%2Ftree%2FPython-Text-Analysis%2F&branch=main)

El DataHub descarga este repositorio, junto con los paquetes necesarios, y
le permite ejecutar los materiales en un cuaderno de Jupyter que se almacena en UC
Los servidores de Berkeley. No es necesaria ninguna instalación por su parte, solo necesita
un navegador de Internet y una identificación de CalNet para iniciar sesión. Al usar DataHub, puede
Guarde su trabajo y vuelva a él en cualquier momento. Cuando quieras volver a tu
trabajo guardado, simplemente vaya directamente a [DataHub] (https://datahub.berkeley.edu), firme
y haga clic en la carpeta 'Python-Text-Analysis'.

Si no tiene una identificación de Berkeley CalNet, aún puede ejecutar estas lecciones en el
cloud, haciendo clic en este botón:

[![Binder](https://img.shields.io/badge/launch-binder-579aca.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/dlab-berkeley/Python-Text-Analysis/HEAD)

Binder funciona de manera similar al D-Lab DataHub, pero en un conjunto diferente de
Servidores. Sin embargo, al usar Binder, no puede guardar su trabajo.

## Ejecutar el código

Ahora que tiene todo el software y los materiales necesarios, debe ejecutar el
código.

1. Abra la aplicación Anaconda Navigator. Deberías ver el logotipo de la serpiente verde
en tu pantalla. Tenga en cuenta que esto puede tardar unos minutos en cargar el archivo
primera vez. 

2. Haga clic en el botón "Iniciar" debajo de "JupyterLab" y navegue por su archivo
sistema en el panel izquierdo a la carpeta 'Python-Text-Analysis'
Descargado arriba. Tenga en cuenta que, si descarga los materiales de GitHub, el
el nombre de la carpeta puede ser 'Python-Text-Analysis-main'.

3. Vaya a la carpeta 'lecciones' y busque el cuaderno correspondiente a la
taller al que asiste.

4. Presione Mayús + Entrar (o Ctrl + Entrar) para ejecutar una celda.

5. Deberá instalar paquetes adicionales según el taller que
están asistiendo. Los comandos de instalación se realizan en los cuadernos, ya que
Continúe con cada parte del taller.

Tenga en cuenta que todos los pasos anteriores se pueden ejecutar desde la terminal, si está
familiarizado con cómo interactuar con Anaconda de esa manera. Sin embargo, el uso de
Anaconda Navigator es la forma más fácil de comenzar si es tu primera vez
trabajando con Anaconda.

# Recursos adicionales

- [Grupo de Trabajo de Análisis de Texto Computacional (CTAWG)](http://dlabctawg.github.io)
- [Info 256: Procesamiento aplicado del lenguaje natural](https://www.ischool.berkeley.edu/courses/info/256)
- [*Procesamiento del habla y el lenguaje*](https://web.stanford.edu/~jurafsky/slp3/) por Jurafsky y Martin.
- [Técnicas modernas de aprendizaje profundo aplicadas al procesamiento del lenguaje natural](https://nlpoverview.com/index.html) (libro de texto en línea)

# Acerca del D-Lab de UC Berkeley

D-Lab trabaja con profesores, personal de investigación y estudiantes de Berkeley para avanzar
Investigación intensiva en ciencias sociales y humanidades con uso intensivo de datos. Nuestro objetivo en D-Lab es
proporcionar capacitación práctica, apoyo del personal, recursos y espacio para permitirle
use R para sus propias aplicaciones de investigación. Nuestros servicios se adaptan a todos los niveles de habilidad
y no se necesitan antecedentes en programación, estadística o informática.
Ofrecemos estos servicios en forma de talleres, consultoría personalizada y
grupos de trabajo que cubren una variedad de temas de investigación, herramientas digitales y
lenguajes de programación.

Visite la [página de inicio de D-Lab](https://dlab.berkeley.edu/) para obtener más información sobre nosotros.
Puede ver nuestro [calendario](https://dlab.berkeley.edu/events/calendar) para
próximos eventos, aprenda cómo utilizar nuestros
[consultoría](https://dlab.berkeley.edu/consulting) y [datos
servicios](https://dlab.berkeley.edu/data), y echa un vistazo a los próximos
[talleres](https://dlab.berkeley.edu/events/workshops). Suscríbete a nuestro
[newsletter](https://dlab.berkeley.edu/news/weekly-newsletter) para mantenerse al día
fecha en eventos, servicios y oportunidades de D-Lab.

# Otros talleres de D-Lab Python

D-Lab ofrece una variedad de talleres de Python, dirigidos a diferentes niveles de
pericia.

## Talleres introductorios

- [Python Fundamentals](https://github.com/dlab-berkeley/Python-Fundamentals)
- [Manejo de datos de Python](https://github.com/dlab-berkeley/Python-Data-Wrangling)
- [Visualización de datos de Python](https://github.com/dlab-berkeley/Python-Data-Visualization)

## Talleres intermedios y avanzados

- [Fundamentos geoespaciales de Python](https://github.com/dlab-berkeley/Geospatial-Data-and-Mapping-in-Python)
- [Raspado web y API de Python](https://github.com/dlab-berkeley/Python-Web-Scraping)
- [Aprendizaje automático de Python](https://github.com/dlab-berkeley/Python-Machine-Learning)
- [Análisis de texto de Python](https://github.com/dlab-berkeley/Python-Text-Analysis)
- [Aprendizaje profundo de Python](https://github.com/dlab-berkeley/Python-Deep-Learning)

# Colaboradores

-  [Mingyu Yuan](https://github.com/mingyu-yuan)
- [Pratik Sachdeva](https://github.com/pssachdeva)
- [Tom van Nuenen](https://github.com/tomvannuenen)
- [Ben Gebre-Medhin](http://gebre-medhin.com)
- [Laura Nelson](http://www.lauraknelson.com)
- [Teddy Roland](https://teddyroland.com/about/)
- [Geoff Bacon](http://linguistics.berkeley.edu/~bacon/)
- [Caroline Le Pennec-Caldichoury](https://dlab.berkeley.edu/people/caroline-le-pennec)

Estos materiales han evolucionado a lo largo de varios años. Se desarrollaron por primera vez
por Laura Nelson y Teddy Roland, con contribuciones y revisiones realizadas por Ben
Gebre-Medhin, Geoff Bacon y Caroline Le Pennec-Caldichoury y Pratik Sachdeva. 
Fueron renovados por Mingyu Yuan en el verano de 2024.
