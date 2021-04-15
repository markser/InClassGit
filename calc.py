def calc(a,b):
    calcSum = a + b
    print(calcSum)
    calcSub = a - b
    print(calcSub)
    calcMul = a * b
    print(calcMul)
    calcDiv = a / b
    print(calcDiv)

    calcList = [calcSum,calcSub,calcMul,calcDiv]
    sumOfList = sum(calcList)

    print(sumOfList)

calc(3,3)