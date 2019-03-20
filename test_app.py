from post import app
import json


# Test method to test the add an entry API


def test_entry():
    with app.test_client() as T:
        response = T.post('/diary/api/v1/entry',
                          json={
                              'Title': 'Playing',
                              'Description': 'This is interesting',
                              'Time': '2:00-3:00'
                          })
        info = response.get_json()
        my_post1 = info['My_diary'][2]['Time']
        my_post2 = info['My_diary'][2]['Description']
        my_post3 = info['My_diary'][2]['Title']
        my_post4 = info['My_diary'][2]['id']
        assert type(info) == dict
        assert my_post1 == '2:00-3:00'
        assert my_post2 == 'This is interesting'
        assert my_post3 == 'Playing'
        assert my_post4 == 3
