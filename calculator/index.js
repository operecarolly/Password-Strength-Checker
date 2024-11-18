// Append to display
function appendToDisplay(value) {
    const display = document.getElementById('display');
    display.value += value;
}

// Clear display
function clearDisplay() {
    document.getElementById('display').value = '';
}

// Perform calculation
function calculate() {
    const display = document.getElementById('display');
    try {
        display.value = eval(display.value);
    } catch (e) {
        display.value = 'Error';
    }
}



// Fraction to decimal (reciprocal)
function fractionToDecimal() {
    const display = document.getElementById('display');
    try {
        display.value = 1 / eval(display.value);
    } catch (e) {
        display.value = 'Error';
    }
}

// Placeholder for additional fraction-related functionality
function convertFraction() {
    alert('Fraction conversion not implemented yet.');
}
// Function to calculate square root of the current display value
function calculateSquareRoot() {
    const display = document.getElementById('display');
    try {
        const value = parseFloat(display.value); // Get the current value from the display
        if (isNaN(value)) {
            display.value = 'Error'; // Handle invalid input
        } else {
            display.value = Math.sqrt(value); // Calculate the square root
        }
    } catch (e) {
        display.value = 'Error'; // Handle any unexpected errors
    }
}
// Function to append a value to the display (used for digits and operators)
function appendToDisplay(value) {
    const display = document.getElementById('display');
    display.value += value; // Add the clicked value (either number or operator) to the display
}

// Function to clear the display
function clearDisplay() {
    const display = document.getElementById('display');
    display.value = ''; // Clear the display
}

// Function to calculate the result when "=" is pressed
function calculate() {
    const display = document.getElementById('display');
    try {
        // Evaluate the expression in the display (will calculate square roots if any)
        display.value = eval(display.value); 
    } catch (e) {
        display.value = 'Error'; // Handle invalid expressions
    }
}

