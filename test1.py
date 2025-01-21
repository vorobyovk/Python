
import requests
import cherrypy
from datetime import datetime
import time
from pywebcopy import save_webpage, save_website
import validators

def webpage (url, folder, name):
	save_webpage(
		url=url,
		project_folder=folder,
		project_name=name,
		bypass_robots=True,
		debug=True,
		open_in_browser=True,
		delay=None,
		threaded=False,
    )

def website(url, folder, name):
	save_website(
		url=url,
		project_folder=folder,
		project_name=name,
		bypass_robots=True,
		debug=True,
		open_in_browser=True,
		delay=None,
		threaded=False,
	)	

start_time=datetime.now()
r = requests.get('https://portal.librus.pl/rodzina/synergia/loguj', auth=('11754603', '!QAZ-2wsx'))
print(r.status_code)
print(datetime.now() - start_time)
#save_website("https://zabbix.storkgroup.com.ua/index.php", "D:/temp/librus-rodzina", "start_time2", True, True, True, None, False)

#url = input("https://synergia.librus.pl/gateway/ms/studentdatapanel/ui/lekcje/plan-lekcji")
url = "https://zabbix.storkgroup.com.ua/index.php"
folder = input("D:/temp/librus-rodzina")
name = input("start_time")
website(url, folder, name)


