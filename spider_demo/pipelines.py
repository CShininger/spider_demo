import openpyxl
import pymysql

class SpiderDemoPipeline:
    def __init__(self):
        self.wb=openpyxl.Workbook()
        self.ws=self.wb.active
        self.ws.title='Top250'
        self.ws.append(('标题','评分','主题','时长','简介'))
    def open_spider(self, spider):
        pass
    def close_spider(self, spider):
        self.wb.save('电影数据.xlsx')
    def process_item(self, item, spider):
        title=item.get('title','')
        rank=item.get('rank','')
        subject=item.get('subject','')
        duration = item.get('duration', '')
        intro = item.get('intro', '')
        self.ws.append((title,rank,subject,duration,intro))
        return item

class DbPipeline:
    def __init__(self):
        self.conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='spider',charset='utf8mb4')
        self.cursor=self.conn.cursor()
        self.data=[]
    def open_spider(self, spider):
        pass
    def close_spider(self, spider):
        if len(self.data)>0:
            self._write_to_db()
        self.conn.close()
    def process_item(self, item, spider):
        title=item.get('title','')
        rank=item.get('rank',0)
        subject=item.get('subject','')
        duration = item.get('duration', '')
        intro = item.get('intro', '')
        self.data.append((title,rank,subject,duration,intro))
        if len(self.data)==100:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into tb_top_movie(title,rating,subject,duration,intro) values (%s,%s,%s,%s,%s)',
            self.data
        )
        self.conn.commit()
