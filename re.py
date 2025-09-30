<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />

<title> Regalo para DAVIDS — 30 de septiembre </title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: #000;
      color: #fff;
      text-align: center;
      overflow-x: hidden;
    }

    header {
      padding: 30px 20px;
    }

    header h1 {
      font-size: 28px;
      color: #ff3b3b;
      text-shadow: 0 0 12px rgba(255,59,59,0.6);
    }

    header p {
      font-size: 18px;
      opacity: 0.9;
    }

    /* pista estilo Hot Wheels */
    .track {
      margin: 40px auto;
      width: 90%;
      max-width: 600px;
      height: 200px;
      background: linear-gradient(90deg, #222, #111);
      border-radius: 20px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 0 30px rgba(0,0,0,0.6);
    }

    .lane {
      position: absolute;
      top: 90px;
      left: 0;
      right: 0;
      height: 20px;
      border-top: 3px dashed #fff;
    }

    .car {
      position: absolute;
      bottom: 40px;
      left: -120px;
      width: 100px;
      height: 50px;
      background: linear-gradient(90deg,#ff3b3b,#ff8a8a);
      border-radius: 10px;
      animation: drive 4s linear infinite;
      box-shadow: 0 8px 20px rgba(255,59,59,0.6);
    }

    .car::before, .car::after {
      content: '';
      position: absolute;
      bottom: -15px;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #000;
      border: 3px solid #666;
    }

    .car::before { left: 10px; }
    .car::after { right: 10px; }

    @keyframes drive {
      0% { left: -120px; }
      100% { left: 100%; }
    }

    /* flores azules */
    .flowers {
      margin: 30px 0;
      font-size: 32px;
      color: #3b82f6;
      text-shadow: 0 0 10px rgba(59,130,246,0.6);
    }

    .message {
      margin: 20px auto;
      max-width: 600px;
      padding: 20px;
      border-radius: 12px;
      background: rgba(59,130,246,0.1);
      border: 1px solid rgba(59,130,246,0.4);
    }

    .message p {
      font-size: 18px;
      line-height: 1.5;
    }

    /* botones */
    .controls {
      margin: 30px 0;
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
    }

    button {
      padding: 12px 20px;
      border-radius: 10px;
      border: none;
      cursor: pointer;
      font-weight: bold;
      background: linear-gradient(90deg,#3b82f6,#60a5fa);
      color: #fff;
      box-shadow: 0 6px 16px rgba(59,130,246,0.5);
      transition: transform 0.2s;
    }

    button:hover {
      transform: scale(1.05);
    }

    button.red {
      background: linear-gradient(90deg,#ff3b3b,#ff7b7b);
      box-shadow: 0 6px 16px rgba(255,59,59,0.5);
    }
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
      DAVIDS, que la chispa de nuestra velocidad juntos nunca se apague.  
      En este Día del Enamorado, recuerda: <strong>me aceleras el corazón</strong>.
    </p>
  </div>

  <div class="flowers">💙🌸💙🌸💙🌸💙</div>

  <div class="controls">
    <button id="engineBtn" class="red">Encender motor</button>
    <button id="downloadBtn">Descargar este regalo</button>
  </div>

  <script>
    // --- botón de descarga ---
    document.getElementById('downloadBtn').addEventListener('click', function() {
      const html = '<!doctype html>\\n' + document.documentElement.outerHTML;
      const blob = new Blob([html], {type:'text/html'});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'Regalo_Davids.html';
      document.body.appendChild(a);
      a.click();
      a.remove();
      setTimeout(()=>URL.revokeObjectURL(url), 2000);
    });

    // --- sonido de motor con Web Audio ---
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    const ctx = AudioContext ? new AudioContext() : null;

    function playRev(){
      if(!ctx) return;
      const now = ctx.currentTime;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(80, now);
      osc.frequency.exponentialRampToValueAtTime(1200, now + 0.45);
      gain.gain.setValueAtTime(0.0001, now);
      gain.gain.exponentialRampToValueAtTime(0.28, now + 0.08);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.9);
      osc.connect(gain); gain.connect(ctx.destination);
      osc.start(now); osc.stop(now + 0.9);
    }

    document.getElementById('engineBtn').addEventListener('click', function(){
      if(!ctx){
        alert('Tu navegador no soporta sonido Web Audio.');
        return;
      }
      if(ctx.state === 'suspended') ctx.resume();
      playRev();
    });
  </script>
</body>
</html>
