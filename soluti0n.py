def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        if i == j:
            answer.append(array[i-1])
            continue

     answer.append(sorted(array[i-1:j])[k-1])
    
     


    return answer
      
    