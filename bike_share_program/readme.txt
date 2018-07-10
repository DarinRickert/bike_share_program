25 # This while loop was adapted from the information on this website: https://stackoverflow.com/questions/23377818/loop-on-if-statement-to-reject-invalid-input
    while True:
        try:
             city = input("Would you like more information on Chicago, New York City or Washington? ").title()
        except ValueError:
             continue
        if city in ("Chicago", "New York City", "Washington"):
             break   
81 # Copied straight from the Udacity practice exercise 
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
117 # This was adapted from the practice exerices on Udacity
    
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
158 # This code was adapted from this source: https://stackoverflow.com/questions/3594514/how-to-find-most-common-elements-of-a-list
    # Creates a dictionary and counts the number of start stations before printing the station with the highest frequency
    start_station_counter = {}
    for station in df['Start Station']:
        if station in start_station_counter:
            start_station_counter[station] += 1
        else:
            start_station_counter[station] = 1
                
    start_stations = sorted(start_station_counter, key = start_station_counter.get, reverse = True)
    popular_start_station = start_stations[:1]
