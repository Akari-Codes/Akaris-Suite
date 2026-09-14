const nsfw = ["Scarletprincess [i love rias!]",
    "Rias Up. Highschool DxD",
"Rias Gremory. Hands on Teaching",
"MINECRAFT LETS FUCK EDITION. Monsters in the Night",
"euphoria ~highschooldxd~",
"Cumballs. The Amazing World of Gumball",
"Critical Senses. Fire Emblem. Three Houses. Kinkymation",
"Critical Luxuriass",
"B-Trayal 28",
"B-Trayal 22-2 Akeno",
"B-Trayal 22-3 Akeno",
"B-Trayal 19",
"B-Trayal 15 + Extras",
"B-Trayal 14",
"B-Trayal 13",
"B-Trayal 13-2",
"B-Trayal 13-3",
"Asuna! Close Call",
"A Critical Failure. Baldurs Gate 3. TSFSingularity"];
const sfw=[];
for (let i = 0; i < sfw.length; i++) {
  document.getElementById("sfw").innerHTML +=`<div class="sfw-item">
                    <br>
                    <img src="./mangas/` + sfw[i] + `/poster.cover" width="180" height="275">
                    <br>
                    <h3></h3>
                    <p>` + sfw[i] + `</p>
                    <button class="open-btn"  onclick="window.open('./mangas/` + sfw[i] + `/')">Read</button>
                </div>`;
};
for (let i = 0; i < nsfw.length; i++) {
  document.getElementById("nsfw").innerHTML +=`<div class="nsfw-item">
                    <br>
                    <img src="./mangas/` + nsfw[i] + `/poster.cover" width="180" height="275">
                    <br>
                    <h3></h3>
                    <p>` + nsfw[i] + `</p>
                    <button class="open-btn"  onclick="window.open('./mangas/` + nsfw[i] + `/')">Read</button>
                </div>`;
};
function toggleOn() {
    document.getElementById("container-3").style.display = "block";
    document.getElementById("toggle").setAttribute("onchange", "toggleOff()");
};
function toggleOff() {
    document.getElementById("container-3").style.display = "none";
    document.getElementById("toggle").setAttribute("onchange", "toggleOn()");
};