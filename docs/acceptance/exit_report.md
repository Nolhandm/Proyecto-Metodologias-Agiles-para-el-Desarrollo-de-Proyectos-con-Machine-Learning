# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning orientado a la agrupación automática de países según su dinámica socioeconómica y medioambiental. El objetivo fue aplicar técnicas de clustering no supervisado para identificar patrones globales que permitan orientar políticas diferenciadas de desarrollo sostenible. Se utilizó una red neuronal autoorganizada (SOM) y un algoritmo KMeans para lograr este objetivo. El despliegue del modelo se realizó mediante una aplicación desarrollada en Streamlit.

## Resultados del proyecto

- Entendimiento del negocio: Se estableció como objetivo la segmentación de países a partir de sus indicadores y socioeconomicos para identificar paises con dinamicas similares.

- Preparación de los datos: Se seleccionaron 34 indicadores socioeconómicos y ambientales desde el conjunto del Banco Mundial. Se conservaron 114 paises para realizar la agrupacion.

- Modelamiento y evaluación : Se utilizaron dos enfoques principales: KMeans y Self-Organizing Maps. El modelo SOM se combinó con KMeans para una segmentación más estructurada. Se aplicaron métricas como Silhouette Score (0.26), índice de Calinski-Harabasz (30.41) e índice Davies-Bouldin (1.89).

- Despliegue: Se desarrolló una aplicación funcional en Streamlit para visualizar los resultados del clustering y facilitar su interpretación por los usuarios.

- Descripción de los resultados :

Índice de silueta : 0.26 -> Es bajo, lo que indica que muchos países están cerca de los límites de sus respectivos clusters.

Índice de Calinski-Harabasz: 30.41 → Indica una separación razonable entre los clusters y buena dispersión interna.

Índice de Davies-Bouldin: 1.89 → Valor moderado, indica que algunos clusters podrían solaparse o tener formas no esféricas.

## Lecciones aprendidas

- Analisis y preprocesamiento de datos
- Utilizacion de SOM 
- Utilizacion de Streamlit
- Metodologia de desarollo de proyecto de machine learning

## Impacto del proyecto

El modelo permitió segmentar a los países en grupos con características comunes: países ricos y contaminantes, países pobres con bajo desarrollo y emisiones, y países en desarrollo con trayectorias mixtas. Sería necesario refinar aún más la agrupación para tener resultados mas utilizables.

## Conclusiones

Las métricas de evaluación indican una agrupación razonable pero que podría mejorarse. Visualmente la agrupación con Kmeans y la red SOM parece también pertinenta. A primera vista, la agrupación parece separar a los países pobres, los países en desarrollo y los países ricos. Sería interesante afinar el modelo para realizar un análisis más preciso.
