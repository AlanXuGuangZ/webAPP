'''
Created on 2016-1-15

@author alan
'''
# config_default.py

configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'database': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
           #在一次修改内容，加上这段话，然后提交到git
           #continue  test a test 
}