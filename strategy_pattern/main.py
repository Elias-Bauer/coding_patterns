from __future__ import annotations

from abc import ABC, abstractmethod

# Strategy #####################################################################

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


# Client #######################################################################


class Duck:
    fly_behavior: InterfaceFlyBehavior
    quack_behavior: InterfaceQuackBehavior

    def performFly(self):
        self.fly_behavior.fly()

    def performQuack(self):
        self.quack_behavior.quack()

    def display(self):
        pass

    def setflybehavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def setquackbehavior(self, quack_behavior):
        self.quack_behavior = quack_behavior


# Concrete Ducks


class MallardDuck(Duck):
    fly_behavior = FlyWithWings()
    quack_behavior = Quack()

    def display(self):
        print("I'm a Mallard Duck")


class RedheadDuck(Duck):
    fly_behavior = FlyNoWay()
    quack_behavior = Squeak()

    def display(self):
        print("I'm a Redhead Duck")


# Main #########################################################################


def main():
    mallard = MallardDuck()
    redhead = RedheadDuck()

    mallard.display()
    mallard.performFly()
    mallard.performQuack()

    redhead.display()
    redhead.performFly()
    redhead.performQuack()

    mallard.setflybehavior(FlyWithRocket())
    mallard.performFly()

    redhead.setquackbehavior(MuteQuack())
    redhead.performQuack()


if __name__ == "__main__":
    main()
