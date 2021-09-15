import random
import Utils

goalState = [ [1,2,3],
              [4,5,6],
              [7,8,0] ]

class EightPuzzle:

  def __init__(self):
    self.heuristcValue = 0
    self.depth = 0
    self.parent = None
    self.matrix = []

    for i in range(3):
        self.matrix.append(goalState[i][:])

  def shuffle(self, stepCount):
    for i in range(stepCount):
      row, col = self.find(0)
      free = self.getLegalMoves()
      target = random.choice(free)
      self.swap((row, col), target)
      row, col = target

  def getLegalMoves(self):
    row, col = self.find(0)
    free = []

    if row > 0:
      free.append((row - 1, col))
    if col > 0:
      free.append((row, col -1))
    if row < 2:
        free.append((row + 1, col))
    if col < 2:
        free.append((row, col + 1))

    return free

  def find(self, value):
    if value < 0 or value > 8:
      raise Exception('Value out of range')

    for row in range(3):
      for col in range(3):
        if self.matrix[row][col] == value:
          return row, col
  
  def swap(self, positionA, positionB):
    temp = self.peek(*positionA)
    self.poke(positionA[0], positionA[1], self.peek(*positionB))
    self.poke(positionB[0], positionB[1], temp)
  
  def peek(self, row, col):
    return self.matrix[row][col];

  def poke(self, row, col, value):
    self.matrix[row][col] = value;

  def solve(self):

    nodeOpened = [self]
    nodeClosed = []
    moveCount = 0
    while len(nodeOpened) > 0:
      node = nodeOpened.pop(0)
      moveCount += 1
      if(self.isSolved(node)):
        if len(nodeClosed) > 0:
          return node.generateSolutionPath([]), moveCount
        else:
          return [node], moveCount

      moves = node.generateMoves()
      idxOpen = idxClosed = -1
      for move in moves:
        idxOpen = Utils.index(move, nodeOpened)
        idxClosed = Utils.index(move, nodeClosed)
        heuristcValue = Utils.manhattan(move)
        fval = heuristcValue + move.depth

        if idxClosed == -1 and idxOpen == -1:
          move.heuristcValue = heuristcValue
          nodeOpened.append(move)
        elif idxOpen > -1:
          copy = nodeOpened[idxOpen]
          if fval < copy.heuristcValue + copy.depth:
            copy.heuristcValue = heuristcValue
            copy.parent = move.parent
            copy.depth = move.depth
          elif idxClosed > -1:
            copy = nodeClosed[idxClosed]
            if fval < copy.heuristcValue + copy.depth:
              move.heuristcValue = heuristcValue
              nodeClosed.remove(copy)
              nodeOpened.append(move)

        nodeClosed.append(node)
        nodeOpened = sorted(nodeOpened, key=lambda p: p.heuristcValue + p.depth)

    return [], 0

  def isSolved(self, puzzle):
    return puzzle.matrix == goalState

  def generateSolutionPath(self, path):
    if self.parent == None:
      return path
    else:
      path.append(self)
      return self.parent.generateSolutionPath(path)
  
  def generateMoves(self):
    free = self.getLegalMoves()
    zero = self.find(0)

    def swapAndClone(a, b):
      p = self.clone()
      p.swap(a, b)
      p.depth = self.depth + 1
      p.parent = self
      return p

    return map(lambda pair: swapAndClone(zero, pair), free)
  
  def clone(self):
    p = EightPuzzle()
    for i in range(3):
      p.matrix[i] = self.matrix[i][:]
    return p

  