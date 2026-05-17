jobs = [
    ('J1', 2, 100),
    ('J2', 1, 50),
    ('J3', 2, 10),
    ('J4', 1, 20),
    ('J5', 3, 30)
]

jobs.sort(key=lambda x:x[2],reverse=True)
max_deadline=max(job[1] for job in jobs)
n=len(jobs)
slots=[-1]*max_deadline
total_profit=0
print("Selected Jobs:")
for job in jobs:
    job_id=job[0]
    deadline=job[1]
    profit=job[2]

    for i in range(deadline-1,-1,-1):
        if slots[i]==-1:
            slots[i]=job_id
            total_profit+=profit
            print(job_id)
            break

print("\nTotal profit:",total_profit)