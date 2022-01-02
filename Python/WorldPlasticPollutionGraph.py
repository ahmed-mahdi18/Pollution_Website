"""this function is wrapped around the whole code so that it can be repeated whenever needed"""
def main():

    """ this imports the matplotlib package from python to allow me to graph data"""
    import matplotlib.pyplot as plt
    """this opens the file i am working with.. reads in the file, the file is then closed when it has been read in."""
    file = open("cumulative-global-plastics.csv", "r")
    data = file.read()
    file.close()

    """this replaces all the unnecessary writing and data from the excel file with commas"""
    data = data.replace("World",",")
    data = data.replace("\n",",")
    data = data.replace("OWID_WRL",",")
    data = data.replace("\n",",")
    data = data.replace("Entity",",")
    data = data.replace("\n",",")
    data = data.replace("Code",",")
    data = data.replace("\n",",")
    data = data.replace("Year",",")
    data = data.replace("\n",",")
    data = data.replace("Cumulative global plastics production (million tonnes) (tonnes)",",")
    data = data.replace("\n",",")
    data = data.replace(",",",")
    """The the string is split into a list called myList. The items in the list are still
    strings and will need to be changed later."""
    DataList = data.split(",")



    position = 0

    """a new list called year list is created"""
    year_list = []
    """If the item in the list is "" then
    we change it to be 0.Then I will look at the index of the list and if the index of the value gives a remainder of 0
    when divided by 2 it will be in the right colunm. The for loop does this.
    the int item line turns the items into integers since python cannot graph strings.
    the new item is then added to the year list and the list is printed"""
    for item in DataList:
        if item == "":
            x = 0
        elif position % 2 == 0:
            item = int(item)
            year_list.append(item)
        position = position + 1
    """print(year_list)"""



    position = 0
    """a new list called plastic production is created"""
    plastic_production = []
    """If the item in the list is "" then
    we change it to be 0.Then I will look at the index of the list and if the index of the value gives a remainder of 1
    when divided by 2 it will be in the right colunm. The for loop does this.
    the int item line turns the items into integers since pyhton cannot graph strings.
    the new item is then added to the year list and the list is printed"""
    for item in DataList:
        if item =="":
            x = 0
        elif position % 2 == 1:
            item = int(item)
            plastic_production.append(item)
        position = position + 1
    """print(plastic_production)"""
   
    """the question is printed and the user is asked to input yes or no as a response to the question"""
    """if the answer is yes, using an if statement a prgram calculating the mean of the plastic production
    from 1950 to 2015 is run"""
    """if the answer is no it says thank you for your time and exits"""
    """if the response is not yes or no the user is asked to restart the program as it is invalid"""
    print ("Do you want to know the average amount of plastic produced from 1950-2015?")
    answer = str(input("Enter Yes or No:")).lower()
    if answer == "yes":
        totalplastic = sum(plastic_production)
        totalNumberofyears = 65
        average = totalplastic / totalNumberofyears
        average = round(average)
        print("the average is", average ,"tonnes of plastic.In 1950 the world produced only 2 million tonnes per year. Since then the annual production has increased nearly 200-fold,reaching 381 million tonnes in 2015. For context this is roughly equivalent to the mass of two-thirds of the world population.")

    elif answer == "no":
        print("thank you for your time")
    else:
        print("invalid answer please restart the programme")

    """ this plots the graph and the x and y axis are labelled, then finally the plt show lne of code prints out the graph"""
    plt.plot(year_list , plastic_production)
    plt.ylabel("cumulative plastic production")
    plt.xlabel("Year")
    plt.show()
   
    """this asks the user if they want to restart the program after the top part is finished. if answer is
    equal to yes the whole program re runs as it is in procedure called main. if not it exits"""
    repeat = input("Do you wish to restart the programme?").lower()
    if repeat == "yes":
        main()
    else:
        print("bye")
        exit()
main()
