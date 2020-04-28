import requests,threading
print(''' 
 ____       ____       ____   _          
|  _ \  ___|  _ \ __ _|  _ \ / \   __  __
| |_) ||_  / |_) / _` | |_) / _ \  \ \/ /
|  _ <  / /|  __/ (_| |  __/ ___ \  >  < 
|_| \_\/___|_|   \__,_|_| /_/   \_\/_/\_\

''')
fname_s=input("Enter Site File Name: ")
fadm=['admin','manager','user','login'] # You can Increase Your List

found=open("Admined.txt","w+")
wpf=open("wpf.txt","w+")
def adminf(e):
    e=e.rstrip()
    if e[0:8]=="https://" or e[0:7]=="http://":
        url=e
    else:
        url="https://"+e
    if url[-1]=='/':
        url=url
    else:
        url=url+'/'
    for adm in fadm:
        urla=url+adm
        print('\nGoing For url: '+urla)
        try:
            r=requests.get(urla)
            co=r.content
            if r.status_code==200:
                print('\t[+] Admin FOund at: '+urla)
                if 'wp-admin' in str(co):
                    print('\t[+] Wp site: '+urla)
                    wpf.write('[+]WP: '+urla+'\n')
                    break
                else: 
                    found.write("\t[+] Admin : "+urla+'\n')
                    break
            else:
                print('[-] Admin Not Found At: '+urla) 
        except: 
            print('[-]Invalid Link: '+urla)
        

def th(num,link):
    index = links.index(link)
    threads=[]
    try:
        for i in range(num):
            t=threading.Thread(target=adminf,args=[links[index+i]])
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
    except:
        pass


with open(fname_s, 'r') as inp:
    links = list(set([x.rstrip() for x in inp.readlines()]))
    threads = 30
    for a in links[::threads]:
        th(threads, a)
wpf.close()
found.close()