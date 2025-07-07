from models.Rent import Rent
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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