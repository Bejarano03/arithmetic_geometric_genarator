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

def combined_sequence_generator():
    print("=== Sequence Generator ===")
    print("1. Arithmetic Sequence")
    print("2. Geometric Sequence")

    try:
        choice = int(input("Choose sequence type (1 or 2): "))

        if choice == 1:
            print("\n--- Arithmetic Sequence ---")
            first_term = float(input("Enter first term: "))
            common_diff = float(input("Enter common difference: "))
            num_terms = int(input("Enter number of terms: "))

            sequence, sequence_sum = generate_arithmetic(first_term, common_diff, num_terms)

            print(f"\nArithmetic Sequence: {sequence}")
            print(f"Sum of sequence: {sequence_sum}")

        elif choice == 2:
            print("\n--- Geometric Sequence ---")
            first_term = float(input("Enter first term: "))
            common_ratio = float(input("Enter common ratio: "))
            num_terms = int(input("Enter number of terms: "))

            sequence, product = generate_geometric(first_term, common_ratio, num_terms)

            print(f"\nGeometric Sequence: {sequence}")
            print(f"Product of sequence: {product}")

        else:
            print("Invalid choice! Please select 1 or 2.")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

combined_sequence_generator()