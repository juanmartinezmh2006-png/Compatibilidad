import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Test de Compatibilidad", page_icon="💖", layout="centered")

# 2. Datos del Personaje X y las Opciones
respuestas_personaje_x = {
    "Pelicula": "Ciencia Ficción",
    "Comida": "Pizza",
    "Plan Ideal": "Quedarse en casa viendo series",
    "Mascota": "Perro"
}

categorias = {
    "Pelicula": ["Acción", "Comedia", "Ciencia Ficción", "Terror"],
    "Comida": ["Pizza", "Hamburguesa", "Ensalada", "Pasta"],
    "Plan Ideal": ["Salir de fiesta", "Quedarse en casa viendo series", "Ir a un museo", "Hacer camping"],
    "Mascota": ["Perro", "Gato", "Ninguna", "Otro"]
}

# Convertimos las claves (categorías) en una lista para saber el orden de las preguntas
lista_categorias = list(categorias.keys())
total_preguntas = len(lista_categorias)

# 3. Inicializamos las variables de estado (Memoria de la app)
if "indice_pregunta" not in st.session_state:
    st.session_state.indice_pregunta = 0  # Empezamos en la pregunta 0 (la primera)

if "respuestas_usuario" not in st.session_state:
    st.session_state.respuestas_usuario = {}  # Diccionario vacío para guardar respuestas

if "test_finalizado" not in st.session_state:
    st.session_state.test_finalizado = False  # Indica si ya terminó el test


# 4. Título Principal
st.title("💖 Test de Compatibilidad")
st.write("Descubre qué tan compatible eres con el Personaje X respondiendo una pregunta a la vez.")
st.divider()

# 5. Flujo del Test
if not st.session_state.test_finalizado:
    # Obtenemos la categoría actual según el índice
    pregunta_actual = lista_categorias[st.session_state.indice_pregunta]
    opciones_actuales = categorias[pregunta_actual]
    
    # Barra de progreso para que el usuario sepa cuánto le falta
    progreso = (st.session_state.indice_pregunta) / total_preguntas
    st.progress(progreso, text=f"Pregunta {st.session_state.indice_pregunta + 1} de {total_preguntas}")
    
    # Mostramos la pregunta y las opciones
    st.subheader(f"¿Cuál es tu opción favorita en **{pregunta_actual}**?")
    
    # Usamos st.radio para la selección de una sola opción
    opcion_seleccionada = st.radio(
        label="Selecciona una alternativa:",
        options=opciones_actuales,
        key=f"radio_{st.session_state.indice_pregunta}" # Key única por pregunta
    )
    
    # Botón para guardar respuesta y pasar a la siguiente
    if st.button("Siguiente Pregunta ➡️", use_container_width=True):
        # Guardamos la respuesta elegida
        st.session_state.respuestas_usuario[pregunta_actual] = opcion_seleccionada
        
        # Avanzamos a la siguiente pregunta
        st.session_state.indice_pregunta += 1
        
        # Verificamos si ya respondiendo la última
        if st.session_state.indice_pregunta >= total_preguntas:
            st.session_state.test_finalizado = True
            
        # Volvemos a cargar la app para mostrar el nuevo estado
        st.rerun()

# 6. Mostrar Resultados Finales
else:
    st.success("🎉 ¡Has completado todas las preguntas!")
    
    # Calculamos los aciertos
    aciertos = 0
    for cat, resp_ideal in respuestas_personaje_x.items():
        if st.session_state.respuestas_usuario[cat] == resp_ideal:
            aciertos += 1
            
    # Calculamos el porcentaje
    porcentaje = (aciertos / total_preguntas) * 100
    
    # Recuadro destacado con el porcentaje obtenido (st.metric o st.success/info)
    st.markdown("### 📊 Resultado Obtenido")
    
    # Usamos st.metric para un recuadro limpio y vistoso
    st.metric(label="Porcentaje de Compatibilidad", value=f"{porcentaje:.0f}%")
    
    # Mensaje según el resultado dentro de un recuadro de color (st.info, st.success, etc.)
    if porcentaje == 100:
        st.balloons() # Animación de globos
        st.success("✨ ¡Son 100% almas gemelas! Tienen exactamente los mismos gustos.")
    elif porcentaje >= 50:
        st.info("😊 ¡Tienen buena compatibilidad! Hay varios puntos en común.")
    else:
        st.warning("🤝 Tienen gustos muy diferentes, ¡pero los opuestos se atraen!")

    # Desglose de respuestas
    with st.expander("Ver detalle de respuestas"):
        for cat in lista_categorias:
            resp_u = st.session_state.respuestas_usuario[cat]
            resp_x = respuestas_personaje_x[cat]
            coincide = "✅ Coinciden" if resp_u == resp_x else "❌ Diferentes"
            st.write(f"**{cat}:** Tu elegiste *'{resp_u}'* | Personaje X prefiere *'{resp_x}'* → {coincide}")

    # Botón para reiniciar el test
    if st.button("🔄 Volver a intentar", use_container_width=True):
        st.session_state.indice_pregunta = 0
        st.session_state.respuestas_usuario = {}
        st.session_state.test_finalizado = False
        st.rerun()
