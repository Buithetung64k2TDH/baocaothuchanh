print('Bui The Tung MSV 235752021610074')
import shutil

def copy_file( A, B):
    shutil.copyfile(A, B)

# Gọi hàm sao chép
copy_file('A.txt', 'B.txt')
