# import argparse
# parser=argparse.ArgumentParser()
# # login_group=parser.add_argument('-u','--user',help="enter the user name")
# # login_group=parser.add_argument('-p','--password',help="enter the password")
# # personal_data=parser.add_argument_group('personal data')
# # personal_data.add_argument('-n','--name',help="enter name")
# # personal_data.add_argument('-a','--age',help="enter age")
# # args=parser.parse_args()

# group=parser.add_mutually_exclusive_group(required=True)
# group.add_argument('--upload',action='store_true',help="upload a file")
# group.add_argument('--download',action='store_true',help="download a file")

# args=parser.parse_args()

# if args.upload:
#     print("uploading")

# elif args.download:
#     print("downloading..")

#   tasks

#  task 1`>>` take a list of number and print their average

# import sys
# a=[]
# for i in sys.argv[1:]:
#     a.append(int(i))

# b=sum(a)
# av=b/len(a)
# print(av)

# task 2
# accept the file name and count the lines it has

# import sys
# cnt=0
# with open('demo.txt','r') as f:
#     cnt=sum(1 for i in f)
# print(cnt)

# task 3
# pass two words and print bigger one
# import sys

# def main():
#     if len(sys.argv) != 3:
#         print("Please provide exactly two words as command-line arguments.")
#         return

#     word1 = sys.argv[1]
#     word2 = sys.argv[2]

#     if len(word1) > len(word2):
#         print(f"The bigger word is: {word1}")
#     elif len(word2) > len(word1):
#         print(f"The bigger word is: {word2}")
#     else:
#         print("Both words are of equal length.")


# main()                                                                                                                                                                                                                       
                   

# task  7
# add two number using arparse

# import argparse

# parser=argparse.ArgumentParser()

# parser = argparse.ArgumentParser(description="Add two numbers.")

# parser.add_argument('num1',type=int,help="enter the num1")
# parser.add_argument('num2',type=int,help="enter the num1")


# args=parser.parse_args()
# print(args.num1+args.num2)



# task 8  Goal: Accept a word and a count as arguments, print the word that many times.

import argparse
parser=argparse.ArgumentParser()
parser= argparse.ArgumentParser(description="print multiple time word")
parser.add_argument('word',type=str,help="the word to printed")
parser.add_argument('count',type=int,help="how many times ")

args=parser.parse_args()

for _ in range(args.count):
    print(args.word)
