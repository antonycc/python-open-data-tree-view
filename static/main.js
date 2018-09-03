// Purpose: Tree View API calls and rendering

function getBuildings() {
   fetch("/buildings/", {cache: "no-cache"})
         .then(function(response) {
            return response.json();
         })
         .then(function(jsonResponse) {
            var buildingsTable = toBuildingsTable(jsonResponse)
            var buildingsDisplay = document.getElementById("buildings");
            buildingsDisplay.innerHTML = "";
            buildingsDisplay.appendChild(buildingsTable);
         });
}


function getBuilding(buildingId) {
   fetch("/buildings/" + buildingId, {cache: "no-cache"})
         .then(function(response) {
            return response.json();
         })
         .then(function(jsonResponse) {
            var buildingTable = toBuildingTable(jsonResponse)
            var buildingDisplay = document.getElementById("building");
            buildingDisplay.innerHTML = "";
            buildingDisplay.appendChild(buildingTable);
         });
}


function toBuildingsTable(buildings){
   var buildingsTable = document.createElement("table");
   var tr = buildingsTable.insertRow(-1);
   var th = document.createElement("th");
   th.innerHTML = "Building Id";
   tr.appendChild(th);
   var th = document.createElement("th");
   th.innerHTML = "Building filename";
   tr.appendChild(th);
   for (var i = 0; i < buildings.length; i++) {
      tr = buildingsTable.insertRow(-1);
      var buildingId = buildings[i][0]
      var a = document.createElement("a")
      a.href = "#"
      a.innerHTML = buildingId
      a.onclick = function(){
         var buildingId = event.target.innerHTML
         console.log("Getting building for: " + buildingId)
         getBuilding(buildingId)
      }
      var tabCell = tr.insertCell(-1);
      tabCell.innerHTML = "";
      tabCell.appendChild(a)
      var tabCell = tr.insertCell(-1);
      tabCell.innerHTML = buildings[i][1];
   }
   return buildingsTable;
}


function toBuildingTable(windows){
   var buildingTable = document.createElement("table");
   var tr = buildingTable.insertRow(-1);
   var th = document.createElement("th");
   th.innerHTML = "floor_height";
   tr.appendChild(th);
   var th = document.createElement("th");
   th.innerHTML = "face_direction";
   tr.appendChild(th);
   var th = document.createElement("th");
   th.innerHTML = "window_vertical_position";
   tr.appendChild(th);
   var th = document.createElement("th");
   th.innerHTML = "window_height";
   tr.appendChild(th);
   var th = document.createElement("th");
   th.innerHTML = "window_width";
   tr.appendChild(th);
   for (var i = 0; i < Object.keys(windows["floor_height"]).length; i++) {
      tr = buildingTable.insertRow(-1);
      var tabCell = tr.insertCell(-1);
      tabCell.innerHTML = windows["floor_height"]["" + i];
      var tabCell = tr.insertCell(-1);
      tabCell.innerHTML = windows["face_direction"]["" + i];
      var tabCell = tr.insertCell(-1);
      tabCell.innerHTML = windows["window_vertical_position"]["" + i];
      var tabCell = tr.insertCell(-1);
      tabCell.innerHTML = windows["window_height"]["" + i];
      var tabCell = tr.insertCell(-1);
      tabCell.innerHTML = windows["window_width"]["" + i];
   }
   return buildingTable;
}

window.onload = getBuildings
