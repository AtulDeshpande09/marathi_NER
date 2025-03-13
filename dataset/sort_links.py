categories = {"politics" : 0 ,
              "lifestyle" : 0 ,
              "career" : 0 ,
              "desh-videsh" : 0 ,
              "maharashtra": 0 ,
              "manoranjan" : 0 ,
              "tech": 0 ,
              "business" : 0}

def classify_links(input_file="loksattalinks.txt"):

    category_files = {cat : open(f"{cat}.txt" , "w" , encoding="utf-8") for cat in categories }

    misc_file = open("misc.txt" , "w" , encoding ="utf-8")

    with open(input_file , "r" , encoding="utf-8") as file:

        for line in file:

            link = line.strip()

            found_category = False

            for category , value in categories.items() :

                if category in link:

                    category_files[category].write(link + "\n")
                    categories[category]  += 1
                    found_category = True
                    break

            if not found_category:
                misc_file.write(link + "\n" )


    for file in category_files.values():
        file.close()
    misc_file.close()
    print("Links Sorted Successfully!!!")

    for category , value in categories.items():
        print(f"{category} ---> {value}")


if __name__ == "__main__":
    classify_links()



