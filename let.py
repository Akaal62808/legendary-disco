import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

body {
  margin: 0;
  overflow: hidden;
  font-family: Arial;
}

/* Background image after open */
.finalScreen {
  display: none;
  position: absolute;
  width: 100%;
  height: 100%;
  background-image: url('https://images.unsplash.com/photo-1513151233558-d860c5398176');
  background-size: cover;
  background-position: center;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

/* Happy Birthday text */
.birthdayText {
  font-size: 50px;
  color: white;
  font-weight: bold;
  text-shadow: 2px 2px 10px black;
  animation: fadeIn 2s ease forwards;
}

/* Plane */
.plane {
  position: absolute;
  top: 25%;
  left: -400px;
  font-size: 100px;  /* BIG PLANE */
  animation: fly 4s ease forwards;
}

/* Rope */
.rope {
  width: 4px;
  height: 120px;
  background: black;
  margin: auto;
}

/* Gift */
.gift {
  font-size: 80px; /* BIG GIFT */
  cursor: pointer;
  animation: bounce 2s infinite;
}

/* Fly */
@keyframes fly {
  0% { left: -400px; }
  100% { left: 40%; }
}

/* Bounce */
@keyframes bounce {
  0%,100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}

/* Fade in */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

</style>
</head>

<body>

<div class="plane" id="plane">
  ✈️
  <div class="rope"></div>
  <div class="gift" onclick="openGift()">🎁</div>
</div>

<div class="finalScreen" id="final">
  <div class="birthdayText">🎉 Happy Birthday Komal 🎂💖</div>
  <div style="font-size:25px; color:white;">From Gurshan 💙</div>
</div>

<script>
function openGift() {
  document.getElementById("plane").style.display = "none";
  document.getElementById("final").style.display = "flex";
}
</script>

</body>
</html>
""", height=650)
