# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 08:47:10 2020

@author: Laptop Masstel
"""

"""
thư viện OS
các hàm:
    os.getcwd():trả về thư mục làm việc hiện tại (CWD) của tệp.
    os.error:xác định các lỗi cấp độ hệ điều hành. 
    os.popen():mở một tệp đến hoặc từ lệnh được chỉ định và nó trả về một đối tượng tệp được kết nối với một pipe.
    os.close(): dùng để đóng file.
    os.rename():đổi tên
    os.access():sử dụng uid/gid thực để kiểm tra xem người dùng có quyền truy cập vào đường dẫn hay không.
    os.remove():xóa file or thư mục
     os.mkdir():tạo thư mực mới
"""
  
import os
list1=[]
list2=[]
for (root,dirs,files) in os.walk('C:\\', topdown=True):
    list2 += dirs
    list1 += files
    print(root)
    print(dirs)
    print(files)
    print('--------------------------------')
print('Danh sách tất cả các thư mục:',list2)
print('--------------------------------')
print('Danh sách tất cả các tập tin:',list1)