#You will get the values for two moments in time of the same day: when Megan went for a walk, and when it started to rain. It is known that the first
#event happened earlier than the second one. Find out how many seconds passed between them.
#The program gets the input of six integers, each on a separate line. The first three integers represent hours, minutes, and seconds of the first
#event, and the rest three integers define similarly the second event. Print the number of seconds between these two moments of time.
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
n6 = int(input())
print((n4 * 60 * 60 + n5 * 60 + n6) - (n1 * 60 * 60 + n2 * 60 + n3))
