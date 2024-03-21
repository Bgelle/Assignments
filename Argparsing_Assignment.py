import argparse
parser = argparse.ArgumentParser()#//to get the parser object
parser.add_argument('-n1','--number1', type=int,default=10,required=False, help="an integer number")
parser.add_argument('-n2','--number2', type=int,default=40,required=False, help="an integer number")
args = parser.parse_args()
#result = args.number * 2
#print("Result:", result)

sum=args.number1+args.number2
sub=args.number1-args.number2
mul=args.number1*args.number2
div=args.number1/args.number2
#sum=args['number1']+args['number2']
print("Sum:", sum)
print("Sub:",sub)
print("Mul:",mul)
print("Div:",div)

