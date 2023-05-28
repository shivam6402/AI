def job_schedule(jobs) :
	jobs.sort(key = lambda x: x[2]/x[1] , reverse = True)
	schedule =  [-1]* max(jobs, key = lambda x : x[1])[1]
	scheduled_jobs = set()
	
	for job in jobs :
		deadline = job[1]
		while deadline > 0 and schedule[deadline - 1] != -1 :
			deadline -= 1
		if deadline > 0 :
			schedule[deadline - 1] = job[0]
			scheduled_jobs.add(job[0])
	return [job for job in schedule if job != -1] , scheduled_jobs
	
num_jobs = int(input("Enter the number of jobs : "))
jobs = []
for i in range(num_jobs) :
    job_id = i + 1
    profit = int(input(f"Enter the profit of job {job_id} : "))
    deadline = int(input(f"Enter the deadline of job {job_id} : "))
    jobs.append((job_id,deadline,profit))
scheduled_jobs, _ = job_schedule(jobs)
print ("Scheduled jobs : ", scheduled_jobs)