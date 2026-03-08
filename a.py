import streamlit as st
import base64
import random

isim = "Sıla"


st.set_page_config(page_title="Kadınlar Günü", page_icon="🌸")

# session state
if "music_on" not in st.session_state:
    st.session_state.music_on = False

# -------- CSS --------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#ffd1dc,#ffe4f0);
overflow:hidden;
}

.title{
text-align:center;
font-size:55px;
color:#c2185b;
font-weight:bold;
}

.subtitle{
text-align:center;
font-size:28px;
color:#880e4f;
}

.message{
font-size:45px;
text-align:center;
background:white;
padding:30px;
border-radius:20px;
box-shadow:0 5px 20px rgba(0,0,0,0.2);
color:#e91e63;
margin-top:30px;
}

.petal{
position: fixed;
top:-50px;
font-size:30px;
pointer-events:none;
animation: fall linear infinite;
}

@keyframes fall{
0%{
transform:translateY(-50px) rotate(0deg);
opacity:1;
}
100%{
transform:translateY(110vh) rotate(360deg);
opacity:0.6;
}
}

</style>

<div class="petal" style="left:2%; animation-duration:8s;">🌸</div>
<div class="petal" style="left:5%; animation-duration:9s;">🌸</div>
<div class="petal" style="left:8%; animation-duration:7s;">🌸</div>
<div class="petal" style="left:12%; animation-duration:10s;">🌸</div>
<div class="petal" style="left:16%; animation-duration:11s;">🌸</div>
<div class="petal" style="left:20%; animation-duration:8s;">🌸</div>
<div class="petal" style="left:25%; animation-duration:9s;">🌸</div>
<div class="petal" style="left:30%; animation-duration:7s;">🌸</div>
<div class="petal" style="left:35%; animation-duration:10s;">🌸</div>
<div class="petal" style="left:40%; animation-duration:11s;">🌸</div>
<div class="petal" style="left:45%; animation-duration:8s;">🌸</div>
<div class="petal" style="left:50%; animation-duration:9s;">🌸</div>
<div class="petal" style="left:55%; animation-duration:7s;">🌸</div>
<div class="petal" style="left:60%; animation-duration:10s;">🌸</div>
<div class="petal" style="left:65%; animation-duration:11s;">🌸</div>
<div class="petal" style="left:70%; animation-duration:8s;">🌸</div>
<div class="petal" style="left:75%; animation-duration:9s;">🌸</div>
<div class="petal" style="left:80%; animation-duration:7s;">🌸</div>
<div class="petal" style="left:85%; animation-duration:10s;">🌸</div>
<div class="petal" style="left:90%; animation-duration:11s;">🌸</div>
<div class="petal" style="left:95%; animation-duration:8s;">🌸</div>

""", unsafe_allow_html=True)

# -------- başlık --------
st.markdown(f'<div class="title">🌸 {isim} için 🌸</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">8 Mart Dünya Kadınlar Günün Kutlu Olsun 💖</div>', unsafe_allow_html=True)

# -------- resim --------
st.image("resim.jpg", use_container_width=True)

# -------- müzik başlat --------
if st.button("🎵 Sana özel bir şey var (müziği başlat)"):
    st.session_state.music_on = True

# -------- müzik çal --------
if st.session_state.music_on:

    with open("muzik.mp3", "rb") as f:
        audio_bytes = f.read()

    b64 = base64.b64encode(audio_bytes).decode()

    st.markdown(f"""
    <audio autoplay loop>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """, unsafe_allow_html=True)

# -------- mesaj --------
mesajlar = [
f"{isim}, iyi ki varsın 🌸",
f"{isim}, gülüşün dünyayı güzelleştiriyor ✨",
f"{isim}, harika bir arkadaşsın 💖",
f"{isim}, hayatı güzelleştiren insanlardan birisin 🌸"
]

if st.button("💌 Sana bir mesajım var (tıkla)"):
    st.balloons()
    st.markdown(
        f'<div class="message">{random.choice(mesajlar)}</div>',
        unsafe_allow_html=True
    )