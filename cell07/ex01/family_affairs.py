def find_the_redheads(family_dict):
    return list(filter(lambda key: family_dict[key] == "red", family_dict.keys()))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))