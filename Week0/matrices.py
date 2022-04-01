def matrice():
    matrix = [[
        input("input a number "),
        input("input a number "),
        input("input a number ")
    ],
              [
                  input("input a number "),
                  input("input a number "),
                  input("input a number ")
              ],
              [
                  input("input a number "),
                  input("input a number "),
                  input("input a number ")
              ]]
    newMatrix = []
    matrice2(matrix, newMatrix)
    matrice3(newMatrix)


def matrice2(matrix, newMatrix):
    for w in range(len(matrix)):
        for y in range(len(matrix[w])):
            newMatrix.append(matrix[w][y])
    return (newMatrix)


def matrice3(newMatrix):
    print(newMatrix[0], newMatrix[1], newMatrix[2])
    print(newMatrix[3], newMatrix[4], newMatrix[5])
    print(newMatrix[6], newMatrix[7], newMatrix[8])

    # terminal print commands