from abc import ABC, abstractmethod

# Fly Behaviors


class InterfaceFlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyNoWay(InterfaceFlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyWithWings(InterfaceFlyBehavior):
    def fly(self):
        print("I'm flying with wings")


class FlyWithRocket(InterfaceFlyBehavior):
    def fly(self):
        print("I'm flying with a rocket")


# Quack Behaviors


class InterfaceQuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(InterfaceQuackBehavior):
    def quack(self):
        print("Quack")


class Squeak(InterfaceQuackBehavior):
    def quack(self):
        print("Squeak")


class MuteQuack(InterfaceQuackBehavior):
    def quack(self):
        print("<< Silence >>")
