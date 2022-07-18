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

    #람다 활용시 커맨즈의 값하나만 x로 활용되는게 아니고 x의 주소값
    #을 이용해서 커맨즈배열 안 여러 수를 한번의 연산에 활용하는게 신기
 
      
    