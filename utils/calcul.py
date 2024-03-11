def calcul_gravity(potentiality, impact):
    # Assuming wish_matrix is a 4x4 matrix
    wish_matrix = [
        [1, 1, 1, 2],
        [1, 2, 2, 3],
        [2, 3, 3, 4],
        [2, 3, 4, 4]
    ]

    # Check if potentiality and impact are within valid range
    if 0 <= potentiality < 4 and 0 <= impact < 4:
        # Access the corresponding value in the wish matrix
        result = wish_matrix[potentiality][impact]
        return result
    else:
        return "Invalid potentiality or impact value"