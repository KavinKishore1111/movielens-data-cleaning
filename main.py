import pandas as pd
import numpy as np
import os

# Ensure the 'output' folder exists
if not os.path.exists('output'):
    os.makedirs('output')

# Step 1: Load datasets
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')

print("Sample Movies Data:")
print(movies.head())
print("\nSample Ratings Data:")
print(ratings.head())

# Step 2: Handle missing values

# Display missing value counts
print("\nMissing values in Movies:\n", movies.isnull().sum())
print("Missing values in Ratings:\n", ratings.isnull().sum())

# Fill missing values in movies data
movies.fillna({'title': 'Unknown', 'genres': 'Unknown'}, inplace=True)

# Fill missing values in ratings data
ratings.fillna({'rating': ratings['rating'].mean(), 'timestamp': 0}, inplace=True)


# Step 3: Remove duplicate rows
movies.drop_duplicates(inplace=True)
ratings.drop_duplicates(inplace=True)

# Step 4: Extract release year from movie titles (e.g., Toy Story (1995))
movies['year'] = movies['title'].str.extract(r'\((\d{4})\)')
movies['year'] = pd.to_numeric(movies['year'], errors='coerce')  # Handle non-numeric cases gracefully

# Step 5: Convert genre strings to list format (e.g., 'Action|Comedy' → ['Action', 'Comedy'])
movies['genres'] = movies['genres'].apply(lambda x: x.split('|') if isinstance(x, str) else [])

# Step 6: Display basic statistics for ratings
print("\nRatings Data Statistics:")
print("Mean Rating:", np.mean(ratings['rating']))
print("Standard Deviation:", np.std(ratings['rating']))
print("Minimum Rating:", np.min(ratings['rating']))
print("Maximum Rating:", np.max(ratings['rating']))

# Step 7: Filter out invalid ratings (keep only between 0.5 and 5.0)
ratings = ratings[(ratings['rating'] >= 0.5) & (ratings['rating'] <= 5.0)]

# Step 8: Export cleaned datasets
movies.to_csv('output/cleaned_movies.csv', index=False)
ratings.to_csv('output/cleaned_ratings.csv', index=False)

print("\nData cleaning complete. Cleaned files saved in 'output' folder!")
