// function openCity(cityName) {
//     var i;
//     var x = document.getElementsByClassName("city");
//     for (i = 0; i < x.length; i++) {
//         x[i].style.display = "none";
//     }
//     document.getElementById(cityName).style.display = "block";
// }

// function create() {
//     // Create Button
//     var button = document.createElement("button");
//     button.setAttribute('onclick', "openCity('Rome')");
//     button.innerHTML = "Rome"
//     document.getElementById("tabs").appendChild(button)

//     // Create Tab Content
//     var div = document.createElement('div');
//     div.id = 'Rome';
//     div.className = "city"
//     div.style="display:none";
//     var h2 = document.createElement('h2');
//     h2.textContent = 'Rome';
//     div.appendChild(h2)
//     document.getElementById("tab_content").appendChild(div);
// }