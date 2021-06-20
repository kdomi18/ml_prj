# generating parameters

with open("out.txt", "w") as file:
    file.write("nrFeatures,accuracy")
    file.write("\n")
    for i1 in range(10,110,10):
        file.write("%d," % (i1)) 
        file.write("\n")

# temp 0.5194444444444445

# generating csv
# with open("out.txt", "r") as file1:
#     first = file1.readlines()

# with open("data.txt", "r") as file2:
#     second = file2.readlines()


# with open("final.txt",'w') as file3:
#     for i in range(len(first)):
#         file3.write(first[i]+second[i])
            

