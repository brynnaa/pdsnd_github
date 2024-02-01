import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    #while loop that breaks when user enters a valid city name
    # .lower() to convert user input to all lowercase

    while True:
        city = input("\nWhich city would you like to filter by? new york city, chicago, or washington?\n").lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print("Please enter a valid city name.")
            continue
        # if an invalid city is entered a statement is printed prompting user to retype city name
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    # list variables months defined the available months for user to type
    months = [ 'all', 'january', 'february', 'april', 'may', 'june']
    #while loop to get user to enter desired month
    # .lower() to conver user input to all lowercase
    while True:
        month = input("\nWhat month would you like to filter by?\n").lower()
        # if entered month is in months list variable break otherwise statement is printed asking user to try again
        if month not in months:
            print("Please enter a month january to june, or all")
            continue
        else:
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)\
    #days list variable defining available days for user to input
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    #while loop for user to enter desired day
    #.lower() converts user input into all lowercase
    #if valid day is entered loop breaks
    #if erroneous day is entered a statement is printed requesting the user to try again
    while True:
        day = input("\nWhich day would you like to filter by?\n").lower()
        if day not in days:
            print("Please enter a valid day or all")
            continue
        else:
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
    # load city data
    df = pd.read_csv(CITY_DATA[city])
    # convert to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #create analysis columns for month, day, and hour
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # month filter
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        #day filter
    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #display the most common month
    month_popular = df['month'].mode()[0]
    print('Most Common Month: \n', month_popular)

    # TO DO: display the most common day of week
    #display most common day
    day_popular = df['day'].mode()[0]
    print('Most Common Day: \n', day_popular)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour_popular = df['hour'].mode()[0]
    print('Most Common Start Hour: \n', hour_popular)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_popular = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station: \n', start_station_popular)

    # TO DO: display most commonly used end station
    end_station_popular = df['End Station'].mode()[0]
    print('Most Commonly Used End Station: \n', end_station_popular)

    # TO DO: display most frequent combination of start station and end station trip
    combination_stations = df['Start Station'] + "to" + df['End Station']
    combination_stations_popular = combination_stations.mode()[0]
    print('Most Common Combination of Start and End Stations (Start to End): \n', combination_stations_popular)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #total travel time in seconds
    total_travel_time = df['Trip Duration'].sum()
    # seconds to hours
    print('Total Travel Time = {:} hours'.format(int(total_travel_time / 3600)))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time = {} minutes'.format(int(average_travel_time/60)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Count of User Types: \n', user_type_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print('Count of Genders: \n', genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year_early = df['Birth Year'].min()
        print('Earliest Birth Year: ', int(birth_year_early))
        birth_year_common = df['Birth Year'].mode()[0]
        print('Most Common Birth Year: ', int(birth_year_common))
        birth_year_recent = df['Birth Year'].max()
        print('Most Recent Birth Year: ', int(birth_year_recent))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    while True:
        choices=['yes','no']
        raw_data= input("Would you like to see five rows of raw data? Type 'yes' or 'no'\n").lower()
        if raw_data in choices:
            if raw_data=='yes':
                start=0
                end=6
                print(df.iloc[start:end])
            break
        else:
            print('please try again :)')
    if  raw_data=='yes':
            while True:
                raw_data_2= input("Would you like to see five additional rows of data? Type 'yes' or 'no'\n").lower()
                if raw_data_2 in choices:
                    if raw_data_2=='yes':
                        start+=5
                        end+=5
                        print(df.iloc[start:end])

                    else:
                        break
                else:
                    print('please try again :)')




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
