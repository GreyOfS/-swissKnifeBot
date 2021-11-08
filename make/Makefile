all:
	if[dpkg-query -l | gerp screen]
	then
		cp $(ls | grep -v make) /swissKinfeBot
	else
		echo ("\"screen\" package missing")