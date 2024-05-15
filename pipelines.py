# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class Myscrapy3Pipeline:
    def __init__(self):
        self.counter = 0
        self.file_number = 0

    def process_item(self, item, spider):

        self.counter += 1

        if self.counter == 31:
            self.close_file()
            self.file_number += 1
            self.counter = 0

        Novel = item['Novel']
        Novel_style = item['Novel_style']
        Author = item['Author']
        Publication_date = item['Publication_date']
        Score = item['Score']
        Read_times = item['Read_times']
        New_page = item['New_page']
        Introduction = item['Introduction']

        print(Novel)
        print(Novel_style)
        print(Author)
        print(Publication_date)
        print(Score)
        print(Read_times)
        print(New_page)
        print(Introduction)

        with open(f'第{self.file_number+1}页.txt','a',encoding='utf-8') as f:
            # file_path = item['Novel']+'.txt'
            # f = open(file_path, "wb")
            f.write('小说名：' + str(Novel) + '\n')
            f.write('小说类型：' + str(Novel_style))
            f.write('作者：' + str(Author) + '\n')
            f.write('出版时间：' + str(Publication_date) + '\n')
            f.write('评分：'+str(Score)+'分'+'\n')
            f.write('总阅读人数：'+str(Read_times)+'\n')
            f.write('最新章节：'+str(New_page)+'\n')
            f.write('简介：' + str(Introduction) + '\n')
            f.write('\n')

        return item

    def close_file(self):
        if hasattr(self,"file") and not self.file_number:
            self.file.close()