var light_data_elem = document.getElementById("light-data");
var temp_data_elem = document.getElementById("temperature-data");
var humidity_data_elem = document.getElementById("humidity-data");
var switch_state_elem = document.getElementById("switch-state");


function fetchData() {
  // Perform your data fetching logic here
  // For example, you can use the Fetch API or XMLHttpRequest

  fetch("/monitor/get-states")
    .then((response) => response.json())
    .then((data) => {
      // Process the fetched data
      light_data_elem.textContent = data.light;
      temp_data_elem.textContent = data.temperature;
      humidity_data_elem.textContent = data.humidity;
    })
    .catch((error) => {
      // Handle any errors that occurred during fetching
      console.error("Error:", error);
    });

  fetch("/switch")
    .then((response) => response.json())
    .then((data) => {
      // Process the fetched data
      switch_state_elem.textContent = data.state;
    })
    .catch((error) => {
      // Handle any errors that occurred during fetching
      console.error("Error:", error);
    });
}

function toggleSwitch() {
  fetch("/switch", {
    method: "POST",
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
  })
    .then((response) => response.json())
    .then((data) => {
      //   console.log("Response:", data);
      switch_state_elem.textContent = data.state;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

setInterval(fetchData, 5000);
