## Building Histograms

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Guazzihub/Building-histograms
   ```
2. Navigate to the project directory:
   ```bash
   cd Building-histograms
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Add your data to `sample.txt` in the following format:
   ```
   1 2 3 4 5
   6 7 8 9 10
   ```
2. Run the script:
   ```bash
   python Statistics.py
   ```
3. Outputs:
   - **Table**: Displays frequency, cumulative frequency, relative frequency, and midpoints.
   - **Histogram**: Shows a bar chart of the frequency distribution.

### Example Outputs

#### Table Output:
```
Classes (h=5)  Frequency  Cumulative Frequency  Relative Frequency  Midpoint
0-5            4          4                    0.40               2.5
5-10           6          10                   0.60               7.5
```

#### Histogram Output:
A frequency bar chart visualizing the data.
