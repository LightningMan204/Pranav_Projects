let displayValue = '';

function appendToDisplay(value) {
  displayValue += value;
  document.getElementById('display').value = displayValue;
}

function calculate() {
  try {
    displayValue = eval(displayValue);
    document.getElementById('display').value = displayValue;
  } catch (error) {
    document.getElementById('display').value = 'Error';
  }
}

function clearDisplay() {
  displayValue = '';
  document.getElementById('display').value = displayValue;
}
