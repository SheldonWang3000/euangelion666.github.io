import os.path
import datetime
import codecs
time = datetime.datetime.now()
title = "测试脚本2"
filename = '_posts/' + time.strftime("%Y-%m-%d-") + title + ".md"
if not os.path.exists(filename):
    with codecs.open(filename, 'w+', 'utf-8') as f:
        f.write('---\n')
        f.write('layout: post\n')
        f.write('title: ' + title + '\n')
        f.write('date: ' + time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
        f.write('summary: \n')
        f.write('categories: jekyll\n')
        f.write('thumbnail: jekyll\n')
        f.write('tags:\n')
        f.write(' - \n')
        f.write('---\n')
        f.close()
    print("Generate new posts done")
else:
    print("Error: File exists!!")

# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
