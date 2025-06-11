"""
Marco Bejarano Oseguera
06/11/2025
"""

def generate_arithmetic(first_term, common_diff, num_terms):
    if num_terms <= 0:
        return [], 0

    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_diff)
        sequence.append(term)

    sequence_sum = sum(sequence)
    return sequence, sequence_sum

def generate_geometric(first_term, common_ratio, num_terms):
    if num_terms <= 0:
        return [], 0

    if first_term == 0:
        return [0] * num_terms, 0

    sequence = []
    for i in range(num_terms):
        term = first_term * (common_ratio ** i)
        sequence.append(term)

    product = 1
    for term in sequence:
        product *= term

    return sequence, product