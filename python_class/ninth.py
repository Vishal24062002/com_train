# COMMAND AND ARGS
# import sys
# print('hello')
# print(sys.argv)
# print(sys.argv[0])
# print(sys.argv[1:])

# print(f' file name {sys.argv[0]}')


# print sum of the args while convert into int
  
# print(sum(int(i) for i in sys.argv[1:]))
 


# import argparse

# parser =argparse.ArgumentParser()

# parser.add_argument('name',help="enter the name") # positional argument
# parser.add_argument('phone',type=int ,nargs='?',default=1234,help="enter phone number") #  argument
# parser.add_argument('--age',help="enter the age")# - make optinal
# parser.add_argument('-t','--true',action='store_true')
                                                 
# args=parser.parse_args()

# print(args.name)
# print(type(args.phone))
# print(args.phone)
# # print(args.phone)
# print(args.age)
# print(args.true)


import argparse
 
parser=argparse.ArgumentParser()
 
 
# parser.add_argument('name',nargs='?',default="abc",help='enter your name') # accept
# parser.add_argument('colors',nargs="*",help='Enter colors') # variable length
 
 
# args=parser.parse_args()
# print(args.name) 
# print(args.colors)

# parser.add_argument('city',help="enter the city")
# parser.add_argument('country',help="enter the country")-

# parser.add_argument('--name',default="unknown",help="enter ypur name")
# parser.add_argument('--age',type=int,default=0,help="enter your age ")

# args=parser.parse_args()

# print(f'name : {args.name}')
# print(f'name : {args.age}')
# print(f'name : {args.city}')
# print(f'name : {args.country}')


# parser.add_argument('fruits',choices=['orange','malta'],help="enter the fruit")

# args=parser.parse_args()

# print(args.fruits)

# parser=argparse.ArgumentParser(


#     description='enter the name of command'

# )
# parser.add_argument('--limit',metavar='1-10',type=int,help="maximum value to process")

# args=parser.parse_args()




def greeti(name,lang):
    greet={
        "english":"namste",
        "hindi":" kya hal h",
        "haryanvi":"k hal h"

    }

    msg=f'{greet[lang]} {name}!'
    print(msg)

parser=argparse.ArgumentParser('get language from by using cmd')
parser.add_argument('-n','--name',metavar="name",required=True)
parser.add_argument('-l','--lang',choices=['english','hindi','haryanvi'],required=True)

args=parser.parse_args()

greeti(args.name,args.lang)
