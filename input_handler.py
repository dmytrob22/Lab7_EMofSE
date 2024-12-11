import random


class InputHandler:
    @staticmethod
    def input_sample():
        while True:
            choice = input("Enter data manually (M) or generate (G) a uniform/normal distribution? (M/G): ").strip().upper()
            if choice == "M":
                try:
                    raw_data = input(
                        "Enter integers between 0 and 20 (space-separated): "
                    ).split()
                    sample = [int(x) for x in raw_data if 0 <= int(x) <= 20]
                    if len(sample) == len(raw_data):
                        return sample
                    else:
                        print("Invalid input. Ensure all values are integers between 0 and 20.")
                except ValueError:
                    print("Invalid input. Ensure all values are integers between 0 and 20.")
            elif choice == "G":
                dist_choice = input("Generate uniform (U) or normal (N) distribution? (U/N): ").strip().upper()
                size = int(input("Enter the size of the sample: "))
                if dist_choice == "U":
                    return [random.randint(0, 20) for _ in range(size)]
                elif dist_choice == "N":
                    mean = 10  # Center of the range
                    std_dev = 3.5  # Reduced standard deviation to make data more concentrated around 10
                    return [
                        min(max(int(random.gauss(mean, std_dev)), 0), 20) for _ in range(size)
                    ]
                else:
                    print("Invalid choice. Please select U or N.")
            else:
                print("Invalid choice. Please select M or G.")

    @staticmethod
    def input_alpha():
        while True:
            try:
                alpha = float(input("Enter significance level (e.g., 0.05): "))
                if 0 < alpha < 1:
                    return alpha
                else:
                    print("Invalid input. Alpha must be between 0 and 1.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
