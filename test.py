import requests
#while True:
    #sid = int(input('Enter your id of student data'))
    #resp = requests.get(url='http://127.0.0.1:8000/demoapi/firstapi/{0}/'.format(sid))
    #print(resp.json())



try:
    while True:
        sid = int(input('Enter your id of student data'))
        resp = requests.get(url='http://127.0.0.1:8000/demoapi/firstapi/{0}/'.format(sid))
        print(resp.json())
except:
    print("Student not found")
    

    
