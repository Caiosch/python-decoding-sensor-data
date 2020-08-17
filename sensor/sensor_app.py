from datetime import date, datetime
from statistics import mean
from load_data import load_sensor_data
from house_info import HouseInfo
from temperature_info import TemperatureData
from humidity_info import HumidityData
from particle_count_info import ParticleData
from energy_info import EnergyData


data = []
print("Sensor Data App")
print('-' * 15)

data = load_sensor_data()
print("\nLoaded records: {}".format(len(data)))

house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area('id', rec_area=test_area)
print('\t- House sensor records from area {} = {}'.format(test_area, len(recs)))
test_date = datetime.strptime('5/9/20', '%m/%d/%y')
recs = house_info.get_data_by_date('id', rec_date=test_date)
print('\t- House sensor records for date {} = {}'.format(
    test_date.strftime('%m/%d/%y'), len(recs)))

temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)
print('\n\nHouse Temperature sensor record for area {} = {}'.format(
    test_area, len(recs)))
print('\t- Maximum: {0}, Minimum: {1} temperatures'.format(max(recs), min(recs)))
recs = temperature_data.get_data_by_date(rec_date=test_date)
print('\nHouse Temperature sensor records for date: {} = {}'.format(
    test_date.strftime('%m/%d/%y'), len(recs)))
print('\t- Maximum: {0}, Minimum: {1} temperature'.format(max(recs), min(recs)))

humidity_data = HumidityData(data)
recs = humidity_data.get_data_by_area(rec_area=test_area)
print('\n\nHouse Humidity sensor records for area {} = {}'.format(
    test_area, len(recs)))
print('\t- Average: {} humidity'.format(mean(recs)))
recs = humidity_data.get_data_by_date(rec_date=test_date)
print('\nHouse Humidity sensor records for date: {} = {}'.format(
    test_date.strftime('%m/%d/%y'), len(recs)))
print('\t- Average: {} humidity'.format(mean(recs)))

particle_data = ParticleData(data)
recs = particle_data.get_data_by_area(rec_area=test_area)
print('\n\nHouse Particle Sensor records for area {} = {}'.format(
    test_area, len(recs)))
concentrations = particle_data.get_data_concentrations(data=recs)
print('\t- Good Air Quality Recs: {}'.format(concentrations['good']))
print('\t- Moderate Air Quality Recs: {}'.format(concentrations['moderate']))
print('\t- Bad Air Quality Recs: {}'.format(concentrations['bad']))
recs = particle_data.get_data_by_date(rec_date=test_date)
print('\nHouse Particle sensor records for date: {} = {}'.format(
    test_date.strftime('%m/%d/%y'), len(recs)))
concentrations = particle_data.get_data_concentrations(data=recs)
print('\t- Good Air Quality Recs: {}'.format(concentrations['good']))
print('\t- Moderate Air Quality Recs: {}'.format(concentrations['moderate']))
print('\t- Bad Air Quality Recs: {}'.format(concentrations['bad']))

energy_data = EnergyData(data)
recs = energy_data.get_data_by_area(rec_area=test_area)
print('\n\nHouse Energy sensor records for area {} = {}'.format(test_area, len(recs)))
total_energy = energy_data.calculate_energy_usage(data=recs)
print('\t- Energy Usage: {:2.2} Watts'.format(total_energy))
recs = energy_data.get_data_by_date(rec_date=test_date)
print('\nHouse Energy sensor records for date: {} = {}'.format(
    test_date.strftime("%m/%d/%y"), len(recs)))
total_energy = energy_data.calculate_energy_usage(data=recs)
print('\t- Energy Usage: {:2.2} Watts\n\n'.format(total_energy))
