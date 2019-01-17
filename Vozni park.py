#class za izdelavo objektov


class Vehicle:
    def __init__(self, manufacturer, model, kilometers, last_servis):
        self.manufacturer = manufacturer
        self.model = model
        self.kilometers = kilometers
        self.last_servis = last_servis

    def get_full_model_name(self):
        return self.manufacturer + " " + self.model

#funkcija za ispisovanje seznama


def list_all_cars(car):
    for index, car in enumerate(car):
        print "Stevilka avtomobila: " + str(index+1)
        print car.get_full_model_name()
        print "Prevozeni kilometri: \n %s " % (car.kilometers)
        print "Zadnji servis narejen na dan %s " % (car.last_servis)
        print ""

#funkcija za dodajane


def add_car(car):
    manufacturer = raw_input("Prosim vpisite proizvajalca avtomobila: ")
    model = raw_input("Prosim vpisite model avtomobila: ")
    kilometers = raw_input("Prosim vpisite prevozene kilometre avtomobila: ")
    last_service = raw_input("Prosim vpisite kilometre kdaj je bil narejen zadnji servis: ")
    answer = raw_input("ali ste prericani da hocete dodat avtomobil? (da/ne) ")

    if answer == "da":
        new = Vehicle(manufacturer=manufacturer, model=model, kilometers=kilometers, last_servis=last_service)
        car.append(new)
    else:
        print "Dodajanje ni bilo vpesno."
#funkcija za brisanje iz seznama


def remove_car(car):
    print "Izberite stevilko avtomobila, ki bi ga radi odstranili iz voznega parka:"

    for index, cars in enumerate(car):
        print str(index+1) + ") " + cars.get_full_model_name()

    select_id = raw_input("Katero vozilo bi radi odstranili iz voznega parka (Vpisite stevilko vozila): ")
    selected_cars = car[int(select_id) - 1]
    answer = raw_input("Ali ste prepricani da zelite odstraniti avtomobil? (da/ne) ")

    if answer == "da":
        car.remove(selected_cars)
        print "Vozilo je bilo vspesno odstranjeno."
    else:
        print "Vozilo ni bilo vspesno odstranjeno."


#funkncija za urejanje kilometrov

def set_kilometers(car):
    print "Izberite stevilko avtomobila, ki bi mu radi spremenili prevozene kilometre: "

    for index, cars in enumerate(car):
        print str(index+1) + ")" + cars.get_full_model_name()

    selected_id = raw_input("Kateremu vozilu bi radi spremenili prevozene kilometre (Vpisite stevilko vozila): ")
    selected_car = car[int(selected_id) - 1]

    new_kilometers = raw_input("Prosim vpisite nove prevozene kilometre za vozilo %s: " % selected_car.get_full_model_name())
    selected_car.kilometers = new_kilometers


def set_last_service(car):
    print "Izberite stevilko avtomobila, ki bi mu radi spremenili datum zadnjega servisa: "

    for index, cars in enumerate(car):
        print str(index+1) + ")" + cars.get_full_model_name()

    select_id = raw_input("Kateremu vozilu bi radi spremenili datum zadnjega servisa (Vpisite stevilko vozila): ")
    selected_cars = car[int(select_id) - 1]

    new_servis = raw_input("Prosim vpisite datum kdaj je bil narejen zadnji servis na (DD/MM/LLLL) %s: " % selected_cars.get_full_model_name())
    selected_cars.last_servis = new_servis

#Funkcija za pisanje v zunanje detoteke

def write_txt(car):
    print "Seznam vozil bo shranjen v zunanjo TXT detoteko."

    cars_file = open("Vehicle.txt", "w+")
    cars_file.write("Seznam vozil:\n \n")
    for index, car in enumerate(car):
        cars_file.write("Stevilka avtomobila: " + str(index+1))
        cars_file.write("\n")
        cars_file.write("%s \n" % (car.get_full_model_name()))
        cars_file.write("Prevozeni kilometri:  %s \n " % (car.kilometers))
        cars_file.write("Zadnji servis narejen na dan %s \n" % (car.last_servis))
        cars_file.write("\n")
    cars_file.close()


def main():
    print "Dobrodosli v Organizatorju Voznega Parka."
    print ""

    bmw = Vehicle(manufacturer="BMW", model="Serija 5", kilometers=195500, last_servis="15/08/2018")
    mercedes = Vehicle(manufacturer="Mercedes-Benz", model="S-Class", kilometers=150000, last_servis="15/05/2018")
    wv = Vehicle(manufacturer="Volkswagen", model="Transporter", kilometers=250800, last_servis="15/05/2018")

    car = [bmw, mercedes, wv]


    while True:
        print "Prosim izberitre eno od moznosti:"
        print "" #Prazna vrstica
        print "a) Seznam vseh vozil"
        print "b) Dodaj nov avtomobil"
        print "c) Odstrani vozilo iz voznega parka"
        print "d) Uredi prevozene kilometre"
        print "e) Uredi datum zadnejga servisa"
        print "f) Shranite seznam v zunanjo TXT detoteko"
        print "g) Zapustite program"
        print "" #prazna vrstica

        select = raw_input("Vpisite vaso izbiro (a, b, c, d, e, f ali g): ")

        if select.lower() == "a":
            list_all_cars(car)
        elif select.lower() == "b":
            add_car(car)
        elif select.lower() == "c":
            remove_car(car)
        elif select.lower() == "d":
            set_kilometers(car)
        elif select.lower() == "e":
            set_last_service(car)
        elif select.lower() == "f":
            write_txt(car)
        elif select.lower() == "g":
            print "END"
            break
if __name__ == "__main__":
    main()