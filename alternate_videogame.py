# -*- coding: utf-8 -*-
"""Alternate_videogame

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jp7nHesPfETn7c_PnUKnon7Jf_P1ssjZ
"""

PHASE 1

#PS1
import pandas as pd

# Read the CSV file
sales_data = pd.read_csv("/content/VGsales_datasets.csv")

# Filter the data for the years 1980 and 1981
atari_1980_1981 = sales_data[sales_data['Year'].isin([1980, 1981])]

# Group the data by year and calculate total sales
sales_by_year = atari_1980_1981.groupby('Year', as_index=False)['Global_Sales'].sum()

# Save the result to a new CSV file
sales_by_year.to_csv('/content/atari_sales_trends.csv', index=False)

# Print the first few rows of the result
print(sales_by_year.head())

#PS2
import pandas as pd

# Load the dataset
df = pd.read_csv('/content/VGsales_datasets.csv')

# Filter for Atari 2600 and years 1980 and 1981
atari_genres = df.loc[(df['Platform'] == '2600') & (df['Year'].isin([1980, 1981]))]

# Group by genre and sum sales
genre_performance = atari_genres.groupby('Genre', as_index=False)['Global_Sales'].sum()

# Save to a new CSV for Power BI
genre_performance.to_csv('/content/atari_genre_performance.csv', index=False)
print(genre_performance.head())

#PS3
import pandas as pd

# Load the dataset
df = pd.read_csv('/content/VGsales_datasets.csv')

# Filter for Atari 2600 and years 1980 and 1981
atari_genres = df[(df['Platform'] == '2600') & (df['Year'].isin([1980, 1981]))]

# Group by genre and sum sales for North America and Europe
regional_genre_sales = atari_genres.groupby('Genre', as_index=False)[['NA_Sales', 'EU_Sales']].sum()

# Calculate the difference between North America and Europe sales
regional_genre_sales['NA_vs_EU'] = regional_genre_sales['NA_Sales'] - regional_genre_sales['EU_Sales']

# Save the preprocessed data to a CSV file for further analysis
preprocessed_file_path = '/content/Regional_genre_popularity.csv'
regional_genre_sales.to_csv(preprocessed_file_path, index=False)

print(regional_genre_sales)

"""PHASE 2"""

#PS4
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("/content/VGsales_datasets.csv")

# Filter records for the X360 platform
x360_df = df.query("Platform == 'X360'")

# Group by Year and sum up the sales
country_sales = x360_df.groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

country_sales.plot(kind='bar', ax=ax)
plt.title('X360 Platform Sales by Year')
plt.xlabel('Year')
plt.ylabel('Sales (in millions)')
plt.xticks(rotation=45)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()

# Global sales
global_sales = country_sales['Global_Sales'].sum()
print("Global Sales for X360 platform:", global_sales)

#PS5
import pandas as pd

# Load the dataset
df = pd.read_csv("VGsales_datasets.csv")

# Convert 'JP_Sales' and 'EU_Sales' columns to numeric data types, ignoring errors
df['JP_Sales'] = pd.to_numeric(df['JP_Sales'], errors='coerce')
df['EU_Sales'] = pd.to_numeric(df['EU_Sales'], errors='coerce')

# Filter data where JP sales are higher than EU sales
jp_sales = df.query("JP_Sales > EU_Sales")

# Save the filtered data to a CSV file
jp_sales.to_csv('JP_Sales.csv', index=False)

# Analyze the contribution of different genres to sales in various regions
genre_sales = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()

print("Genre-Specific Sales in Different Regions:")
print(genre_sales)

#PS6
import pandas as pd

# Load the dataset
df = pd.read_csv("VGsales_datasets.csv")

# Filter for PS3 sports games and sort by global sales
ps3_sports = df.query("Platform == 'PS3' and Genre == 'Sports'").sort_values(by='Global_Sales', ascending=False)

# Save the sorted data to a CSV file
ps3_sports.to_csv('sportsps.csv', index=False)

