print('Bui The Tung MSV 235752021610074')
def file_read(fname):
    from itertools import islice
    with open(fname, "w",encoding='utf-8') as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())
file_read('abc.txt')