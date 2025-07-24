# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** som
- **Plataforma de despliegue:** [Streamlit](https://streamlit.io/)
- **Requisitos técnicos:** Se utilizé Python 3.12.1, requisitos : git, streamlit, pandas, numpy, scikit-learn, matplotlib, joblib, minisom

## Código de despliegue

- **Archivo principal:** `app.py`
- **Rutas de acceso a los archivos:** `src/app.py`
- **Variables de entorno:** archivo `data` y `models` del proyecto

## Documentación del despliegue

- **Instrucciones de instalación:**
- Primero se necesita clonar el proyecto, en un terminal utilizar `git clone https://github.com/Nolhandm/Proyecto-Metodologias-Agiles-para-el-Desarrollo-de-Proyectos-con-Machine-Learning.git`
- Instalar las dependencias con `pip install streamlit pandas numpy scikit-learn matplotlib joblib minisom`
- **Instrucciones de uso:**
- Moverse en el archivo src `cd Proyecto-Metodologias-Agiles-para-el-Desarrollo-de-Proyectos-con-Machine-Learning/src`
- Utilizar la aplicación con `streamlit run app.py`
- Si streamlit no esta reconocido puedes utilizar `export PATH="$HOME/.local/bin:$PATH"`
- Cerrar la aplicación con CTRL + C en el terminal
