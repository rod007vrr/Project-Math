print("Hello, welcome to the rounding calculator. To use this calculator simply input the number to be rounded and what place you would like to round it to")
numberToRound = float(input("Number to be rounded:\n"))
placeToRoundTo = float(input("\nPlace to be rounded to\nIf tens then type 10 if hundreds then write 100 etc.\n"))
if numberToRound % placeToRoundTo >= placeToRoundTo*0.5 :
    print("Round up to: ", numberToRound+( placeToRoundTo-(numberToRound%placeToRoundTo)))
elif numberToRound % placeToRoundTo < placeToRoundTo*0.5 :
    print("Round down to", numberToRound-(numberToRound%placeToRoundTo))