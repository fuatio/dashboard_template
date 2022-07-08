
// Submitting change to json file in local file
//document.getElementById('form').addEventListener('submit', changeCityContent)
var selectedTab = 'London'

function changeCityContent() {
    // get city value that's open right now
    //current_city_name = document.getElementById('city-name').innerHTML
    let data = new FormData()
    data.append('content', document.getElementById('change_content').value)
    data.append('open_city_tab', selectedTab)
    fetch(home, {
        "method": "POST",
        "body": data
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.getElementById('city-content').innerHTML = data[0]['content'];
        })
}

// Changing Tab Values
var tabs = document.querySelectorAll('.cityName')
tabs.forEach(tab => {
    tab.addEventListener('click', getCityDetails);
})

function getCityDetails(e) {
    let data = new FormData()
    data.append('city', e.target.value)
    fetch(home, {
        "method": "POST",
        "body": data
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('city-name').innerHTML = data[0]['city'];
            document.getElementById('city-content').innerHTML = data[0]['content'];
        })
    selectedTab = e.target.value;
}
console.log(home)