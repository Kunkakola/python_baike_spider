#html输出器

class UrlOutputer():
    def __init__(self):
        self.datas=[]

    def collect_data(self,data):
        if data==None:
            return 
        self.datas.append(data)

    def output_html(self):
        #输出成html文件,utf-8格式避免乱码
        fout=open('output.html','w',encoding='utf-8')

        fout.write('<html>')
        fout.write('<body>')
        #写成表格的形式,加上边框显示更格式化
        fout.write('<table border=1>')
        for data in self.datas:
            
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            fout.write('<td>%s</td>'%data['title'])
            fout.write('<td>%s</td>'%data['summary'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()