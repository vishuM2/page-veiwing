import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def page_view_time_series_visualizer(file_path):
    # Load the data into a Pandas DataFrame
    df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')

    # Display the first few rows of the DataFrame
    print("Sample of the data:")
    print(df.head())

    # Basic statistics
    print("\nBasic statistics:")
    print(df.describe())

    # Line plot of page views over time
    plt.figure(figsize=(14, 6))
    sns.lineplot(x=df.index, y='value', data=df)
    plt.title('Page Views Over Time')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()

    # Monthly bar plot of page views
    df['month'] = df.index.month_name()
    plt.figure(figsize=(14, 6))
    sns.barplot(x='month', y='value', data=df, order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.title('Monthly Page Views')
    plt.xlabel('Month')
    plt.ylabel('Average Page Views')
    plt.show()

    # Weekly box plot of page views
    df['day_of_week'] = df.index.day_name()
    plt.figure(figsize=(14, 6))
    sns.boxplot(x='day_of_week', y='value', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.title('Weekly Page Views')
    plt.xlabel('Day of Week')
    plt.ylabel('Page Views')
    plt.show()

if __name__ == "__main__":
    # Provide the path to your time series data CSV file
    file_path = "path/to/your/page_view_time_series_data.csv"
    page_view_time_series_visualizer(file_path)
