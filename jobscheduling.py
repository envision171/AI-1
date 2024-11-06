def job_scheduling(jobs, max_deadline):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[1], reverse=True)
    result = [-1] * max_deadline  # Slots for jobs
    total_profit = 0
    
    for job, profit in jobs:
        for slot in range(min(max_deadline - 1, job - 1), -1, -1):
            if result[slot] == -1:
                result[slot] = profit
                total_profit += profit
                break
                
    return total_profit

# Example jobs (deadline, profit)
jobs = [(2, 100), (1, 50), (2, 10), (1, 20), (3, 30)]
print("Maximum Profit:", job_scheduling(jobs, 3))
