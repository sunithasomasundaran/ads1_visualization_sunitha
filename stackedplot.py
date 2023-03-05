#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:18:48 2023

@author: sunitha
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def getticksforyears(start_year, end_year, step):
    '''
    Returns the array of years to be plotted as ticks.

    Parameters
    ----------
    start_year : Year as integer that is plotted as the first tick.
    end_year : Year as integer that is plotted as the last tick.
    step : Integer representing the interval between each tick.

    Returns
    -------
    years : Integer array of years.

    '''
    years = np.arange(start_year, end_year + 1, step)
    return years


# Read dataset (UK's Carbon Footprint 1990 to 2009)
carbon_emission_df = pd.read_excel('carbon_emission.xlsx')

# extracting the data we neeed for plotting from the dataframe using indexing.
y1_native_emission = carbon_emission_df['native emission']
y2_imported_emission = carbon_emission_df['imported emission']
x_duration = carbon_emission_df['year']

# Set the font size for all the texts appearing on the plot
plt.rcParams.update({'font.size': 22})

# Initializing a figure for plotting the chart
plt.figure(figsize=[15, 10], dpi=600)

# plotting a stacked area chart
plt.stackplot(x_duration, y1_native_emission, y2_imported_emission)

# improving the readability of the chart by providing a meaningful title,
# informative legend
# and proper x-axis tick values.
plt.title('''\nUK's Carbon Footprint 1990 to 2009\n''',
          fontsize='x-large',
          fontweight='bold')
plt.legend(['Native emission', 'Imported emission'], loc='upper left')
plt.xticks(getticksforyears(x_duration.min(),
           x_duration.max(), 1), rotation=60)

# limiting the starting and ending points of the x-axis and y-axis
plt.xlim(x_duration.min(), x_duration.max())
plt.ylim(0, 900000)

# labelling the x-axis and y-axis
plt.xlabel('Years')
plt.ylabel('CO2 (kilo tonnes)')

#automatically adjust the layout of the figure
plt.tight_layout()

# saving the plot as an image
plt.savefig("stackedplot.png")

plt.show()
