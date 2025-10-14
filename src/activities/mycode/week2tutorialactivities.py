from pathlib import Path
import csv
import pandas as pd
import matplotlib.pyplot as plt

def describe_dataframe(df, name="DataFrame"):
    """Prints detailed information about a Pandas DataFrame."""
    print(f"--- {name} ---\n")
    
    # Print the shape (rows, columns)
    print("Shape:", df.shape, "\n")
    
    # Ensure all columns are displayed
    pd.set_option("display.max_columns", None)
    
    # Print the first 5 rows
    print("First 5 rows:")
    print(df.head(), "\n")
    
    # Print the last 5 rows
    print("Last 5 rows:")
    print(df.tail(), "\n")
    
    # Print column labels
    print("Column labels:")
    print(df.columns.tolist(), "\n")
    
    # Print column data types
    print("Column datatypes:")
    print(df.dtypes, "\n")
    
    # Print info
    print("DataFrame info:")
    df.info()
    print("\n")
    
    # Print descriptive statistics
    print("Descriptive statistics:")
    print(df.describe(include='all'), "\n")
    print("="*80, "\n")

def plot_timeseries(df, x, y, title="", xlabel=None, ylabel=None, group=None):

    if group is None:
        plt.plot(df[x], df[y], marker='o', linestyle='-', label=y)
    else:
        for key, group_df in df.groupby(group):
            plt.plot(group_df[x], group_df[y], marker='o', linestyle='-', label=key)

    plt.figure(figsize=(10,6))
    plt.plot(df[x], df[y], marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x)
    plt.ylabel(ylabel if ylabel else y)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    paralympics_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    medal_standings_csv = Path(__file__).parent.parent.joinpath("data", "medal_standings.csv")
    
    events_df = pd.read_csv(paralympics_csv)
    # medal_standings_df = pd.read_csv(medal_standings_csv)

    # describe_dataframe(events_df, name="Events DataFrame")
    # describe_dataframe(medal_standings_df, name="Medal Standings DataFrame")

    # Check what columns we have
    # print(events_df.head())

    print(events_df['type'].unique)


    # events_df.boxplot(figsize=(10,6))

    # plt.title("Boxplot of all variables")
    # plt.show()

    # plot_timeseries(events_df, x='start', y='participants', group='type',
    #             title='Paralympic Participants Over Time by Season',
    #             xlabel='Year', ylabel='Participants')

    
    