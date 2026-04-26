import pathlib
import glob
class Tree:
    def __init__(self,path="",skip=None):
        if isinstance(skip,str):
            self.skiplist=[skip]
        elif isinstance(skip,(list,tuple)):
            self.skiplist=list(skip)
        else:
            self.skiplist=None
        self.tree(path=path,root=str(pathlib.Path(path).parent))
    def tree(self,path="",layer=0,is_last=False,indent_current=" ",root="",skip=None):
        def replaces(path:str):
            return pathlib.Path(path).name
        if skip is not None:
            effective_skip=skip
        else:
            effective_skip=self.skiplist
        current=replaces(path.split("/")[::-1][0])
        if layer==0:
            print(f"{current}")
        else:
            print(f"{indent_current}{"└── " if is_last else "├── "}{current}")
        paths=[p for p in sorted(glob.glob(path+"/*")) if pathlib.Path(p).is_dir() or pathlib.Path(p).is_file()]
        ps=[p for p in sorted(glob.glob(path+"/.*")) if pathlib.Path(p).is_dir() or pathlib.Path(p).is_file()]
        if ps!=[]:
            for i in ps:
                paths.append(i)
        filtered_paths=[p for p in paths if effective_skip is None or pathlib.Path(p).name not in effective_skip]
        for i,p in enumerate(filtered_paths):
            lens=(i==len(filtered_paths)-1)
            indent_lower=indent_current
            if layer!=0:
                if is_last:
                    indent_lower+="    "
                else:
                    indent_lower+="│   "
            if pathlib.Path(p).is_dir():
                self.tree(p,layer=layer+1,is_last=lens,indent_current=indent_lower,root=root,skip=effective_skip)
            else:
                print(f"{indent_lower}{"└── " if lens else "├── "}{replaces(p.split("/")[::-1][0])}")
class Treetxt:
    def __init__(self,path="",save=None,skip=None):
        if isinstance(skip,str):
            self.skiplist=[skip]
        elif isinstance(skip,(list,tuple)):
            self.skiplist=list(skip)
        else:
            self.skiplist=None
        self.txt=""
        self.tree(path=path,root=str(pathlib.Path(path).parent))
        with open(save,"w",encoding="utf-8") as f:
            f.write(self.txt[:-1])
    def tree(self,path="",layer=0,is_last=False,indent_current=" ",root="",skip=None):
        def replaces(path:str):
            return pathlib.Path(path).name
        if skip is not None:
            effective_skip=skip
        else:
            effective_skip=self.skiplist
        current=replaces(path.split("/")[::-1][0])
        if layer==0:
            self.txt+=f"{current}\n"
        else:
            self.txt+=f"{indent_current}{"└── " if is_last else "├── "}{current}\n"
        paths=[p for p in sorted(glob.glob(path+"/*")) if pathlib.Path(p).is_dir() or pathlib.Path(p).is_file()]
        ps=[p for p in sorted(glob.glob(path+"/.*")) if pathlib.Path(p).is_dir() or pathlib.Path(p).is_file()]
        if ps!=[]:
            for i in ps:
                paths.append(i)
        filtered_paths=[p for p in paths if effective_skip is None or pathlib.Path(p).name not in effective_skip]
        for i,p in enumerate(filtered_paths):
            lens=(i==len(filtered_paths)-1)
            indent_lower=indent_current
            if layer!=0:
                if is_last:
                    indent_lower+="    "
                else:
                    indent_lower+="│   "
            if pathlib.Path(p).is_dir():
                self.tree(p,layer=layer+1,is_last=lens,indent_current=indent_lower,root=root,skip=effective_skip)
            else:
                self.txt+=f"{indent_lower}{"└── " if lens else "├── "}{replaces(p.split("/")[::-1][0])}\n"
if __name__=="__main__":
    paths=input("パスを指定する")
    savepaths=input("テキストファイルの保存先を指定する")
    Tree(paths)
    Treetxt(paths,save=savepaths)