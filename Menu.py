import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Menú de Compatibilidad", page_icon="💖", layout="centered")

st.title("💖 Menú de Compatibilidad")
st.write("Descubre qué tan compatible eres respondiendo las preguntas paso a paso.")
st.divider()

# 1. Inicializamos las variables en el estado de Streamlit (Memoria)
if "paso" not in st.session_state:
    st.session_state.paso = 0  # 0: Pedir nombre, 1 al 5: Preguntas, 6: Resultados

if "nombre" not in st.session_state:
    st.session_state.nombre = ""

if "puntos_obtenidos" not in st.session_state:
    st.session_state.puntos_obtenidos = 0

puntos_maximos = 25  # 5 categorías * 5 puntos máximos

# ==========================================
# PASO 0: PEDIR NOMBRE Y BIENVENIDA
# ==========================================
if st.session_state.paso == 0:
    st.subheader("¡Bienvenido al Test!")
    nombre_input = st.text_input("Pon tu nombre:")
    
    if st.button("Comenzar Test ➡️", use_container_width=True):
        if nombre_input.strip() != "":
            st.session_state.nombre = nombre_input
            st.session_state.paso = 1  # Pasamos a la primera pregunta
            st.rerun()
        else:
            st.warning("⚠️ Por favor, ingresa tu nombre para continuar.")

# ==========================================
# PASO 1: COLOR FAVORITO
# ==========================================
elif st.session_state.paso == 1:
    st.subheader(f"Hola, {st.session_state.nombre}! 👋")
    st.write("### Categoría 1: COLOR FAVORITO")
    
    opcion1 = st.radio(
        "Selecciona tu opción:",
        ["1. Rojo", "2. Azul", "3. Rosado", "4. Verde"],
        key="radio_color"
    )
    
    if st.button("Siguiente Pregunta ➡️", use_container_width=True):
        if opcion1.startswith("1"):
            st.session_state.puntos_obtenidos += 5
        elif opcion1.startswith("2"):
            st.session_state.puntos_obtenidos += 4
        elif opcion1.startswith("3"):
            st.session_state.puntos_obtenidos += 2
        elif opcion1.startswith("4"):
            st.session_state.puntos_obtenidos += 3
            
        st.session_state.paso = 2
        st.rerun()

# ==========================================
# PASO 2: ANIMAL FAVORITO
# ==========================================
elif st.session_state.paso == 2:
    st.write("### Categoría 2: ANIMAL FAVORITO")
    
    opcion2 = st.radio(
        "Selecciona tu opción:",
        ["1. Gato", "2. Perro", "3. Conejo", "4. Tortuga", "5. Otro"],
        key="radio_animal"
    )
    
    if st.button("Siguiente Pregunta ➡️", use_container_width=True):
        if opcion2.startswith("1"):
            st.session_state.puntos_obtenidos += 5
        elif opcion2.startswith("2"):
            st.session_state.puntos_obtenidos += 4
        elif opcion2.startswith("3"):
            st.session_state.puntos_obtenidos += 3
        elif opcion2.startswith("4"):
            st.session_state.puntos_obtenidos += 2
        elif opcion2.startswith("5"):
            st.session_state.puntos_obtenidos += 3
            
        st.session_state.paso = 3
        st.rerun()

# ==========================================
# PASO 3: TIPO DE MÚSICA
# ==========================================
elif st.session_state.paso == 3:
    st.write("### Categoría 3: TIPO DE MÚSICA")
    
    opcion3 = st.radio(
        "Selecciona tu opción de música:",
        ["1. Pop", "2. Rap", "3. Reguetón", "4. Dembow", "5. Rock"],
        key="radio_musica"
    )
    
    if st.button("Siguiente Pregunta ➡️", use_container_width=True):
        if opcion3.startswith("1"):
            st.session_state.puntos_obtenidos += 3
        elif opcion3.startswith("2"):
            st.session_state.puntos_obtenidos += 4
        elif opcion3.startswith("3"):
            st.session_state.puntos_obtenidos += 2
        elif opcion3.startswith("4"):
            st.session_state.puntos_obtenidos += 1
        elif opcion3.startswith("5"):
            st.session_state.puntos_obtenidos += 5
            
        st.session_state.paso = 4
        st.rerun()

