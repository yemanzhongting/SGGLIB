from bs4 import BeautifulSoup
import requests
url="http://xxfb.hydroinfo.gov.cn/ssIndex.html"
url2="http://xxfb.hydroinfo.gov.cn/svg/svgwait.jsp?gcxClass=1&gcxKind=1&DateL=2016-01-01&DateM=2016-02-01&gcxData=7&site=宜昌"

header={
#'cookie':'UM_distinctid=1651c5bf8b42d3-0b07e1bd5cf812-514d2f1f-144000-1651c5bf8b54c2; safedog-flow-item=; ASPSESSIONIDSCSQTATD=HHKFNNFBFMMAEJELJCGFHBGF; _pk_ref.1.5dd0=%5B%22%22%2C%22%22%2C1538999793%2C%22http%3A%2F%2Flib.whu.edu.cn%2F%22%5D; _pk_ses.1.5dd0=*; PDS_HANDLE=8102018192328872705688258862055110; _pk_id.1.5dd0=10fd99cd5720f67a.1533010122.50.1538999858.1538999793.; qq%5Flogin%5Fstate=6C23DB96A2F9EAF8585BF8CC0EBF0D07',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
#'Cookie':'wdcid=1a51b59d0f8e9d45; zhuzhan=79852665; JSESSIONID=F9683B8C67612216CE3AFC3C24B72241.tomcat1; wdlast=1539000419',
'Host': 'xxfb.hydroinfo.gov.cn',
'Referer':'http://xxfb.hydroinfo.gov.cn/svg/svghtml.html',
}
#url="http://opac.lib.whu.edu.cn/F/GSFXK41K3MPHTSB5RLTV6VJC55SLYGDL2HLPKUKI7L19SELC2V-22069?func=bor-loan&adm_library=WHU50"
##hdtable > table > tbody
web_data=requests.get(url2,headers=header)
soup=BeautifulSoup(web_data.text,'lxml')
print(web_data)