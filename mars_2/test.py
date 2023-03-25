from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users/1').json())
print(get('http://localhost:5000/api/v2/users').json())
print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'ewq',
                 'name': 'qwe',
                 'age': '42',
                 'position': '2, 4',
                 'speciality': 'proffessor',
                 'address': '21312',
                 'email': '123@mail.com',
                 'ps': 'asdsa'}).json())

print(delete('http://localhost:5000/api/v2/users/3').json())
print(delete('http://localhost:5000/api/v2/users/100').json())
