# split a csv to 1000 lines per file
#
import os
import pandas as pd

def split_csv(file_path, chunk_size=1000):
    # read the file
    df = pd.read_csv(file_path)
    file_path = file_path.split('.')[0]
    # get the number of chunks
    num_chunks = len(df) // chunk_size
    # create a directory to store the chunks
    for i in range(num_chunks):
        chunk = df[i*chunk_size:(i+1)*chunk_size]
        chunk.to_csv(f'{file_path}_{i}.csv', index=False)
    # create the last chunk
    chunk = df[num_chunks*chunk_size:]
    chunk.to_csv(f'{file_path}_{num_chunks}.csv', index=False)
split_csv('wikihowAll.csv')