public class Nourriture extends Thread {
    static Nourriture[] Nourrituretab = new Nourriture[10];
    private volatile Thread blinker;

    private int x;
    private int valeur = 1;
    private boolean isEat = false;

    public Nourriture(int x) {
        this.x = x;
    }

    public int getValeur() {
        return this.valeur;
    }

    public void stopThread() {
        Nourrituretab[x] = null;
        Main.mafenetre.UpdatePigeon();
        blinker = null;
    }

    public void start() {
        blinker = new Thread(this);
        Main.mafenetre.UpdatePigeon();
        blinker.start();
    }

    public void run() {
        Thread thisThread = Thread.currentThread();
        Main.mafenetre.UpdatePigeon();
        while (blinker == thisThread) {
            try {
                sleep(1000);
                if(isEat == true) {
                    this.stopThread();
                   
                }
                else {
                    this.valeur++;
                    System.out.println("Il y a de la nourriture en x="+this.x+" ... Elle moisie petit a petit.");
                }

            }catch(Exception e) {
                e.printStackTrace();
            }
        }
    }

    public void delete() {
        isEat = true;
    }
}



