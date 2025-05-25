from __future__ import annotations

from abc import ABC, abstractmethod

# Interface(s) #################################################################


class InterfaceSubject(ABC):
    @abstractmethod
    def register_observer(self, observer: InterfaceObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: InterfaceObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class InterfaceObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class InterfaceDisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


# WeatherData ##################################################################


class WeatherData(InterfaceSubject):

    def __init__(self):
        self.observer_list: list[InterfaceObserver] = []
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0

    def register_observer(self, observer: InterfaceObserver):
        self.observer_list.append(observer)

    def remove_observer(self, observer: InterfaceObserver):
        self.observer_list.remove(observer)

    def notify_observers(self):
        for observer in self.observer_list:
            observer.update()

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def get_temperature(self) -> float:
        return self.temperature

    def get_humidity(self) -> float:
        return self.humidity

    def get_pressure(self) -> float:
        return self.pressure

    def set_temperature(self, temperature: float):
        self.temperature = temperature
        self.measurements_changed()

    def set_humidity(self, humidity: float):
        self.humidity = humidity
        self.measurements_changed()

    def set_pressure(self, pressure: float):
        self.pressure = pressure
        self.measurements_changed()


# CurrentConditionsDisplay #####################################################
class CurrentConditionsDisplay(InterfaceObserver, InterfaceDisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.weather_data: WeatherData = weather_data
        weather_data.register_observer(self)

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.display()

    def display(self):
        print(
            f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity"
        )


# StatisticsDisplay ###########################################################
class StatisticsDisplay(InterfaceObserver, InterfaceDisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.min_temperature: float | None = None
        self.average_temperature: float | None = None
        self.max_temperature: float | None = None
        self.temperature: list[float] = []
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        new_temperature = self.weather_data.get_temperature()
        self.temperature.append(new_temperature)
        if self.min_temperature is None or new_temperature < self.min_temperature:
            self.min_temperature = new_temperature
        if self.max_temperature is None or new_temperature > self.max_temperature:
            self.max_temperature = new_temperature
        self.average_temperature = sum(self.temperature) / len(self.temperature)

        self.display()

    def display(self):
        print(
            f"Min/Avg/Max temperature = {self.min_temperature}/{self.average_temperature}/{self.max_temperature}"
        )


# Main ########################################################################
def main():
    weather_data = WeatherData()
    current_condition_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)


if __name__ == "__main__":
    main()
    print("Observer Pattern Example Completed")
