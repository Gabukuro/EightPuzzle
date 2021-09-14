from EigthtPuzzleSolver import EightPuzzle
import Utils


p = EightPuzzle()
p.shuffle(20)
path, count = p.solve()
path.reverse()
for i in path:
  Utils.printMatrix(i.matrix)