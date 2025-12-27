import streamlit as st
import base64

st.set_page_config(layout="wide", page_title="Editor Markdown A4", initial_sidebar_state="collapsed")

if "images" not in st.session_state:
    st.session_state.images = {}

if "texto" not in st.session_state:
    st.session_state.texto = ""

# ---------- ESTILOS ----------
st.markdown("""
<style>

.a4-page {
    width: 21cm;
    min-height: 29.7cm;
    padding: 2.5cm 2cm;
    margin: auto;
    background: white;
    box-shadow: 0 0 12px rgba(0,0,0,0.2);
    font-family: "Times New Roman", serif;
}
.a4-page img {max-width: 100%;}
.a4-page p {text-align: justify; line-height: 1.5;}
</style>
""", unsafe_allow_html=True)

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

# ---------- TAB EDITOR ----------
col1, col2, col3 = st.columns([1,2,3])

with col1:
    st.subheader("📂 Imágenes")
    uploads = st.file_uploader("Subir", type=["png","jpg","jpeg"], accept_multiple_files=True)
    for img in uploads or []:
        st.session_state.images[img.name] = img.read()
    if st.session_state.images:
        for name in st.session_state.images:
            st.code(f"![]({name})")

with col2:
    st.subheader("✍️ Markdown")
    text = st.text_area("Texto", height=450, value=st.session_state.texto)
    if st.button(label="Update"):
        st.session_state.texto = text

with col3:
    st.subheader("📄 Vista previa")
    st.markdown(render_a4(st.session_state.texto), unsafe_allow_html=True)