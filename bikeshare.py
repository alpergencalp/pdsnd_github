import time
import pandas as pd
import numpy as np
from datetime import timedelta

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    month_choice_int = 0
    day_choice = 'all'
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_choice = input('Would you like to see data for Chicago, New York City or Washington?\n').lower()
    while city_choice not in CITY_DATA:
          city_choice = input('Wrong input, choose one of Chicago, New York City or Washington?\n').lower()
    print('Looks like you want to hear about {}! If this is not true, restart the program now.\n'.format(city_choice.title()))                   
    ask_user_for_data(city_choice, month_choice_int, day_choice)
    
    # TO DO: get user input for time filter (month,day,none)
    time_filter_choice = input('Would you like to fiter the data by month, day or not at all? Type "none" for no time filter.\n').lower()
    while time_filter_choice not in ('month','day','none'):
          time_filter_choice = input('Wrong input, choose one of month, day or none.\n').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    
    #if case is checking for the right month choice of user.
    if time_filter_choice == 'month':
        month_choice = input('Which month? January, February, March, April, May or June?\n').lower()
        while month_choice not in months:
              month_choice = input('Wrong input, choose one of January, February, March, April, May or June.\n').lower()
        month_choice_int = months.index(month_choice) + 1
        print('Looks like you want to filter by {}! If this is not true, restart the program now.\n'.format(month_choice_int))      
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #if case is checking for the right day choice of user.
    if time_filter_choice == 'day':
        day_choice = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.\n').title()
        while day_choice not in days:
              day_choice = input('Wrong input, choose one of Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.\n').title()
        print('Looks like you want to filter by {}! If this is not true, restart the program now.\n'.format(day_choice))   
    ask_user_for_data(city_choice, month_choice_int, day_choice)
    
    city = city_choice
    month = month_choice_int
    day = day_choice
   
#print(city + ',' + month + ',' + day) 
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 0:
         df = df[df['month'] == month]
    if day != 'all':
         df = df[df['day_of_week'] == day]
    return df

def ask_user_for_data(city, month,day):
#this function is asking user for printing extra data.
    DataFrame = load_data(city, month, day)
    row_count = 5
    print(DataFrame.head(row_count))
    continue_choice = input('Would you like to see more data? Yes or No\n').lower()
    while continue_choice == 'yes':
          row_count+=5
          print(DataFrame.head(row_count))
          continue_choice = input('Would you like to see more data? Yes or No\n').lower()


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    popular_month = months[popular_month-1].title()
    print('Most popular month for travelling: {}'.format(popular_month)) 
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most popular day for travelling: {}'.format(popular_day)) 
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour of the day to start your travels: {}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station for travelling: {}'.format(popular_start_station)) 
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station for travelling: {}'.format(popular_end_station)) 
    # TO DO: display most frequent combination of start station and end station trip
    df['popular_trip_combination'] = df['Start Station'] +'/' + df['End Station']
    popular_trip_combination = df['popular_trip_combination'].mode()[0]
    print('Most popular start and end station for travelling: {}'.format(popular_trip_combination)) 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/3600
    print('Total travelling time in hours: {}\n'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/3600
    print('Average time spent on each trip in hours: {}\n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types are:\n{}\n'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns.values.tolist():
        gender_types = df['Gender'].value_counts()
        print('Gender types are:\n{}\n'.format(gender_types))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns.values.tolist():
        youngest = df['Birth Year'].max()
        print('Earliest year of birth::\n{}\n'.format(youngest))
        oldest = df['Birth Year'].min()
        print('Oldest year of birth::\n{}\n'.format(oldest))
        most_common = df['Birth Year'].mode()[0]
        print('Most common year of birth::\n{}\n'.format(most_common))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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