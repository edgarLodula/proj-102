import os
import shutil

from_dir=r'D:\User\Documents\bijus\python\Projetos\Projeto 102'
to_dir=r'D:\User\Documents\bijus\python\Projetos\Projeto 102\ Arquivos Documentos'

list_of_files= os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    

    if extension=="":
        continue
    if extension in ['.jpg','.png','.jpeg','.gif','.jfif']:
        path1=from_dir+'/'+file_name
        path2=to_dir
        path3=to_dir+'/'+ file_name

        if os.path.exists(path2):
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            shutil.move(path1,path3)    