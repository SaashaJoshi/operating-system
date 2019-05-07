# Shortest Remaining Time First (Pre-emptive SJF) CPU Scheduling algorithm
# for processes with same arrival time (Arrival Time = 0).

import sys

def waitingTime(process, wt):
	n=len(process)
	rt=[0]*n

	for i in range(n):
		rt[i]=process[i][2]

	complete=0
	short=0
	current_t=0
	min_t=sys.maxsize
	flag=False

	while(complete!=n):
		for i in range(n):
			if process[i][1]<=current_t and rt[i]<min_t and rt[i]>0:
				min_t=rt[i]
				short=i
				flag=True

		if flag==False:
			current_t+=1
			continue

		rt[short]-=1
		min_t=rt[short]

		if(min_t==0):
			min_t=sys.maxsize

		if rt[short]==0:
			complete+=1
			flag=False
			final_t=current_t+1
			wt[short]=final_t-process[short][1]-process[short][2]
			#wt = tat-bt = (et-at)-bt

			if wt[short]<0:
				wt[short]=0

		current_t+=1
	
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

def display(process, wt, tat, avg_wt, avg_tat):
	print('Process\t Arrival Time\t Burst Time\t Waiting Time\t Turn Around Time')

	for i in range(len(process)):
		print('{}\t {}\t\t {}\t\t {}\t\t {}'.format(process[i][0], process[i][1], process[i][2], wt[i], tat[i]))

	print('\nAverage Waiting Time: ', avg_wt)
	print('Average Turn Around: ', avg_tat)

def main():
	'''
	process=input('Enter the process: ')
	process=process.split()
	'''
	process=[[1, 0, 3], [2, 1, 4], [3, 2, 5], [4, 3, 1], [5, 4, 2]]

	'''
	at=input('Enter Arrival Time of the respective process: ')
	at=at.split()
	
	bt=input('Enter Burst Time of the respective process: ')
	bt=bt.split()
	'''

	avgTime(process)

if __name__=='__main__':
	main()
