import streamlit as st
import streamlit.components.v1 as components
import os
import base64

st.set_page_config(page_title="💖 For Marryl", layout="centered")

# -------------------------
# 🔐 LOVE PASSCODE GATE
# -------------------------
st.markdown("### 💌 Gate code")
name_input = st.text_input("Enter your name  💖", placeholder="hint: as his wife")

allowed = [
    "marryl bahati",
    "bahati marryl",
    "marryl.. bahati",
    "bahati.. marryl"
]

if name_input.strip().lower() not in allowed:
    st.info("✨ This gift opens only with the right names ✨")
    st.stop()

# -------------------------
# 🎵 BACKGROUND MUSIC
# -------------------------
def audio_base64(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

music_path = os.path.join("unity.mp3")
music_b64 = audio_base64(music_path) if os.path.exists(music_path) else None

# -------------------------
# 💖 MAIN CONTENT
# -------------------------
st.title("💖 To My Dearest Marryl 💖")
st.subheader("Always in my mind, always in my heart ❤️")

# -------------------------
# 🖼️ PREPARE PHOTOS
# -------------------------
image_folder = "photos"
image_files = [
    os.path.join(image_folder, f)
    for f in os.listdir(image_folder)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

image_data = [img_to_base64(img) for img in image_files]
js_images = str([f"data:image/jpeg;base64,{d}" for d in image_data])

# -------------------------
# 🌈 HTML + JS
# -------------------------
html_code = f""" 
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Dancing+Script:wght@500;700&family=Poppins:wght@300;400;500&display=swap');

html, body {{
    margin: 0;
    padding: 0;
    overflow: hidden;
    font-family: 'Poppins', sans-serif;
}}

h1, h2, h3 {{
    font-family: 'Playfair Display', serif;
}}

#slideshow {{
    position: fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    z-index:-2;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    transition: background-image 2s ease-in-out;
    background-color: #000;
}}

#loveCanvas {{
    position: fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    z-index:0;
}}

.fade-text {{
    position: fixed;
    bottom: 18%;
    width: 100%;
    text-align: center;
    font-family: 'Dancing Script', cursive;
    font-size: 2rem;
    color: white;
    font-weight: 600;
    opacity: 0;
    animation: fadeCycle 24s infinite;
    text-shadow: 0 3px 15px rgba(0,0,0,0.75);
    z-index:1;
}}

#musicOverlay {{
    position: fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    display:flex;
    align-items:center;
    justify-content:center;
    background: rgba(0,0,0,0.5);
    color:white;
    font-family:'Dancing Script', cursive;
    font-size:2rem;
    z-index:10;
    cursor:pointer;
    text-align:center;
}}

@keyframes fadeCycle {{
    0% {{opacity:0; transform:translateY(20px);}}
    10% {{opacity:1; transform:translateY(0);}}
    30% {{opacity:1;}}
    40% {{opacity:0;}}
}}
</style>

<div id="slideshow"></div>
<canvas id="loveCanvas"></canvas>
<div class="fade-text" id="loveText"></div>
<div id="musicOverlay">Tap his eye and listen 💖</div>

<audio id="bgMusic" loop>
    <source src="data:audio/mp3;base64,{music_b64}" type="audio/mp3">
</audio>

<script>
const images = {js_images};
let index = 0;
const slideshow = document.getElementById("slideshow");

function changeBackground(){{
    slideshow.style.backgroundImage = `url('${{images[index]}}')`;
    index = (index + 1) % images.length;
}}
changeBackground();
setInterval(changeBackground, 6000);

// ---------------- CANVAS ----------------
const canvas = document.getElementById("loveCanvas");
const ctx = canvas.getContext("2d");
function resize(){{ canvas.width = window.innerWidth; canvas.height = window.innerHeight; }}
resize();
window.addEventListener("resize", resize);

function random(min,max){{ return Math.random()*(max-min)+min; }}
const isMobile = window.innerWidth < 768;
const HEARTS = isMobile ? 20 : 40;

class Heart {{
    constructor(){{ this.reset(); this.y=random(0,canvas.height); }}
    reset(){{
        this.x=random(0,canvas.width);
        this.y=canvas.height+random(0,300);
        this.size=random(12,26);
        this.speed=random(0.3,1.2);
        this.color=`hsl(${{random(330,360)}},100%,70%)`;
    }}
    draw(){{
        ctx.fillStyle=this.color;
        ctx.beginPath();
        ctx.moveTo(this.x,this.y);
        ctx.bezierCurveTo(this.x,this.y-this.size,
            this.x-this.size,this.y-this.size,
            this.x-this.size,this.y);
        ctx.bezierCurveTo(this.x-this.size,this.y+this.size,
            this.x,this.y+this.size*1.4,
            this.x,this.y+this.size*1.8);
        ctx.bezierCurveTo(this.x,this.y+this.size*1.4,
            this.x+this.size,this.y+this.size,
            this.x+this.size,this.y);
        ctx.bezierCurveTo(this.x+this.size,this.y-this.size,
            this.x,this.y-this.size,
            this.x,this.y);
        ctx.fill();
        this.y-=this.speed;
        if(this.y<-60) this.reset();
    }}
}}

class Spark {{
    constructor(x,y){{
        this.x=x; this.y=y;
        this.vx=random(-3,3);
        this.vy=random(-3,3);
        this.alpha=1;
        this.size=random(2,5);
        this.color=`hsl(${{random(0,360)}},100%,60%)`;
    }}
    draw(){{
        ctx.globalAlpha=this.alpha;
        ctx.fillStyle=this.color;
        ctx.beginPath();
        ctx.arc(this.x,this.y,this.size,0,Math.PI*2);
        ctx.fill();
        ctx.globalAlpha=1;
        this.x+=this.vx;
        this.y+=this.vy;
        this.alpha-=0.04;
    }}
}}

const hearts=[...Array(HEARTS)].map(()=>new Heart());
let sparks=[];

function spawn(x,y){{
    for(let i=0;i<25;i++) sparks.push(new Spark(x,y));
}}
canvas.addEventListener("click",e=>spawn(e.clientX,e.clientY));
canvas.addEventListener("touchstart",e=>spawn(e.touches[0].clientX, e.touches[0].clientY));

function animate(){{
    ctx.clearRect(0,0,canvas.width,canvas.height);
    hearts.forEach(h=>h.draw());
    sparks=sparks.filter(s=>{{ s.draw(); return s.alpha>0; }});
    requestAnimationFrame(animate);
}}
animate();

// ---------------- TEXT ----------------
const messages=[
    "Marryl ❤️",
    "My every breath spells you name",
    "Even without words",
    "My mind thinks of you",
    "💖"
];
let i=0;
const txt=document.getElementById("loveText");
function changeText(){{
    txt.textContent=messages[i];
    i=(i+1)%messages.length;
}}
changeText();
setInterval(changeText,5000);

// ---------------- MUSIC ----------------
const music = document.getElementById("bgMusic");
const overlay = document.getElementById("musicOverlay");

function startMusic() {{
    if (!music || !music.paused) return;

    // remove overlay immediately
    overlay.style.display = "none";

    // start music with fade
    music.volume = 0;
    music.play().then(() => {{
        let v = 0;
        const fade = setInterval(() => {{
            v += 0.02;
            music.volume = Math.min(v, 0.4);  // fade to 40%
            if (v >= 0.4) clearInterval(fade);
        }}, 120);
    }}).catch(() => {{}});
}}

// Listen for first click or touch
document.addEventListener("click", startMusic, {{ once: true }});
document.addEventListener("touchstart", startMusic, {{ once: true }});
</script>
"""

components.html(html_code, height=720)

# -------------------------
# 💌 POETIC ENDING (UNCHANGED)
# -------------------------
st.markdown("""
<div style="
background: linear-gradient(135deg,#ff9a9e,#fad0c4);
padding:30px;
border-radius:20px;
text-align:center;
box-shadow:0 10px 30px rgba(0,0,0,0.2);
font-size:1.2rem;
color:#4a0026;
">
💌 <b>Marryl,  
even when words fail me,  
my heart never forgets you.  
In quiet moments,  
in unseen thoughts,  
you live there —  
always. ❤️</b>
</div>
""", unsafe_allow_html=True)
