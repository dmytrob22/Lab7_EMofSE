from chi_squared_test import ChiSquaredTest
from input_handler import InputHandler
from plotter import Plotter


def main():
    sample = InputHandler.input_sample()
    alpha = InputHandler.input_alpha()

    # If sample size is too small, suggest using other tests
    if len(sample) < 30:
        print("Sample size is small. Chi-squared test might not be accurate. Consider using other tests.")

    test = ChiSquaredTest(sample, alpha)
    results = test.run_test()

    print("\nSample:", sample)
    print("Observed Frequencies:", results["observed"])
    print(f"Chi-squared (Normal): {results['chi_squared_normal']:.4f}")
    print(f"Chi-squared (Uniform): {results['chi_squared_uniform']:.4f}")
    print(f"Chi-squared Critical: {results['chi_squared_critical']:.4f}")
    print("Normal Distribution Match:", results["is_normal"])
    print("Uniform Distribution Match:", results["is_uniform"])

    Plotter.plot_frequencies(results["observed"])


if __name__ == "__main__":
    main()
