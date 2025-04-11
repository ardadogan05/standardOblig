# standardOblig
Her er forklarigen min til hver oppgave. Forklarer det viktigste.

Oppg 1,2 og 3:
Her var det bare å implementere metoden som er oppgitt i oppgavene, og deretter sammenligne resulatene. Jeg tolket det som at jeg skulle prøve å finne beste h verdier for hver metode. Resultat er vedlagt i koden som en kommmentar.

Oppg 4:
Vi ser at varmen er skeiv mot høyre aller først, men den sprer seg utover elementet. Større h gir mer kantet graf, mens høyere k gir deg mindre tidsintervall i animasjonen. Det er også viktig med stabilitet i den eksplisitte formelen, det kreves at k/h^2 <= 1/2. Det slik at den eksplisitte formelene konvergerer, og dette er det største mulige forholdet som funker.

Oppg 5:
Når man bruker en implisittmetode får man neste verdi på begge sider av likningen, f.eks X_n+1. Derfor trenger vi først en likningsløser (f.eks. fikspunktiterasjon. Kunne brukt newtonsmetode, vanskeligere.) for å estimere en verdi for neste verdi, som vi kan bruke i euler implisitt for å beregne en bedre verdi. Benytter jeg både fikspunktiterasjon som numerisk løser i oppg 5. Valg av k og h bestemmer henholdvis "nøyaktighet" i med hensyn på tid og rom. Jo lavere, jo mer nøyaktig, men det krever mer maskinkraft. Det er også samme kriterie for stabilitet her: k/h^2 <= 1/2. Derfor må man være obs på verdiene en velger.

Oppg 6:
Mye av det samme som oppgave 5, forskjellen er hvordan man regner ut neste u verdi. Benytter fortsatt fikspunktiterasjon, da Crank-Nicolson er en kombinasjon av implisitt og eksplisitt euler. Minner litt trapesmetoden, altså at den tar snittet mellom to forskjellige metoder for å gi et bedre estimat. Det er fortsatt samme kriterie for stabilitet.

Kommentarer: 
-Burde kanskje ha laget en fil for hver oppgave, beklager det.
-Vet det er mye redundant kode, men det var bare å kopiere og lime over det meste.
-Kanskje ha laget en funksjon for å velge metode, men valgte bare å kommentere ut. Bare å fjerne #


