#list and tuples only have one difference that is lists are mutable and tuples are immutable
#lists in python represent a series of comma separated values of any datatype
#for eg:[1,"a",4.8] or[1,2,"neha"]
list=["Teju",17,8.75]
tuple=("Sudhanshu",25,9.56)
print(list)
list[2]="10"
print(list) 
print(tuple)
tuple[1]="10"#tuple is immutable i.e you can't assign/change values once set
print(tuple)