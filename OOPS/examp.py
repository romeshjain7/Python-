# def calculate_impact_sum():
#     n = int(input("Enter the number of products: "))
#     weights = list(map(int, input("Enter the product weights separated by spaces: ").split()))
#     c = int(input("Enter the maximum threshold value: "))
    
#     total_sum = sum(weights)
#     result = []
    
#     for weight in weights:
#         impact_sum = total_sum - weight  # Excluding the current product's weight
#         result.append(min(impact_sum, c))  # Apply threshold
    
#     return result

# # Function call and output
# output = calculate_impact_sum()
# print(output)


def alphabet_cost(input1: str, input2: list) -> int:
    input1 = input1.upper()  # Convert input to uppercase
    available_letters = set(input1)  # Store available letters in a set
    
    total_cost = 0
    
    # Iterate only from 'A' to 'Z'
    for ch in range(ord('A'), ord('Z') + 1):
        if chr(ch) not in available_letters:
            total_cost += input2[ch - ord('A')]
    
    return total_cost
