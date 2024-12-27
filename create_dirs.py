import os

dirs = ['uploads', 'outputs', 'utils']
for dir in dirs:
    os.makedirs(dir, exist_ok=True)
