import random 
import hashlib
import time

#function for generating random inputs. takes in number of random inputs to generate and the length of those inputs.
def generate_random_inputs(num_inputs, input_length):
    return [''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=input_length)) for _ in range(num_inputs)]

#function for computing SHA-256 hashes for multiple inputs and counts the number of 1 bits in each hash
def count_ones(inputs):
    bit_counts = []
    for input_str in inputs:
        hash_value = hashlib.sha256(input_str.encode('utf-8')).hexdigest()
        bit_count = bin(int(hash_value, 16)).count('1')
        bit_counts.append(bit_count)
    return bit_counts

#generates histogram using a dictionary, where keys are bit counts and the values are their frequencies. 
def generate_histogram(bit_counts):
    histogram = {}
    for count in bit_counts:
        histogram[count] = histogram.get(count, 0) + 1
    return histogram

#measures the hash rate given input
def measure_hash_rate(inputs):
    start_time = time.time()
    for input_str in inputs:
        hashlib.sha256(input_str.encode('utf-8')).hexdigest()
    end_time = time.time()

    total_time = end_time - start_time
    hash_rate = len(inputs) / total_time
    return total_time, len(inputs), hash_rate

#user input
while True:
    try:
        choice = input("1) Self-input \n2) Birthday attack and brute force showcase: ")
        match(choice):
            case "1":
                num_inputs = int(input("Enter number of inputs: "))
                input_length = int(input("Enter input length: "))
                break  
            case "2":
                num_inputs = 10000
                input_length = 10
                inputs = generate_random_inputs(num_inputs, input_length)
                _, _, hash_rate = measure_hash_rate(inputs) #calculate general hash_rate 

                birthday_attack_hashes = 2 ** 128
                brute_force_hashes = 2 ** 256

                birthday_attack_time = birthday_attack_hashes / hash_rate
                brute_force_time = brute_force_hashes / hash_rate

                print(f"\nEstimation for Large-Scale Attacks:")
                print(f"Time for Birthday Attack (2^128 hashes): {birthday_attack_time / (60 * 60 * 24 * 365):.2e} years")
                print(f"Time for Brute-Force Attack (2^256 hashes): {brute_force_time / (60 * 60 * 24 * 365):.2e} years")
    except ValueError:
        print("Invalid input. Please enter integer values.")
    
inputs = generate_random_inputs(num_inputs, input_length)
bit_counts = count_ones(inputs)
histogram = generate_histogram(bit_counts)

print("Histogram of 1-bit counts in SHA-256 hashes:")
for bit_count, frequency in sorted(histogram.items()):
    print(f"{bit_count} bits: {frequency}")

total_time, num_hashes, hash_rate = measure_hash_rate(inputs)
print(f"\nTime, hashes, and hash rate:")
print(f"Total Time: {total_time:.2f} seconds")
print(f"Number of Hashes: {num_hashes}")
print(f"Hashes per Second: {hash_rate:.2f}")