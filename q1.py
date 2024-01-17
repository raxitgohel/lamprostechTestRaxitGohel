# Get neccessary inputs. Write 'None' if a course doesn't have prerequisite.
courses = input().split(' ') 
prereqs = input().split(' ') 

n = len(courses)
ordered_list = []
for i in range(n):
    if prereqs[i]!='None' and prereqs[i] not in courses:
        ordered_list.append(prereqs[i])