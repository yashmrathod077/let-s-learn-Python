amount = int(input(" enter a money amount : "))
if amount / 500 >0:
    note500 = amount // 500
    print(f"{note500} of 500 $ ")
    if (amount-(note500*500)) /  200 > 0:
        note200 = (amount-(note500*500)) // 200
        print(f"{note200} of 200 $ ")
        if (amount-(note500*500)-(note200*200)) / 100 > 0:
            note100 = (amount-(note500*500)-(note200*200))// 100
            print(f"{note100} of 100 $ ")
            if (amount-(note500*500)-(note200*200)-(note100*100)) / 50 > 0:
                note50 = (amount-(note500*500)-(note200*200)-(note100*100)) // 50
                print(f"{note50} of 50 $ ")
                if (amount-(note500*500)-(note200*200)-(note100*100)-(note50*50))/ 20 > 0:
                    note20 = (amount-(note500*500)-(note200*200)-(note100*100)-(note50*50))// 20
                    print(f"{note20} of 20 $ ")
                    if (amount-(note500*500)-(note200*200)-(note100*100)-(note50*50)-(note20*20)) / 10 > 0:
                        note10 = (amount-(note500*500)-(note200*200)-(note100*100)-(note50*50)-(note20*20)) // 10
                        print(f"{note10} of 10 $ ")
                        if (amount-(note500*500)-(note200*200)-(note100*100)-(note50*50)-(note20*20)-(note10*10)) / 5 > 0:
                            note5 = (amount-(note500*500)-(note200*200)-(note100*100)-(note50*50)-(note20*20)-(note10*10)) // 5
                            print(f"{note5} of 5 $ ")
                            if (amount-(note500*500)-(note200*200)-(note100*100)-(note50*50)-(note20*20)-(note10*10)-(note5*5)) / 2 > 0:
                                note2 = (amount-(note500*500)-(note200*200)-(note100*100)-(note50*50)-(note20*20)-(note10*10)-(note5*5)) // 2
                                print(f"{note2} of 2 $ ")
                                if (amount-(note500*500)-(note200*200)-(note100*100)-(note50*50)-(note20*20)-(note10*10)-(note5*5)-(note2*2)) / 1 > 0:
                                    print(f"{note2} of 1 $ ")