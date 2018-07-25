function openCity(cityName, elmnt) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "black";
    }

    // Show the specific tab content
    document.getElementById(cityName).style.display = "block";

    // Add the specific color to the button used to open the tab content
    elmnt.style.backgroundColor = '#777';
}

// function populateTabs(arr) {
//     for (i=0; i<arr.length;i++) {
//         console.log(arr[i])
//         document.getElementsByClassName('buttons').innerHTML = "<div><button class=\"tablink\" onclick=\"openCity('Person{{ i }}', this)\"><img src='../static/imj/{{ arr[i]['name'] }}_icon.jpg' ></button></div>";
//     }
// }


