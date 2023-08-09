// Create a 9x9 grid of input cells
const sudokuGrid = document.getElementById("sudoku-grid");
for (let i = 0; i < 9; i++) {
  const row = document.createElement("tr");
  for (let j = 0; j < 9; j++) {
    const cell = document.createElement("td");
    cell.innerHTML = `<input type="number" min="1" max="9">`;
    row.appendChild(cell);
  }
  sudokuGrid.appendChild(row);
}

// Function to solve the Sudoku puzzle
// ... (Previous code)

// Function to solve the Sudoku puzzle
function solveSudoku() {
    const grid = [];
    const inputCells = document.querySelectorAll("#sudoku-grid input");
  
    // Convert the input values to a 2D array
    for (let i = 0; i < 9; i++) {
      grid.push([]);
      for (let j = 0; j < 9; j++) {
        const inputValue = parseInt(inputCells[i * 9 + j].value);
        grid[i].push(inputValue || 0);
      }
    }
  
    if (solve(grid)) {
      // Update the input cells with solved values
      for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
          inputCells[i * 9 + j].value = grid[i][j];
        }
      }
      console.log("Sudoku solved!");
    } else {
      console.log("No solution found.");
    }
  }
  
  function solve(grid) {
    const emptyCell = findEmptyCell(grid);
    if (!emptyCell) {
      return true; // All cells are filled, puzzle is solved
    }
  
    const [row, col] = emptyCell;
  
    for (let num = 1; num <= 9; num++) {
      if (isValidMove(grid, row, col, num)) {
        grid[row][col] = num;
  
        if (solve(grid)) {
          return true;
        }
  
        // If placing num in the current cell leads to a dead end, backtrack
        grid[row][col] = 0;
      }
    }
  
    return false; // No valid number found, trigger backtracking
  }
  
  function findEmptyCell(grid) {
    for (let row = 0; row < 9; row++) {
      for (let col = 0; col < 9; col++) {
        if (grid[row][col] === 0) {
          return [row, col];
        }
      }
    }
    return null; // All cells are filled
  }
  
  function isValidMove(grid, row, col, num) {
    for (let i = 0; i < 9; i++) {
      if (grid[row][i] === num || grid[i][col] === num) {
        return false; // Check row and column
      }
    }
  
    const startRow = Math.floor(row / 3) * 3;
    const startCol = Math.floor(col / 3) * 3;
  
    for (let i = startRow; i < startRow + 3; i++) {
      for (let j = startCol; j < startCol + 3; j++) {
        if (grid[i][j] === num) {
          return false; // Check 3x3 subgrid
        }
      }
    }
  
    return true; // Valid move
}
const solveButton = document.getElementById("solve-button");
solveButton.addEventListener("click", solveSudoku);
  


