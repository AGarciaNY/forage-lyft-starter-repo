from new_car import Car

# engines
from engines.capulet_engine import CapuletEngine
from engines.sterman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

# batterys
from batterys.nubbin import NubbinBattery
from batterys.spindler import SpidlerBatter


class CarFactory():
    def create_calliope(slefCalliope, current_date, last_service_date, current_mileage, last_service_mileage):
        newCar = Car(CapuletEngine(last_service_mileage, current_mileage), SpidlerBatter(last_service_date, current_date))
        return newCar

    def create_glissade(selfGlissade, current_date, last_service_date, current_mileage, last_service_mileage):
        newCar = Car(WilloughbyEngine(last_service_mileage, current_mileage), SpidlerBatter(last_service_date, current_date))
        return newCar

    def create_palindrome(selfPalindrome, current_date, last_service_date, warning_light_on):
        newCar = Car(SternmanEngine(warning_light_on), SpidlerBatter(last_service_date, current_date))
        return newCar

    def create_rorschach(selfRorschach, current_date, last_service_date, current_mileage, last_service_mileage):
        newCar = Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))
        return newCar

    def create_thovex(selfThovex, current_date, last_service_date, current_mileage, last_service_mileage):
        newCar = Car(CapuletEngine(last_service_mileage,current_mileage), NubbinBattery(last_service_date, current_date))
        return newCar