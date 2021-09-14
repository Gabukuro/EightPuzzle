
def index(item, seq):
  if item in seq:
    return seq.index(item)
  else:
    return -1

def manhattan(puzzle):
  return heur(puzzle,
              lambda r, tr, c, tc: abs(tr - r) + abs(tc - c),
              lambda t : t)

def heur(puzzle, itemTotalCalc, totalCalc):
  t = 0
  for row in range(3):
    for col in range(3):
      val = puzzle.peek(row, col) - 1
      targetCol = val % 3
      targetRow = val / 3

      if targetRow < 0:
        targetRow = 2

      t += itemTotalCalc(row, targetRow, col, targetCol)

  return totalCalc(t)

def printMatrix(matrix):
  text = "\n{}\n{}\n{}"
  print(text.format(matrix[0], matrix[1], matrix[2]))