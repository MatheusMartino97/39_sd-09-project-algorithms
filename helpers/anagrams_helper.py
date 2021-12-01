def sort_word(word):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False

        for i in range(len(word) - num_of_iterations - 1):
            if word[i] > word[i + 1]:
                word[i], word[i + 1] = word[i + 1], word[i]
                has_swapped = True
        num_of_iterations += 1

    return word


# Baseado no bubble sort do course Bloco 35 - Algoritmos
