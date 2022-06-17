#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd 
import numpy as np
import re

max_followers = 5000
min_followers = 100
head = 0
file = "replace_with_csv_file_path"

df = pd.read_csv(file, header = head)
df.columns = ["name", "bio", "username", "followers"]
df = df.loc[df["followers"] < max_followers]
df = df[df["bio"].notna()]
df = df[df["followers"] > min_followers]

hs_query = 'qa|nchs|ice|ahs|south division 21’|whitney 2020|ccat|carver|ascs|bdhs|kchs|cuyahoga falls|oak hill|high school|highschool|mshs|ajhs|battle mountain|avhs|eleanor roosevelt high'
highschool = df[df['bio'].str.contains(query, flags = re.IGNORECASE)]

college_query = 'university|jhu|college|john hopkins|stanford|mit|cmu|university of maryland|goucher|Frostburg|gt|purdue|florida state|jmu|Dsu|morgan state|upenn|penn state|hopkins|ic|isu|ksu|lmu|mcla|2021🎓|niu|occ|rwu|full sail|tamu|uchicago|U of C|virginia tech|xavier|yale|rit|george mason|temple|florida tech|cal poly|C’O 19|berkeley'
university = df[df['bio'].str.contains(college_query, flags=re.IGNORECASE)]

year_query = 'c"\\"o2021|\'21|‘21|co21|c"\\"o21|c"\\"o2020|\'20|co20|‘20|c"\\"o20|c"\\"o2019|‘19|\'19|co19|c"\\"o19|c"\\"o2018|‘18|\'18|co18|c"\\"o18|c"\\"o2017|\'17|‘17|co17|c"\\"o17'
year = df[df['bio'].str.contains(year_query, flags=re.IGNORECASE)]


private_query = 'sspp'
private = df[df['bio'].str.contains(private_query, flags=re.IGNORECASE)]

all_valid_students = year.append([university,highschool,private])
all_valid_students = all_valid_students.drop_duplicates()

public_students = highschool.append(year)
delete_query = 'c"\\"o2022|‘22|22|22\'|22”|\'22|2022|co22|22\"|c"\\"o22|c"\\"o2023|23”|23\'|‘23|23|\'23|co23|2023|c"\\"o23|23\"|c"\\"o2024|‘24|24\'|24|24”|\'24|co24|2024|c"\\"o24|es|elementary school|elementary|ms|middle school'
public_students = public_students[~public_students['bio'].str.contains(delete_query, flags=re.IGNORECASE)]
public_students = public_students.drop_duplicates()

delete = df[~df.isin(all_valid_students)].dropna()

directory = 'instagram query'
file = 'output.xlsx'

if not os.path.exists(directory): 
    os.makedirs(directory)
path = os.path.join(directory, file)

with pd.ExcelWriter(path) as writer: 
    delete.to_excel(writer, sheet_name = 'delete', index = False, header = True)
    private.to_excel(writer, sheet_name = 'private', index = False, header = True)
    public_students.to_excel(writer, sheet_name = 'public_students', index = False, header = True)
    university.to_excel(writer, sheet_name = 'university', index = False, header = True)
    all_valid_students.to_excel(writer, sheet_name = 'all_valid', index = False, header = True)

