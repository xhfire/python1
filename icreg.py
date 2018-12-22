import requests

def testic():
    url = 'http://www.ic.net.cn/ictest/demo.php'


    res = requests.post(url)

    print (res)

if __name__=='__main__':

    for n in range(0,1000):
        testic()
