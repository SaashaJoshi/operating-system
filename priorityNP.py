# Priority (Non-Pre-emptive) CPU SCheduling algorithm
# for processes with same arrival time (Arrival Time = 0).

def waitingTime(process, wt):
	n=len(process)
	wt[0]=0
	for i in range(1, n):
		wt[i]=process[i-1][2]+wt[i-1]

def turnAroundtime(process, wt, tat):
	for i in range(len(process)):
		tat[i]=process[i][2]+wt[i]

def avgTime(process):
	n=len(process)
	wt=[0]*n
	tat=[0]*n
	total_wt=0
	total_tat=0

	waitingTime(process, wt)
	turnAroundtime(process, wt, tat)

	for i in range(n):
		total_wt=total_wt+wt[i]

	for i in range(n):
		total_tat=total_tat+tat[i]

	avg_wt=total_wt/n
	avg_tat=total_tat/n

	display(process, wt, tat, avg_wt, avg_tat)

def findOrder(process):
	process.sort(key= lambda process:process[3])
	return process

def display(process, wt, tat, avg_wt, avg_tat):
	print('Process\t Arrival Time\t Burst Time\t Priority\t Waiting Time\t Turn Around Time')

	for i in range(len(process)):
		print('{}\t {}\t\t {}\t\t {}\t\t {}'.format(process[i][0], process[i][1], process[i][2], process[i][3], wt[i], tat[i]))

	print('\nAverage Waiting Time: ', avg_wt)
	print('Average Turn Around: ', avg_tat)

def main():
	'''
	process=input('Enter the process: ')
	process=process.split()
	'''
	process=[[1, 0, 3, 4], [2, 0, 4, 2], [3, 0, 5, 3], [4, 0, 1, 1], [5, 0, 2, 5]]

	'''
	at=input('Enter Arrival Time of the respective process: ')
	at=at.split()
	
	bt=input('Enter Burst Time of the respective process: ')
	bt=bt.split()
	'''

	process=findOrder(process)
	avgTime(process)

if __name__=='__main__':
	main()
