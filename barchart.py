#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:30:45 2023

@author: sunitha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def getruralpopulation(year):
    '''
    Returns the rural population for the given year.

    Parameters
    ----------
    year : Year as integer for which the population is required.

    Returns
    -------
    rural_population : Rural population for the given year as a dataframe.

    '''
    rural_population = electricity_df.loc[
        'Access to electricity, rural (% of rural population)', year]
    return rural_population


def geturbanpopulation(year):
    '''
    Returns the urban population for the given year.

    Parameters
    ----------
    year : Year as integer for which the population is required.

    Returns
    -------
    urban_population : Urban population for the given year as a dataframe.

    '''
    urban_population = electricity_df.loc[
        'Access to electricity, urban (% of urban population)', year]
    return urban_population

#reading the dataset from an excel file.
electricity_df = pd.read_excel('electricity.xlsx')

#extracting the data we neeed for plotting from the dataframe
#using indexing.
electricity_df.set_index('Series Name', inplace=True)
countries = electricity_df['Country Name'].unique()

#Set the font size for all the texts appearing on the plot
plt.rcParams.update({'font.size': 22})

#Initializing a figure for plotting the chart
plt.figure(figsize=[15, 10], dpi=600)

#setting the offset value to arrange the bars
bar_position = np.arange(len(countries))

#plotting multiple bar charts for the urban and rural population
#for the list of countries.
plt.bar(bar_position, getruralpopulation(2005), width=0.25)
plt.bar(bar_position + 0.25, geturbanpopulation(2005), width=0.25)

#improving the readability of the chart by providing a meaningful title,
#informative legend
#and proper y-axis and x-axis tick values.
plt.title('''\nPopulation with access to electricity - 2005\n''',
          fontsize='x-large',
          fontweight='bold')
plt.legend(['Rural Population', 'Urban Population'])
plt.xticks([c + 0.25 for c in range(len(countries))], countries, rotation=60)
plt.yticks(np.arange(0, 160, 20))

#labelling the x-axis and y-axis
plt.xlabel('Countries')
plt.ylabel('population (%)')

plt.tight_layout()

#saving the plot as an image
plt.savefig("barplot.png")

plt.show()