#PS7
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("VGsales_datasets.csv")

# Filter for sports games in action or shooter genres since 2010
sports_action_shooter = df.query("Year >= 2010 and Genre in ['Action', 'Shooter']")

# Plot the distribution of global sales
plt.figure(figsize=(10, 6))
plt.hist(sports_action_shooter['Global_Sales'], bins=20, edgecolor='k')
plt.title('Distribution of Global Sales for Sports, Action, and Shooter Games (Post-2010)')
plt.xlabel('Global Sales (in millions)')
plt.ylabel('Number of Games')
plt.show()

# Save the filtered data to a CSV file
sports_action_shooter.to_csv('/content/sports_action_shooter.csv', index=False)

# Explain the findings
print("Summary Statistics of Global Sales for Sports Games (Action/Shooter) Since 2010:")
print(sports_action_shooter['Global_Sales'].describe())

"""PHASE 3"""

#PS8
import pandas as pd

# Load the dataset
df = pd.read_csv("VGsales_datasets.csv")

# Filter data for Atari 2600 games released in 1980 and 1981
atari_data = df.query("Platform == '2600' and Year in [1980, 1981]")

# Group by Genre and calculate the number of releases and total global sales for each genre
genre_analysis = atari_data.groupby('Genre').agg(
    Number_of_Releases=('Name', 'count'),
    Total_Global_Sales=('Global_Sales', 'sum')
).reset_index()

# Display the results
print(genre_analysis)

# Save the results to a CSV file
genre_analysis.to_csv('/content/genre_analysis.csv', index=False)

#PS9
import pandas as pd

# Assuming 'df' is the DataFrame containing the dataset
# Filter data for Atari 2600 games released in 1980 and 1981
atari_data = df[(df['Platform'] == '2600') & (df['Year'].isin([1980, 1981]))]

# Group by Genre and calculate the number of releases and total global sales for each genre
genre_analysis = atari_data.groupby('Genre').agg(
    Number_of_Releases=('Name', 'count'),
    Total_Global_Sales=('Global_Sales', 'sum')
).reset_index()

# Display the results
print(genre_analysis)

#PS10
import pandas as pd

# Load the CSV file
file_path = '/content/VGsales_datasets.csv'
data = pd.read_csv(file_path)

# Filter the records with sales between 2 million and 10 million
filtered_data = data[(data['Global_Sales'] >= 2) & (data['Global_Sales'] <= 10)]

# Create a function to categorize years into decades
def categorize_decade(year):
    if 1990 <= year <= 1999:
        return '1990-1999'
    elif 2000 <= year <= 2009:
        return '2000-2009'
    elif 2010 <= year <= 2016:
        return '2010-2016'
    else:
        return 'Other'

# Apply the function to the dataset
filtered_data['Decade'] = filtered_data['Year'].apply(categorize_decade)

# Filter out any records that fall into the 'Other' category
filtered_data = filtered_data[filtered_data['Decade'] != 'Other']

# Group by Decade and Genre and sum the sales
genre_sales_by_decade = filtered_data.groupby(['Decade', 'Genre'])['Global_Sales'].sum().reset_index()

# Pivot the table for better visualization
pivot_table = genre_sales_by_decade.pivot(index='Genre', columns='Decade', values='Global_Sales')

# Display the pivot table
pivot_table

"""PHASE 4"""

#PS11
import pandas as pd

# Load data (replace 'path/to/data.csv' with your actual file path)
data = pd.read_csv('/content/VGsales_datasets.csv')

# Filter for games with global sales data
data_filtered = data.dropna(subset=['Global_Sales'])

# Top Performers
top_performers = data_filtered.nlargest(10, 'Global_Sales')  # Top 10 by default

# Underperformers
underperformers = data_filtered.nsmallest(10, 'Global_Sales')  # Bottom 10 by default

# Print results (optional)
print("Top Performers:")
print(top_performers)
print("\nUnderperformers:")
print(underperformers)

