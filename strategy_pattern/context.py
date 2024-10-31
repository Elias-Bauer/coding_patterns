from __future__ import annotations

from strategy_pattern.strategy import (
    FlyNoWay,
    FlyWithWings,
    InterfaceFlyBehavior,
    InterfaceQuackBehavior,
    Quack,
    Squeak,
)


class Duck:
    fly_behavior: InterfaceFlyBehavior
    quack_behavior: InterfaceQuackBehavior

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
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
