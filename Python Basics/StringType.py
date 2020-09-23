s = "Tejeswara Sai Appikatla"
print(s)

#Creating a String across Lines
s1 = """I am very Good at Mathematics
so I chose Data Science as My Specilization
I want to Pursue a Career as a Data Scientist or like a Python Developer"""
print(s1)

# Replication in Strings
print(s*2)  # It prints the string multiple number of time respect to the number Given

# To know the Length of the String Provided
print(len(s))
print(s[0:13])
print(s[0:13:2])
print()
k = "   Stripping the Spaces  "
print(k)
print(k.strip())    #Strips the Trailing and Ending Spaces
print(k.lstrip())   #Strips the Left Side Spaces
print(k.rstrip())   #strips the Right Side Spaces


# Few Other String Functions in Python
print(k.find("pp"))    #Searches for the substring
print(k.find("pp",0,4)) #Searches for the substring in the range specified if found returns the index else returns -1
print(k.count("a")) #counts number of times the substring in the main string
print(k.replace("the","a")) #Replacing the with a in the main string whenever encountered or found in the main string
print(s.upper())    # Prints the whole string in upper case
print(s.lower())    # Prints the whole string in Lower Case
print(s.title())    # Prints the Whole String in Title Case