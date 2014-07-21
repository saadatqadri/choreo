import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choreo.settings")
from wrench.models import *


if __name__ == "__main__":
    # add a new case
    proj = Project(
        name="NMS 3.0 Upgrade",
        description = 'NMS Upgrade Project, required for compliance'
    )
    proj.save()

    plan = Plan(
        project=proj,
        name="Factory Acceptance Test Plan",
        description = "FAT Tests for NMS Upgrade Project",
    )
    plan.save()

    suite = Suite(
        name="e-terrabrowser SVPP", 
        project=proj,
    )
    suite.save()


    c1 = Case(
        suite = suite,
        title="WebFG client lost connection", 
        description='Previous Test', 
        procedure="Stop WebFGServer Task", 
        expected="Should get a lost connection message.", 
        notes = "No notes",
        clean_up = "Check RUSERVER message."
    )
    c1.save()

    c2 = Case(
        suite = suite,
        title="Display List Builder", 
        description='Testing of this function from the command line is done directly.', 
        procedure="Start up WebFGDirUI by double clicking the file itself.", 
        expected="The following file is created.", 
        notes = "No notes",
        clean_up = "This test is setup for the next one."
    )
    c2.save()


    run = Run(
        name="Regression Test - July", 
        project = proj,
        assigned_to='Linda',
    )
    run.save()



