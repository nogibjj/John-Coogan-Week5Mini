"""
Test goes here

"""

from mylib import extract, query,transform_load


def test_query("SELECT Name FROM GameDB WHERE User_Score = (SELECT MAX(User_Score) FROM GameDB))"):
    
    pass
def test_extract():
    pass
def test_transform_load():
    pass

