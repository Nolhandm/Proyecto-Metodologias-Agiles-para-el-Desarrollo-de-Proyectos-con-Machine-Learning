# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

Se aplicaron dos técnicas principales de agrupamiento:

KMeans: algoritmo clásico de clustering basado en la minimización de la varianza intra-cluster. Se utilizó una versión escalada de los datos mediante MinMaxScaler y se evaluó con distintos valores de k.

Self-Organizing Maps (SOM): una red neuronal no supervisada que proyecta datos de alta dimensión en un espacio bidimensional conservando la topología. Posteriormente, se aplicó KMeans sobre las activaciones del SOM para obtener agrupamientos definidos.

Ambas metodologías se apoyaron en la reducción de dimensiones mediante PCA para visualización, y los resultados se interpretaron tanto cuantitativa como visualmente (U-Matrix, clusters, etiquetas de países).

## Variables de entrada

Las variables de entrada corresponden a los indicadores conservados en el preprocesamiento :
- Access to clean fuels and technologies for cooking (% of population)
- Adjusted savings: natural resources depletion (% of GNI)
- Adjusted savings: net forest depletion (% of GNI)
- Agricultural land (% of land area)
- Agriculture, forestry, and fishing, value added (% of GDP)
- Annual freshwater withdrawals, total (% of internal resources)
- CO2 emissions (metric tons per capita)
- Energy intensity level of primary energy (MJ/$2017 PPP GDP)
- Food production index (2014-2016 = 100)
- Forest area (% of land area)', 'GDP growth (annual %)
- Government expenditure on education, total (% of government expenditure)
- Heat Index 35
- Labor force participation rate, total (% of total population ages 15-64) (modeled ILO estimate)
- Land Surface Temperature
- Level of water stress: freshwater withdrawal as a proportion of available freshwater resources
- Methane emissions (metric tons of CO2 equivalent per capita)
- Mortality rate, under-5 (per 1,000 live births)', 'Net migration
- Nitrous oxide emissions (metric tons of CO2 equivalent per capita)
- Political Stability and Absence of Violence/Terrorism: Estimate
- Population ages 65 and above (% of total population)
- Population density (people per sq. km of land area)
- Prevalence of undernourishment (% of population)
- Proportion of seats held by women in national parliaments (%)
- Ratio of female to male labor force participation rate (%) (modeled ILO estimate)
- Renewable energy consumption (% of total final energy consumption)
- Rule of Law: Estimate
- School enrollment, primary (% gross)
- Scientific and technical journal articles
- Standardised Precipitation-Evapotranspiration Index
- Terrestrial and marine protected areas (% of total territorial area)
- Tree Cover Loss (hectares)
- Unemployment, total (% of total labor force) (modeled ILO estimate)

## Variable objetivo

El modelo baseline es no supervisado, por lo tanto no se utiliza una variable objetivo explícita. El objetivo es identificar grupos (clusters) similares sin etiquetas predefinidas.

## Evaluación del modelo

### Métricas de evaluación

Se utilizaron métricas de validación interna para evaluar la cohesión y separación de los clusters obtenidos:

Índice de Silueta (Silhouette Score)
Evalúa la similitud de cada punto con su propio cluster frente a otros clusters (rango: -1 a 1).

Índice de Calinski-Harabasz
Relación entre la dispersión inter-cluster y intra-cluster.

Índice de Davies-Bouldin
Mide la compacidad y separación (menor es mejor).

### Resultados de evaluación

Índice de silueta : 0.26 -> Es bajo, lo que indica que muchos países están cerca de los límites de sus respectivos clusters.

Índice de Calinski-Harabasz: 30.41 → Indica una separación razonable entre los clusters y buena dispersión interna.

Índice de Davies-Bouldin: 1.89 → Valor moderado, indica que algunos clusters podrían solaparse o tener formas no esféricas.

## Conclusiones

Las métricas de evaluación indican una agrupacion razonable pero que podria mejorarse. Visualmente la agrupacion con Kmeans y la red SOM parece también pertinenta. A primera vista, la agrupación parece separar a los países pobres, los países en desarrollo y los países ricos. Sería interesante afinar el modelo para realizar un análisis más preciso.

## Referencias

[1] Ministère de la Transition Écologique et de la Cohésion des Territoires – SDES. (2024). Cifras clave del clima - Francia, Europa y el mundo - Edición 2024. Service des données et études statistiques (SDES).

[2] Nimerenco, I., Leoveanu Soare, B. E., & Zanescu (Panait), D. (2024). Assessment of the link between CO₂ emissions and socio-economic indicators. Proceedings of the 18th International Conference on Business Excellence, 2594–2608.

[3] Alotaibi, A. A., & Alajlan, N. (2021). Using quantile regression to analyze the relationship between socioeconomic indicators and carbon dioxide emissions in G20 countries. Sustainability, 13(13), 7011.

[4] Panayotou, T. (1997). Demystifying the Environmental Kuznets Curve: Turning a black box into a policy tool. Environment and Development Economics, 2(4), 465–484. Cambridge University Press.

[5] Stern, D. I. (2004). The rise and fall of the Environmental Kuznets Curve. World Development, 32(8), 1419–1439.

[6] Acheampong, A. O., & Boateng, E. B. (2019). Modelling carbon emission intensity: Application of artificial neural network. Journal of Cleaner Production, 225, 833–856.

[7] Mardani, A., Liao, H., Nilashi, M., Alrasheedi, M., & Cavallaro, F. (2020). A multi-stage method to predict carbon dioxide emissions using dimensionality reduction, clustering, and machine learning techniques. Journal of Cleaner Production, 275, 122942.

[8] ChatGPT, OpenAI
