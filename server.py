<!DOCTYPE html>
<html lang="pt-br">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>CORE AI PRO</title>

<style>

:root{
--bg:#020617;
--card:#1e293b;
--accent:#38bdf8;
--ok:#10b981;
--text:#f1f5f9;
}

*{
box-sizing:border-box;
transition:0.2s;
}

body{
margin:0;
background:var(--bg);
color:var(--text);
font-family:Arial;
display:flex;
min-height:100vh;
}

nav{
width:250px;
background:#0f172a;
padding:20px;
}

.logo{
color:var(--accent);
font-size:20px;
margin-bottom:20px;
}

.nav-item{
padding:10px;
cursor:pointer;
}

main{
flex:1;
display:flex;
flex-direction:column;
}

header{
padding:10px;
border-bottom:1px solid #334155;
}

.workspace{
flex:1;
display:grid;
grid-template-columns:2fr 1fr;
gap:10px;
padding:10px;
}

.card{
background:var(--card);
padding:10px;
border-radius:6px;
}

.command-grid{
display:grid;
grid-template-columns:1fr 1fr;
gap:5px;
}

button{
background:#0f172a;
color:white;
border:1px solid #334155;
padding:8px;
cursor:pointer;
}

button:hover{
border-color:var(--accent);
}

#console{
background:black;
height:200px;
overflow:auto;
padding:5px;
font-family:monospace;
}

.footer{
display:flex;
padding:5px;
background:#0f172a;
}

input{
flex:1;
background:black;
color:white;
border:1px solid #334155;
padding:5px;
}

.exec{
background:var(--accent);
color:black;
}

</style>

</head>

<body>

<nav>

<div class="logo">CORE AI</div>

<div class="nav-item">Dashboard</div>
<div class="nav-item">Explorar</div>
<div class="nav-item">Editar</div>
<div class="nav-item">Config</div>

</nav>

<main>

<header>

STATUS:
<span style="color:#10b981">ONLINE</span>

</header>

<div class="workspace">

<div class="card">

<h3>Comandos</h3>

<div class="command-grid">

<button onclick="runCmd('SCAN')">SCAN</button>
<button onclick="runCmd('EDIT')">EDIT</button>
<button onclick="runCmd('DATA')">DATA</button>
<button onclick="runCmd('TEST')">TEST</button>

</div>

<div id="console"></div>

</div>

<div class="card">

<h3>Memória</h3>

<div id="memory"></div>

</div>

</div>

<div class="footer">

<input id="input">

<button class="exec" onclick="manualExec()">
EXEC
</button>

</div>

</main>

<script>

const API_URL =
"https://core-ai-api.onrender.com/cmd"


function log(t){

let c=document.getElementById("console")

let d=document.createElement("div")

d.innerText=t

c.appendChild(d)

c.scrollTop=c.scrollHeight

}


function memory(t){

let m=document.getElementById("memory")

let d=document.createElement("div")

d.innerText=t

m.prepend(d)

}


async function runCmd(cmd){

log("Executando "+cmd)

let r = await fetch(API_URL,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
cmd:cmd
})
})

let j = await r.json()

log(j.msg)

memory(cmd)

}


async function manualExec(){

let v=document.getElementById("input").value

if(!v) return

log("CMD "+v)

let r = await fetch(API_URL,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
cmd:v
})
})

let j = await r.json()

log(j.msg)

memory(v)

}

</script>

</body>
</html>
