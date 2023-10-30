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




*Dokumentation af salve programmet*:



*Beskrivelse af udviklingsprocessen*:
Vi havde store problemer med at committe ind til github, og er også blevet nødt til at lave et nyt respository, så vi har noget dokumentation af vores udviklinsprocces. Vi valgte bare at lave videre på vores kode, og så bare uploade den til sidst.






