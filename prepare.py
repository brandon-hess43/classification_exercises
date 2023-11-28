import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


def prep_iris(df):
    """
    write meaningful docstrings
    """
    df = df.drop(columns=['species_id','measurement_id'])
    df = df.rename(columns={"species_name":'species'})
    
    return df

def clean_titanic(df):
    """
    students - write docstring
    """
    #drop unncessary columns
    df = df.drop(columns=['embarked', 'age','deck', 'class'])
    
    #made this a string so its categorical
    df.pclass = df.pclass.astype(object)
    
    #filled nas with the mode
    df.embark_town = df.embark_town.fillna('Southampton')
    
    return df

def prep_telco(df):
    '''
    please write good docstrings
    '''
    df = df.drop(columns = ['payment_type_id','internet_service_type_id','contract_type_id'])
    df.total_charges = df.total_charges.str.replace(' ', '0.0')
    
    return df

def splitting_data(df, col):
    '''
    i will write a docstring, like send in target variable
    '''

    #first split
    train, validate_test = train_test_split(df,
                     train_size=0.6,
                     random_state=123,
                     stratify=df[col]
                    )
    
    #second split
    validate, test = train_test_split(validate_test,
                                     train_size=0.5,
                                      random_state=123,
                                      stratify=validate_test[col]
                        
                                     )
    return train, validate, test