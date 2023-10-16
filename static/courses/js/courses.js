
// To get the elements that will be collapsed - teacher options/ settings
const buttonElement = document.querySelector('.option-elements');
const buttonElement2 = document.querySelector('#option-elements2');
const buttonElement3 = document.querySelector('#option-elements3');
const buttonElement4 = document.querySelector('#option-elements4');

// Get the collapse element 1
const collapseElement = document.getElementById('collapseoption1');
// Toggle the collapse when the button is clicked
buttonElement.addEventListener('click', function () {
    const bsCollapse = new bootstrap.Collapse(collapseElement);
    bsCollapse.toggle();
});


// Get the collapse element 1
const collapseElement2 = document.getElementById('collapseoption2');
// Toggle the collapse when the button is clicked
buttonElement2.addEventListener('click', function () {
    const bsCollapse = new bootstrap.Collapse(collapseElement2);
    bsCollapse.toggle();
});


// Get the collapse element 1
const collapseElement3 = document.getElementById('collapseoption3');
// Toggle the collapse when the button is clicked
buttonElement3.addEventListener('click', function () {
    const bsCollapse = new bootstrap.Collapse(collapseElement3);
    bsCollapse.toggle();
});


// Get the collapse element 1
const collapseElement4 = document.getElementById('collapseoption4');
// Toggle the collapse when the button is clicked
buttonElement4.addEventListener('click', function () {
    const bsCollapse = new bootstrap.Collapse(collapseElement4);
    bsCollapse.toggle();
});





function showgraphs()
{
    document.getElementById('teacher-dashboard-main-content').innerHTML = ` <div style="text-align:center;"> Student Analytics </div> <div id="chart-container" style="border: 1px solid black; padding: 0.3em; width:fit-content;"></div>
     <br> <canvas width="100" height="25" id="completionChart" ></canvas> `;

    // D3.js for graphs

const data = [10, 20, 30, 40, 190];
const labels = ["A", "B", "C", "D", "E"]; // Labels for the bars

// Set up chart dimensions
const width = 400;
const height = 200;
const barWidth = width / data.length;

// Create an SVG element for the chart
const svg = d3.select("#chart-container")
.append("svg")
.attr("width", width)
.attr("height", height);

// Create and append rectangles for the bars
svg.selectAll("rect")
.data(data)
.enter()
.append("rect")
.attr("x", (d, i) => i * barWidth)
.attr("y", (d) => height - d)
.attr("width", barWidth - 1)
.attr("height", (d) => d)
.attr("fill", "steelblue");

// Add labels for each bar
svg.selectAll("text")
.data(labels)
.enter()
.append("text")
.text((d, i) => labels[i]) // Use the labels array for text
.attr("x", (d, i) => i * barWidth + barWidth / 2) // Center the text
.attr("y", (d) => height - d - 5) // Adjust vertical position
.attr("text-anchor", "middle") // Center align the text
.attr("fill", "white"); // Text color



// For chart.js
const completedCount = 75; // Number of students who completed the course
const notCompletedCount = 25; // Number of students who did not complete the course

// Get the canvas element
const ctx = document.getElementById("completionChart").getContext("2d");

// Create a data object for the chart
const data2 = {
  labels: ["Completed", "Not Completed"],
  datasets: [{
    label: "Number of Students that have completed the course",
    data: [completedCount, notCompletedCount],
    backgroundColor: ["green", "red"],
  }]
};

// Create a chart using Chart.js
const myChart = new Chart(ctx, {
  type: "bar",
  data: data2,
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
}); // End of chart.js graph

}

document.getElementById('showgraphs').addEventListener('click', showgraphs)



