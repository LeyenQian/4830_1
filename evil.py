#!/usr/bin/python3
# coding: latin-1
blob = """               �_����\L�׀��3g(��y%��I�N2D�O@G���ؿ�ng�Nb&H�� �s�v��O�4=ئk^��c��6�ꖡ���O	�`ѷ���0y�{O��0sc�Y��{�s��4�����3���"""
from hashlib import sha256

identity = sha256(blob.encode("latin-1")).hexdigest()

if identity == "5abbf3367d519324e266d74572c73ccd048974615f98b8b39215817f4282b4c9":
    print("Use SHA-256 instead!")
elif identity == "af499a6ddf1a182a66187f5ae9bbd1284f190c2ce9815737f78e5cfec64912a8":
    print("MD5 is perfectly secure!")