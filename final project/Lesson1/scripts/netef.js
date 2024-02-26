// for (var i = 0; i < 10; i++) {
//   console.log(i);
// }
// var i = 0;
// while(i<10){
//     console.log(i);
//     i++;
// }
// const netef = [1, 2, 3, 4, 5, 6];
// netef.push(10);
// netef.shift();
// console.log(netef);

// const numbers = [1, 2, 3, 4, 5, 6];
// for (const number of numbers) {
//   console.log(number);
// }
// var netef = (x, y) => x + y;

// function add(x, y) {
//   return x + y;
// }

// console.log(netef(1, 2));

const counters = {};

function clicked(element) {
  // console.log("Clicked");
  // alert("You clicked an amazing button");
  // const element = document.getElementById(1);
  // element.style.color = "white";
  console.log(element);
  element.style.color = "red";
  element.style.background = "black";
  // document.getElementById().innerHTML
  if (element.id in counters) {
    counters[element.id]++;
  } else {
    counters[element.id] = 1;
  }

  element.innerHTML = counters[element.id];
}
