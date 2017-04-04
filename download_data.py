import urllib
import os

datasets = ['https://data.cityofnewyork.us/api/views/erm2-nwe9/rows.csv?accessType=DOWNLOAD', \
           'https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/mappluto_14v2.zip']
directories = ['data_initial/complaints.csv', 'data_initial/mappluto_14v2.zip']
for i, j in enumerate(directories):
    if not os.path.exists(j):
        urllib.urlretrieve(datasets[i], directories[i])
    else:
        pass