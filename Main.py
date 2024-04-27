from Airbnb import AirbnbManager

if __name__ == '_main__':
    airbnb = AirbnbManager('test.csv')
    airbnb.write_to_csv()

