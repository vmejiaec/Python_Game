from game import  Spawner_Esqueletos, Spawner_Trols

if __name__ == '__main__':

    spEsqueletos = Spawner_Esqueletos()
    spTrols = Spawner_Trols()

    EsqueletoJuan = spEsqueletos.spawn("Juan")
    EsqueletoPepe = spEsqueletos.spawn("Pepe")
    TrolLuis = spTrols.spawn("Luis")

    ronda = 0;

    while (EsqueletoJuan.esta_vivo() or EsqueletoPepe.esta_vivo()) and TrolLuis.esta_vivo():
        ronda += 1
        print(f"Ronda {ronda} ---------------------------------------------------");
        daño_al_trol = 0
        daño_al_esqueleto = 0

        esqueleto_que_ataca = EsqueletoJuan if EsqueletoJuan.esta_vivo() else EsqueletoPepe
        daño_al_trol = esqueleto_que_ataca.ataca()
        
        TrolLuis.recibe_daño(daño_al_trol)

        daño_al_esqueleto = TrolLuis.ataca()
        
        esqueleto_que_ataca.recibe_daño(daño_al_esqueleto)