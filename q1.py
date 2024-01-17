# Get neccessary inputs. Write 'None' if a course doesn't have prerequisite.
courses = input().split(' ') 
prereqs = input().split(' ') 

n = len(courses)
ordered_list = []
for i in range(n):
    if prereqs[i]!='None' and prereqs[i] not in courses:
        ordered_list.append(prereqs[i])
        prereqs[i] = 'None'
    
for i in courses:
    if i not in ordered_list:
        ordered_list.append(i)
print(ordered_list)
    