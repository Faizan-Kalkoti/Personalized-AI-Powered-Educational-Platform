
// To get the elements that will be collapsed - teacher options/ settings
const buttonElement = document.querySelector('.option-elements');
const buttonElement2 = document.querySelector('#option-elements2');
const buttonElement3 = document.querySelector('#option-elements3');
const buttonElement4 = document.querySelector('#option-elements4');

// Get the collapse element 1
const collapseElement = document.getElementById('collapseoption1');
// // Toggle the collapse when the button is clicked
// buttonElement.addEventListener('click', function () {
//     // const bsCollapse = new bootstrap.Collapse(collapseElement);
//     // bsCollapse.toggle();
//     if(collapseElement.classList.contains('show'))
//     {
//       collapseElement.classList.remove('show')
//     }
//     else{
//       collapseElement.classList.add('show')
//     }
// });

// function collapse1(){
//   const collapseElement = document.getElementById('collapseoption1');
//   const bsCollapse = new bootstrap.Collapse(collapseElement);
//     bsCollapse.toggle();
// }


// // Get the collapse element 1
// const collapseElement2 = document.getElementById('collapseoption2');
// // Toggle the collapse when the button is clicked
// buttonElement2.addEventListener('click', function () {
//     const bsCollapse = new bootstrap.Collapse(collapseElement2);
//     bsCollapse.toggle();
// });


// // Get the collapse element 1
// const collapseElement3 = document.getElementById('collapseoption3');
// // Toggle the collapse when the button is clicked
// buttonElement3.addEventListener('click', function () {
//     const bsCollapse = new bootstrap.Collapse(collapseElement3);
//     bsCollapse.toggle();
// });


// // Get the collapse element 1
// const collapseElement4 = document.getElementById('collapseoption4');
// // Toggle the collapse when the button is clicked
// buttonElement4.addEventListener('click', function () {
//     const bsCollapse = new bootstrap.Collapse(collapseElement4);
//     bsCollapse.toggle();
// });





function showgraphs()
{
    document.getElementById('teacher-dashboard-main-content').innerHTML = ` 
  <div style="background: linear-gradient(rgba(236, 240, 243, 0.4), rgba(209,215,227, 0.4));
  padding: 0.5em 1em;">
     <div style="padding: 1em;"></div>
     <h3 style="text-align:center;">
     Student Analytics </h3> 
     <div class="row" style="margin:0px; padding: 2em 1em; border-radius: 1em;">

     <div class="col-lg-3 col-graph" >
       <div style="width: 15em; height: 17.5em; border: 1px solid grey; padding: 0.5em; box-shadow: -1em 1em 2em rgb(200, 200, 200);
        background-color: white; border-radius: 1em;"> 
          <div style="border-bottom: 1px solid grey; padding-bottom:5px;"> Students Capabilities </div> 
          <canvas id="studentChart" width="100" height="100"></canvas> 
       </div>
     </div> 
     
     <div class="col-lg-6 mx-auto col-graph" >
     <div style="width: 25em; height: 17.5em; border: 1px solid grey; padding: 0.5em; box-shadow: -1em 1em 2em rgb(200, 200, 200);
     background-color: white; border-radius: 1em;"> 
     <div style="border-bottom: 1px solid grey; padding-bottom:5px;"> Course completed by students </div>
     <canvas width="25" height="15" id="completionChart" ></canvas> </div>
     </div>

    <div class="col-lg-3 col-graph" >
    <div style="width: 15em; height: 17.5em; border: 1px solid grey; padding: 0.5em; box-shadow: -1em 1em 2em rgb(200, 200, 200);
    background-color: white; border-radius: 1em;"> 
    <div style="border-bottom: 1px solid grey; padding-bottom:5px;"> Different student levels </div> 
     <canvas id="studentChart3" width="100" height="100"></canvas> </div>
     </div>
      </div>  <!-- End of the row -->

      <!-- new row begins -->
      <div class="row" style="margin: 0px; justify-content:space-evenly; padding:0em 2em; align-items:center;">
         
         <div class="col-lg-7 col-graph">
             <div style="width: 32em; height: 17.5em; border: 1px solid grey; padding: 0.5em; box-shadow: -1em 1em 2em rgb(200, 200, 200);
              background-color: white; border-radius: 1em;"> 
                     <div style="border-bottom: 1px solid grey; padding-bottom:5px;">
                       Number of students per Course </div>
                     <canvas width="30" height="14" id="Students-by-Courses" ></canvas>        
             </div>
         </div>

         <div class="col-lg-5 col-graph">
            <div style="width: 25em; height: 17.5em; border: 1px solid grey; padding: 0.5em; box-shadow: -1em 1em 2em rgb(200, 200, 200);
             background-color: white; border-radius: 1em;">
                <div style="border-bottom: 1px solid grey; padding-bottom:5px;">
                  Test Scores </div>
            </div>
         </div>

      </div>  <!-- end of new row -->


  </div> `;

// (1) - For [pie chart]-  chart.js
const data3 = {
  labels: ["Passed", "Failed"],
  datasets: [
    {
      data: [75, 25], // You can adjust these values based on your data
      backgroundColor: ["#36A2EB", "#FFCE56"], // Colors for each segment
    },
  ],
};
const ctx2 = document.getElementById("studentChart").getContext("2d");

const options1 = {
  title: {
    display: true,
    text: "Student Course Progress",
    fontSize: 16,
  },
  responsive: true,
};

const pieChart = new Chart(ctx2, {
  type: "pie",
  data: data3,
  options: options1,
});
//Ended here ....



// (2) - For chart.js
const completedCount = 45; // Number of students who completed the course
const notCompletedCount = 25; // Number of students who did not complete the course

// Get the canvas element
const ctx = document.getElementById("completionChart").getContext("2d");

// Create a data object for the chart
const data2 = {
  labels: ["Completed", "Not Completed"],
  datasets: [{
    label: "Student Completed Course",
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



// (3) - chart.js chart-3 "doughnut chart! "
const ctx4 = document.getElementById("studentChart3").getContext("2d");

const data4 = {
  labels: ["Level 1", "Level 2", "Level 3", "Level 4"],
  datasets: [
    {
      label: "Students by Level",
      data: [10, 20, 30, 40],
      backgroundColor: ["#FF0000", "#FF9900", "#FFFF00", "#00FF00"],
    },
  ],
};

const options3 = {
  title: {
    display: true,
    text: "Number of Students by Level",
  },
};

const chart = new Chart(ctx4, {
  type: "doughnut",
  data: data4,
  options: options3,
}); //End of the 3rd chart



// (4) - Histogram chart of chart.js
const data5 = {
  labels: ["Course 1", "Course 2", "Course 3", "Course 4"],
  datasets: [
    {
      label: "Student Distribution",
      data: [45, 60, 80, 95], // Example scores for each difficulty
      backgroundColor: ["#36A2EB", "#FFCE56", "#FF6384", "#4BC0C0"], // Colors for each bar
    },
  ],
};

const ctx5 = document.getElementById("Students-by-Courses").getContext("2d");

const histogramChart = new Chart(ctx5, {
  type: "bar",
  data: data5,
  options: {
    scales: {
      y: {
        beginAtZero: true,
        // max: 500, // Set the maximum value on the y-axis to 100%
        title: {
          display: true,
          text: "Number of students",
        },
      },
    },
  },
}); //End of the (4)th graph

}

document.getElementById('showgraphs').addEventListener('click', showgraphs)



