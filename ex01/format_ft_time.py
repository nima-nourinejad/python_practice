import datetime

now = datetime.datetime.now()
micro_sec = int(int(now.strftime("%f")) / 100)
seconds = now.strftime("%s")

def make(n: int) -> str:
    if n < 10:
        n = "00" + str(n)
        return n
    elif n < 100:
        n = "0" + str(n)
        return n
    else:
        return str(n)

temp = int(seconds)
part1 = int(temp % 1000)
temp = int(temp / 1000)
part2 = int(temp % 1000)
temp = int(temp / 1000)
part3 = int(temp % 1000)
temp = int(temp / 1000)
part4 = int(temp % 1000)
date = now.strftime("%b %d %Y")
scientific_notation = f"{int(seconds):.2e}"

print(f"Seconds since January 1, 1970: {make(part4)},{make(part3)},{make(part2)},{make(part1)}.{micro_sec}  or {scientific_notation} in scientific notation")
print(date)
