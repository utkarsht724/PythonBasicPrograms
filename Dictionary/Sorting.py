#Program to sort the dictionary in ascending and descending order by value
import operator
def sort_by_value():
    epic={1:10, 4:3, 3:45, 5:56}
    print(epic)
    #sort the dictionary by ascending order
    sort_by_value_ascending=sorted(epic.items() ,key =lambda items:items[1])
    print("sort by value in ascending order",sort_by_value_ascending)
    #soer the dictionary by descending order
    sort_by_value_descending=sorted(epic.items(),key= operator.itemgetter(1),reverse=True)
    print("sort by value in descending order",sort_by_value_descending)

sort_by_value()