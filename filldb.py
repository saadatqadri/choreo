import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choreo.settings")
from wrench.models import *


if __name__ == "__main__":
	# add a new case
	
	proj = Project(name="NMS 3.0 Upgrade")
	proj.save()

	plan = Plan(name="Regression Test Plan", project=proj)
	plan.save()

	suite = Suite(name="e-terrabrowser", plan=plan)
	suite.save()

	run = Run(name="July Test Run", plan=plan, assigned_to='Linda')
	run.save()

	c = Case(title="WebFG client lost connection", description='Previous Test', procedure="Stop WebFGServer Task", expected="Should get a lost connection message.", suite=suite)
	c.save()


	


