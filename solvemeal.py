

def solve(meal_cost,tip_percent,tax_percent):
    meal = 0
    
    meal = meal_cost +(meal_cost*tax_percent)+ (meal_cost*tip_percent)

    return int(meal)
if __name__ == '__main__':
    print (solve(12,2.4,0.96))


       




