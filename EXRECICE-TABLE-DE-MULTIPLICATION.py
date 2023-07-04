def multiplication_table(n, mini, maxi):
    while not (n.isdigit() and mini.isdigit() and maxi.isdigit()):
        n = input("entrer le nombre n ")
        mini = input("entrer min ")
        maxi = input("entrer max ")

    if int(mini) > int(maxi):
        print("erreur: min doit etre inferieure a max")
        return

    n = int(n)
    mini = int(mini)
    maxi = int(maxi)
    for i in range(mini, maxi+1):
        print(f"{n} x {i} = {i * n}")


multiplication_table("", "", "")
