print("Welcome To The Dungeons And Dragons Game!\n")
print("""
   ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___   
 ~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~ 
         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~         
        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-        
             ~\_        // *******.:|\^^^/|:.******* \\        _/~             
                \      / ********.::(>: :<)::.******** \      /                
                 \   /  ********.::::\\|//::::.********  \   /                 
                  \ /   *******.:::::(o o):::::.*******   \ /                  
                   /.   ******.::::'*|V_V|***`::.******   .\                   
                     ~~--****.:::'***|___|*****`:.****--~~                     
                           *.::'***//|___|\\*****`.*                           
                           .:'  **/##|___|##\**    .                           
                          .    (v(VVV)___(VVV)v)
""")
print("*" * 30)
print("You are a brave knight on a mission to rescue the princess from a castle that is guarded by a huge dragon!!")
print("*" * 30)
print("\nYou are standing at the entrance to the castle")
direction = input("Which direction do you want to go? L or R: ").lower()
if direction == "l":
	print("You pick the lock to the front door")
	direction = input("You are now in the castle, which way do you go? L or R: ").lower()
	if direction == "r":
		print("You go up the stairs, at the top are two doors")
		door = input("Which door do you go through? Blue or Red: ").lower()
		if door == "red":
			print("You found the princess!!")
			final_move = input("She is asleep, what do you do? Wake her or Leave: ").lower()
			if final_move == "leave":
				print("On leaving the room the princess wakes and follows you out of the castle!")
				print("Congratulations!! You rescued the princess.")
			else:
				print("Game Over! When waking the princess she has a heart attack and dies")
		else:
			print("Game Over! You picked the wrong door and fall to your death.")
	else:
		print("Game Over! You ran into the dragons lair and were burned alive.")
else:
	print("Game Over! You went the wrong way and were eaten alive by the dragon.")