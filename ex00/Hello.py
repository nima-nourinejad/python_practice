ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
new_tuple = ("Hello", "Finland!")
ft_tuple = new_tuple
ft_set.remove("tutu!")
ft_set.add("Helsinki!")
ft_dict["Hello"] = "Hive!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)