# ==========================================
# PASO 4: DEPORTE FAVORITO
# ==========================================
elif st.session_state.paso == 4:
    st.write("### Categoría 4: DEPORTE FAVORITO")
    
    opcion4 = st.radio(
        "Selecciona tu respuesta:",
        ["1. Fútbol", "2. Baloncesto", "3. Voleibol", "4. Patinaje", "5. Skate"],
        key="radio_deporte"
    )
    
    if st.button("Siguiente Pregunta ➡️", use_container_width=True):
        if opcion4.startswith("1"):
            st.session_state.puntos_obtenidos += 1
        elif opcion4.startswith("2"):
            st.session_state.puntos_obtenidos += 5
        elif opcion4.startswith("3"):
            st.session_state.puntos_obtenidos += 4
        elif opcion4.startswith("4"):
            st.session_state.puntos_obtenidos += 3
        elif opcion4.startswith("5"):
            st.session_state.puntos_obtenidos += 3
            
        st.session_state.paso = 5
        st.rerun()

# ==========================================
# PASO 5: GÉNERO DE PELÍCULA
# ==========================================
elif st.session_state.paso == 5:
    st.write("### Categoría 5: GÉNERO DE PELÍCULA FAVORITO")
    
    opcion5 = st.radio(
        "Selecciona tu opción:",
        ["1. Terror", "2. Acción", "3. Suspenso", "4. Animada", "5. Comedia"],
        key="radio_pelicula"
    )
    
    if st.button("Ver Resultados 📊", use_container_width=True):
        if opcion5.startswith("1"):
            st.session_state.puntos_obtenidos += 5
        elif opcion5.startswith("2"):
            st.session_state.puntos_obtenidos += 3
        elif opcion5.startswith("3"):
            st.session_state.puntos_obtenidos += 2
        elif opcion5.startswith("4"):
            st.session_state.puntos_obtenidos += 4
        elif opcion5.startswith("5"):
            st.session_state.puntos_obtenidos += 1
            
        st.session_state.paso = 6
        st.rerun()

# ==========================================
# PASO 6: RESULTADOS FINALES
# ==========================================
elif st.session_state.paso == 6:
    porcentaje_compatibilidad = (st.session_state.puntos_obtenidos / puntos_maximos) * 100

    st.success("🎉 ¡Has completado todas las preguntas!")
    st.markdown("---")
    
    st.subheader("📊 RESULTADOS")
    st.write(f"**Puntos totales obtenidos:** {st.session_state.puntos_obtenidos} de {puntos_maximos}")
    
    # Recuadro métrico vistoso con el porcentaje
    st.metric(label="Porcentaje de Compatibilidad", value=f"{porcentaje_compatibilidad:.1f}%")
    
    # Mensaje personalizado según tu lógica original
    if porcentaje_compatibilidad >= 80:
        st.balloons()
        st.success(f"¡{st.session_state.nombre}, son el uno para el otro! Tienen muchísima química. 💖")
    elif porcentaje_compatibilidad >= 50:
        st.info(f"¡{st.session_state.nombre}, tienen cosas en común! Se llevan bastante bien. 👍")
    else:
        st.error(f"¡{st.session_state.nombre}, no conectan en ni mierda! 💀")

    st.markdown("---")
    
    # Botón para reiniciar
    if st.button("🔄 Volver a intentar", use_container_width=True):
        st.session_state.paso = 0
        st.session_state.nombre = ""
        st.session_state.puntos_obtenidos = 0
        st.rerun()
