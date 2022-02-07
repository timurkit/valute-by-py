import requests, xml.etree.ElementTree as ET
while 1:
    res=requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    root=ET.fromstring(res)
    print('1 [left valute] = ... [right valute] ')
    left=input('Input num. or alphabet. left code of valute: ')
    right=input('Input num. or alphabet. right code of valute: ')
    if left.isdigit():
        l=0
    else:
        l=1 
    if right.isdigit():
        r=0
    else:
        r=1      
    for valute in root:
        if left.lower()==valute[l].text.lower():
            left_val=(float(valute[4].text.replace(',','.'))/int(valute[2].text),valute[1].text)
            l=4
        if right.lower()==valute[r].text.lower():
            right_val=(float(valute[4].text.replace(',','.'))/int(valute[2].text),valute[1].text)
            r=4
        if l==4 and r==4: break

    try:            
        left_in_right=left_val[0]*(1/right_val[0])
    except NameError:
        print('Something went wrong') 
    else:
        break
print('1',left,'[',left_val[1],']','=',round(left_in_right,4),right,'[',right_val[1],']')
