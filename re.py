<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Regalo Hot Wheels para DAVIDS</title>
  <style>
    body { margin: 0;
      font-family: 'Arial', sans-serif;
      background: radial-gradient(circle at center, #001, #000);
      color: #fff;
      text-align: center;
      overflow-x: hidden;}

    header {padding: 25px;}

    header h1 {
      font-size: 34px;
      color: #ff3b3b;
      text-shadow: 0 0 15px rgba(255,59,59,0.7);}
    

    header p {
      font-size: 18px;
      opacity: 0.9;}
    

    /* pista */
    .track {
      margin: 40px auto;
      width: 90%;
      max-width: 600px;
      height: 200px;
      background: linear-gradient(90deg, #333, #111);
      border-radius: 20px;
      box-shadow: 0 0 25px rgba(0,0,0,0.6);
      position: relative;
      overflow: hidden;}
    

    .lane {
      position: absolute;
      top: 90px;
      left: 0;
      right: 0;
      height: 20px;
      border-top: 3px dashed #fff;}
    

    .car {
      position: absolute;
      bottom: 40px;
      left: -120px;
      width: 100px;
      height: 50px;
      border-radius: 10px;
      background: linear-gradient(90deg,#3b82f6,#60a5fa);
      animation: drive 6s linear infinite;
      box-shadow: 0 8px 20px rgba(59,130,246,0.6);}
    

    .car::before, .car::after {
      content: '';
      position: absolute;
      bottom: -15px;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #000;
      border: 3px solid #666;}
    

    .car::before { left: 10px; }
    .car::after { right: 10px; }

    @keyframes drive {
      0% { left: -120px; }
      100% { left: 100%; }}

    
    /* flores azules */
    .flowers {
      font-size: 34px;
      margin: 20px 0;
      text-shadow: 0 0 12px rgba(59,130,246,0.7);}
    

    /* mensaje */
    .message {
      margin: 20px auto;
      max-width: 600px;
      padding: 20px;
      border-radius: 12px;
      background: rgba(59,130,246,0.15);
      border: 1px solid rgba(59,130,246,0.4);}
    

    .message p {
      font-size: 20px;
      line-height: 1.5;}
    

    /* corazones flotantes */
    .heart {
      position: fixed;
      bottom: -50px;
      color: #ff3b3b;
      font-size: 24px;
      animation: float 6s linear infinite;
      opacity: 0.7;}
    

    @keyframes float {
      0% { transform: translateY(0) scale(1); opacity: 0.7; }
      100% { transform: translateY(-120vh) scale(1.8); opacity: 0; }}
    
  </style>
</head>
<body>
  <header>
    <h1>🚗💙 Regalo Hot Wheels para DAVIDS 💙🚗</h1>
    <p>30 de septiembre — Día del Enamorado</p>
  </header>

  <div class="track">
    <div class="lane"></div>
    <div class="car"></div>
  </div>

  <div class="flowers">🌸💙🌸💙🌸💙🌸</div>

  <div class="message">
    <p>
      DAVIDS, en esta pista llamada vida, eres mi copiloto favorito.  
      En este Día del Enamorado, <strong>mi corazón acelera por ti</strong>.
    </p>
  </div>

  <div class="flowers">💙🌸💙🌸💙🌸💙</div>

  <script>
    // corazones flotantes
    function createHeart(){
      const heart = document.createElement("div");
      heart.className = "heart";
      heart.innerHTML = "❤";
      heart.style.left = Math.random()*100 + "vw";
      heart.style.fontSize = (20 + Math.random()*20) + "px";
      heart.style.animationDuration = (4 + Math.random()*4) + "s";
      document.body.appendChild(heart);
      setTimeout(()=>heart.remove(), 8000);}
    
    setInterval(createHeart, 800);
  </script>
</body>
</html>
