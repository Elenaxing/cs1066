"""Search for trends and generate plots until the user chooses to stop."""

import trends_save
import trends_plot


def main():
    while True:
        trends_save.main()
        trends_plot.main()

        while True:
            answer = input("Would you like to search for another term? (yes/no): ").strip().lower()
            if answer in ("yes", "y"):
                break
            if answer in ("no", "n"):
                return
            print("Please enter yes or no.")


if __name__ == "__main__":
    main()
