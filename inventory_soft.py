# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:00:59 2020

@author: 18502
"""

import pandas as pd

def print_mainmenu():
    print('================Test Inventory Soft===============')
    print('\n')
    print('Enter the function number to do selected tasks\n')
    print('1.Add data')
    print('2.Delete Data')
    print('3.Search Data')
    print('4.View Data')
    print('5. Save to file')
    
def add_data(table):
    check='yes'
    while check=='yes':
        pid=input('Enter the product_id ')
        pname=(input('Enter the product name '))
        pquant=(input('Enter the product quantity '))
        newentry={'product_id':[pid],'product_name':[pname],'Quantity':[pquant]}
        new_table=pd.DataFrame(newentry)    
        table=pd.concat([table,new_table],ignore_index=True)
        check=input("Enter yes to add more data Enter no to exit ") 
    return table

def delete_data(table):
    name=input('Enter the product name to delete ')
    return table[table.product_name != name]

def search_data(table):
    name=input('Enter the product name to search ')
    print( table[table.product_name==name] )

def view_data(table):
    print(table)
    
def savetofile(table):
# =============================================================================
#     table=table.reset_index()  #'it adds new column name index'
#     print(table)
#     table=table.drop(['index'],axis=1)  
# =============================================================================
    table.to_csv('C:/Users/18502/Desktop/test/inventory_data.csv',index=False)
    
def loaddata():
    table=pd.read_csv('C:/Users/18502/Desktop/test/inventory_data.csv')
    return table

def main():
    try:
        table=loaddata()
    except:
        tt={'product_id':[],'product_name':[],'Quantity':[]}
        table=pd.DataFrame(tt)
        
    option='run'
    while option!='quit':
        print_mainmenu()
        option=input()
        if option=='1':
            table=add_data(table)
        elif option=='2':
            table=delete_data(table)
        elif option=='3':
            search_data(table)
        elif option=='4':
            view_data(table)
        elif option=='5':
            savetofile(table)



main()