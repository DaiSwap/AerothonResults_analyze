import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# File path
file_path = r"C:\Users\Pv\Desktop\results.csv"
data = pd.read_csv(file_path)

# Filter the data for the top 5 teams
top_5_teams = data.nsmallest(5, 'Rank')

# Filter the data for Aeronyx team
aeronyx_team = data[data['Team Name'] == 'Aeronyx']

# Calculate the average scores for the top 5 teams, excluding non-numeric columns
numeric_columns = top_5_teams.select_dtypes(include='number').columns

# Remove specified features
excluded_features = ['Design\nReport\nScore\n(Max 90)', 'Presentati\non Score\n(Max 10)', 'Total\nScore', 'Rank']
numeric_columns = [col for col in numeric_columns if col not in excluded_features]

top_5_avg = top_5_teams[numeric_columns].mean()
aeronyx_scores = aeronyx_team[numeric_columns].mean()

# Combine Aeronyx and top 5 average for comparison
comparison = pd.DataFrame({
    'Feature': numeric_columns,
    'Top 5 Avg': top_5_avg.values,
    'Aeronyx': aeronyx_scores.values
})

# Visualization
features = comparison['Feature']
x = np.arange(len(features))

plt.figure(figsize=(16, 10))

# Bar plot for comparison
bar_width = 0.35
plt.bar(x, comparison['Top 5 Avg'], width=bar_width, label='Top 5 Avg', color='#1f77b4')
plt.bar(x + bar_width, comparison['Aeronyx'], width=bar_width, label='Aeronyx', color='#ff7f0e')

# Add labels and title
plt.xlabel('Features', fontsize=14, fontweight='bold')
plt.ylabel('Scores', fontsize=14, fontweight='bold')
plt.title('Comparison of Scores: Top 5 Avg vs. Aeronyx', fontsize=16, fontweight='bold')
plt.xticks(x + bar_width / 2, features, rotation=90, fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
plt.legend(fontsize=14, frameon=True, shadow=True)

# Annotate scores on the bars
for i in range(len(features)):
    plt.text(i - bar_width/2, comparison['Top 5 Avg'][i] + 0.05, round(comparison['Top 5 Avg'][i], 2), 
             ha='center', fontsize=12, fontweight='bold', color='black')
    plt.text(i + bar_width/2, comparison['Aeronyx'][i] + 0.05, round(comparison['Aeronyx'][i], 2), 
             ha='center', fontsize=12, fontweight='bold', color='black')

# Grid and tight layout for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show plot
plt.show()

# Optionally, save the comparison data to a new CSV file
comparison.to_csv('detailed_comparison_with_top_5_teams.csv', index=False)
