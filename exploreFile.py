import pandas as pd

face = pd.read_csv("path_face_file) 
doc = pd.read_csv("path_doc_file)

# if you want to explore the data
face.head() #print the first 10 lines of the file

doc.head() # same for doc document

faceDoc = face.join(doc, lsuffix='user_id', rsuffix='user_id')

# here you can start looking for duplicate attempts and ect...
