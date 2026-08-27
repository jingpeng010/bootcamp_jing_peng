## Cleaning Strategy

The data cleaning workflow is implemented in `src/cleaning.py` and includes three reusable functions:

- `fill_missing_median()`: fills missing numeric values with the median of each column. Median imputation is used because it is less sensitive to outliers than the mean.
- `drop_missing()`: removes rows with missing values when those observations are assumed not to be critical to the analysis.
- `normalize_data()`: scales numeric columns using MinMax scaling by default so that numeric features are placed on a comparable scale.

The raw dataset is loaded from `data/raw/`. The cleaning functions are applied in a Jupyter notebook, and the cleaned dataset is saved to `data/processed/`.

The original and cleaned datasets are compared using their shapes, missing-value counts, and summary statistics.

### Assumptions

- Missing numeric values are filled with the median because the median is less sensitive to outliers than the mean.
- Rows with remaining missing values are dropped because they are assumed not to be critical to the analysis.
- Numeric columns are normalized using MinMax scaling so that values are placed on a comparable scale.
- The cleaning functions assume that future datasets have a similar column structure and data types.