import os

list_of_files = os.listdir()
# print(list_of_files)
dict_ = {}
for file_ in list_of_files:
    if file_.endswith('.txt'):
        with open(file_) as f:
            counter = 0
            for line in f:
                counter += 1
            dict_[file_] = counter
print(dict_)

res_file = open('res.txt', 'a')
for file_ in sorted(dict_, key=lambda x: x[1]):
    print(file_)
    info = f'{file_}\n{dict_[file_]}\n'
    res_file.write(info)

    with open(file_, 'r') as text:
        for line in text:
            res_file.write(line)
        print(res_file.write('\n\n'))
res_file.close()
