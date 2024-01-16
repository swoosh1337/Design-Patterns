from abc import ABC, abstractmethod

# product interface
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass



# concrete Product 1
class WindowsButton(Button):
    def render(self):
        print("Rendering Windows button!")


    def onClick(self, f):
        print("Windows button has been clicked!")


# concrete Product 2
class HTMLButton(Button):
    def render(self):
        print("Rendering HTML button")

    def onClick(self, f):
        print("HTML button has been clicked!")



# creator Class
class Dialog(ABC):
    @abstractmethod
    def createButton(self):
        pass

    def render(self):
        okButton = self.createButton()
        okButton.onClick(lambda: print("closing dialog"))



# concrete Creator 1
class WindowsDialog(Dialog):
    def createButton(self):
        return WindowsButton()

# concrete Creator 2
class WebDialog(Dialog):
    def createButton(self):
        return HTMLButton()


# Application Class
class Application:
    def __init__(self):
        self.dialog = None

    def initialize(self):
        config_OS = self.readApplicationConfigFile()

        if config_OS == "Windows":
            self.dialog = WindowsDialog()
        elif config_OS == "Web":
            self.dialog = WebDialog()
        else:
            raise Exception("Error! Unknown operating system.")

    def readApplicationConfigFile(self):
        # Simplified configuration reading, in real scenario, it should read from a config file
        return "Windows"  # or "Web"

    def main(self):
        self.initialize()
        self.dialog.render()

# Running the application
app = Application()
app.main()
