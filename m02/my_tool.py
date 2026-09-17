"""Prompt for a search term, save its trends data, and generate a plot."""

import trends_save
import trends_plot


def main():
    trends_save.main()
    trends_plot.main()


if __name__ == "__main__":
    main()
