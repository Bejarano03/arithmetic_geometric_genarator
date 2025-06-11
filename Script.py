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

def test_cases():
    print("=== Running Test Cases ===\n")
    print("Arithmetic Sequence Test:")
    print("-" * 40)

    # Normal Test Cases

    print("1. Normal Case - Positive difference:")
    seq, sum_val = generate_arithmetic(2, 3, 5)
    print(f"   Input: first_term=2, common_diff=3, num_terms=5")
    print(f"   Output: {seq}, Sum: {sum_val}")
    print(f"   Expected: [2, 5, 8, 11, 14], Sum: 40")
    print(f"   ✓ PASS" if seq == [2, 5, 8, 11, 14] and sum_val == 40 else "   ✗ FAIL")

    print("\n2. Normal Case - Negative difference:")
    seq, sum_val = generate_arithmetic(10, -2, 4)
    print(f"   Input: first_term=10, common_diff=-2, num_terms=4")
    print(f"   Output: {seq}, Sum: {sum_val}")
    print(f"   Expected: [10, 8, 6, 4], Sum: 28")
    print(f"   ✓ PASS" if seq == [10, 8, 6, 4] and sum_val == 28 else "   ✗ FAIL")

    print("\n3. Normal Case - Zero difference:")
    seq, sum_val = generate_arithmetic(5, 0, 3)
    print(f"   Input: first_term=5, common_diff=0, num_terms=3")
    print(f"   Output: {seq}, Sum: {sum_val}")
    print(f"   Expected: [5, 5, 5], Sum: 15")
    print(f"   ✓ PASS" if seq == [5, 5, 5] and sum_val == 15 else "   ✗ FAIL")

    # Edge Test Cases

    print("\n4. Edge Case - First term is zero:")
    seq, prod = generate_geometric(0, 5, 3)
    print(f"   Input: first_term=0, common_ratio=5, num_terms=3")
    print(f"   Output: {seq}, Product: {prod}")
    print(f"   Expected: [0, 0, 0], Product: 0")
    print(f"   ✓ PASS" if seq == [0, 0, 0] and prod == 0 else "   ✗ FAIL")

    print("\n5. Edge Case - Single term:")
    seq, prod = generate_geometric(5, 2, 1)
    print(f"   Input: first_term=5, common_ratio=2, num_terms=1")
    print(f"   Output: {seq}, Product: {prod}")
    print(f"   Expected: [5], Product: 5")
    print(f"   ✓ PASS" if seq == [5] and prod == 5 else "   ✗ FAIL")

    print("\n6. Edge Case - Zero terms:")
    seq, prod = generate_geometric(3, 2, 0)
    print(f"   Input: first_term=3, common_ratio=2, num_terms=0")
    print(f"   Output: {seq}, Product: {prod}")
    print(f"   Expected: [], Product: 1")
    print(f"   ✓ PASS" if seq == [] and prod == 1 else "   ✗ FAIL")

    print("\n=== TEST CASES COMPLETED ===")
