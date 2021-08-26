import os

os.chdir(r"C:\Users\danza\Python-course")

parent_folder = input('parent_folder: ')
os.mkdir(parent_folder)
os.chdir(os.path.join(r'C:\Users\danza\Python-course', parent_folder))
num_folders = int(input('num_folders?: '))
for i in range(num_folders):
    internal_folder_1 = input('parent_folder: ')
    os.mkdir(internal_folder_1)


