let countdown = 5;
let timer = setInterval(() => {
  console.log(countdown);
  countdown--;
  if (countdown < 0) {
    clearInterval(timer);
    console.log("Time's up!");
  }
}, 1000);
