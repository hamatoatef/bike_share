import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


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
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? \n").lower()
        if city in CITY_DATA:
            break
        else:
            print("please enter right input\n")

    while True:
        type_of_analysis = input('Would you like to filter the data by month, day, or both?\n').lower()
        if type_of_analysis in ('month', 'day', 'both'):
            break
        else:
            print('please enter right input\n')

    # TO DO: get user input for month (all, january, february, ... , june)

    if type_of_analysis == "month":
        day = "all"
        while True:
            month = input(
                "\nWhich month would you like to filter by? January, February, March, April, May or June ?\n").lower()
            if month in ('january', 'february', 'march', 'april', 'May', 'june'):
                break
            else:
                print("please enter right input\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif type_of_analysis == 'day':
        month = "all"
        while True:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n").title()
            if day in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
                break
            else:
                print("please enter right input \n")

    elif type_of_analysis == 'both':
        while True:
            month = input(
                "\nWhich month would you like to filter by? January, February, March, April, May or June ?\n").lower()
            if month in ('january', 'february', 'march', 'april', 'May', 'june'):
                break
            else:
                print("please enter right input\n")

        while True:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n").title()
            if day in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
                break
            else:
                print("please enter right input \n")

    print('-' * 40)
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

    # load data file
    file_name = pd.read_csv(CITY_DATA[city])
    df = pd.DataFrame(file_name)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:\n', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:\n', popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common hour:\n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:\n', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('Most Commonly used end station:\n', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('Most Commonly used combination of start station and end station trip:\n', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = sum(df['Trip Duration'])
    print('Total travel time: \n', total_travel / 3600, "hour")
    # TO DO: display mean travel time
    Mean_Travel = df['Trip Duration'].mean()
    print('Mean travel time: \n', Mean_Travel / 60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Counts of User Types: \n', user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_gender = df['Gender'].value_counts()
        print('Counts of Gender: \n', count_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print('Earliest Year of birth :\n', earliest_year)
        most_recent = df['Birth Year'].max()
        print('most Recent Year of birth :\n', most_recent)
        most_common = df['Birth Year'].mode()[0]
        print('most Common Year of birth :\n', most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
