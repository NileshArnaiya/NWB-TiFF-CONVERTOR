# NWB-TiFF-CONVERTOR
Convertor for NWB(Neural Data without Border) Files to Compatible Tiff Files to be used with various tools like Caiman or DeepLabCut. 
## Overview

This project provides a command line tool for processing Neurodata Without Borders (NWB) files. It includes functionalities to load NWB files, convert them to various formats, and utilize tools for further analysis.

## Features
### 1. Command line utility. 

### 2. Load NWB File

The tool leverages the `pynapple` library to load NWB files. This allows seamless integration with NWB files and provides a foundation for subsequent operations.

### 3. Convert Numpy Array to TIFF

The project supports the conversion of NumPy arrays to TIFF format. This functionality is useful for transforming numerical data into an image format for visualization or analysis.

### 4. Convert TIFF to Workable TIFF using Tiffit

The tool integrates with `tiffit` to convert TIFF files into a workable format. This step ensures that the TIFF files are processed and formatted in a way that is conducive to further analysis.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/NileshArnaiya/NWB-TiFF-CONVERTOR.git
pip install -r requirements.txt

python main.py --input_file your_nwb_file.nwb output_file_name.tiff
or
python main.py --dandiset_id 000582 --file_path sub-10073_ses-17010302_behavior+ecephys.nwb --output_path output_file.tiff

License

This project is licensed under the Creative Commons License - see the LICENSE.md file for details

## Usage

To use the command line tool, follow the steps below:

1. Run the command line tool with the appropriate input parameters.
2. Load the NWB file using `pynapple` or you can load DANDI datasets.
3. Convert NumPy arrays to TIFF files.
4. Utilize `tiffit` to process TIFF files for analysis.
5. Choose the option to convert NWB files to DLC or point to additional tools in the NWB ecosystem.

## Requirements

- Python (version 3.8 and above)
- Additional dependencies in `requirements.txt`


