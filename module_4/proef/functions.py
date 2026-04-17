import time
from termcolor import colored
from config import *

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    silver = copper2silver(amount)
    gold = silver2gold(silver)
    return gold

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    result =  (
        personCash["gold"]
        + copper2gold(personCash["copper"])
        + silver2gold(personCash["silver"])
        + platinum2gold(personCash["platinum"])
    )
    return result

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    total_copper = (people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS
    return copper2gold(total_copper)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    result = []
    for item in list:
        if key in item and item[key] == value:
            result.append(item)
    return result

def getAdventuringPeople(people:list) -> list:
    result = []
    for i in people:
        if i.get("adventuring") is TRUE:
            result.append(i)
    return result

def getShareWithFriends(friends:list) -> list:
    result = []
    for i in friends:
        if i.get("shareWith") is TRUE:
            result.append(i)
    return result

def getAdventuringFriends(friends:list) -> list:
    result = []
    for i in friends:
        if i.get("shareWith") is TRUE and i.get("adventuring") is TRUE:
            result.append(i)
    return result

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return (people + 1) // 2


def getNumberOfTentsNeeded(people:int) -> int:
    return (people + 2) // 3

def getTotalRentalCost(horses:int, tents:int) -> float:
    nights = JOURNEY_IN_DAYS - 1
    horse_cost_silver = horses * COST_HORSE_SILVER_PER_DAY * nights
    horse_cost_gold = silver2gold(horse_cost_silver)
    tent_weeks = (nights + 6) // 7
    tent_cost_gold = tents * COST_TENT_GOLD_PER_WEEK * tent_weeks
    return horse_cost_gold + tent_cost_gold

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    item_texts = []
    for item in items:
        text = '{}{} {}'.format(item.get('amount', ''), item.get('unit', ''), item.get('name', '')).strip()
        item_texts.append(text)

    item_count = len(item_texts)
    if item_count == 0:
        return ''
    if item_count == 1:
        return item_texts[0]
    if item_count == 2:
        return ' & '.join(item_texts)
    return ', '.join(item_texts[:-1]) + ' & ' + item_texts[-1]


def getItemsValueInGold(items:list) -> float:
    total_gold = 0.0
    for item in items:
        price = item.get('price', {})
        amount = price.get('amount', 0)
        price_type = price.get('type', 'gold')
        item_total = item.get('amount', 0) * amount
        if price_type == 'copper':
            total_gold += copper2gold(item_total)
        elif price_type == 'silver':
            total_gold += silver2gold(item_total)
        elif price_type == 'platinum':
            total_gold += platinum2gold(item_total)
        else:
            total_gold += item_total
    return total_gold

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    gold_barry = getPersonCashInGold(mainCharacter['cash'])
    gold_friends = getPersonCashInGold(friends['cash'])
    result = gold_barry + gold_friends
    print(result)
##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    return [inv for inv in investors if inv.get('profitReturn', 0) <= 10]


def getAdventuringInvestors(investors:list) -> list:
    return [inv for inv in investors if inv.get('adventuring') is True]


def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    if not investors or not gear:
        return 0.0

    investors_coming = [inv for inv in investors if inv.get('adventuring') is True and inv.get('profitReturn', 0) <= 10]
    if len(investors_coming) == 0:
        return 0.0

    gear_cost = getItemsValueInGold(gear)
    nights = JOURNEY_IN_DAYS - 1
    horse_cost_silver = COST_HORSE_SILVER_PER_DAY * nights
    horse_cost_gold = silver2gold(horse_cost_silver)
    tent_weeks = (nights + 6) // 7
    tent_cost_gold = COST_TENT_GOLD_PER_WEEK * tent_weeks
    food_copper = (COST_FOOD_HUMAN_COPPER_PER_DAY + COST_FOOD_HORSE_COPPER_PER_DAY) * nights
    food_cost_gold = copper2gold(food_copper)

    cost_per_investor = gear_cost + horse_cost_gold + tent_cost_gold + food_cost_gold
    return round(cost_per_investor * len(investors_coming), 2)

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    if leftoverGold is None or leftoverGold <= 0 or people <= 0 or horses < 0:
        return 0

    silver_cost = people * COST_INN_HUMAN_SILVER_PER_NIGHT
    copper_cost = horses * COST_INN_HORSE_COPPER_PER_NIGHT
    nightly_cost_gold = silver2gold(silver_cost) + copper2gold(copper_cost)

    if nightly_cost_gold <= 0:
        return 0

    max_nights = JOURNEY_IN_DAYS - 1
    affordable_nights = int(leftoverGold // nightly_cost_gold)
    return min(affordable_nights, max_nights)


def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    if nightsInInn <= 0 or people <= 0 and horses <= 0:
        return 0.0

    silver_cost = people * COST_INN_HUMAN_SILVER_PER_NIGHT * nightsInInn
    copper_cost = horses * COST_INN_HORSE_COPPER_PER_NIGHT * nightsInInn
    total_cost_gold = silver2gold(silver_cost) + copper2gold(copper_cost)
    return round(total_cost_gold, 2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()