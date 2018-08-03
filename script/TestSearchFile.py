import os, glob


folder_path = 'C://Users/Hasher/PycharmProjects/StumpNew/'
for filename in glob.glob(os.path.join(folder_path, '*.html')):
  with open(filename, 'r') as f:
    print(filename)
    last=os.path.basename(filename)
    print(last)
