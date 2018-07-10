import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

df_chicago = pd.read_csv(CITY_DATA['chicago'])
df_nyc = pd.read_csv(CITY_DATA['new york city'])
df_washington = pd.read_csv(CITY_DATA['washington'])


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # This while loop was adapted from the information on this website: https://stackoverflow.com/questions/23377818/loop-on-if-statement-to-reject-invalid-input
    while True:
        try:
             city = input("Would you like more information on Chicago, New York City or Washington? ").lower()
        except ValueError:
             continue
        if city in CITY_DATA.keys():
             break   

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "may", "june"]
    
    while True:
        try:
             month = input("Which month would you like to take a look at? (Enter the full name of one of the first six months) ").lower()
        except ValueError:
             continue
        if month in months:
             break   
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    while True:
        try:
             day = input("Which day of the week would you like information on? (Enter the full name of a day of the week) ").lower()
        except ValueError:
             continue
        if day in days:
             break   
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city == "chicago":
        df = pd.read_csv("chicago.csv")
    elif city == "new york city":
        df = pd.read_csv("new_york_city.csv")
    elif city == "washington":
        df = pd.read_csv("washington.csv")
    else:
        get_filters()
    
    # Copied straight from the Udacity practice exercise 
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    # This was adapted from the practice exerices on Udacity
    
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most common month (from 0 to 12)
    popular_month = df['month'].mode()[0]
    
    # TO DO: display the most common day of week
    # This was adapted from the practice exerices on Udacity
    
    # extract day of week from the Start Time column to create a day of week column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # find the most common day of week (from 0 to 7)
    popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    # This was borrowed straight from the practice exerices on Udacity
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    
    print('Most Common Month:', popular_month)
    print('Most Common Day:', popular_day)
    print('Most Frequent Start Hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # This code was adapted from this source: https://stackoverflow.com/questions/3594514/how-to-find-most-common-elements-of-a-list
    # Creates a dictionary and counts the number of start stations before printing the station with the highest frequency
    start_station_counter = {}
    for station in df['Start Station']:
        if station in start_station_counter:
            start_station_counter[station] += 1
        else:
            start_station_counter[station] = 1
                
    start_stations = sorted(start_station_counter, key = start_station_counter.get, reverse = True)
    popular_start_station = start_stations[:1]
     
    print("Most Popular Start Station: ", popular_start_station)

    # TO DO: display most commonly used end station
    end_station_counter = {}
    for station in df['End Station']:
        if station in end_station_counter:
            end_station_counter[station] += 1
        else:
            end_station_counter[station] = 1
                
    end_stations = sorted(end_station_counter, key = end_station_counter.get, reverse = True)
    popular_end_station = start_stations[:1]
     
    print("Most Popular End Station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Combines the Start and End Station dictionaries in order to compare them for the most frequent combination
    station_counter = {}
    for start,end in zip(df['Start Station'], df['End Station']):
        if start and end in station_counter:
            station_counter[start,end] += 1
        else:
            station_counter[start,end] = 1
                
    stations = sorted(station_counter, key = station_counter.get, reverse = True)
    popular_station = stations[:1]
     
    print("Most Frequent Start and End Stations: ", popular_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    
    print("The total travel time is: ", total_travel_time, "s")
    print("The average travel time is: ", average_travel_time, "s")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nNumber of User Types:\n", user_types)

    # TO DO: Display counts of gender
    # Skips data that doesn't contain the field 'Gender'
    while True:
        try: 
            df['Gender']
        except KeyError:
            break
        if "Male" or "Female" in df['Gender']:
                print("\nGender Counts:\n", df['Gender'].value_counts())
                break
        
                
    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try: 
            df['Birth Year']
        except KeyError:
            break
        if 1 or 2 in df['Birth Year']:
            earliest_DOB = int(df['Birth Year'].min())
            most_recent_DOB = int(df['Birth Year'].max())
            most_common_DOB = int(df['Birth Year'].mode())
    
            print("\nEarliest DOB: ", earliest_DOB)
            print("Most Recent DOB: ", most_recent_DOB)
            print("Most Common DOB: ", most_common_DOB)
            break
 
    print("\nNote: Washington does not contain records of either Gender or Birth Year")   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """ Displays raw data upon user request """
    while True:
        try:
            ask_raw = input('\nWould you like to see raw data from the selected city? Enter yes or no.\n').lower()
        except ValueError:
            continue
        if ask_raw == "yes":
            print(df.head(5))
            break
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
