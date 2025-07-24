const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
resize();
window.addEventListener('resize', resize);

const GRAVITY = 0.5;

const player = {
  x: 50,
  y: 0,
  vx: 0,
  vy: 0,
  width: 20,
  height: 30,
  speed: 2.5,
  jump: 10,
  grounded: false
};

const level = {
  platforms: [
    {x:0, y:canvas.height-40, w:canvas.width, h:40},
    {x:150, y:canvas.height-120, w:120, h:20},
    {x:350, y:canvas.height-200, w:120, h:20},
    {x:550, y:canvas.height-280, w:120, h:20}
  ],
  portal:{x:700, y:canvas.height-320, w:40, h:60}
};

let keys = {};
document.addEventListener('keydown', e => keys[e.key]=true);
document.addEventListener('keyup', e => keys[e.key]=false);

document.getElementById('startBtn').addEventListener('click', () => {
  document.getElementById('overlay').style.display='none';
  loop();
});

function update(){
  if(keys['ArrowLeft']) player.vx = -player.speed;
  if(keys['ArrowRight']) player.vx = player.speed;
  if(!keys['ArrowLeft'] && !keys['ArrowRight']) player.vx = 0;
  if(keys[' '] && player.grounded){
    player.vy = -player.jump;
    player.grounded=false;
  }

  player.vy += GRAVITY;
  player.x += player.vx;
  player.y += player.vy;

  // collisions
  player.grounded = false;
  level.platforms.forEach(p=>{
    if(player.x < p.x+p.w && player.x+player.width>p.x &&
       player.y < p.y+p.h && player.y+player.height>p.y){
      if(player.vy>0 && player.y+player.height - player.vy <= p.y){
        player.y = p.y-player.height;
        player.vy = 0;
        player.grounded = true;
      }
    }
  });
}

function draw(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  ctx.fillStyle='#87CEEB';
  ctx.fillRect(0,0,canvas.width,canvas.height);

  ctx.fillStyle='#654321';
  level.platforms.forEach(p=> ctx.fillRect(p.x,p.y,p.w,p.h));

  // portal
  ctx.fillStyle='#FFD700';
  ctx.fillRect(level.portal.x,level.portal.y,level.portal.w,level.portal.h);

  // player
  ctx.fillStyle='#FF69B4';
  ctx.fillRect(player.x,player.y,player.width,player.height);
}

function loop(){
  update();
  draw();

  // check win
  if(player.x < level.portal.x + level.portal.w &&
     player.x + player.width > level.portal.x &&
     player.y < level.portal.y + level.portal.h &&
     player.y + player.height > level.portal.y){
       alert('You stabilized this timeline!');
       window.location.reload();
       return;
  }

  requestAnimationFrame(loop);
}
