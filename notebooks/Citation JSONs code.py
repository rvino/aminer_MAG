import pandas as pd
import json
import os

from progressbar import ProgressBar
pbar = ProgressBar()

from pandas.io.json import json_normalize #package for flattening json in pandas df 

filename = "C:\Users\clibassi\Downloads\mag_papers_0\mag_papers_0.txt"

with open('C:\Users\clibassi\Downloads\mag_papers_0\mag_papers_0.txt') as file:
    status = []
    for line in file:
        status.append(json.loads(line))
		

dfs = []

len_min_one = len(status)-1 

for df in pbar(range(1, 1000)):
        
    dfs.append(json_normalize(data=status[df], record_path='authors', 
                               meta=['title', 'year', 'n_citation', 'doc_type', 'lang', 'isbn', 'doi', 'id'], errors='ignore'))
    
	
subset_test = [s for s in dfs if s['lang'].iloc[0] == 'en']

len(subset_test)

combined = pd.concat(dfs)

combined