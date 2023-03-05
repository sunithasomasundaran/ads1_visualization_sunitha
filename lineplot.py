#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:29:55 2023

@author: sunitha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def getpopulationbycountry(country_name):
    '''
    Returns the population of a given country.

    Parameters
    ----------
    country_name : Country name as a string.

    Returns
    -------
    population : Population of the given country as dataframe.

    '''
    population = electricity_df.loc[(
        (electricity_df['Country Name'] == country_name) &
        (electricity_df['Series Name'] ==
         'Access to electricity, rural (% of rural population)')
    )].iloc[:, 2:].values.tolist()[0]
    return population


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

#reading the dataset from an excel file.
electricity_df = pd.read_excel('electricity.xlsx')

#extract the data we neeed for plotting from the dataframe
#using indexing and slicing.
years = electricity_df.columns.values[2:]

#The list of countries being compared in the plot
countries = ['India', 'Pakistan', 'Sri Lanka', 'Bangladesh']

#Set the font size for all the texts appearing on the plot
plt.rcParams.update({'font.size': 22})

#Initializing a figure for plotting the chart
plt.figure(figsize=[15, 10], dpi=600)

#plotting multiple line charts for the list of countries
for c in countries:
    plt.plot(years, getpopulationbycountry(c), linewidth=4)

#improving the readability of the chart by providing a meaningful title,
#informative legend
#and proper y-axis and x-axis tick values.
plt.title('''\nRural population with access to electricity - 2000 to 2020\n''',
          fontsize='x-large',
          fontweight='bold')
plt.legend(countries, loc=4)
plt.yticks(np.arange(0, 110, 10))
plt.xticks(getticksforyears(years.min(), years.max(), 1), rotation=60)

#labelling the x-axis and y-axis
plt.xlabel('Years')
plt.ylabel('population (%)')

#automatically adjust the layout of the plot
plt.tight_layout()

#saving the plot as an image
plt.savefig("lineplot.png")

plt.show()
