Jonas og Jakob 2.P.
Spil lavet i Python med brug af Pygame.
Vi har brugt Visual Code Studio til at kode.
Vores kode er (ANTAL TEGN). (Ved ikke om det er antal tegn på kode eller på readme).

*Beskrivelse af spillet*:
Vi har lavet et Frogger spil, som går ud på at man er en frø som skal hoppe over en vej og over en flod, for så at komme hen på nogle åkander. På vejen kører der biler frem og tilbage som man skal undgå at blive ramt af. I flod er der nogle træstammer som flyder frem og tilbage som man kan hoppe på. Man dør af at blive ramt af en bil eller hvis man hopper i vandet. Man har 3 liv til at komme hen på alle 5 åkander, for at komme til næste level. For hvert liv har du 30 sekunder til at nå hen på en åkande, og hvis tiden løber ud tæller det også som at du er død.


*Funktionsbeskrivelse*:
class Frog(Object):

    def __init__(self,position,sprite_frog):
        self.sprite = sprite_frog
        self.position = position
        self.lives = 3
        self.animation_counter = 0
        self.animation_tick = 1
        self.way = "UP"
        self.can_move = 1

Parametre:

    - position (tuple): En tuple, der repræsenterer frøets startposition.
    - sprite_frog: Sprite, der er forbundet med frøet.

Attributter:

    - sprite: Sprite, der er forbundet med frøet.
    - position (tuple): Frøets nuværende position på spilskærmen.
    - lives (int): Antallet af liv, som frøet har i spillet (sat som standard til 3).
    - animation_counter (int): En tæller, der bruges til at spore animationsrelaterede handlinger.
    - animation_tick (int): En tælletakt for animationopdateringer.
    - way (str): Retningen, hvori frøet vender (sat som standard til "OP").
    - can_move (int): En markør, der angiver, om frøet i øjeblikket kan bevæge sig.

Vi valgte at lave nogle veje hvor der kørte biler frem og tilbage. Dem lavede vi først ved at finde nogle sprites som billeder.

```
car1_filename = 'car1.png'
car2_filename = 'car2.png'
car3_filename = 'car3.png'
car4_filename = 'car4.png'
car5_filename = 'car5.png'
sprite_car1 = pygame.image.load(car1_filename).convert_alpha()
sprite_car2 = pygame.image.load(car2_filename).convert_alpha()
sprite_car3 = pygame.image.load(car3_filename).convert_alpha()
sprite_car4 = pygame.image.load(car4_filename).convert_alpha()
sprite_car5 = pygame.image.load(car5_filename).convert_alpha()

Efter det lavede vi dem så til enemies, og fik dem til at køre til højre og venstre på de stedder hvor det matchede baggrunden.

def createEnemys(list,enemys,game):
    for i, tick in enumerate(list):
        list[i] = list[i] - 1
        if tick <= 0:
            if i == 0:
                list[0] = (40*game.speed)/game.level
                position_init = [-55,436]
                enemy = Enemy(position_init,sprite_car1,"right",1)
                enemys.append(enemy)
            elif i == 1:
                list[1] = (30*game.speed)/game.level
                position_init = [506, 397]
                enemy = Enemy(position_init,sprite_car2,"left",2)
                enemys.append(enemy)
            elif i == 2:
                list[2] = (40*game.speed)/game.level
                position_init = [-80, 357]
                enemy = Enemy(position_init,sprite_car3,"right",2)
                enemys.append(enemy)
            elif i == 3:
                list[3] = (30*game.speed)/game.level
                position_init = [516, 318]
                enemy = Enemy(position_init,sprite_car4,"left",1)
                enemys.append(enemy)
            elif i == 4:
                list[4] = (50*game.speed)/game.level
                position_init = [-56, 280]
                enemy = Enemy(position_init,sprite_car5,"right",1)
                enemys.append(enemy)


Vi har lavet så man kan bevæge frøen med piletasterne. Her har vi altså skrevet hvilke knapper den skal bevæge sig med og hvor meget den skal bevæge sig med.


def updateSprite(self,key_pressed):
        if self.way != key_pressed:
            self.way = key_pressed
            if self.way == "up":
                frog_filename = 'sprite_sheets_up.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()
            elif self.way == "down":
                frog_filename = 'sprite_sheets_down.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()
            elif self.way == "left":
                frog_filename = 'sprite_sheets_left.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()
            elif self.way == "right":
                frog_filename = 'sprite_sheets_right.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()


    def moveFrog(self,key_pressed, key_up):
         
        if self.animation_counter == 0 :
            self.updateSprite(key_pressed)
        self.incAnimationCounter()
        if key_up == 1:
            if key_pressed == "up":
                if self.position[1] > 39:
                    self.position[1] = self.position[1]-13
            elif key_pressed == "down":
                if self.position[1] < 473:
                    self.position[1] = self.position[1]+13
            if key_pressed == "left":
                if self.position[0] > 2:
                    if self.animation_counter == 2 :
                        self.position[0] = self.position[0]-13
                    else:
                        self.position[0] = self.position[0]-14
            elif key_pressed == "right":
                if self.position[0] < 401:
                    if self.animation_counter == 2 :
                        self.position[0] = self.position[0]+13
                    else:
                        self.position[0] = self.position[0]+14



*Dokumentation af salve programmet*:



*Beskrivelse af udviklingsprocessen*:
Vi havde store problemer med at committe ind til github, og er også blevet nødt til at lave et nyt respository, så vi har noget dokumentation af vores udviklinsprocces. Vi valgte bare at lave videre på vores kode, og så bare uploade den til sidst.






