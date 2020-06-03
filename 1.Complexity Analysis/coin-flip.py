#In this game the player will use N coins numbered from 1 to N, and all the coins will be facing in "Same direction" (Either Head or Tail),which will be decided by the player before starting of the game.
#The player needs to play N rounds.In the k-th round the player will flip the face of the all coins whose number is less than or equal to k. That is, the face of coin i will be reversed, from Head to Tail, or, from Tail to Head, for i ≤ k.
#Elephant needs to guess the total number of coins showing a particular face after playing N rounds. Elephant really becomes quite fond of this game COIN FLIP, so Elephant plays G times. Please help the Elephant to find out the answer.

t = int(input())
for _ in range(t):
    g = int(input())
    for a in range(g):
        i, n, q = (input().split())
        i, n, q = int(i), int(n), int(q)
        count = n//2
        if (i == q):
            print(count)
        else:
            print(n - count )
