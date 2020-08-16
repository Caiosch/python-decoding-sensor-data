from load_data import load_sensor_data
from house_info import HouseInfo
from datetime import date, datetime
from temperature_info import TemperatureData


data = []
print("Sensor Data App")

data = load_sensor_data()
print("\nLoaded records: {}".format(len(data)))

house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area('id', rec_area=test_area)
print('\nHouse sensor records from area {} = {}'.format(test_area, len(recs)))
test_date = datetime.strptime('5/9/20', '%m/%d/%y')
recs = house_info.get_data_by_date('id', rec_date=test_date)
print('\nHouse sensor records for date {} = {}'.format(
    test_date.strftime('%m/%d/%y'), len(recs)))

temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)
print('\nHouse Temperature sensor record for area {} = {}'.format(test_area, len(recs)))
print('\nMaximum: {0}, Minimum: {1} temperatures'.format(max(recs), min(recs)))
recs = temperature_data.get_data_by_date(rec_date=test_date)
print('\nHouse Temperature sensor records for date: {} = {}'.format(test_date.strftime('%m/%d/%y'), len(recs)))
print('\nMaximum: {0}, Minimum: {1} temperature'.format(max(recs), min(recs)))
