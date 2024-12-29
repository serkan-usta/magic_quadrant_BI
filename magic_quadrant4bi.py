import matplotlib.pyplot as plt
import numpy as np

# Define data for the Magic Quadrant
companies = [
    "Microsoft", "Salesforce (Tableau)", "Google", "Qlik", "Oracle", "SAP", "ThoughtSpot", 
    "Pyramid Analytics", "MicroStrategy", "Amazon Web Services", "Alibaba Cloud", "Domo", 
    "IBM", "Spotfire", "SAS", "Tellius", "Zoho", "Sisense", "GoodData", "Incorta"
]

x_coords = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.35, 0.4, 0.5, 0.55, 0.45, 0.5, 0.3, 0.25, 0.2, 0.15, 0.1, 0.1, 0.05, 0.15]
y_coords = [0.9, 0.8, 0.75, 0.7, 0.65, 0.5, 0.55, 0.5, 0.6, 0.65, 0.6, 0.65, 0.3, 0.35, 0.3, 0.25, 0.4, 0.35, 0.2, 0.25]

# Define figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
fig.patch.set_facecolor('#232023')
ax.set_facecolor('#232023')

# Plot gridlines for quadrants
ax.axhline(0.5, color='white', linewidth=1)
ax.axvline(0.5, color='white', linewidth=1)

# Add labels for quadrants
ax.text(0.25, 0.75, 'NICHE PLAYERS', fontsize=12, ha='center', color='white')
ax.text(0.75, 0.75, 'CHALLENGERS', fontsize=12, ha='center', color='white')
ax.text(0.25, 0.25, 'VISIONARIES', fontsize=12, ha='center', color='white')
ax.text(0.75, 0.25, 'LEADERS', fontsize=12, ha='center', color='white')

# Plot each company
for company, x, y in zip(companies, x_coords, y_coords):
    ax.scatter(x, y, s=50, color='white', label=company)
    ax.text(x, y, company, fontsize=8, ha='center', va='bottom', color='white')

# Set axis limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("COMPLETENESS OF VISION", color='white')
ax.set_ylabel("ABILITY TO EXECUTE", color='white')

# Title
ax.set_title("Gartner Magic Quadrant - Analytics & BI Platforms (2024)", fontsize=14, color='white')

# Save plot as an image
plt.tight_layout()
plt.savefig('magic_quadrant.png')
plt.show()

# Generate HTML
html_content = f"""
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Gartner Magic Quadrant</title>
</head>
<body>
    <h1>Gartner Magic Quadrant - Analytics & BI Platforms (2024)</h1>
    <img src='magic_quadrant.png' alt='Gartner Magic Quadrant'>
    <p>This chart visualizes the positioning of various analytics and business intelligence platforms based on their ability to execute and completeness of vision.</p>
</body>
</html>
"""

# Save HTML to file
with open("magic_quadrant.html", "w") as file:
    file.write(html_content)
