from os import PathLike
from typing import Literal
class Tree:
    def __init__(
self,
path:str=...,
skip:str|list|tuple|None=None
)->None:
        """ドライブ内のパスまたはディスクのディレクトリ構造を表示する
        
        :param path: ディレクトリ構造を表示するディレクトリを指定する。
        :type path: str
        :param skip: 表示しないファイルとフォルダ名を指定する。
        :type skip: str|list|tuple|None"""
class Treetxt:
    def __init__(
self,
path:str=...,
save:str=...,
skip:str|list|tuple|None=None
)->None:
        """ドライブ内のパスまたはディスクのディレクトリ構造をテキストファイルで保存する。

        :param path: ディレクトリ構造を表示するディレクトリを指定する。
        :type path: str
        :param save: 保存するテキストファイルのファイルパスを指定する。
        :type save: str
        :param skip: 表示しないファイル名とフォルダ名を指定する。
        :type skip: str|list|tuple|None"""