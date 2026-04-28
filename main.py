def calculate_combinations(length, has_upper, has_numbers, has_symbols):
    """
    Calculates total possible password combinations using combinatorics.
    (Permutations with repetition allowed: n^r)
    """
    pool_size = 26  # Base 26 for lowercase English letters
    
    if has_upper:
        pool_size += 26
    if has_numbers:
        pool_size += 10
    if has_symbols:
        pool_size += 32  # Standard special characters
        
    total_combinations = pool_size ** length
    return total_combinations, pool_size

def estimate_crack_time(combinations, guesses_per_second):
    """Converts raw guesses into human-readable time."""
    seconds = combinations / guesses_per_second
    
    if seconds < 60:
        return f"{round(seconds, 2)} seconds"
    elif seconds < 3600:
        return f"{round(seconds / 60, 2)} minutes"
    elif seconds < 86400:
        return f"{round(seconds / 3600, 2)} hours"
    elif seconds < 31536000:
        return f"{round(seconds / 86400, 2)} days"
    else:
        years = seconds / 31536000
        return f"{round(years, 2):,} years"

def main():
    print("--- Brute-Force Password Time Estimator ---")
    print("This tool uses combinatorics to calculate password security.\n")
    
    try:
        length = int(input("Enter password length (e.g., 8, 12, 16): "))
        has_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        has_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        has_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        combinations, pool_size = calculate_combinations(length, has_upper, has_numbers, has_symbols)
        
        # Simulating a modern GPU cracking rig doing 10 Billion guesses a second
        guesses_per_sec = 10_000_000_000 
        time_to_crack = estimate_crack_time(combinations, guesses_per_sec)
        
        print("\n--- Security Report ---")
        print(f"Character Pool Size: {pool_size} possible characters per slot")
        print(f"Total Combinations: {combinations:,}")
        print(f"Estimated Time to Crack (at 10B guesses/sec): {time_to_crack}\n")
        
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
