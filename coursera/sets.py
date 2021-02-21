
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

A.add("NSYC")
print(A)

A.remove("NSYC")
print(A)

print("AC/DC" in A)


##########intersection

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

intersection = album_set1 & album_set2
print(intersection)


inter = album_set1.intersection(album_set2)
print(inter)

#########difference

difference =album_set1.difference(album_set2)  
print(difference)

# Find the union of two sets

united = album_set1.union(album_set2)
print(united)

# Check if superset

superset = set(album_set1).issuperset(album_set2) 
print(superset)

# Check if subset

subset = set(album_set2).issubset(album_set1) 
print(subset)

# Check if subset

sub_1 = set({"Back in Black", "AC/DC"}).issubset(album_set1) 
print(sub_1)

# Check if superset

super_1 = album_set1.issuperset({"Back in Black", "AC/DC"})   
print(super_1)