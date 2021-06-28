#!/usr/bin/python3

import subprocess
import cgi

print("content-type: text/html")
print()
#add admin.conf file
#append --kubeconfig admin.conf after every cmd
f=cgi.FieldStorage()
cmd=f.getvalue("x")
if "get" in cmd or "show" in cmd or "Show" in cmd or "Get" in cmd or "GET" in cmd or "SHOW" in cmd:
	if "pod" in cmd or "pods" in cmd or "Pod" in cmd or "Pods" in cmd:
		print(subprocess.getoutput("sudo kubectl get pods --kubeconfig admin.conf")) 
	elif "svc" in cmd or "SVC" in cmd or "Svc" in cmd:
		print(subprocess.getoutput("sudo kubectl get svc --kubeconfig admin.conf"))
	else:
		print(subprocess.getoutput("sudo kubectl get deployments --kubeconfig admin.conf"))
elif "describe" in cmd or "DESCRIBE" in cmd or "Describe" in cmd:
	print(subprocess.getoutput("sudo kubectl describe pods --kubeconfig admin.conf"))
else:
	print(subprocess.getoutput("sudo "+cmd+" --kubeconfig admin.conf"))
#print(subprocess.getoutput("sudo "+cmd+" --kubeconfig admin.conf"))
