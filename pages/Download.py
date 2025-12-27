import streamlit as st
import base64

st.set_page_config(
    layout="wide",
    page_title="Editor Markdown A4",
    initial_sidebar_state="collapsed"
)

# Render markdown con imágenes locales
# ---------- FUNCIÓN RENDER ----------
def render_a4(text):
    rendered = text
    for name, data in st.session_state.images.items():
        b64 = base64.b64encode(data).decode()
        mime = "image/png" if name.lower().endswith("png") else "image/jpeg"
        rendered = rendered.replace(
            f"]({name})",
            f"](data:{mime};base64,{b64})"
        )
    return f'<div class="a4-page">{rendered}</div>'

st.markdown(render_a4(st.session_state.texto), unsafe_allow_html=True)
