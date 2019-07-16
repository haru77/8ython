n=5
m=9
for i in range(m):
   if (i == 0 or i == m-1):
       for j in range(n):
            print('*', end = '')
   else:
       if (j == 0 or j == n-1):
            print('*', end = '')

   print('\n')