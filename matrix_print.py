import os

alphabit = {
  "A": [
  [0,1,1,0],
  [1,0,0,1],
  [1,1,1,1],
  [1,0,0,1],
  [1,0,0,1]
  ],
  "B": [
  [1,1,1,0],
  [1,0,0,1],
  [1,1,1,0],
  [1,0,0,1],
  [1,1,1,0]
  ],
  "C": [
  [0,1,1,1],
  [1,0,0,0],
  [1,0,0,0],
  [1,0,0,0],
  [0,1,1,1]
  ],
  "D": [
  [1,1,1,0],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [1,1,1,0]
  ],
  "E": [
  [1,1,1,1],
  [1,0,0,0],
  [1,1,1,1],
  [1,0,0,0],
  [1,1,1,1]
  ],
  "F": [
  [1,1,1,1],
  [1,0,0,0],
  [1,1,1,1],
  [1,0,0,0],
  [1,0,0,0]
  ],
  "G": [
  [0,1,1,0],
  [1,0,0,0],
  [1,0,1,0],
  [1,0,0,1],
  [0,1,1,0]
  ],
  "H": [
  [1,0,0,1],
  [1,0,0,1],
  [1,1,1,1],
  [1,0,0,1],
  [1,0,0,1]
  ],
  "I": [
  [1,1,1,1],
  [0,1,1,0],
  [0,1,1,0],
  [0,1,1,0],
  [1,1,1,1]
  ],
  "J": [
  [0,0,1,0],
  [0,0,1,0],
  [0,0,1,0],
  [1,0,1,0],
  [0,1,0,0]
  ],
  "K": [
  [1,0,0,1],
  [1,0,1,0],
  [1,1,0,0],
  [1,0,1,0],
  [1,0,0,1]
  ],
  "L": [
  [1,0,0,0],
  [1,0,0,0],
  [1,0,0,0],
  [1,0,0,0],
  [1,1,1,1]
  ],
  "M": [
  [1,0,0,1],
  [1,1,1,1],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1]
  ],
  "N": [
  [1,0,0,1],
  [1,1,0,1],
  [1,0,1,1],
  [1,0,1,1],
  [1,0,0,1]
  ],
  "O": [
  [0,1,1,0],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [0,1,1,0]
  ],
  "P": [
  [1,1,1,0],
  [1,0,0,1],
  [1,1,1,0],
  [1,0,0,0],
  [1,0,0,0]
  ],
  "Q": [
  [0,1,1,0],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,1,1],
  [0,1,1,1]
  ],
  "R": [
  [1,1,1,0],
  [1,0,0,1],
  [1,1,1,0],
  [1,0,0,1],
  [1,0,0,1]
  ],
  "S": [
  [0,1,1,0],
  [1,0,0,1],
  [0,1,0,0],
  [1,0,1,0],
  [0,1,1,1]
  ],
  "T": [
  [1,1,1,1],
  [0,1,1,0],
  [0,1,1,0],
  [0,1,1,0],
  [0,1,1,0]
  ],
  "U": [
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [0,1,1,0]
  ],
  "V": [
  [1,0,0,1],
  [1,0,0,1],
  [1,0,0,1],
  [0,1,1,0],
  [0,1,1,0]
  ],
  "W": [
  [1,0,0,1],
  [1,0,0,1],
  [1,1,1,1],
  [1,1,1,1],
  [0,1,1,0]
  ],
  "X": [
  [1,0,0,1],
  [0,1,1,0],
  [0,1,1,0],
  [0,1,1,0],
  [1,0,0,1]
  ],
  "Y": [
  [1,0,1,0],
  [1,0,1,0],
  [0,1,0,0],
  [0,1,0,0],
  [0,1,0,0]
  ],
  "Z": [
  [1,1,1,1],
  [0,0,1,0],
  [0,1,0,0],
  [1,0,0,0],
  [1,1,1,1]
  ],
  "SPACE": [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0]
  ]
}


def build_message(mes):
  mes = mes.upper()
  mes_matrix = [
    [],
    [],
    [],
    [],
    []
  ]
  for c in list(mes):
    c = c if c != ' ' else "SPACE"
    if alphabit[c]:
      for index, row in enumerate(alphabit[c]):
        mes_matrix[index].extend(row)
        mes_matrix[index].extend([0])
  return mes_matrix

# print(build_message('TEST'))


for row in build_message('hello world'):
  row_string = ''
  for col in row:
    char = col if col == 1 else ' '
    row_string = row_string + str(char) + ' '
  print(row_string)
