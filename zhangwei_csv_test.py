import pandas as pd
import numpy as np
import random

excel_file = '1.xlsx'
star_standard_file = '2.xlsx'

class find_points :
    def __init__(self):
        self.datas = pd.read_excel(star_standard_file)
        self.datas= self.datas.fillna(0)
        self.name_list = []
        self.star_dict = {}
        self.point_list = []
        self.df = pd.DataFrame(self.datas)
        self.df1=pd.read_excel(excel_file)
        self.df2 = pd.DataFrame(self.df1)
        self.get_stars_dict()
        self.find_line()
        self.give_points_to_review_headline()


    def write_into_xlsx(self):
        self.df2['point']=self.point_list
        #print(self.df2)
        self.df2.to_excel(excel_file,index=None)
        print("done")

    def give_points_to_review_headline(self):
        for sentence in self.review_headline_list:
            try:
                if_find = False
                sentence = sentence.lower()
            except:
                print('nothing')
                sentence="giao"
            for keyword in self.name_list:
                if keyword in sentence :
                    if_find = True
                    point = self.make_point(keyword)
                    break
            if not if_find:
                point = 0
            self.point_list.append(point)
        print(len(self.point_list))


    def make_point(self,keyword):
        list_point = self.star_dict[keyword]
        point = 5
        random_num  = random.random()
        for i in list_point:
            if i>0 :
                if random_num-i<0:
                    point = point
                    break
                else:
                    point=point-1
                    break
            point-=1
        return point
    def find_line(self):
        coordinate = 0

        # df = pd.read_excel(excel_file)

        self.review_headline_list= self.df2[['review_headline']].values.T.tolist()[:][0]
        #print(self.review_headline_list)

    #find_line()
    def get_stars_dict(self):

        star_name = self.datas.columns
        for i in range(0,len(star_name)):
            self.name_list.append(star_name[i])
        self.star_dict = self.df.to_dict(orient='list')
        #print(self.name_list)

a= find_points()
a.write_into_xlsx()
#a.get_stars_dict()
#a.find_line()
