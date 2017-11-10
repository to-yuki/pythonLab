import psutil
from naoqi import ALProxy

naoIP = 'nao.local'
naoPORT = 9559
try:
	log = ALProxy("ALLogger", naoIP, naoPORT)
	log.info("python","[Hello from Real NAO]")
except RuntimeError:
		for proc in psutil.process_iter():
			try:
				pinfo = proc.as_dict(attrs=['pid', 'name', 'status'])
			except psutil.NoSuchProcess:
				pass
			else:
				if pinfo['name'] == 'naoqi-bin.exe':
					naopid = pinfo['pid']

		naoIP = psutil.Process(naopid).connections()[0][3][0]
		naoPORT = psutil.Process(naopid).connections()[0][3][1]

		log = ALProxy("ALLogger", naoIP, naoPORT)
		log.info("python","[Hello from Simulated NAO]")
