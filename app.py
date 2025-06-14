import streamlit as st

st.set_page_config(page_title="SlideForge - Graph Cloner", layout="centered")
st.title("📤 SlideForge : Upload ton graphique")

uploaded_file = st.file_uploader("📎 Glisse une image ici", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Image envoyée", use_column_width=True)

    if st.button("▶️ Lancer la séquence Copilot"):
        st.info("📨 Message 1 envoyé : Décalque cette image pour en faire un graph parfaitement identique sur PowerPoint.")
        st.success("✅ Réponse Copilot reçue (simulation)")

        st.info("📨 Message 2 envoyé : Réponds aux questions et corrige le graph.")
        st.success("✅ Corrections appliquées")

        st.info("📨 Message 3 envoyé : Envoie le PowerPoint final")
        st.success("✅ PowerPoint final généré")

        with open("graph_final.pptx", "rb") as file:
            st.download_button("📥 Télécharger PowerPoint", file, file_name="graph_final.pptx")

else:
    st.warning("⬆️ Merci de déposer une image pour commencer.")
