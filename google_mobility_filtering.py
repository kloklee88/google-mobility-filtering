# google_mobility_filtering.py - Parses and filters the desired records from Google Mobility Report CSV

import time
import csv
import traceback
import sys
from datetime import datetime
from datetime import timedelta


class Record:
    def __init__(self, country_region_code, country_region, sub_region_1, sub_region_2, metro_area, iso_3166_2_code, census_fips_code, date, retail_and_recreation_percent_change_from_baseline, grocery_and_pharmacy_percent_change_from_baseline, parks_percent_change_from_baseline, transit_stations_percent_change_from_baseline, workplaces_percent_change_from_baseline, residential_percent_change_from_baseline):
        self.country_region_code = country_region_code
        self.country_region = country_region
        self.sub_region_1 = sub_region_1
        self.sub_region_2 = sub_region_2
        self.metro_area = metro_area
        self.iso_3166_2_code = iso_3166_2_code
        self.census_fips_code = census_fips_code
        self.date = date
        self.retail_and_recreation_percent_change_from_baseline = retail_and_recreation_percent_change_from_baseline
        self.grocery_and_pharmacy_percent_change_from_baseline = grocery_and_pharmacy_percent_change_from_baseline
        self.parks_percent_change_from_baseline = parks_percent_change_from_baseline
        self.transit_stations_percent_change_from_baseline = transit_stations_percent_change_from_baseline
        self.workplaces_percent_change_from_baseline = workplaces_percent_change_from_baseline
        self.residential_percent_change_from_baseline = residential_percent_change_from_baseline

    def __iter__(self):
        return iter([self.country_region_code,
                     self.country_region,
                     self.sub_region_1,
                     self.sub_region_2,
                     self.metro_area,
                     self.iso_3166_2_code,
                     self.census_fips_code,
                     self.date,
                     self.retail_and_recreation_percent_change_from_baseline,
                     self.grocery_and_pharmacy_percent_change_from_baseline,
                     self.parks_percent_change_from_baseline,
                     self.transit_stations_percent_change_from_baseline,
                     self.workplaces_percent_change_from_baseline,
                     self.residential_percent_change_from_baseline])


def read_csv():
    # Read records into CSV
    records = []
    with open('Global_Mobility_Report.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skips the header
        for row in reader:
            records.append(Record(row[0], row[1], row[2],
                                  row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))
    return records


def write_csv(csv_name, records):
    # Store records into CSV file
    with open(csv_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['country_region_code', 'country_region','date', 'retail_and_recreation_percent_change_from_baseline',
                         ])
        #writer.writerow(['country_region_code', 'country_region', 'sub_region_1', 'sub_region_2', 'metro_area', 'iso_3166_2_code', 'census_fips_code', 'date', 'retail_and_recreation_percent_change_from_baseline', 'grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline', 'transit_stations_percent_change_from_baseline', 'workplaces_percent_change_from_baseline', 'residential_percent_change_from_baseline'])
        for record in records:
            writer.writerow([record.country_region_code, record.country_region, record.date, record.retail_and_recreation_percent_change_from_baseline])
            #writer.writerow(record)


def filter_csv():
    print('Starting google mobility filtering script')
    start_time = datetime.now()
    try:
        filtered_records = []
        records = read_csv()
        for record in records:
            if '' in record.sub_region_1:
                filtered_records.append(record)
    except Exception as e:
        print("ERROR! did not complete filtering")
        print(e)
        traceback.print_exc()
    finally:
        write_csv('Global_Mobility_Report_Filtered.csv', filtered_records)
        completion_time = datetime.now() - start_time
        print(f'Time to complete (seconds): {completion_time.seconds}')
        print('Finished price automation script')


# Run program
filter_csv()
