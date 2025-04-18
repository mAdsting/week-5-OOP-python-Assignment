from pet import Pet

def main():
    name = "Bosco"  # Set the pet's name to "Bosco"
    my_pet = Pet(name)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Put your pet to sleep")
        print("3. Play with your pet")
        print("4. Check your pet's status")
        print("5. Exit")
        print("6. Train your pet")
        print("7. Show your pet's tricks")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            my_pet.eat()
        elif choice == '2':
            my_pet.sleep()
        elif choice == '3':
            my_pet.play()
        elif choice == '4':
            my_pet.get_status()
        elif choice == '5':
            break
        elif choice == '6':
            trick = input("Enter a trick to teach your pet: ")
            my_pet.train(trick)
        elif choice == '7':
            my_pet.show_tricks()
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()