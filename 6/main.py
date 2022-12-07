import collections

def part(limit):
     with open("input.txt", "r") as file:
        starting = True
        line = file.readline()
        last4 = collections.deque(maxlen=limit)
        for index, char in enumerate(line):
            last4.append(char)
            if (len(last4) == limit):
                starting = False
            if (starting):
                continue
            if len(set(last4)) == limit:
                return index+1

if __name__ == "__main__":
   print(part(4))
   print(part(14))
