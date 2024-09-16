This directory contains 2 Python files. 
Supporting py Scripts
|_merge.py
|_delete_extra_Index.py

These Py scripts only needed to run when the main .ipynb file `main_team_qstar_amazon` ran several times targeting different range of images in the test dataset to extract info resulting in more than 1 CSV files.
These 2 py files, create one final CSV solution file for the test.csv dataset.

`merge.py`: It takes prediction from different output CSV files having different indexes and merges it into one CSV file having an index from 0-131287 (Note: test dataset index starts from 0 to 131287) 
`delete_extra_Index.py`: The below index values were not present in original test dataset but when **merge.py** file run then it creates CSV files containing index 0-131287. So this script deletes these indexes.

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
