
## Overview

This project processes and manages water quality monitoring data collected from various locations. It handles different types of measurements including:

- Temperature data
- Conductivity data
- Specific conductance data
- Depth data

## Data Processing Workflow

1. Raw data is collected and stored in the `fabric/Raw data/` directory
2. Data is processed through Jupyter notebooks:
   - `wb_new.ipynb`: Main processing workflow
   - `API_test.ipynb`: API integration testing
   - `googleapi.ipynb`: Google API integration

3. Processed data is organized into:
   - Site-specific files
   - Master files
   - Final files ready for upload

## Monitoring Locations

The system processes data from multiple monitoring locations, including:

- ALOU01-04
- ANCI02
- BOLI01-02
- BROT01-06
- COUG01-05
- CLOV01
- CYPR01
- And more...

## File Naming Convention

Files follow this naming pattern:
`[SITE_ID] - [data_type] - DataStream upload - CURRENT-UPDATED VERSION.csv`

Example: `ALOU01 - temp data - DataStream upload - CURRENT-UPDATED VERSION.csv`

## Dependencies

The project requires the following Python packages:
- pandas
- numpy
- glob


## Contact

For questions about this data processing workflow, please contact the repository maintainers at DFO-MPO.

## License

This project is maintained by Fisheries and Oceans Canada (DFO-MPO). All rights reserved.