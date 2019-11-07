from bs4 import BeautifulSoup

ventionCMSHtml = open("VentionCMS.html", 'r')
ventionCMS = BeautifulSoup(ventionCMSHtml, 'html.parser')
ventionCMSHtml.close()

techDocHtml = open("README--nov_07_2019--11h41.html", 'r')
techDoc = BeautifulSoup(techDocHtml, 'html.parser')
techDocHtml.close()

for techDocImage in techDoc.find_all('img'):
    
    #find the image tag in the tech docc
    techDocSearchKey = techDocImage['src']
    techDocSearchKey = techDocSearchKey.split("/")[-1]

    #find the amazon Link from the downloaded CMS webpage
    amazonUrl=ventionCMS.find('p', text=techDocSearchKey)
    amazonUrl = amazonUrl.parent.find('button')['data-link']
    amazonUrl = str(amazonUrl)

    techDocImage['src'] = amazonUrl
    
techDocHtml = open("README--nov_07_2019--11h41.html", 'w')
techDocHtml.write(techDoc.prettify("utf-8"))
techDocHtml.close()
ventionCMSHtml.close()