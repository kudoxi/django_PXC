from SecondhandsCar.celery import app
from time import sleep
@app.task
def start_running(nums):
  print('***>%s<***' %nums)
  print('--->>开始执行任务<<---')
  for i in range(10):
    print('>>'*(i+1))
    sleep(1)
  print('>---任务结束---<')