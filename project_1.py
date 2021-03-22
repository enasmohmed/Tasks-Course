# A program that takes a number from the user and prints the multiplication table from 2 to that number :
#A program that takes a word from me and prints the letters of the word without repetition :
'''
start = int(input('Enter Start Number :' ))
end = int(input('Enter End Number :' ))

for number in range(start, end+1):
     for value in range(1, 4):
          result = number * value
          print(f'{number} x {value} = {result}')

     print('*************************')
        


word = input('Enter a Word : ')
letters= []

for letter in word:
     if letter in letters:
          continue
     else:
          letters.append(letter)
print(letters)


 #A simple program that takes a number and is normal. Is it my husband or individual?  

x = int(input('Enter Your Number : '))


if  x % 2 == 0:
     print('even')
     
     
elif x % 2 != 0:
     print('odd')
     
else:
     print('The Number is not matched')


     

# The program takes a set of numbers and prints the doubles for one and the odd ones for one


even = []
odd =[]

x = input('choise even or odd: ') 
y = int(input('Enter number : '))

if x == 'even' :
     for i in range(y):
          if i %2 == 0 :
               even.append(i)
     print(even)
    
elif x == 'odd' :
     for i in range(y):
          if i %2 == 1:
             odd.append(i)
     print(odd)
    
else :
       print('please enter even or odd ')


# Print all the numbers that this number can divide from 1 to 10

number = int(input('Enter the Number :'))

for x in range(1,11):
     if (number % x) ==0:
          print(x)

     
'''


class Game:
     def __init__(self):
          print('Welcom In Our Game')
          print('''
                    Press the Game Number :
                    1 : Multiplication Table
                    2 : Remove Dublicated Chars
                    3 : Print is even or odd
                    4 : Print doubles for one and singles for one
                    5 : Print all the numbers 
                    ''')
          
          user_choice = int(input('Enter Your Choice Number : '))

          if user_choice == 1:
               self. Multiplication_table()

          elif user_choice == 2:
               self.remove_deplicates()

          elif user_choice == 3:
               self.Print_even_or_odd()

          elif user_choice == 4 :
               self.Print_doubles_or_singles()

          elif user_choice == 5:
               self.Print_all_numbers()

          else:
               print('Plase Enter A Valid Chioce')


     def Multiplication_table(self):
          start = int(input('Enter Start Number :' ))
          end = int(input('Enter End Number :' ))

          for number in range(start, end+1):
               for value in range(1, 4):
                    result = number * value
                    print(f'{number} x {value} = {result}')

               print('*************************')


     def remove_deplicates(self):
          word = input('Enter a Word : ')
          letters= []

          for letter in word:
               if letter in letters:
                    continue
               else:
                    letters.append(letter)
          print(letters)


     def Print_even_or_odd(self):
          x = int(input('Enter Your Number : '))

          if  x % 2 == 0:
               print('even')
               
               
          elif x % 2 != 0:
               print('odd')
               
          else:
               print('The Number is not matched')


     def Print_doubles_or_singles(self):
          even = []
          odd =[]

          x = input('choise even or odd: ') 
          y = int(input('Enter number : '))

          if x == 'even' :
               for i in range(y):
                    if i %2 == 0 :
                         even.append(i)
               print(even)
              
          elif x == 'odd' :
               for i in range(y):
                    if i %2 == 1:
                       odd.append(i)
               print(odd)
              
          else :
                 print('please enter even or odd ')




     def Print_all_numbers(self):
          number = int(input('Enter the Number :'))

          for x in range(1,11):
               if (number % x) ==0:
                    print(x)
          

g = Game()
               

















