#JugsMugsPugs
def JugsMugsPugs(num):
  a=num
  digit=int(num)
  if (digit%3==0)or(digit%5==0)or(digit%7==0)or('3'in num)or('5'in num)or('7'in num):
    a=""
    if (digit%3==0)or('3'in num):
      a=a+"Jugs"
    if (digit%5==0) or ('5' in num):
      a = a+"Mugs"
    if (digit%7==0) or ('7' in num) :
      a =a+"Pugs"
    print(a)
  else:
    return int(a)
num=input()
JugsMugsPugs(num)
#JugsMugsPugs Reverse
def jugs_mugs_pugs(num, rev):
    for i in range(1, num + 1):
        if rev:
            string = 'Jugs' * bool(i % 3 == 0 or '3' in str(i))
            string = 'Mugs' * bool(i % 5 == 0 or '5' in str(i)) + string
            string = 'Pugs' * bool(i % 7 == 0 or '7' in str(i)) + string
            print(string or i)
        else:
            print("Jugs" * (i % 3 == 0 or '3' in str(i)) + "Mugs" * (i % 5 == 0 or '5' in str(i)) +
                  "Pugs" * (i % 7 == 0 or '7' in str(i)) or i)

# Example usage
num_input = int(input("Enter a number: "))
rev_input = int(input("Enter 1 for reverse order, 0 for normal order: "))
jugs_mugs_pugs(num_input, rev_input)
