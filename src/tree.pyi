from os import PathLike
from typing import Literal
class Tree:
    def __init__(
self,
path:str|PathLike[str]=...,
reference:bool|Literal["relative","absolute"]=...
):
        """ドライブ内のパスまたはディスクのディレクトリ構造を表示する
        
        :param path: ディレクトリ構造を表示するディレクトリを指定する。
        :type path: str|PathLike[str]
        :param reference: 絶対パスで表示するか相対パスで表示するか指定する。
        :type reference: bool|Literal["relative","absolute"]"""
class Treetxt:
    def __init__(
self,
path:str|PathLike[str]=...,
reference:bool|Literal["relative","absolute"]=...
):
        """ドライブ内のパスまたはディスクのディレクトリ構造をテキストファイルで保存する。

        :param path: ディレクトリ構造を表示するディレクトリを指定する。
        :type path: str|PathLike[str]
        :param reference: 絶対パスで表示するか相対パスで表示するか指定する。
        :type reference: bool|Literal["relative","absolute"]"""