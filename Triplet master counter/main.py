while True:
    a1 = input('\n Insert your raw copy of exon: \n (or type "exit" to finish the script)\n')
    if a1 == 'exit':
        break
    nullstr = []
    for i in a1:
        if i.isalpha():
            nullstr.append(i)

    b1 = ''.join(nullstr)
    while True:
        intent = input('\n Type "triplet" to find triplet sequence knowing its number,\n or "number" to find triplet number using its sequence (all matches), \n or type "show" to see your exon sequence with marked and counted triplets, \n or "back" to return to sequence entering.\n')
        if intent == 'number':
            exnum = int(input('\n Guess exon number:\n'))
            print(b1[3*exnum-3:3*exnum])

        elif intent == 'triplet':
            def grouper(iterable, n):
                args = [iter(iterable)] * n
                return zip(*args)

            l = [''.join(i) for i in grouper(b1, 3)]
            code = input('\n Enter triplet:\n')
            posi = [i for i in range(len(l)) if l[i] == code]
            for i in posi:
                print(int(i)+1)

        elif intent == 'show':
            def grouper(iterable, n):
                args = [iter(iterable)] * n
                return zip(*args)

            l = [''.join(i) for i in grouper(b1, 3)]
            l1 = []
            for i in range(len(l)):
                j = l[i] + str(i+1)
                l1.append(j)
            print(*l1)

        elif intent == 'back':
            break

        else:
            print('try again')
