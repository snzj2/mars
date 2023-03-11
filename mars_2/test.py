from requests import get, post, delete

print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/jobs/2').json())

print(get('http://localhost:5000/api/jobs/asd').json())


print(post('http://localhost:5000/api/jobs',
           json={'team_leader': '5',
                 'job': 'work',
                 'work_size': 'hours',
                 'collaborators': "asd",
                 'is_finished': False}).json())

print(delete('http://localhost:5000/api/jobs/3').json())
