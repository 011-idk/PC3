# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1 (no es necesario instarlo)

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
#with st.sidebar:
     #selected = option_menu("Selecciona una sección: ",['Inicio', 'Experiencia', 'Gráficos'] , 
        #icons=['0-circle','1-circle', '2-circle'], menu_icon="tv", default_index=0)
    # Crea un menú de selected dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de selected disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
selected = option_menu(
    menu_title= None, 
    options=['Inicio', 'Experiencia', 'Gráficos'], 
    icons=['gitlab', 'journal', 'egg-fried'], 
    menu_icon= None, default_index=0, orientation="horizontal")
    # Título que aparece antes de las selected del menú -> menu_title="Selecciona una sección: "
    # Lista de selected que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por  selected"
if selected == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>Pensando computacionalmente</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("Perfil.jpeg", caption='Perfil', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
    Hola! Soy Joselyn, soy de Lima, Perú y estudio la carrera de comunicación audiovisual en PUCP aka Cato. Escogí esta carrera ya que me apasiona el cine y en si la producción de material audiovisual, el cual es uno de los aspectos por los cuales me encanta esta carrera, aun con sus complicaciones. En un futuro que
    espero sea proximo, me gustaria trabajar como parte de la producción y/o dirección de material audiovisual, así como generar contenido en linea sobre analisis de peliculas, series, entre otros. Además de publicar proyectos independientes relacionados a la fotografía. En lo que respecta a un ambito fuera de lo académico,
    me encanta ver series y películas, así como escuchar música y, de vez en cuando, leer libros, especialmente de terror y/o distopicos. También me encantan tomar fotografias, y practicar deportes de contacto, como actualmente hago practicando taekwondo. Y eso es toda la info básica sobre mi, gracias!
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif selected == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>Videos sobre programación (¿Salio bien?)</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    Este curso ha sido mi primer acercamiento a la programación, en un principio pense que sería bastante complicado e inicialmente hubieron temas que no entendía del todo, pero logre adaptarme y me encanto la idea de poder hacer mi propio blog desde cero. Aprender a programar a sido una experiencia
    interesate y divertida, una vez lo entiendes se vuelve sensillo, uno de los aspectos que más me gustaron fueron las bibliotecas y los mapas interactivos. Esta experiencia me ha hecho plantearme el llevar un curso de especialización respecto a esto, me gustaría poder segui haciendolo en el futuro próximo, quizá
    como medio para hacer visible proyetos personales relacionados con la fotografía. Y finalmente, considero que este curso es relevante para la carrera que estudio actualmente, comunicación audiovisual, ya que permite expandirme a un rubro mucho más amplio de acción, que me brinda mayores posibilidades laborales y
    promoción de proyectos independientes en ambitos como la fotografía, e inclusive para la creación de noticias y/o analisis de datos, bastante importante en cualquier carrera laboral, a percepción personal.
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video PC 1")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.link_button(
        "Ver video",
        "https://drive.google.com/file/d/1vzIdZ-2aPHsql1zs43Q7Ewiy198UrhrF/view?usp=sharing"
        )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta las diferencias entre string y listas en python, con ejemplos propios de estas diferencias para permitir un mejor entendimiento"
    )

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video PC 2")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1DGiJoJ-7uwrEowEEmzB16gABFyoMM0vO/view?usp=sharing"
        )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta las diferencias entre un bucle for y bucle while, empezando desde un análisis de los conceptos hasta las diferencias entre los mismos con ejemplos claros para su mejor entendimiento"
    )

elif selected == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'>'Gráficos...y un mapa'</h2>", unsafe_allow_html=True)

    graficos = ['Harry_Potter', 'Real_Madrid', 'Tarjetas_Rojas', 'Barcelona', 'Top_5']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Harry_Potter':
        # Título de la sección
        st.subheader("📊 Harry Potter")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            En esta imagen se muestra una nube de palabras con, evidentemente, palabras extraidas de un escrito de Harry Potter
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "nube_palabras_harry_potter_1.png",
                width=800
            )

    elif grafico_seleccionado == 'Real_Madrid':
        # Título de la sección
        st.subheader("📊 SP1 - Real Madrid")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Este histograma busca mostrar a modo de comparación los goles anotados y recibidos por el Real Madrid en sus partidos como visitante y local en la temporada 2025 - 2026.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "goles_SP1.png",
                width=800
            )
    elif grafico_seleccionado == 'Tarjetas_Rojas':
        # Título de la sección
        st.subheader("📊 Promedio de tarjetas rojas")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            En el siguiente grafico de barras se busca mostrar el promedio de tarjetas rojas que los equipos recibieron como locales en promedio con los goles anotados.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "barras_verticales_promedio_tarjeta_rojas.png",
                width=800
            )
    elif grafico_seleccionado == 'Barcelona':
        # Título de la sección
        st.subheader("📊 Pastelito de Barcelona")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            El siguiente gráfico muesra los resultados de los partidos ganados, perdidos y empatados de Barcelona como visitante en el SP1 2025-2026.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "pastel_Barcelona (1).png",
                width=800
            )
    elif grafico_seleccionado == 'Top_5':
        # Título de la sección
        st.subheader("🗺️ Series y Películas - Top 5")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            El mapa en cuestión muestra la ubicación en donde se grabaron escenas de mis series y películas favoritas. Debido a la cercanía de entre algunos de estos puntos los iconos se superponen en el mapa, pero se tratan de lugares distintos.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapa_top5.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )
