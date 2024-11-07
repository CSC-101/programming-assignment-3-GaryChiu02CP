import build_data
import county_demographics
import data
from data import CountyDemographics

#task 1
def population_total(array:list[CountyDemographics]) -> int:
    total = 0
    for i in array:
        total += i.population['2014 Population']
    return total

#task 2
def filter_by_state(array:list[CountyDemographics], string:str) -> list[CountyDemographics]:
    list = []
    for i in array:
        if i.state == string:
            list.append(i)
    print(list)
    return list

#task 3
def population_by_education(array:list[CountyDemographics], string:str) -> float:
    if string not in array[0].education:
        return None
    total = 0.0
    for i in array:
        total += i.population['2014 Population']*(i.education[string]/100)
    return total

def population_by_ethnicity(array:list[CountyDemographics], string:str) -> float:
    if string not in array[0].ethnicities:
        return None
    total = 0.0
    for i in array:
        total += i.population['2014 Population']*(i.ethnicities[string]/100)
    return total

def population_below_poverty_level(array:list[CountyDemographics], string:str) -> float:
    total = 0.0
    for i in array:
        total += i.population['2014 Population']*(i.income["Persons Below Poverty Level"]/100)
    return total

#task 4
def percent_by_education(array:list[CountyDemographics], string:str) -> float:
    if string not in array[0].education:
        return None
    totalnum = 0.0
    totalden = 0.0
    for i in array:
        totalnum += i.population['2014 Population']*(i.education[string]/100)
        totalden += i.population['2014 Population']
    total = totalnum/totalden
    return total

def percent_by_ethnicity(array:list[CountyDemographics], string:str) -> float:
    if string not in array[0].ethnicities:
        return None
    totalnum = 0.0
    totalden = 0.0
    for i in array:
        totalnum += i.population['2014 Population']*(i.ethnicities[string]/100)
        totalden += i.population['2014 Population']
    total = totalnum/totalden
    return total

def percent_below_poverty_level(array:list[CountyDemographics]) -> float:
    totalnum = 0.0
    totalden = 0.0
    for i in array:
        totalnum += i.population['2014 Population']*(i.income["Persons Below Poverty Level"]/100)
        totalden += i.population['2014 Population']
    total = totalnum/totalden
    return total

#task 5
def education_greater_than(array:list[CountyDemographics], string:str, x:float) -> list[CountyDemographics]:
    list = []
    for i in array:
        if i.education[string]/100 > x:
            list.append(i)
    return list

def education_less_than(array:list[CountyDemographics], string:str, x:float) -> list[CountyDemographics]:
    list = []
    for i in array:
        if i.education[string]/100 < x:
            list.append(i)
    return list

def ethnicity_greater_than(array:list[CountyDemographics], string:str, x:float) -> list[CountyDemographics]:
    list = []
    for i in array:
        if i.ethnicities[string]/100 > x:
            list.append(i)
    return list

def ethnicity_less_than(array:list[CountyDemographics], string:str, x:float) -> list[CountyDemographics]:
    list = []
    for i in array:
        if i.ethnicities[string]/100 < x:
            list.append(i)
    return list

def below_poverty_level_greater_than(array:list[CountyDemographics], string:str, x:float) -> list[CountyDemographics]:
    list = []
    for i in array:
        if i.ethnicities[string]/100 > x:
            list.append(i)
    return list

def below_poverty_level_less_than(array:list[CountyDemographics], string:str, x:float) -> list[CountyDemographics]:
    list = []
    for i in array:
        if i.ethnicities[string]/100 < x:
            list.append(i)
    return list

def below_poverty_level_greater_than(array:list[CountyDemographics], string:str, x:float) -> list[CountyDemographics]:
    list = []
    for i in array:
        if i.income["Persons Below Poverty Level"]/100 > x:
            list.append(i)
    return list

def below_poverty_level_less_than(array:list[CountyDemographics], string:str, x:float) -> list[CountyDemographics]:
    list = []
    for i in array:
        if i.income["Persons Below Poverty Level"]/100 < x:
            list.append(i)
    return list