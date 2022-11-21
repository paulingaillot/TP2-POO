

public class Pigeon extends Thread{
        static Pigeon[] Pigeontab = new Pigeon[10];
        private volatile Thread blinker;
       
        private int x;
        private boolean isEat;

        public Pigeon(int x) {
            this.x = x;
            Pigeontab[x] = this;
            isEat = false;
        }

        public void stopThread() {
            Pigeontab[this.x] = null;
            Main.mafenetre.UpdatePigeon();
            blinker = null;
        }

        public void start() {
            blinker = new Thread(this);
            blinker.start();
        }

    	public void run() {
            Thread thisThread = Thread.currentThread();

            while (blinker == thisThread) {
                try {
                    if(isEat == true) {
                        System.out.println("Suppression");
                        this.stopThread();
                    }else {
                    sleep(1000);
                    
                    // Le pigeon peut prendre peur 

                    int aleapeur = 0 + (int)(Math.random() * ((25 - 0) + 1));
                    if(aleapeur == 1) {
                        // Le pigeon prend peur

                        System.out.println("Les pigeons ont pris peur");
                        this.stopThread();
                    }

                    // On verifei l'existence de nourriture

                    int min = -1;
                    int direction = -1;
                    for(int i=0; i<10; i++) {
                        if(Nourriture.Nourrituretab[i] != null && (Nourriture.Nourrituretab[i].getValeur()<min || min ==-1)) {
                            min = Nourriture.Nourrituretab[i].getValeur();
                            direction = i;
                        }
                    }

                    // Deplacement

                    if(direction != -1) {

                        if(direction == this.x) {
                            System.out.println("Je mange ...");
                            isEat = true;
                            Nourriture.Nourrituretab[direction].delete();
                        }
                        else if(direction > this.x && Pigeontab[x+1] == null) {
                            System.out.println("pos : "+x);
                            Pigeontab[x] = null;
                            this.x ++;
                            Pigeontab[x] = this;
                            System.out.println("Je me deplace");
                        }
                        else if(direction < this.x && Pigeontab[x-1] == null) {
                            Pigeontab[x] = null;
                            this.x--;
                            Pigeontab[x] = this;
                            System.out.println("Je me deplace");
                        }
                        else {
                            System.out.println("je suis bloqué :'(");
                        }
                        Main.mafenetre.UpdatePigeon();

                    } else {
                        System.out.println("Je dors ...(pos="+this.x+")");
                    }
                }
                    
                }catch(Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }


