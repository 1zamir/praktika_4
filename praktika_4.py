
justNumbers = [ 4, 1, 13, 0, 6 ]
len( justNumbers ) # количество элементов в списке
5
sum( justNumbers ) # сумма элементов
24
sorted( justNumbers ) # сортировка
[0, 1, 4, 6, 13]
sorted( justNumbers, reverse = True ) # сортировка в обратном порядке
[13, 6, 4, 1, 0]
justNumbers.append( 55 ) # добавление элемента
justNumbers
[4, 1, 13, 0, 6, 55]

# склеивание листов

[1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]


a = [1, 2, 3]
b = a
b.append( 8 )
copyNumbers = justNumbers
copyNumbers.append( 66 )
justNumbers
id( justNumbers )
id( copyNumbers )
justNumbers = [ 4, 1, 13, 0, 6, 55 ]
import copy
copyNumbers = copy.deepcopy( justNumbers )
copyNumbers.append( 66 )
a = 1
b = a
id(a), id(b)
b = 3
a
id( justNumbers )
id( copyNumbers )
justNumbers
copyNumbers

sequence = [ 'Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый' ]
sequence[1:]
sequence[1:2][0]
type( sequence[-2:] )

print( sequence[2:3] )
print( sequence[2] )
print( type(sequence[2:3]  ) )
print( type(sequence[2]  ) )
print( sequence[:3] )
print( sequence[-1] )
print( sequence[-2:] )

sequence
';'.join( sequence )
','.join( sequence )
'one;two;three'.split(';')

for i in range(10):
    print( i )
for i in range( 5, 10, 3 ):
    print(i)
list( range(10) )

sequence = range( 0, 40, 3 )

for num in sequence:
    if num % 5 == 0:
        print( num )

filteredSequence = []

for num in sequence:
    if num % 5 == 0:
        filteredSequence.append( num )

print( filteredSequence )

print( [ x for x in sequence if x % 5 == 0 ] )
queries = ['смотреть сериалы онлайн', 'новости', 'какая рыба вобла', 'пхенчхан золото онлайн', 'сколько дней до 8 марта']
length_of_words = [ len(x.split(' ')) for x in queries ]
length_of_words

empty_list = []

numbers = [40, 20, 90, 11, 5]


fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']


fractions = [3.14, 2.72, 1.41, 1.73, 17.9]


values = [3.14, 10, 'Hello world!', False, 'Python is the best']


list_of_lists = [[2, 4, 0], [11, 2, 10], [0, 19, 27]]


fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
print(fruits[0])
print(fruits[1])
print(fruits[4])

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
fruits[0] = 'Watermelon'
fruits[3] = 'Lemon'
print(fruits)

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])


letters = list('abcdef')
numbers = list(range(10))
even_numbers = list(range(0, 10, 2))
print(letters)
print(numbers)
print(even_numbers)

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
print(len(fruits))


numbers = [40, 20, 90]
print(len(numbers))

string = 'Hello world'
print(len(string))


fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
part_of_fruits = fruits[0:3]
print(part_of_fruits)


fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
print(fruits[0:1])
print(fruits[:2])
print(fruits[:3])
print(fruits[:4])
print(fruits[:5])
print(fruits[:len(fruits)])
print(fruits[::])


fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
print(fruits[::2])
print(fruits[::3])
print(fruits[::-1])
print(fruits[4:2:-1])
print(fruits[3:1:-1])

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
for fruit in fruits:
    print(fruit, end=' ')

for index in range(len(fruits)):
    print(fruits[index], end=' ')

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
if 'Apple' in fruits:
    print('В списке есть элемент Apple')


fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
if 'Lemon' in fruits:
    print('В списке есть элемент Lemon')
else:
    print('В списке НЕТ элемента Lemon')


all_fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
my_favorite_fruits = ['Apple', 'Banan', 'Orange']
for item in all_fruits:
    if item in my_favorite_fruits:
        print(item + ' is my favorite fruit')
    else:
        print('I do not like ' + item)

numbers = list(range(0,10,2))
numbers.append(200)
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)

all_types = [10, 3.14, 'Python', ['I', 'am', 'list']]
all_types.append(1024)
all_types.append('Hello world!')
all_types.append([1, 2, 3])
print(all_types)

numbers = list(range(10))
numbers.insert(0, 999)
print(numbers) # первый print
numbers.insert(2, 1024)
print(numbers) # второй print
numbers.insert(5, 'Засланная строка-шпион')
print(numbers) # третий print

numbers = list(range(10))
print(numbers) # 1
numbers.pop(0)
print(numbers) # 2
numbers.pop(0)
print(numbers) # 3
numbers.pop(2)
print(numbers) # 4
numbers.pop()
print(numbers) # 5
numbers.pop()
print(numbers) # 6

all_types = [10, 'Python', 10, 3.14, 'Python', ['I', 'am', 'list']]
all_types.remove(3.14)
print(all_types) # 1
all_types.remove(10)
print(all_types) # 2
all_types.remove('Python')
print(all_types) # 3

numbers = [100, 100, 100, 200, 200, 500, 500, 500, 500, 500, 999]
print(numbers.count(100)) # 1
print(numbers.count(200)) # 2
print(numbers.count(500)) # 3
print(numbers.count(999)) # 4


numbers = [100, 2, 11, 9, 3, 1024, 567, 78]
numbers.sort()
print(numbers) # 1
fruits = ['Orange', 'Grape', 'Peach', 'Banan', 'Apple']
fruits.sort()
print(fruits) # 2

fruits = ['Orange', 'Grape', 'Peach', 'Banan', 'Apple']
fruits.sort()
print(fruits) # 1
fruits.sort(reverse=True)
print(fruits) # 2

numbers = [100, 2, 11, 9, 3, 1024, 567, 78]
numbers.reverse()
print(numbers) # 1
fruits = ['Orange', 'Grape', 'Peach', 'Banan', 'Apple']
fruits.reverse()
print(fruits) # 2

fruits = ['Banana', 'Apple', 'Grape']
vegetables = ['Tomato', 'Cucumber', 'Potato', 'Carrot']
fruits.extend(vegetables)
print(fruits)


fruits = ['Banana', 'Apple', 'Grape']
vegetables = ['Tomato', 'Cucumber', 'Potato', 'Carrot']
fruits.clear()
vegetables.clear()
print(fruits)
print(vegetables)


fruits = ['Banana', 'Apple', 'Grape']
print(fruits.index('Apple'))
print(fruits.index('Banana'))
print(fruits.index('Grape'))


fruits = ['Banana', 'Apple', 'Grape']
new_fruits = fruits
print(fruits)
print(new_fruits)


fruits = ['Banana', 'Apple', 'Grape']
new_fruits = fruits
fruits.pop()
print(fruits)
print(new_fruits)

fruits = ['Banana', 'Apple', 'Grape']
new_fruits = fruits.copy()
fruits.pop()
print(fruits)
print(new_fruits)

fruits = ['Banana', 'Apple', 'Grape', ['Orange','Peach']]
new_fruits = fruits.copy()
fruits[-1].pop()
print(fruits) # 1
print(new_fruits) # 2


print("------------------------ЗАДАНИЕ-------------------------------")


size = sorted(map(int, input('Рост учеников через пробел: ').split()))
Petya = int(input('Введите рост Пети: '))
s = 0 
for i in size:
    if i <= Petya:
        s += 1
        continue
    break
size.insert(s, Petya)
print(size)
print("Индекс Пети в строю: ", s)

#результат задания: https://clck.ru/32Bezv