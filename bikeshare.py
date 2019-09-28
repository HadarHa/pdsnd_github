import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    city= input('Would you like to see data for Chicago, New York, or Washington? ').lower()
    
    while True:
        if (city == 'new york' or city == 'washington' or city == 'chicago'):
            break
        else:
            city= input('Please try again- Would you like to see data for Chicago, New York, or Washington? ')
            city= city.lower()
            continue
    month= input('Please enter the name of the month to filter by, or enter \"all\" to apply no month filter: ')
    month= month.title()
    if (month != 'All'):
        while True:
            if (month == 'January' or  month == 'February' or month == 'March' or month== 'April'or month == 'May' or month == 'June' or month == 'July' or month == 'August' or month == 'September'  or month == 'October' or month == 'November' or month == 'December'):
                break
            else:
                month= input('Please try again-Please enter the name of the month to filter by, or enter \"all\" to apply no month filter: ')
                month= month.title()
                continue
    day= input('Please enter the name of the day of week to filter by, or \"all\" to apply no day filter: ')
    day= day.title()
    if (day != 'All'):
        while True:
            if (day == 'Sunday' or day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday'):
                break
            else:
                day= input('Please try again- Please enter the name of the day of week to filter by, or \"all\" to apply no day filter: ')
                day= day.title()
                continue
    return (city, month, day)
    print('-'*40)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data not filtered by month and day
        df_filter- Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month == 'All':
        df_filtered = df
    else:
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df_filtered = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df_filtered = df_filtered[df_filtered['day_of_week'] == day.title()]

    return df, df_filtered


def time_stats(df):
    """Displays statistics  most frequent times of travel- df (not filtered)"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month: ' + str(popular_month))
    print()

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week: ' + str(popular_day))
    print()

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour: ' +  str(popular_hour))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df_filtered):
    """Displays statistics on the most popular stations and trip- df_filtered"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start_st= df_filtered['Start Station'].value_counts().index[0]
    print('The Most Popular Start Station is: ' + most_popular_start_st)
    print('Count: ' + str(df_filtered['Start Station'].value_counts()[0]))
    print()

    # TO DO: display most commonly used end station
    most_popular_end_st= df_filtered['End Station'].value_counts().index[0]
    print('The Most Popular End Station is: ' +most_popular_end_st)
    print('Count: ' + str(df_filtered['End Station'].value_counts()[0]))
    print()

    # TO DO: display most frequent combination of start station and end station trip
    df_filtered['Trip']= df_filtered['Start Station'] + ' to ' + df_filtered['End Station']
    most_popular_Trip_st= df_filtered['Trip'].value_counts().index[0]
    print('The Most Frequent Combination of Start Station and End Station Trip: ' + most_popular_Trip_st)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df_filtered):
    """Displays statistics on the total and average trip duration- df_filtered"""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration_sum= df_filtered['Trip Duration'].sum()
    print('Total Travel Time: ' +  str(trip_duration_sum))
    print()

    # TO DO: display mean travel time
    trip_duration_mean= df_filtered['Trip Duration'].mean()
    print('Avgeage travel time: ' + str(trip_duration_mean))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df_filtered, city):
    """Displays statistics on bikeshare users- df filtered"""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Display Counts of User Types:')
    print(df_filtered['User Type'].value_counts())
    print()


    # TO DO: Display counts of gender

    if (city != 'washington'):
        print('Display Counts of Gender:')
        print(df_filtered['Gender'].value_counts())
        print()

        # TO DO: Display earliest, most recent, and most common year of birth
        #most common
        common_year= df_filtered['Birth Year'].mode()[0]
        print('Most Common Year of Birth: ', int(common_year))
        print()

        #earliest birth year
        min_year= df_filtered['Birth Year'].min()
        print('The Earliest Birth Year is: ', int(min_year))
        print()

        #most recent birth year
        max_year= df_filtered['Birth Year'].max()
        print('The Most Recent Birth Year is: ', int(max_year))
        print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_dis(df_filtered):
    """present 5 lines of data per user request"""
    answer= input('do you want to see raw data, asnwer \'yes\' or \'no\'? ')
    answer= answer.lower()
    i= 0
    if (answer =='no'):
        print('Your answer is \'no\' - thank you')
    else:
        while True:
            while (answer == 'yes'):
                print('please see below 5 lines:')
                print(df_filtered.iloc[[i,i+1,i+2, i+3, i+4]])
                print()
                i+=5
                answer= input('do you want to see additional 5 lines, asnwer \'yes\' or \'no\'? ')
                answer= answer.lower()
            if (answer !='yes') and (answer!='no'):
                answer= input('please neter anser again- do you want to see raw data, asnwer \'yes\' or \'no\'? ')
                answer= answer.lower()
                continue
            elif (answer == 'no'):
                print('Your answer is \'no\' - thank you')
                break

def main():
    while True:
        city, month, day = get_filters()
        df, df_filtered = load_data(city, month, day)

        time_stats(df)
        station_stats(df_filtered)
        trip_duration_stats(df_filtered)
        user_stats(df_filtered, city)
        data_dis(df_filtered)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
