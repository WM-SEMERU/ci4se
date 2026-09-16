def waznlike(word1, wazn):
    stack1 = stack.Stack(word1)
    stack2 = stack.Stack(wazn)
    root = stack.Stack()
    last1 = stack1.pop()
    last2 = stack2.pop()
    vowels = HARAKAT
    while last1 != None and last2 != None:
        if last1 == last2 and last2 not in (FEH, AIN, LAM):
            last1 = stack1.pop()
            last2 = stack2.pop()
        elif last1 not in vowels and last2 in (FEH, AIN, LAM):
            root.push(last1)
            last1 = stack1.pop()
            last2 = stack2.pop()
        elif last1 in vowels and last2 not in vowels:
            last1 = stack1.pop()
        elif last1 not in vowels and last2 in vowels:
            last2 = stack2.pop()
        else:
            break
    root.items.reverse()
    if not (stack1.is_empty() and stack2.is_empty()):
        return False
    else:
        return True