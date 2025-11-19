"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of followed by lines of commands
where each command will be of the  types listed above. Iterate through each command
in order and perform the corresponding operation on your list.
The first line contains an integer, denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

!!!Don't convert list to string for output!!!!
l = [1, 2, 3]
print(l) # correct
print(str(l) # wrong
"""


def main():
    """Perform list commands."""
    n = int(input())
    lst = []
    for _ in range(n):
        cmd_line = input().strip().split() # split command into parts
        cmd = cmd_line[0]

        if cmd == "insert":
            i = int(cmd_line[1])
            e = int(cmd_line[2])
            lst.insert(i, e)
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            e = int(cmd_line[1])
            lst.remove(e)
        elif cmd == "append":
            e = int(cmd_line[1])
            lst.append(e)
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
