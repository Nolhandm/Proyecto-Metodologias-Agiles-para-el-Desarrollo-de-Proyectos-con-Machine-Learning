# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

Número de registros:  13703
Número de características:  66
Número de países:  193
Número de indicadores de desarrollo:  71
Tamaño del conjunto de datos: 9.55 MB

2 variables textuales : Country Name y Indicator Name que permiten identificar un pais y el indicador considerado
64 variables numericas : Las valores del indicador para el pais considerado entre 1960 y 2023

## Resumen de calidad de los datos

56.33% de datos faltantes en el conjunto. El numero de valores faltantes varia mucho segun el año, el indicador y el pais. 

Se eligé de conservar solo los datos de 2020 o más recientes y de eliminar indicadores presentes en menos de 75% de los paises. Mas detalles en el notebook [preprocesamiento y analisis de datos](https://github.com/Nolhandm/Proyecto-Metodologias-Agiles-para-el-Desarrollo-de-Proyectos-con-Machine-Learning/blob/master/scripts/preprocessing/preprocesamiento_y_an%C3%A1lisis_exploratorio.ipynb)

El conjunto no parece tener valores erroneos. Un resumen de las decisiones sobre las variables basada en valores extremos es disponible en el notebook [preprocesamiento y analisis de datos](https://github.com/Nolhandm/Proyecto-Metodologias-Agiles-para-el-Desarrollo-de-Proyectos-con-Machine-Learning/blob/master/scripts/preprocessing/preprocesamiento_y_an%C3%A1lisis_exploratorio.ipynb)

## Variable objetivo

El objetivo del proyecto es de realizar una agrupacion no hay variable objetivo.

## Variables individuales

Se realizó un análisis de correlación entre las variables para eliminar algunas de las que presentaban una correlación elevada entre ellas. Mas detalles en el notebook [preprocesamiento y analisis de datos](https://github.com/Nolhandm/Proyecto-Metodologias-Agiles-para-el-Desarrollo-de-Proyectos-con-Machine-Learning/blob/master/scripts/preprocessing/preprocesamiento_y_an%C3%A1lisis_exploratorio.ipynb)

Se puede ver en este reporte un análisis detallado de cada variable conservada al final de la análisis de datos y del preprocesamiento : [reporte.html](https://github.com/Nolhandm/Proyecto-Metodologias-Agiles-para-el-Desarrollo-de-Proyectos-con-Machine-Learning/blob/master/docs/data/reporte.html)

