from subprocess import call

def start_cluster(host, Nengines):
	call("ssh -f {0} \"bash -tlc 'ipcluster start -n {1}'\"".format(host, Nengines), shell=True)

def shutdown_cluster(host, client):
	client.shutdown(hub=True)
	call("ssh -f {0} \"bash -tlc 'ipcluster stop'\"".format(host), shell=True)
	call("ssh -f {0} \"bash -tlc 'pkill -u dtamayo'\"".format(host), shell=True)

bubbles = {'ipython_dir':'/cita/d/sunny-home/dtamayo/.ipython', 'sshserver':'bubbles'}
ricky = {'ipython_dir':'/cita/d/sunny-home/dtamayo/.ipython', 'sshserver':'ricky'}
homard = {'sshserver':'homard'}
lobster = {'sshserver':'lobster'}
kingcrab = {'sshserver':'kingcrab'}
prawn = {'sshserver':'prawn'}
trinity = {'sshserver':'trinity'}
