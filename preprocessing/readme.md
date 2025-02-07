# Dataset-Specific Preprocessing Scripts

This directory contains Python scripts designed for preprocessing individual datasets used in our project. Each script focuses on a specific dataset, loading its raw data, performing necessary cleaning and transformations, and saving the processed data in a standardized format.  These scripts ensure that each dataset is properly prepared for subsequent analysis and modeling.

## Script Descriptions

The scripts are named after the datasets they process, making it easy to identify their purpose. Common operations performed by these scripts include:

*   **Data Loading:** Reading the raw data from a CSV file.
*   **Data Cleaning:** Handling missing values, removing irrelevant columns, and correcting inconsistencies.
*   **Data Transformation:** Mapping categorical values to binary labels (e.g., 0/1 or "Yes"/"No"), renaming columns for consistency, and creating new columns based on existing ones.
*   **Data Selection:** Selecting relevant columns for the final processed dataset.
*   **Data Saving:** Saving the processed data to a CSV file in a standardized format.

## Usage

To run a script, simply execute it using Python:

```bash
python irf.py
python sdcnl.py
python dreaddit.py
# ... and so on for each dataset.
```