import pathlib
import glob
import os
class Tree:
    def __init__(self,path="",reference=True):
        if path=="" or not pathlib.Path(path).is_absolute():
            raise FileNotFoundError("パスが見つかりません")
        if isinstance(reference,str):
            if reference=="absolute":
                self.reference=False
            else:
                self.reference=True
        elif isinstance(reference,bool):
            self.reference=reference
        else:
            self.reference=False
        self.tree(path,reference=self.reference,root=str(pathlib.Path(path).parent))
    def tree(self,path="",layer=0,is_last=False,indent_current=" ",reference=True,root=""):
        def replaces(path:str):
            if reference:
                path=pathlib.Path(path).name
            return path
        current=replaces(path.split("/")[::-1][0])
        if layer==0:
            print(current)
        else:
            print("{indent}{branch}{dirname}".format(indent=indent_current,branch="└── " if is_last else "├── ",dirname=current))
        paths=[p for p in glob.glob(path+"/*") if os.path.isdir(p) or os.path.isfile(p)]
        def is_last_path(i):
            return i==len(paths)-1
        for i,p in enumerate(paths):
            indent_lower=indent_current
            if layer!=0:
                if is_last:
                    indent_lower+="    "
                else:
                    indent_lower+="│   "
            if os.path.isfile(p):
                print("{indent}{branch}{filename}".format(indent=indent_lower,branch="└── " if is_last_path(i) else "├── ",filename=replaces(p.split("/")[::-1][0])))
            if os.path.isdir(p):
                self.tree(p,layer=layer+1,is_last=is_last_path(i),indent_current=indent_lower,reference=reference,root=root)
class Treetxt:
    def __init__(self,path="",reference=True):
        if path=="" or not pathlib.Path(path).is_absolute():
            raise FileNotFoundError("パスが見つかりません")
        if isinstance(reference,str):
            if reference=="absolute":
                self.reference=False
            else:
                self.reference=True
        elif isinstance(reference,bool):
            self.reference=reference
        else:
            self.reference=False
        self.txt=""
        self.tree(path=path,reference=self.reference,root=str(pathlib.Path(path).parent))
        with open(f"{os.path.dirname(__file__)}/tree.txt","w",encoding="utf-8") as f:
            f.write(self.txt)
    def tree(self,path="",layer=0,is_last=False,indent_current=" ",reference=True,root=""):
        def replaces(path:str):
            if reference:
                path=pathlib.Path(path).name
            return path
        current=replaces(path.split("/")[::-1][0])
        if layer==0:
            self.txt+=f"{current}\n"
        else:
            self.txt+=f"{"{indent}{branch}{dirname}".format(indent=indent_current,branch="└── " if is_last else "├── ",dirname=current)}\n"
        paths=[p for p in glob.glob(path+"/*") if os.path.isdir(p) or os.path.isfile(p)]
        def is_last_path(i):
            return i==len(paths)-1
        for i,p in enumerate(paths):
            indent_lower=indent_current
            if layer!=0:
                if is_last:
                    indent_lower+="    "
                else:
                    indent_lower+="│   "
            if os.path.isfile(p):
                self.txt+=f"{"{indent}{branch}{filename}".format(indent=indent_lower,branch="└── " if is_last_path(i) else "├── ",filename=replaces(p.split("/")[::-1][0]))}\n"
            if os.path.isdir(p):
                self.tree(p,layer=layer+1,is_last=is_last_path(i),indent_current=indent_lower,reference=reference,root=root)
if __name__=="__main__":
    paths=input("パスを指定する。")
    Tree(paths)
    Treetxt(paths)