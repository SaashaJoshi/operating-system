# Operating System (CS403 / CS453)

This repository contains the following CPU Scheduling algorithms written in Python.

| Algorithm |  |
| ------ | ------ |
| FCFS | First Come First Serve |
| SJF | Shortest Job First |
| SRTF | Shortest Remaining Time First |
| PriorityNP | Priority Based Scheduling (Non Pre-emptive) |
| PriorityP | Priority Based Scheduling (Pre-emptive) |
| RR | Round Robin |

and 
>deadlockDetection

# Description of time wrt to a process:

Arrival Time: Time at which the process arrives in the ready queue.

Completion Time: Time at which process completes its execution.

Burst Time: Time required by a process for CPU execution.

Turn Around Time: Time Difference between completion time and arrival time.
>Turn Around Time = Completion Time – Arrival Time

Waiting Time: Time Difference between turn around time and burst time.
>Waiting Time = Turn Around Time – Burst Time
