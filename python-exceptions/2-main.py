#!/usr/bin/python3
safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers

print("Test 1 : liste avec que des entiers")
my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list_integers(my_list, 3)
print("=> Nombre imprimé :", nb_print)

print("\nTest 2 : liste avec des types mixtes")
my_list = [1, "a", 3, "b", 5]
nb_print = safe_print_list_integers(my_list, 0)
print("=> Nombre imprimé :", nb_print)

print("\nTest 3 : liste avec aucun entier")
my_list = ["a", "b", "c"]
nb_print = safe_print_list_integers(my_list, 2)
print("=> Nombre imprimé :", nb_print)

print("\nTest 4 : liste plus courte que x")
my_list = [10, 20]
nb_print = safe_print_list_integers(my_list, 5)
print("=> Nombre imprimé :", nb_print)

print("\nTest 5 : liste vide")
my_list = []
nb_print = safe_print_list_integers(my_list, 1)
print("=> Nombre imprimé :", nb_print)

print("\nTest 6 : liste avec erreurs possibles")
my_list = [1, 2, "a", None, 5, 6.7]
nb_print = safe_print_list_integers(my_list, 4)
print("=> Nombre imprimé :", nb_print)

