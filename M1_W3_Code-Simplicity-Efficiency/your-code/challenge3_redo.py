def triangle_sides(X):
#Improve the efficiency of the code by using list comprehension

    solutions = [[x, y, z] for x in range(5, X) for y in range(4, X) for z in range(3, X) if ((x*x)==(y*y)+(z*z))]

    m = 0
    for solution in solutions:
        if m < max(solution):
            m = max(solution)
    return m

user_input = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(triangle_sides(int(user_input))))