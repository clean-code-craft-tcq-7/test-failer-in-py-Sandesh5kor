

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def HighPrecipitationsensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 40
    }

def BadWeatherSensorStub():
    return {
        'temperatureInC': 40,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 80
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] >= 25):
        if readings['precipitation'] < 20:
            weather = "Sunny Day"
        elif readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['precipitation'] >= 60 and readings['windSpeedKMPH'] < 50:
            weather = "Rainy"
        elif readings['precipitation'] >= 60 and readings['windSpeedKMPH'] >= 50:
            weather = "Alert, Stormy with heavy rain"
    else:
        weather = "Cool Day"
    return weather


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    weather = report(HighPrecipitationsensorStub)

    assert(len(weather) > 0)
    assert("Rainy" in weather)

def testBadWeather():
    weather = report(BadWeatherSensorStub)
    print(weather)
    assert(len(weather) > 0)
    assert('Alert' in weather)

if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    testBadWeather()
    print("All is well (maybe!)");