# Save to CSV
top_performers.to_csv('/content/top_performers.csv', index=False)
underperformers.to_csv('/content/underperformers.csv', index=False)

#PS12
import pandas as pd

# Assuming 'df' is the DataFrame containing the dataset
# Filter for racing genre and years 2000-2009
racing_sales = df[(df['Genre'] == 'Racing') & (df['Year'].between(2000, 2009))]

# Filter where EU sales are greater than JP, NA, and other sales
eu_dominant_sales = racing_sales[
    (racing_sales['EU_Sales'] > racing_sales['JP_Sales']) &
    (racing_sales['EU_Sales'] > racing_sales['NA_Sales']) &
    (racing_sales['EU_Sales'] > racing_sales['Other_Sales'])
]

# Get top 5 records for EU sales
top_5_eu_sales = eu_dominant_sales.nlargest(5, 'EU_Sales')[['Name', 'EU_Sales']].set_index('Name')

# Save to a new CSV for Power BI
top_5_eu_sales.to_csv('/content/racing_eusales.csv')
print(top_5_eu_sales.head())

#PS13
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("VGsales_datasets.csv")

# Filter for XB platform
xb_sales = df[df['Platform'] == 'XB']

# Calculate the cumulative sum of NA and JP sales
xb_sales['Cumulative_NA_Sales'] = xb_sales['NA_Sales'].cumsum()
xb_sales['Cumulative_JP_Sales'] = xb_sales['JP_Sales'].cumsum()

# Plot the cumulative sum of NA sales
plt.figure(figsize=(10, 6))
plt.plot(xb_sales['Year'], xb_sales['Cumulative_NA_Sales'], label='Cumulative NA Sales', marker='o')
plt.plot(xb_sales['Year'], xb_sales['Cumulative_JP_Sales'], label='Cumulative JP Sales', marker='o')
plt.title('Cumulative Sales for XB Platform')
plt.xlabel('Year')
plt.ylabel('Cumulative Sales (in millions)')
plt.legend()
plt.grid(True)
plt.show()

# Save the data to a CSV file
xb_sales.to_csv('xb_sales.csv', index=False)

"""FINAL PHASE"""

#PS14
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("VGsales_datasets.csv")

# Create a new column for decades
df['Decade'] = pd.cut(df['Year'], bins=[1980, 1989, 1999, 2009, 2016], labels=['1980s', '1990s', '2000s', '2010s'])

# Sum global sales across decades for each region
region_sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

# Ensure the columns exist in the DataFrame
region_sales_columns = [col for col in region_sales_columns if col in df.columns]

# Group by Decade and sum sales for each region
sales_across_decades = df.groupby('Decade')[region_sales_columns].sum()

# Plot the sales across decades
sales_across_decades.plot(kind='bar', stacked=True, figsize=(12, 7))
plt.title('Global Sales Across Decades')
plt.xlabel('Decade')
plt.ylabel('Global Sales (in millions)')
plt.legend(title='Region')
plt.show()

#PS15
import pandas as pd

# Load the dataset
data = pd.read_csv("VGsales_datasets.csv")

# Filter for Atari 2600 games published by Atari
atari_2600_games = data[(data['Platform'] == '2600') & (data['Publisher'] == 'Atari')]

# Descriptive statistics for sales data
atari_2600_stats = atari_2600_games.describe()

# Sales by Genre
sales_by_genre = atari_2600_games.groupby('Genre').sum()[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].mean()

# Sales by Publisher
sales_by_publisher = atari_2600_games.groupby('Publisher').sum()[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].mean()

# Calculate correlation matrix
correlation_matrix = atari_2600_games[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].corr()

# Print results
print("Descriptive Statistics for Atari 2600 Sales Data:")
print(atari_2600_stats)
print("\nSales by Genre:")
print(sales_by_genre)
print("\nSales by Publisher:")
print(sales_by_publisher)
print("\nCorrelation Matrix:")
print(correlation_matrix)