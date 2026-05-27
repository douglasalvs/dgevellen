import streamlit as st

# CONFIG
st.set_page_config(page_title="Perfil", layout="wide")

# TOPO
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("""
    <div style="text-align:center; margin-bottom:40px;">
        <a href="https://www.netflix.com/br/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg"
                 width="300">
        </a>
    </div>
    """, unsafe_allow_html=True)

# LAYOUT PRINCIPAL
col_left, col_right = st.columns([3,1])

with col_left:

    st.markdown("""
    <h1>Douglas</h1>
    """, unsafe_allow_html=True)

    subcol1, subcol2 = st.columns([1,4])

    # FOTO PERFIL
    with subcol1:
        st.image(
            "WhatsApp Image 2026-05-27 at 11.52.06.png",
            width=220
        )

    # TEXTO
    with subcol2:

        st.markdown("""
        <div style="
            text-align:justify;
            font-size:20px;
            line-height:2;
        ">
        <b>Sobre Douglas:</b><br><br>

        Douglas é estudante do Ensino Médio no IFPB Campus Itabaiana,
        dedicado aos estudos e interessado em tecnologia.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.link_button(
        "Visitar Site da Netflix",
        "https://www.netflix.com/br/"
    )

# WHATSAPP
st.markdown("""
<div style="text-align:center; margin-top:40px;">

<a href="https://wa.me/5583998234415" target="_blank">

<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"
     width="90">

</a>

</div>
""", unsafe_allow_html=True)
