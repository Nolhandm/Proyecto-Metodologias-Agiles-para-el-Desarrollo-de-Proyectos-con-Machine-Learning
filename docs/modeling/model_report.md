# Reporte del Modelo Final

## Resumen Ejecutivo

Este proyecto tuvo como objetivo desarrollar un modelo de agrupamiento no supervisado capaz de clasificar a los países del mundo según sus indicadores ESG (Ambientales, Sociales y de Gobernanza). Se exploraron distintos enfoques de clustering, destacando el uso de KMeans y Mapas Auto-Organizados (Self-Organizing Maps, SOM).

El modelo final seleccionado permitió identificar patrones y similitudes entre países con base en variables sociales y económicas. Se evaluaron diferentes configuraciones y se determinaron los valores óptimos de k mediante el método del codo y el coeficiente de silueta.

Las métricas de validación interna para SOM agrupado con KMeans fueron:

Índice de Calinski-Harabasz: 30.41

Índice de Davies-Bouldin: 1.89

Estos resultados indican que los clusters presentan una separación aceptable, aunque existe margen de mejora en la compactación interna.

## Descripción del Problema

El calentamiento global es ya un problema bien conocido y documentado que afecta a todos los países del mundo.

Sin embargo, podemos ver que este problema está lejos de resolverse. Para la década 2014-2023 se nota temperaturas medianas 1,19 grados más altas que en la era preindustrial (antes de los años 1900). Solo para el año 2023 este cifra sube hasta 1,41 frente a la era preindustrial. Ya podemos ver que el calentamiento global está teniendo una serie de impactos en las actividades humanas y la biodiversidad: aumento del nivel del agua, deshielo de los glaciares, más incendios forestales, sequías, olas de calor, huracanes y tormentas, desregulación climática, impactos en la agricultura y el acceso al agua, etc. Según los escenarios imaginados por los expertos, la temperatura media podría aumentar hasta 5 grados con respecto a la era preindustrial, lo que agravaría aún más los fenómenos ya observados y pondría en peligro la vida de millones de personas. Entonces es urgente actuar sobre este problema.

Este calentamiento se debe a la liberación masiva por las actividades humanas de gases de efecto invernadero que superan la capacidad natural de absorción del planeta : CO2, metano, óxido de nitrógeno y gases fluorados para el principal. Las emisiones mundial de gases de efecto invernadero, en CO2 equivalente, han aumentado de 62 % entre 1990 y 2022.

En lo que respecta a las emisiones de carbono, existen grandes disparidades entre países y regiones del mundo. Por ejemplo, las cantidades de gases de efecto invernadero, en CO2 equivalente, emitidas por América del Norte entre 1990 y 2021 se han mantenido bastante estables (+5,3%) en comparación con el aumento mundial. Por el contrario, las emisiones de América Central y del Sur aumentaron un 68,8% y las de Asia un 188% en el mismo periodo, mientras que las de Europa disminuyeron un 31%. Sólo en términos de emisiones actuales, China encabeza la lista con el 29,2% de las emisiones mundiales. Estados Unidos es responsable del 11,2%, mientras que la Unión Europea de 27 miembros y Sudamérica son responsables del 6,7% y el 5,3% de las emisiones mundiales, respectivamente. Por habitante, Arabia Saudí, Canadá y Estados Unidos ocupan los primeros puestos, con 22,3, 19,4 y 18 toneladas de CO2 emitidas por habitante, respectivamente. China se sitúa en 11,1 toneladas per cápita, la Unión Europea de los 27 en 8 y América Central y del Sur en 5,4.

Sería interesante explorar las diferencias y similitudes entre estos distintos países según diversos criterios (emisiones carbono, acceso a la electricidad, tasa de mortalidad, corrupción, nivel de vida, etc.) para explicar estas disparidades de emisiones. También sería muy interessante de poder agrupar automaticamente los paises con dinámicas socioeconómicas y medioambientales similares lo que permitiría aplicar políticas de transición diferenciadas segun estas dinamicas. El objetivo del proyecto será, por tanto, desarrollar una red neuronal capaz de agrupar automáticamente distintos países del mundo en función de diversos indicadores sociales, económicos y medioambientales.

El proyecto utilizará el conjunto de datos del Banco Mundial «Environment, Social and Governance Data» que almanece 71 indicadores sociales, económicos y medioambientales de 239 países y grupos de países del mundo entre 1960 y 2023. https://datacatalog.worldbank.org/search/dataset/0037651/environment,-social-and-governance-data
El objetivo es utilizar la red neuronal para identificar grupos de países con la misma dinámica socioeconómica y medioambiental (países con alto desarrollo económico y social y altas emisiones, países con alto desarrollo pero bajas emisiones, países con bajo desarrollo y bajas emisiones, etc.).
Se utilizarán varias métricas para medir la eficacia de la agrupación (Silhouette score, índice Davies-Bouldin, índice Calinski-Harabasz, etc.). El objetivo será comparar varias arquitecturas para maximizar estas métricas y la calidad de la agrupación.

## Descripción del Modelo

Se aplicaron dos técnicas principales de agrupamiento:

KMeans: algoritmo clásico de clustering basado en la minimización de la varianza intra-cluster. Se utilizó una versión escalada de los datos mediante MinMaxScaler y se evaluó con distintos valores de k.

Self-Organizing Maps (SOM): una red neuronal no supervisada que proyecta datos de alta dimensión en un espacio bidimensional conservando la topología. Posteriormente, se aplicó KMeans sobre las activaciones del SOM para obtener agrupamientos definidos.

Ambas metodologías se apoyaron en la reducción de dimensiones mediante PCA para visualización, y los resultados se interpretaron tanto cuantitativa como visualmente (U-Matrix, clusters, etiquetas de países).

## Evaluación del Modelo

Se utilizaron las siguientes métricas de evaluación interna para determinar la calidad de los agrupamientos:

Índice de Calinski-Harabasz: 30.41
→ Indica una separación razonable entre los clusters y buena dispersión interna.

Índice de Davies-Bouldin: 1.89
→ Valor moderado, indica que algunos clusters podrían solaparse o tener formas no esféricas.

Estas métricas fueron calculadas sobre los clusters extraídos a partir de las posiciones ganadoras del SOM. Además, se evaluaron visualmente los agrupamientos usando PCA y la matriz U-Matrix..

## Conclusiones y Recomendaciones

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
