import streamlit as st
import base64
import random

isim = "Sıla"

st.set_page_config(page_title="Kadınlar Günü", page_icon="🌸")

# ---- sakura animasyonu ----
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#ffd1dc,#ffe4f0);
overflow:hidden;
}

.title{
text-align:center;
font-size:50px;
color:#c2185b;
font-weight:bold;
}

.subtitle{
text-align:center;
font-size:26px;
color:#880e4f;
}

.petal{
position: fixed;
top:-50px;
font-size:30px;
pointer-events:none;
animation: fall linear infinite;
}

@keyframes fall{
0%{transform:translateY(-50px) rotate(0deg);}
100%{transform:translateY(110vh) rotate(360deg);}
}

</style>

<div class="petal" style="left:5%; animation-duration:8s;">🌸</div>
<div class="petal" style="left:15%; animation-duration:10s;">🌸</div>
<div class="petal" style="left:25%; animation-duration:7s;">🌸</div>
<div class="petal" style="left:35%; animation-duration:11s;">🌸</div>
<div class="petal" style="left:45%; animation-duration:9s;">🌸</div>
<div class="petal" style="left:55%; animation-duration:8s;">🌸</div>
<div class="petal" style="left:65%; animation-duration:10s;">🌸</div>
<div class="petal" style="left:75%; animation-duration:7s;">🌸</div>
<div class="petal" style="left:85%; animation-duration:11s;">🌸</div>
<div class="petal" style="left:95%; animation-duration:9s;">🌸</div>

""", unsafe_allow_html=True)

# ---- başlık ----
st.markdown(f'<div class="title">🌸 {isim} için 🌸</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">8 Mart Dünya Kadınlar Günün Kutlu Olsun 💖</div>', unsafe_allow_html=True)

# ---- sakura resmi ----
st.image(
"resim.jpg",
use_container_width=True
)

# ---- müzik dosyasını base64'e çevir ----
with open("muzik.mp3", "rb") as f:
    audio_bytes = f.read()

b64 = base64.b64encode(audio_bytes).decode()

# ---- müzik butonu ----
if st.button("🎵 Buraya tıkla"):
    st.markdown(f"""
    <audio id="music" autoplay loop>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>

    <script>
    document.getElementById("music").play();
    </script>
    """, unsafe_allow_html=True)

# ---- mesaj ----
mesajlar = [
f"{isim}, sen gerçekten çok özelsin 🌸",
f"{isim}, gülüşün dünyayı güzelleştiriyor ✨",
f"İyi ki varsın {isim} 💖"
]


if st.button("💌 Sana bir mesajım var (tıkla)"):
    st.balloons()
    st.markdown(
        f"<h1 style='text-align:center; color:#e91e63;'>{random.choice(mesajlar)}</h1>",
        unsafe_allow_html=True
    )
    