import time
import subprocess
try:
	start_file = open("startup.csv")
	#InfoLoc = start_file.readline().split(',')
	#enter mosquitto
	#startup = subprocess.Popen("mosquitto_sub --cert " + InfoLoc[0] + " --key " + InfoLoc[1] + " --cafile " + 
	#			   InfoLoc[2] + " -t 'owntracks/#' -h " + InfoLoc[3] + " -p " + InfoLoc[4] , stdout=subprocess.PIPE)

	start_file.close()

	while True:
		process = subprocess.Popen("tail -n 1 data/output", stdout=subprocess.PIPE)
		output = process.communicate()[0]

		data_list = str(output)
		data_list = data_list.split(',')

except KeyboardInterrupt:
	#Exit mosquitto 
        print("EXIT")
