# instagram-query
Designed using Juypter Notebook in order to filter and query different users based on the schools they are currently enrolled into. Allows for the user to insert a .csv file that contains name, biography, username, and followers count data resepctively. 

## Usage
Replace and insert your own .csv file. Take note that python doesn't recongize backwards slash. 
```python
max_followers = 10000
min_followers = 100
head = 0
file = "replace_with_csv_file_path"
```

The program will use specific queries in order to export an output.xlsx file that contains all of the query information. Edit any of the following queries to match personal usages. 

```python

# list of queries for high schools 
hs_query = 'ccat|carver|ascs|bdhs|kchs|cuyahoga falls|oak hill|high school|highschool|mshs|ajhs|battle mountain|avhs|eleanor roosevelt high'

# lists of queries for colleges 
college_query = 'goucher|Frostburg|gt|purdue|florida state|jmu|ic|isu|ksu|lmu|mcla|2021🎓|niu|occ|rwu|uchicago|U of C|virginia tech|xavier|yale|rit'

# list of queries for years
year_query = 'c"\\"o2021|\'21|‘21|co21|c"\\"o21|co20|‘20|c"\\"o20|c"\\"o2019|‘19||c"\\"o19|c"\\"o2018|‘18|\'18|c"\\"o2017|\'17|‘17|co17'
```

Change the directory of the output file by editing the `directory` to be the absolute path of where you want the file to be exported. 

```python
directory = 'instagram query'
file = 'output.xlsx'

if not os.path.exists(directory): 
    os.makedirs(directory)
path = os.path.join(directory, file)
```
