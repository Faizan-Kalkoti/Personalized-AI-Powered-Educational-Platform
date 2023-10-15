// var teach_dashboard1 = document.getElementById('teacher-dashboard-main-content')

// var dashboard_course = `<!-- Start pasting from here! -->
// <div class="courses-made-teacher" style="background-color: rgb(224, 255, 245); padding: 1em;">
//         <h3 style="text-align: center;">Courses made by you</h3>
// <!-- start of the course list -->        
// <div style="padding:2em; margin:0px;" class="row">
//     {% for course in courses %}
    
//     <div class="col" style="margin-bottom: 1em; overflow-x: wrap;">
//     <div class="card course-card" >
//     <a href="{% url 'courses:singlecourse' slug=course.slug %}" alt="single-course"
//      style="text-decoration:none; color: black; ">
//         <img src="{{course.course_img.url}}" style="width: 18rem; height:10em;" class="card-img-top course-img" alt="coures image">
//         <div class="card-body" style="margin-top: 0px; padding: 10px;">
//           <p class="card-text" style="">
//             <h5>{{course.course_name}}</h5>
//             by {{course.made_by_teacher.name}}
//         <br> at {{course.date_generated|date:"l, F j, Y"}}</p>
//       </div>
//     </a>
//     </div>
//     </div> <!--end of a card column-->
//     {% endfor %}
// </div> <!-- end of the row -->
    
// </div> <!-- end of the teacher dashboard column --> `; /* end */

// function showcourses()
// {
 
//     teach_dashboard1.innerHTML = dashboard_course;
//     console.log("function executed! ");
// }

// var button12 = document.getElementById('showcourse');
// button12.addEventListener('click', showcourses); 





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