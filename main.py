from EigthtPuzzleSolver import EightPuzzle
import Utils


p = EightPuzzle()
p.shuffle(20)
path, count = p.solve()
path.reverse()
for i in path:
  Utils.printMatrix(i.matrix)

print('\n\n===================================')
print('    (☞ﾟヮﾟ)☞ Finally ☜(ﾟヮﾟ☜)    ')
text = '\n(づ￣ ³￣)づ {:2} states are explored'
print(text.format(count))
print('===================================')