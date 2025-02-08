import os

def generate_multiplication_tables(filename="result/multiplication_tables.txt"):
    # Create the result directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, "w") as file:
        for i in range(2, 21):  # Tables from 2 to 20
            file.write(f"Multiplication Table for {i}\n")
            file.write("=" * 30 + "\n")
            for j in range(1, 11):  # Multiplication up to 10
                file.write(f"{i} x {j} = {i * j}\n")
            file.write("\n")
    print(f"Multiplication tables saved in {filename}")

# Run the function
generate_multiplication_tables()