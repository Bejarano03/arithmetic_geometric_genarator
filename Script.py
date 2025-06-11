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
