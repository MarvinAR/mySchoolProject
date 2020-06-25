
N = int(input())

hour = N // 3600
N -= hour * 3600

minutes = N // 60
N -= minutes * 60


print("%i:%i:%i"%(hour,minutes,N))
