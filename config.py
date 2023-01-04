import requests
URL ="https://github.com/dobby1725/AIML/blob/main/lab3/lab3.md"
res = requests.get(URL).text
start=‘lablabstart’
end=‘lablabend’
print(res.split(start)[1].split(end)[0])
