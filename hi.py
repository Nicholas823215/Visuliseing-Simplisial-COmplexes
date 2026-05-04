from Simplitial_Complises import *
import time

'''SimC = SC([Set([1]),Set([2]),Set([3]),Set([4]),Set([5]),Set([6]),
          Set([1,2]),Set([2,3]),Set([3,4]),Set([4,2]),Set([1,5]),Set([5,6]),Set([6,1])])
SimC1 = SC([Set([1]),Set([2]),Set([3]),Set([4]),Set([5]),Set([6]),
          Set([2,3]),Set([1,2]),Set([3,4]),Set([4,2]),Set([1,5]),Set([5,6]),Set([6,1])])
start_time1 = time.perf_counter()
SimC.findNoOfCrit_Meth1()
timer_1= time.perf_counter()


print("Not Optimal choice of removing simplisies")

for i in SimC.No_crit_Meth1.items():
    print(f"Number of Critical point with index{i[0]}: {i[1]}")
print(f"Took {-start_time1+timer_1} sec to compute\n")
print("Optimal choice of removing simplisies")
start_time2 = time.perf_counter()
SimC1.findNoOfCrit_Meth1()
timer_2= time.perf_counter()
for i in SimC1.No_crit_Meth1.items():
    print(f"Number of Critical point with index{i[0]}: {i[1]}")
print(f"Took {-start_time1+timer_1} sec to compute")'''

SimC = SC([Set([1]),Set([2]),Set([3]),Set([4]),Set([5]),
               Set([1,2]),Set([1,5]),Set([2,4]),Set([2,5]),Set([5,4]),Set([1,4]),Set([1,3]),Set([3,4]),Set([2,3]),
               Set([1,2,5]),Set([5,2,4]),Set([2,4,3]),Set([1,3,4]),
               Set([6]),Set([7]),Set([8]),Set([9]),Set([10]),Set([11]),
               Set([9,6]),Set([9,7]),Set([9,10]),Set([9,11]),Set([9,3]),Set([3,11]),Set([3,8]),Set([3,6]),Set([6,7]),Set([6,8]),Set([7,8]),Set([7,10]),Set([10,8]),Set([10,11]),Set([11,8]),
               Set([6,9,7]),Set([9,7,10]),Set([10,7,8]),Set([10,11,8]),Set([6,3,8]),Set([3,11,8]),Set([3,9,11]),
               Set([4,8,7]),Set([4,5,7]),Set([5,7,6]),Set([5,1,6]),Set([1,6,8]),Set([1,4,8]),
               Set([2,1,6]),Set([2,9,6]),Set([2,3,9]),Set([1,6,3]),
               Set([12]),Set([13]),Set([14]),Set([15]),Set([16]),
               Set([12,16]),Set([12,14]),Set([12,15]),Set([12,13]),Set([16,15]),Set([13,15]),Set([13,14]),Set([14,15]),Set([14,16]),
               Set([12,14,16]),Set([14,15,16]),Set([13,14,15]),Set([12,13,15])])

start_time1 = time.perf_counter()
SimC.findNoOfCrit_Meth1()
timer_1= time.perf_counter()


print("Removing Simplisies algorithem with Bigs house")

for i in SimC.No_crit_Meth1.items():
    print(f"Number of Critical point with index {i[0]}: {i[1]}")
print(f"Took {-start_time1+timer_1} sec to compute\n")