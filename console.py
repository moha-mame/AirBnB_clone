import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    # exit the program
    def EOF(self):
        pass
    def quit(self):
        pass

    # how it works
    def help(self):
        pass

    # execute anything
    def ENTER(self):
        pass

    # create new instance of BaseModel
    def create(self):
        pass
    # prints string representation of instance based on class name and id
    def show(self):
        pass
    # deletes instance based on the class name and id
    def destroy(self):
        pass
    # prints all string representation of all instances based or not onthe class name
    def all(self):
        pass
    # updates instance based on the class name and id
if __name__ == "__main__":
    HBNBCommand().cmdloop()