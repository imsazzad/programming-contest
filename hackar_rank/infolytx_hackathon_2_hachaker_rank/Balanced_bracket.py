#!/bin/python3


def isBalanced(str):
    stack = []
    pushChars, popChars = "<({[", ">)}]"
    for c in str:
        if c in pushChars:
            stack.append(c)
        elif c in popChars:
            if not len(stack):
                return False
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(c)]
                if stackTop != balancingBracket:
                    return False
        else:
            return False
    return not len(stack)


if __name__ == "__main__":
    t = int(input().strip());

    for a0 in range(t):
        string = input().strip();
        if (isBalanced(string)):
            print("YES");
        else:
            print("NO");
# 3
# {[()]}
# {[(])}
# {{[[(())]]}}
