"""
Test goes here

"""

from mylib.query import query


def test_query():
    assert query("SELECT Name FROM GameDB ORDER BY User_Score DESC, Critic_Score DESC LIMIT 2") == [('Name',), ('Super Mario Galaxy 2',)]
    
    pass
def test_extract():
    pass
def test_transform_load():
    pass

