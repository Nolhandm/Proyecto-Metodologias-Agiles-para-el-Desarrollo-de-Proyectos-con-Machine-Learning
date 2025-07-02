# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Agrupación automática de los países del mundo en función de su dinámica socioeconómica y medioambiental

## Objetivo del Proyecto

El calentamiento global es ya un problema bien conocido y documentado que afecta a todos los países del mundo.

Sin embargo, podemos ver que este problema está lejos de resolverse. Para la década 2014-2023 se nota temperaturas medianas 1,19 grados más altas que en la era preindustrial (antes de los años 1900). Solo para el año 2023 este cifra sube hasta 1,41 frente a la era preindustrial. Ya podemos ver que el calentamiento global está teniendo una serie de impactos en las actividades humanas y la biodiversidad: aumento del nivel del agua, deshielo de los glaciares, más incendios forestales, sequías, olas de calor, huracanes y tormentas, desregulación climática, impactos en la agricultura y el acceso al agua, etc. Según los escenarios imaginados por los expertos, la temperatura media podría aumentar hasta 5 grados con respecto a la era preindustrial, lo que agravaría aún más los fenómenos ya observados y pondría en peligro la vida de millones de personas. Entonces es urgente actuar sobre este problema.

Este calentamiento se debe a la liberación masiva por las actividades humanas de gases de efecto invernadero que superan la capacidad natural de absorción del planeta : CO2, metano, óxido de nitrógeno y gases fluorados para el principal. Las emisiones mundial de gases de efecto invernadero, en CO2 equivalente, han aumentado de 62 % entre 1990 y 2022.

En lo que respecta a las emisiones de carbono, existen grandes disparidades entre países y regiones del mundo. Por ejemplo, las cantidades de gases de efecto invernadero, en CO2 equivalente, emitidas por América del Norte entre 1990 y 2021 se han mantenido bastante estables (+5,3%) en comparación con el aumento mundial. Por el contrario, las emisiones de América Central y del Sur aumentaron un 68,8% y las de Asia un 188% en el mismo periodo, mientras que las de Europa disminuyeron un 31%. Sólo en términos de emisiones actuales, China encabeza la lista con el 29,2% de las emisiones mundiales. Estados Unidos es responsable del 11,2%, mientras que la Unión Europea de 27 miembros y Sudamérica son responsables del 6,7% y el 5,3% de las emisiones mundiales, respectivamente. Por habitante, Arabia Saudí, Canadá y Estados Unidos ocupan los primeros puestos, con 22,3, 19,4 y 18 toneladas de CO2 emitidas por habitante, respectivamente. China se sitúa en 11,1 toneladas per cápita, la Unión Europea de los 27 en 8 y América Central y del Sur en 5,4.

Sería interesante explorar las diferencias y similitudes entre estos distintos países según diversos criterios (emisiones carbono, acceso a la electricidad, tasa de mortalidad, corrupción, nivel de vida, etc.) para explicar estas disparidades de emisiones. También sería muy interessante de poder agrupar automaticamente los paises con dinámicas socioeconómicas y medioambientales similares lo que permitiría aplicar políticas de transición diferenciadas segun estas dinamicas. El objetivo del proyecto será, por tanto, desarrollar una red neuronal capaz de agrupar automáticamente distintos países del mundo en función de diversos indicadores sociales, económicos y medioambientales.

## Alcance del Proyecto

### Incluye:

- El proyecto utilizará el conjunto de datos del Banco Mundial «Environment, Social and Governance Data» que almanece 71 indicadores sociales, económicos y medioambientales de 239 países y grupos de países del mundo entre 1960 y 2023. https://datacatalog.worldbank.org/search/dataset/0037651/environment,-social-and-governance-data
- El objetivo es utilizar la red neuronal para identificar grupos de países con la misma dinámica socioeconómica y medioambiental (países con alto desarrollo económico y social y altas emisiones, países con alto desarrollo pero bajas emisiones, países con bajo desarrollo y bajas emisiones, etc.).
- Se utilizarán varias métricas para medir la eficacia de la agrupación (Silhouette score, índice Davies-Bouldin, índice Calinski-Harabasz, etc.). El objetivo será comparar varias arquitecturas para maximizar estas métricas y la calidad de la agrupación.

### Excluye:

- El proyecto se limitará a una proposicion de red neuronal de agrupación de los paises, con el fin de proponer datos para orientar las políticas de desarrollo sostenible. No propondrá soluciones al problema del calentamiento global ni asesorará sobre las políticas de los distintos países presentes en el estudio.

## Metodología

La metodología que se utilizará en este proyecto será CRISP-DM. Las fases de comprensión y preparación de los datos permitirán seleccionar las variables que se utilizarán en el modelo de agrupación y tratar y completar los datos que faltan, que son numerosos en el conjunto de datos. La fase de modelamiento servirá para probar las distintas arquitecturas

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | del 26 de junio al 3 de julio |
| Entendimiento y preprocesamiento de los datos | 1 semana | del 3 de julio al 10 de julio |
| Modelamiento y evaluacion | 1 semana | del 10 de julio al 17 de julio |
| Despliegue | 1 semana | del 17 de julio al 24 de julio |
| Evaluación y entrega final | 1 semana | del 24 de julio al 31 de agosto|

## Equipo del Proyecto

- Nolhan Dumoulin (ndumoulin@unal.edu.co)

## Presupuesto

Sin costo (uso de datos públicos y software libre)

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
