from strategy_pattern import context, strategy


def main():
    mallard = context.MallardDuck()
    redhead = context.RedheadDuck()

    mallard.display()
    mallard.fly()
    mallard.quack()

    redhead.display()
    redhead.fly()
    redhead.quack()

    mallard.setflybehavior(strategy.FlyWithRocket())
    mallard.fly()

    redhead.setquackbehavior(strategy.MuteQuack())
    redhead.quack()


if __name__ == "__main__":
    main()
