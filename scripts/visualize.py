from models.Rent import Rent
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def visualize_rents_per_year():
    rent=Rent()
    data=rent.show_rents_per_year()

    df=pd.DataFrame(data)


    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='mesec', y='broj_rentiranja', hue='godina', marker='o')
    plt.title("Rentiranja po mesecima i godinama")
    plt.xlabel("Mesec")
    plt.ylabel("Broj rentiranja")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def visualize_rents_per_month():
    rent=Rent()
    data=rent.show_rents_per_month()

    df=pd.DataFrame(data)

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='mesec', y='broj_rentiranja', marker='o')
    plt.title("Rentiranje po mesecima")
    plt.xlabel("Mesec")
    plt.ylabel("Broj rentiranja")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_rents_per_day():
    rent=Rent()
    data=rent.get_all_rented_dates()

    df=pd.DataFrame(data)

    df['rented_at']=pd.to_datetime(df['rented_at'])

    df['year']=df['rented_at'].dt.year
    df['month']=df['rented_at'].dt.month
    df['day_of_week']=df['rented_at'].dt.day_name()

    month_view=df.groupby(['month']).size().reset_index(name='no_rents')


    most_active_month=month_view.sort_values('no_rents',ascending=False).iloc[0]

    mesec_max=most_active_month['month']
    name_of_month=datetime(1900,mesec_max,1).strftime('%B')

    print(f"Mesec sa najvise rentiranja je {mesec_max} sa {most_active_month['no_rents']} rentiranja")

    df_month=df[df['month'] == mesec_max]

    week_view=df_month.groupby('day_of_week').size().reset_index(name='no_rents')

    most_active_day=week_view.sort_values('no_rents',ascending=False).iloc[0]

    print(f"Dan sa najvise rentiranja u {mesec_max} mesecu je {most_active_day['day_of_week']} sa {most_active_day['no_rents']} rentiranja")


    days_of_week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    week_view['day_of_week']=pd.Categorical(week_view['day_of_week'],categories=days_of_week,ordered=True)
    week_view=week_view.sort_values('day_of_week')



    plt.figure(figsize=(10, 5))
    sns.barplot(data=week_view, x='day_of_week', y='no_rents', palette='Set2')
    plt.title(f'Broj rentiranja po danima u nedelji u mesecu sa najvise rentiranja. Mesec sa najvise rentiranja je {name_of_month} sa {most_active_month['no_rents']} rentiranja.')
    plt.xlabel('Day of week')
    plt.ylabel('Number of rents')
    plt.tight_layout()
    plt.show()


