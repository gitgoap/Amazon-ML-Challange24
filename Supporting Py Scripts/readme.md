# Image Range Merge Scripts

This directory contains two Python files that assist in merging and cleaning CSV files after multiple runs of the main Jupyter Notebook.

## Python Scripts:
- **merge.py**
- **delete_extra_Index.py**

### Overview

These Python scripts are needed only when the main `.ipynb` file (`main_team_qstar_amazon.ipynb`) has been executed several times in batches due to compute limitation, targeting different ranges of images in the test dataset. Multiple executions generate more than one CSV file. These scripts create one final CSV solution file for the `test.csv` dataset.

### Script Details

#### `merge.py`
- **Function**: Merges predictions from multiple output CSV files with different indices into one CSV file. The resulting file contains a continuous index from 0 to 131,287.
- **Note**: The test dataset index ranges from 0 to 131,287.

#### `delete_extra_Index.py`
- **Function**: After running `merge.py`, some indices not present in the original test dataset are added to the merged CSV file. This script deletes those extra indices.

  The indices to be deleted are:

  ```python
  {
      4613, 121862, 33803, 33804, 33805, 25115, 25116, 124444, 124445,
      108082, 108083, 17479, 17480, 3150, 54862, 47185, 18514, 18515,
      104531, 71253, 88676, 119400, 119401, 34922, 19567, 19568, 21619,
      21620, 21621, 127615, 120450, 120451, 127110, 43657, 101003, 64168,
      15540, 15541, 55990, 122084, 69367, 69368, 69369, 15098, 1787, 763,
      1788, 3842, 34057, 120077, 20238, 20239, 16144, 120078, 124692,
      124693, 3864, 3865, 8480, 31018, 31019, 15662, 63792, 120112, 120113,
      2871, 63807, 18752, 64848, 109399, 75610, 75611, 75612, 112480, 121198,
      16751, 121199, 63346, 63347, 24950, 24951, 62330, 66951, 66952, 1950,
      36254, 36255, 10662, 86447, 86448, 89529, 89530, 27580, 129532, 73662,
      128461, 39917, 129531, 58364, 58365, 58366
  }
