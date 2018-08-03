import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all','jan','feb','march','april','may','june']
DAYS = ['all','sun','mon','tue','wed','thu','fri','sat']

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
    city = input("Enter city name to get the bikeshare data Chicago, New York City, Washington\n")
    
    while city.lower() not in CITY_DATA.keys():
        city = input("Invalid input. Try again\n")
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input("Enter months from \n"+' '.join(MONTHS)+"\n")
    while month.lower() not in MONTHS:
        month = input("\nInvalid input. Try again\n")
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter days from "+' '.join(DAYS)+"\n")
    while day.lower() not in DAYS:
      day = input("\nInvalid input. Try again\n")
    
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
    city = city.lower()
    df = pd.read_csv(CITY_DATA[city])
    if month=='all' and day=='all':
    	df = df
    if month!='all' and day=='all':
        month_index = MONTHS.index(month)
        df = df.loc[pd.to_datetime(df['Start Time']).dt.month==month_index]
    elif month!='all' and day!='all':
        month_index = MONTHS.index(month)
        day_index = DAYS.index(day)-1
        df = df.loc[(pd.to_datetime(df['Start Time']).dt.month==month_index) & (pd.to_datetime(df['Start Time']).dt.dayofweek==day_index)]
    #print (df.head())
 
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    #start_time = time.time()
    
    # TO DO: display the most common month
    common_month = pd.to_datetime(df['Start Time']).dt.month
    print("\nMost common month of travel %s\n" % (common_month.mode()[0]))
    
    # TO DO: display the most common day of week
    common_dayofweek = pd.to_datetime(df['Start Time']).dt.dayofweek
    print('\nMost common day of week of travel %s\n' % (common_dayofweek.mode()[0]))
    
    # TO DO: display the most common start hour
    common_hour = pd.to_datetime(df['Start Time']).dt.hour
    print('\nMost common hour of travel %s\n' % (common_hour.mode()[0]))
    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    #start_time = time.time()

    # TO DO: display most commonly used start station
    #commom_start_station = df['Start Station'].mode()[0]
    print('\nMost common start station %s\n' % (df['Start Station'].mode()[0]))
    # TO DO: display most commonly used end station
    #commom_end_station = df['End Station'].mode()[0]
    print('\nMost common end station %s\n' % (df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    commom_combo_station = df['Start Station'] + df['End Station']
    #print(commom_combo_station.mode()[0])
    print('\nMost common combination of start and end station %s\n' % (commom_combo_station.mode()[0]))


    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\nTotal travel time %s\n" % (df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("\nMean Travel time %s\n" % (df['Trip Duration'].mean()))

    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    #print('\nCalculating User Stats...\n')
    #start_time = time.time()
    # TO DO: Display counts of user types
    print("\nCount of each user type\n %s" % (df['User Type'].value_counts()))
    #print(df.head())
    # TO DO: Display counts of gender 
    if 'Gender' in df.columns:
        print("\nCount Of gender of each type\n %s" % (df['Gender'].value_counts()))
    else:
        print("No Gender for selected file")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\nOldest Persons birth year %s \n" % (df['Birth Year'].min()))
        print("\nYoungest Persons birth year %s\n" % (df['Birth Year'].max()))
        print("\nMost common birth year %s \n" % (df['Birth Year'].mode()[0]))
    else:
        print("No Birth Year for selected file")

    #print("\nThis took %s seconds." % (time.time() - start_time))

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
