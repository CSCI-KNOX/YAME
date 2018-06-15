function makeSelect() {
	var myDiv = document.getElementById('year');
	var d = new Date();
	var y = d.getFullYear() + 4;
	var array = [];
	//Create array of options to be added
	for (var i = y; i > 1875; i--) {
		array.push(i)
	}
	//Create and append select list
	var selectList = document.createElement("select");
	selectList.setAttribute("name", "year");
	myDiv.appendChild(selectList);

	//Create and append the options
	for (var i = 0; i < array.length; i++) {
	    var option = document.createElement("option");
	    option.setAttribute("value", array[i]);
	    option.text = array[i];
	    selectList.appendChild(option);
	}
}

window.onload = makeSelect;