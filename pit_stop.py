total_laps=50
print("welcome to the F1 strategy desk")
tire_choice=input("what type of tire do you starting on? (soft, medium, hard) ")
if tire_choice == "soft":
    pit_laps=15
    print("soft tires have a lifespan of 15 laps")
    print("you will need to pit at lap 15")
if tire_choice == "medium":
    pit_laps=25
    print("medium tires have a lifespan of 25 laps")
    print("you will need to pit at lap 25")
if tire_choice == "hard":
    pit_laps=35
    print("hard tires have a lifespan of 35 laps")
    print("you will need to pit at lap 35")
else:
    pit_laps=0
    print("Engineer: WE DON'T HAVE THAT TIRE! ")    
if pit_laps>0:
    laps_left=total_laps-pit_laps
    print(f"you will have {laps_left} laps left after the pit stop")
