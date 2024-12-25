import math
import os
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# File paths
INSTRUCTIONS_FILE = 'instructions.txt'
SAMPLE_FILE = 'sample.txt'

# Helper function to read files
def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return None

# Display instructions
instructions = read_file(INSTRUCTIONS_FILE)
if instructions:
    print(instructions)
    input("Press Enter to continue...")

# Load sample data
sample_data = read_file(SAMPLE_FILE)
if not sample_data:
    exit()

# Convert sample data to a list of integers
default = [int(num) for line in sample_data.splitlines() for num in line.strip().split()]

# Calculate statistics
k = round(math.sqrt(len(default)))
default_min = min(default)
default_max = max(default)
range_ = default_max - default_min
h = math.ceil(range_ / k)

# Generate class intervals
classes = []
current = default_min
while current < default_max:
    classes.append(current)
    current += h
classes.append(current)

# Initialize frequency lists
frequency = []
cumulative_frequency = []
relative_frequency = []
cumulative_relative_frequency = []
midpoints = []

# Calculate frequencies
cumulative = 0
for i in range(len(classes) - 1):
    lower, upper = classes[i], classes[i + 1]
    freq = sum(lower <= val < upper for val in default)
    cumulative += freq

    frequency.append(freq)
    cumulative_frequency.append(cumulative)
    relative_frequency.append(round(freq / len(default), 2))
    cumulative_relative_frequency.append(round(cumulative / len(default), 2))
    midpoints.append((lower + upper) / 2)

# Create table using Plotly
fig = go.Figure(data=[
    go.Table(
        header=dict(
            values=[
                f'Classes (h={h})', 'Frequency', 'Cumulative Frequency',
                'Relative Frequency', 'Cumulative Relative Frequency', 'Midpoint'
            ],
            fill_color='#D1E8D9',
            align='center'
        ),
        cells=dict(
            values=[
                [f"{classes[i]}-{classes[i + 1]}" for i in range(len(classes) - 1)],
                frequency,
                cumulative_frequency,
                relative_frequency,
                cumulative_relative_frequency,
                midpoints
            ],
            fill_color='#FFFAE6',
            align='center'
        )
    )
])
fig.update_layout(width=1200, height=600)
fig.show()

# Plot histogram
plt.figure()
plt.bar(
    [f"{classes[i]}-{classes[i + 1]}" for i in range(len(classes) - 1)],
    frequency, color='#ff5349'
)
plt.title('Frequency Histogram')
plt.xlabel('Classes')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Print sorted data
print("Sorted Data:", sorted(default))
