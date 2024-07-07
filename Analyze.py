import pandas as pd
import matplotlib.pyplot as plt
file_path = r"C:\Users\Pv\Desktop\results.csv"
data = pd.read_csv(file_path)
top_10_teams = data.nsmallest(10, 'Rank')


aeronyx_team = data[data['Team Name'] == 'Aeronyx']


comparison = pd.concat([top_10_teams, aeronyx_team])

comparison['Team Name'] = comparison.apply(lambda row: row['Team Name'] if row['Team Name'] != 'Aeronyx' else f"{row['Team Name']} (Your Team)", axis=1)

# Visualization
plt.figure(figsize=(14, 8))

# Bar plot for total scores
plt.bar(comparison['Team Name'], comparison['Total\nScore'], color=['blue' if team != 'Aeronyx (Your Team)' else 'red' for team in comparison['Team Name']])
plt.xlabel('Team Name')
plt.ylabel('Total Score')
plt.title('Comparison of Top 10 Teams Total Scores with Aeronyx')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

