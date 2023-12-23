
// length = 
// const elementsArray = Array.from(cardw);
// console.log(elementsArray)

// elementsArray.forEach(element => {
//     console.log("hello")
// });

//  // Function to be called when the element comes into view
//  function handleIntersection(entries, observer) {
//     entries.forEach(entry => {
//       if (entry.isIntersecting) {
//         // Add your animation or class logic here
//         entry.target.classList.add('centered');
//         // Unobserve the target element to stop further callbacks
//         observer.unobserve(entry.target);
//       }
//     });
//   }

//   // Options for the Intersection Observer
//   const options = {
//     root: null, // Use the viewport as the root
//     rootMargin: '0px', // No margin around the root
//     threshold: 0.5 // Trigger when 50% of the element is visible
//   };

//   // Create an Intersection Observer instance
//   const observer = new IntersectionObserver(handleIntersection, options);

//   // Target element to observe
//   const infoRows = document.querySelectorAll('.info-row');

//   // Start observing the target element
//   infoRows.forEach(row => {
//     observer.observe(row);
//   });

