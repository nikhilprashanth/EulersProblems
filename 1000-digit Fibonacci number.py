fn=0
fn1=1
count=3
fn2=2

while len(str(fn2))<1000:
    fn=fn1
    fn1=fn2
    fn2=fn+fn1
    count=count+1

print("THE ANSWER IS ",count)
print("THE FIBONACCI NUMBER IS ",fn2)
