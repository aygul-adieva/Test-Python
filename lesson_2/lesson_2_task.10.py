def bank():
    stavka = 10
    n = int(input("Сколько у Вас денег?""\n""-> "))
    years = int(input("На сколько лет хотите сделать вклад?""\n""-> "))

    for i in range(years):
        n = int(n+stavka*n/100)
    print("По итогу вы получаете", n, "рублей")
bank()