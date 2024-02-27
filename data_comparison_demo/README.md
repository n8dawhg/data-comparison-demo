# Datacompy Demo

## Description

The script in main.py creates a datacompy comparison report between two hypothetical sets of data. It's intended for use in a testing/dev environment and for demo purposes only. 

## Usage guide

1. Navigate and Initialize the poetry project & install dependencies
   
``` bash
cd data_comparison_demo
poetry init
poetry install
```

2. Run the script
   
``` bash
poetry shell
python main.py
``` 

5. View the results that can be found in the reports folder.

## Enhancements
- Only general errors are being caught.
- The project is not dockerized.
- Storage optimizations (.parquet VS .CSV files). 
- Handle dynamic file's being read in.
- Additional automations.
