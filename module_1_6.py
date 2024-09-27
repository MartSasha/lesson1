#Работа над словарями
my_dick={'Sasha': 1998,'Ann':2008}
print(my_dick)
print(my_dick['Sasha'],my_dick.get('Kiriil'))
my_dick.update({'Max': 1996, 'Nikita': 2005})
del my_dick['Max']
print(my_dick)
#Работа над множествами
my_set={1,2,1,2,'string','string'}
print(my_set)
my_set.update([5,6,'Sasha'])
my_set.remove(2)
print(my_set)

