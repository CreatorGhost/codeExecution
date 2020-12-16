import requests
import time
import sys
url = "https://ide.geeksforgeeks.org/main.php"

languages={
    '1':'c',
    '2': 'cpp',
    '3': 'Java',
    '4':'Python3'
}
lan=input('press 1 for c 2 for c++ 3 for java 4 for python : ')

print("Please enter your code in ",languages[lan],"\n")

code = sys.stdin.readlines()
code="".join(code)

data = {
    'lang': languages[lan],
    'code': code,
    'input': '',
    'save': True
}

r = requests.post(url, data=data)
firstResponse=r.json()

if 'message' in firstResponse:
    print(firstResponse['message'])
    exit()

sid=firstResponse['sid']

codeData={
    'sid': sid,
    'requestType': 'fetchResults'
}
print("Waiting for our code to be executed...")
time.sleep(5)
codeOutputUrl='https://ide.geeksforgeeks.org/submissionResult.php'
re=requests.post(codeOutputUrl, data=codeData)
result=re.json()


if 'output' in result:
    print("The output of your code is: ",result['output'])
elif 'cmpError' in result:
    print("There is an error in your code \n",result['cmpError'])
elif 'rntError'in result:
    print("There is an error in your code \n",result['rntError'])
