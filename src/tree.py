import pathlib
import glob
import os
class Tree:
    def __init__(self,path="",reference=True,skip=None):
        if path=="" or not pathlib.Path(path).is_absolute():
            raise FileNotFoundError("パスが見つかりません")
        if isinstance(skip,str):
            self.skiplist=[skip]
        elif isinstance(skip,(list,tuple)):
            self.skiplist=list(skip)
        else:
            self.skiplist=None
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
    def tree(self,path="",layer=0,is_last=False,indent_current=" ",reference=True,root="",skip=None):
        def replaces(path:str):
            if reference:
                path=pathlib.Path(path).name
            return path
        if skip is not None:
            effective_skip=skip
        else:
            effective_skip=self.skiplist
        current=replaces(path.split("/")[::-1][0])
        if layer==0:
            print(current)
        else:
            print(f"{indent_current}{"└── " if is_last else "├── "}{current}")
        paths=[p for p in glob.glob(path+"/*") if os.path.isdir(p) or os.path.isfile(p)]
        filtered_paths=[p for p in paths if effective_skip is None or pathlib.Path(p).name not in effective_skip]
        for i,p in enumerate(filtered_paths):
            lens=(i==len(filtered_paths)-1)
            indent_lower=indent_current
            if layer!=0:
                if is_last:
                    indent_lower+="    "
                else:
                    indent_lower+="│   "
            if os.path.isfile(p):
                print(f"{indent_lower}{'└── ' if lens else '├── '}{replaces(p.split('/')[::-1][0])}")
            if os.path.isdir(p):
                self.tree(p,layer=layer+1,is_last=lens,indent_current=indent_lower,reference=reference,root=root,skip=effective_skip)
class Treetxt:
    def __init__(self,path="",reference=True,save=None,skip=None):
        if path=="" or not pathlib.Path(path).is_absolute():
            raise FileNotFoundError("パスが見つかりません")
        if isinstance(skip,str):
            self.skiplist=[skip]
        elif isinstance(skip,(list,tuple)):
            self.skiplist=list(skip)
        else:
            self.skiplist=None
        if not isinstance(save,str) or not os.path.isdir(save):
            save=os.path.join(os.path.dirname(os.path.abspath(__file__)),"tree.txt")
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
        with open(save,"w",encoding="utf-8") as f:
            f.write(self.txt)
    def tree(self,path="",layer=0,is_last=False,indent_current=" ",reference=True,root="",skip=None):
        def replaces(path:str):
            if reference:
                path=pathlib.Path(path).name
            return path
        if skip is not None:
            effective_skip=skip
        else:
            effective_skip=self.skiplist
        current=replaces(path.split("/")[::-1][0])
        if layer==0:
            self.txt+=f"{current}\n"
        else:
            self.txt+=f"{indent_current}{"└── " if is_last else "├── "}{current}\n"
        paths=[p for p in glob.glob(path+"/*") if os.path.isdir(p) or os.path.isfile(p)]
        filtered_paths=[p for p in paths if effective_skip is None or pathlib.Path(p).name not in effective_skip]
        for i,p in enumerate(filtered_paths):
            lens=(i==len(filtered_paths)-1)
            indent_lower=indent_current
            if layer!=0:
                if is_last:
                    indent_lower+="    "
                else:
                    indent_lower+="│   "
            if os.path.isfile(p):
                self.txt+=f"{indent_lower}{'└── ' if lens else '├── '}{replaces(p.split('/')[::-1][0])}\n"
            if os.path.isdir(p):
                self.tree(p,layer=layer+1,is_last=lens,indent_current=indent_lower,reference=reference,root=root,skip=effective_skip)
if __name__=="__main__":
    paths=input("パスを指定する")
    savepaths=input("テキストファイルの保存先を指定する")
    Tree(paths)
    Treetxt(paths,save=savepaths)