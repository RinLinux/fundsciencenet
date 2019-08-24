# encoding: utf-8

"""
date: 2019/08/23/11/41

"""
import hashlib

def get_md5(url):
    if isinstance(url,str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()