def about():
    name = input("Write your name")
    age = int(input("How old are you"))
    like = input("WHat you like")
    list =(name,age,like)
    about_sentence = 'Mam na imię {0}, mam {1} lat i lubię {2}'.format(name,age,like)
    print(about_sentence)

about()
