




Backlog

Add plans to project (1 hr)


Views plans in project (1 hr)
View suites in project (1 hr)
View cases in suite ( 1 hr)

Done




# refactor wrench models for test steps and expected results

# Project model: num_test_runs, assigned_to_user, test_runs_in_progress, test_plans, recent_activity

# Plan model: date_created, last_updated, associated_test_suites, description
# Suite model: date_created, last_updated, num_test_cases, associated_test_plan
# Run model: cases_no_run, cases_passed, cases_failed, cases_skipped

# runs should have a foreignkey relationship with Suite not Plan

# write tests steps in markdown

# add images to every step

# case versioning true by default

# url design: 

*done hydroone.wrenchapp.com --> projects ListView
*done hydroone.wrenchapp.com/projects/10202/ --> dashboard/overview project DetailView
*done hydroone.wrenchapp.com/projects/10202/plans --> testing plans ListView
hydroone.wrenchapp.com/projects/10202/suites --> testing suites ListView
hydroone.wrenchapp.com/projects/10202/suites/4343 --> testing suites DetailView
hydroone.wrenchapp.com/projects/10202/runs --> testing runs ListView
hydroone.wrenchapp.com/projects/10202/runs/23434 --> testing runs DetailView
hydroone.wrenchapp.com/projects/10201/suites/27125/cases/new


Each team has its own workflow.
Product Manager/Owner responsible for creating project structure
Developers responsible for documenting tests

