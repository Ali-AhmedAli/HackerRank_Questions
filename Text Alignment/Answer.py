if __name__ == '__main__': 
    n = int(input()) 
    actual_fig_n = 6*n

#left arrow
    for i in range(n):
        print(('H'*(2*i+1)).center(2*n))

#top pillars
    for i in range(n+1):
        print(('H'*n).center(2*n) + (('H'*n).rjust(actual_fig_n - 3*n + n//2)))

#middle horizontal pillar
    for i in range(n//2 +1):
        print(('H'*(n*5)).center(actual_fig_n))

#bottom pillars
    for i in range(n+1):
        print(('H'*n).center(2*n) + (('H'*n).rjust(actual_fig_n - 3*n + n//2)))

#bottom arrow
    for i in range(n-1,-1,-1):
        print((' '*2*n).center(actual_fig_n - 2*n) + ('H'*(2*i+1)).center(2*n))