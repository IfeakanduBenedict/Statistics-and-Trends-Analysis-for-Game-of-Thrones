"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as ss

def plot_relational_plot(df):
    """Plots the relationship between U.S. Viewers and IMDb Rating."""
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df['U.S. Viewers (Millions)'], y=df['IMDb Rating'], alpha=0.7)
    plt.xlabel('U.S. Viewers (Millions)')
    plt.ylabel('IMDb Rating')
    plt.title('Relationship between IMDb Rating and U.S. Viewers')
    plt.savefig('relational_plot.png')
    plt.show()

def plot_categorical_plot(df):
    """Plots the IMDb Ratings across different Seasons using a boxplot."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df['Season'], y=df['IMDb Rating'], palette='coolwarm')
    plt.xlabel('Season')
    plt.ylabel('IMDb Rating')
    plt.title('IMDb Ratings by Season')
    plt.savefig('categorical_plot.png')
    plt.show()

def plot_statistical_plot(df):
    """Plots the distribution of IMDb Ratings with a histogram and KDE."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df['IMDb Rating'], bins=15, kde=True, color='royalblue')
    plt.xlabel('IMDb Rating')
    plt.ylabel('Frequency')
    plt.title('Distribution of IMDb Ratings')
    plt.savefig('statistical_plot.png')
    plt.show()

def statistical_analysis(df, col: str):
    """Computes and returns statistical moments: mean, std dev, skewness, and excess kurtosis."""
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col], nan_policy='omit')
    excess_kurtosis = ss.kurtosis(df[col], nan_policy='omit')
    return mean, stddev, skew, excess_kurtosis

def preprocessing(df):
    """Cleans and preprocesses the dataset by selecting relevant columns and handling missing values."""
    selected_columns = ['Season', 'Running Time (Minutes)', 'U.S. Viewers (Millions)', 'IMDb Rating', 'Rotten Tomatoes Rating (Percentage)']
    df = df[selected_columns].dropna()
    return df

def writing(moments, col):
    """Prints a detailed statistical analysis of the chosen column."""
    print(f'For the attribute {col}:')
    print(f'  Mean = {moments[0]:.2f}\n  Standard Deviation = {moments[1]:.2f}\n  Skewness = {moments[2]:.2f}\n  Excess Kurtosis = {moments[3]:.2f}')
    skew_type = "right-skewed" if moments[2] > 0 else "left-skewed" if moments[2] < 0 else "symmetrical"
    kurtosis_type = "leptokurtic" if moments[3] > 0 else "platykurtic" if moments[3] < 0 else "mesokurtic"
    print(f'The data is {skew_type} and {kurtosis_type}.')

def main():
    """Main function to run the analysis on Game of Thrones dataset."""
    df = pd.read_csv('Game_of_Thrones.csv')
    df = preprocessing(df)
    col = 'IMDb Rating'
    plot_relational_plot(df)
    plot_categorical_plot(df)
    plot_statistical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)

if __name__ == '__main__':
    main()
