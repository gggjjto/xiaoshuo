import requests
from bs4 import BeautifulSoup

fileName = 'output.md'
fileDir = 'my_site/docs/doc1/abc/'
url = 'https://m.qiubiquge.com'
next = '/ml/97953/2885453.html'
bookName = '# 仙人消失之后\n'
response = requests.get(url + next)
title = '1'

def Output(data) :
    with open(fileDir+fileName, 'a', encoding='utf-8') as file:
        if PingBi(data) == 1 :
            file.write(data + '\n')

def XiePeZhi(data) :
    pezhiFile = 'my_site/docs/doc1/sidebar.yaml'
    shuju = '-   label: ' + data + '\n' + '    file: abc/' + data + '.md\n'
    with open(pezhiFile, 'a', encoding='utf-8') as file:
        file.write(shuju)

def PingBi(data) :
    pingbi = ['请点击下一页继续阅读',
              '喜欢仙人消失之后请大家收藏：(m.qiubiquge.com)仙人消失之后笔趣阁更新速度全网最快。',
              '如果点击翻页总是进入广告，请刷新页面后重试。']
    
    for a in pingbi :
        if data.find(a) >= 0:
            return 0
    return 1

def main() :
    while(1):
        if response.status_code == 200:
            # 使用 BeautifulSoup 解析 HTML 内容
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 在这里你可以使用 BeautifulSoup 提供的方法来提取你需要的信息
            titleTemp = soup.find('body').get('article-name')
            paragraphs = soup.find_all('p')
            next = soup.find(id = 'pt_next').get('href')

            # 提取标题
            if title != titleTemp :
                title = titleTemp
                fileName = title + '.md'
                Output(bookName)
                XiePeZhi(title)
                print(title)
                Output('## ' + title + '\n')
            # 正文
            for p in paragraphs:
                Output(p.text)
            # 下一页
            response = requests.get(url + next);

            if next.find('ml') < 0 :
                break
        else:
            print('请求失败:', response.status_code)
            break

def main1() :
    print("1")

if __name__ == "__main__" :
    main1()
