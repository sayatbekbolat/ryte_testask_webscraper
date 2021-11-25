import os

import pandas as pd
import numpy as np
import tqdm


# df1 = pd.DataFrame(
#     {
#         'id':[1,2,3,4],
#         'name':['Tom', 'Jenny', 'James', 'Dan']
#     }
# )

# df1.to_csv('test_data/info1.csv', index=None)

# df2 = pd.DataFrame(
#     {
#         'id':[2,3,4,5],
#         'age':[31, 20, 40, 70],
#         'sex':['F', 'M', 'M', 'F']
#     }
# )

# df2.to_csv('test_data/info2.csv', index=None)

if __name__ == "__main__":
    test_data_dir = 'test_data'
    output_dir = 'results'

    file1 = input("The first file path - ")
    if os.path.exists(os.path.join(test_data_dir, file1)) or (len(file1)<0):
        file1 = os.path.join(test_data_dir, 'info1.csv')

    file2 = input('The second file path - ')
    if os.path.exists(os.path.join(test_data_dir, file2)) or (len(file2)<0):
        file2 = os.path.join(test_data_dir, 'info2.csv')

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df = df1.merge(df2, how='inner', on='id').sort_values(['age'])
    df.to_csv(os.path.join(output_dir, 'customer_full_info.csv'), index=None)