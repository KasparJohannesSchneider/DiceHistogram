import sys
import time
from typing import NoReturn

import numpy as np
from matplotlib import pyplot as plt


def main() -> NoReturn:
    dice_rolls = np.array([])
    bins = np.arange(2, 13)
    hist = np.zeros(11)
    stop_cmds = ['n', 's', 'e', 'exit', 'stop']
    stop = False

    while not stop:
        # Get the user input and stop if desired
        user_input = input('Enter the dice roll: ')

        # Check for an exit command
        stop = user_input in stop_cmds
        if stop:
            print('The program has been stopped.')
            break

        # Make sure, that an int has been entered
        try:
            current_roll = int(user_input)
        except ValueError:
            error_message('Invalid input. Please try again.')
            continue

        if not 2 <= int(user_input) <= 12:
            error_message('The input needs to be between 2 and 12.')
            continue

        # append the current roll to the rolls
        dice_rolls = np.append(dice_rolls, current_roll)
        n = len(dice_rolls)

        # Update the histogram
        hist[current_roll - 2] += 1

        # Update the expected histogram
        expect_hist = np.array(
            [1 / 36, 2 / 36, 3 / 36, 4 / 36, 5 / 36, 6 / 36, 5 / 36,
             4 / 36, 3 / 36, 2 / 36, 1 / 36]) * n

        # print the raw data and histograms for further analysis
        print('\nRaw dice rolls:')
        print(dice_rolls)
        print('\nHistogram:')
        print(hist)
        print('\nExpected histogram:')
        print(expect_hist)
        print('\nBins:')
        print(bins, end='\n\n')

        # plot the results
        plt.clf()

        plt.bar(bins, hist, zorder=2)
        plt.bar(bins, expect_hist, color='none', edgecolor='black', hatch='//', zorder=3)
        plt.title(f'n = {n}')
        plt.xticks(bins)

        # legend and labels
        plt.legend(['actual histogram', 'expected histogram'], loc='upper right')
        plt.xlabel('rolled number')
        plt.ylabel('frequency')

        # grid
        ax = plt.gca()
        ax.yaxis.grid(True)

        # save and show the figure and free the memory
        plt.savefig('dice_histogram.png', dpi=300)
        plt.show()
        plt.close()


def error_message(message: str) -> NoReturn:
    sys.stderr.write(message + '\n')
    sys.stderr.flush()
    time.sleep(0.2)


if __name__ == '__main__':
    main()
