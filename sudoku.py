from sudoku_solver import sudoku_solver
import sudoku_puzzles

sudoku_list = [
    sudoku_puzzles.sudoku_1, sudoku_puzzles.sudoku_2,
    sudoku_puzzles.sudoku_3, sudoku_puzzles.sudoku_4,
    sudoku_puzzles.sudoku_5
]
sudoku_puzzle = sudoku_solver()
for sudoku in sudoku_list:
    sudoku_puzzle.sudoku = sudoku()
    if sudoku_puzzle._solver():
        print(f'Sudoku solved!')
    else:
        print(f'Sudoku has no solution')
    for index, line in enumerate(sudoku_puzzle.sudoku):
        print(f'{sudoku()[index]} -> {line}')
    print(f'Recursoes: {sudoku_puzzle.recursion}')
    print(f'Execution time: {sudoku_puzzle.time_solution}s')
    print()
    print()
