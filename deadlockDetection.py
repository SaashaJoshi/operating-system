from operator import add

def detect(process, allocation, request, work):
	n=len(process)
	finish=[False]*n

	for i in range(n):
		if allocation[i]==[0]*3:
			finish[i]=True

	for i in range(n):
		if finish[i]==False and request[i]<=work:
			work=list(map(add, work, allocation[i]))
			finish[i]=True

	print(finish)
	for i in range(n):
		if finish[i]==False:
			print('Deadlock occurs for the process {}'.format(i))
		if finish==[True]*n:
			print('No Deadlock!')

if __name__=='__main__':
	'''
	n=int(input('Enter number of processes: '))
	process=list(range(n))

	r=int(input('Enter number of resources: '))

	allocation=input('Enter allocation: ').split()
	request=input('Enter request: ').split()
	available=input('Enter available resources: ')
	'''

	process=[0, 1, 2, 3, 4]
	allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
	request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
	available=[0, 0, 0]

	detect(process, allocation, request, available)


