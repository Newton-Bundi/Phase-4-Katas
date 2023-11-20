def sort_strings_by_length(strings):
    return sorted(strings, key=len)

input_strings = [ "twwo","fourrrr" ,"one", "fiveeeeeeee", "threee",]
sorted_strings = sort_strings_by_length(input_strings)

print("Original strings:", input_strings)
print("Sorted strings by length:", sorted_strings)