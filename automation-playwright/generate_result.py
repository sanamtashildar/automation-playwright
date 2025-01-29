def generate_multiplication_tables(filename="multiplication_tables.txt"):
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