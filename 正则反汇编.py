import re

with open('save_location.txt','w+') as b_file:    #d:/文本文件/1.txt
        with open('from_location.txt','w+') as a_file:
            pass



def change_and_save(fi,f2):#改变原始文件并写入
    key_ass = r'^\w{4}\s+\w{4}\s{5}(.+)'
    key_c = r'^\w+\D(.+)'

    with open (fi,'r+') as file:
        with open(f2,'w+') as f2:
            for line in file:
                try :
                    result = re.match(key_ass,line)
                    l = result.group(1)
                except:
                        try:
                            result = re.match(key_c,line)
                            l = result.group(1)
                        except:
                            l = line
                f2.write(l+'\n')

def location_of_file():
    with open('save_location.txt','w+') as b_file:    #d:/文本文件/1.txt
        with open('from_location.txt','w+') as a_file:
            save_l = b_file.read()
            from_l = a_file.read()

        change_and_save(from_l,save_l)
'''
def change_slash():
    st =  'C:\\Users\adan\Documents\Tencent Files\1016867898\FileRecv'
    st.replace('\\','/')
    print('%r'%st)
#change_slash()

'''








