const countDisplay = document.getElementById("count");
const incrementButton = document.getElementById("increment");
const decrementButton = document.getElementById("decrement");

let count = 0;

incrementButton.addEventListener("click", () => {
  count++;
  updateCount();
});

decrementButton.addEventListener("click", () => {
  if (count === 0) {return}
  count--;
  updateCount();
});

function updateCount() {
  countDisplay.textContent = count;
}
