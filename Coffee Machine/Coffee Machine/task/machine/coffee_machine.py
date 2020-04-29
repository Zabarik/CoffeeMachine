class CoffeeMachine:
    def __init__(self):
        self.water_in = 400
        self.milk_in = 540
        self.beans_in = 120
        self.cups_in = 9
        self.money_in = 550
        self.resources_needed = {
                        '1': {'water': 250, 'milk': 0, 'coffee_beans': 16, 'price': 4},
                        '2': {'water': 350, 'milk': 75, 'coffee_beans': 20, 'price': 7},
                        '3': {'water': 200, 'milk': 100, 'coffee_beans': 12, 'price': 6},
                        }

    def remaining(self):
        print("The coffee machine has:")
        print(self.water_in, "of water")
        print(self.milk_in, "of milk")
        print(self.beans_in, "of coffee beans")
        print(self.cups_in, "of disposable cups")
        print(f"${self.money_in} of money")

    def check_resources(self, coffee_type):
        if coffee_type not in ["1", "2", "3"]:
            print("Choice is not defined, going to Main Menu!")
            return False
        if self.water_in < self.resources_needed[coffee_type]['water']:
            print("Sorry, not enough water!\n")
            return False
        if self.milk_in < self.resources_needed[coffee_type]['milk']:
            print("Sorry, not enough milk!\n")
            return False
        if self.beans_in < self.resources_needed[coffee_type]['coffee_beans']:
            print("Sorry, not enough coffee beans!\n")
            return False
        if self.cups_in < 1:
            print("Sorry, not enough disposable cups!\n")
            return False
        print("I have enough resources, making you a coffee!\n")
        return True

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choice == "back":
            return
        elif not self.check_resources(choice):
            return
        self.water_in -= self.resources_needed[choice]['water']
        self.milk_in -= self.resources_needed[choice]['milk']
        self.beans_in -= self.resources_needed[choice]['coffee_beans']
        self.cups_in -= 1
        self.money_in += self.resources_needed[choice]['price']

    def fill(self):
        water_add = int(input("Write how many ml of water do you want to add:"))
        milk_add = int(input("Write how many ml of milk do you want to add:"))
        beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
        cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.water_in += water_add
        self.milk_in += milk_add
        self.beans_in += beans_add
        self.cups_in += cups_add

    def take(self):
        print("I gave you $" + str(self.money_in))
        self.money_in = 0

    @staticmethod
    def quit(choice):
        return choice

    def process_coffee_machine(self):
        want_to_exit = False
        while not CoffeeMachine.quit(want_to_exit):
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                want_to_exit = True
            else:
                print("Please write the right action!")


cf = CoffeeMachine()
cf.process_coffee_machine()
