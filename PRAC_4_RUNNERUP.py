"""KAVIRAJ DESAI 20CE023"""
# taking input for n
n=int(input())
# input for runner-ups
arr=map(int,input().split())
# sorting the list
print(sorted(list(set(arr)))[-2])