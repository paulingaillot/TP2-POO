public class App {

    static Nourriture[] Nourrituretab = new Nourriture[10];
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        
        /*Thread myThread2;
		myThread2 = new Thread(new Pigeon(2));
		myThread2.start();*/

        /*Pigeon pig = new Pigeon(2);
        pig.start();*/

        Thread myThread2;
		myThread2 = new Thread(new Generateur());
		myThread2.start();

        //new Pigeon(2).start();

        Nourrituretab[9] = new Nourriture(9);
        Nourrituretab[9].start();

    }


    static class Generateur extends Thread {

        public void run() {
            while(Thread.currentThread().isAlive()) {
                try {

                
                int alea1 = 5000 + (int)(Math.random() * ((30000 - 5000) + 1));
                int alea2 = 0 + (int)(Math.random() * ((9 - 0) + 1));

                sleep(alea1);

                new Pigeon(alea2).start();
                }catch(Exception e) {
                    
                }
            }
        }
    }
    
    static class Nourriture extends Thread {

        private volatile Thread blinker;

        private int x;
        private int valeur = 1;
        private boolean isEat = false;

        public Nourriture(int x) {
            this.x = x;
        }

        public void stopThread() {
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
                    sleep(1000);
                    if(isEat == true) {
                        this.stopThread();
                        Nourrituretab[x] = null;
                    }
                    else {
                        this.valeur++;
                        System.out.println("Il y a de la nourriture en x="+this.x+" ... Elle moisie petit a petit.");
                    }

                }catch(Exception e) {

                }
            }
        }

        public void delete() {
            isEat = true;
        }
    }

    static class Pigeon extends Thread {

        private volatile Thread blinker;

        private int x;
        private boolean isEat;

        public Pigeon(int x) {
            this.x = x;
            isEat = false;
        }

        public void stopThread() {
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
                    
                    int min = -1;
                    int direction = -1;
                    for(int i=0; i<10; i++) {
                        if(Nourrituretab[i] != null && (Nourrituretab[i].valeur<min || min ==-1)) {
                            min = Nourrituretab[i].valeur;
                            direction = i;
                        }
                    }

                    

                    if(direction != -1) {

                        if(direction == this.x) {
                            System.out.println("Je mange ...");
                            isEat = true;
                            Nourrituretab[direction].delete();
                        }
                        else if(direction > this.x) {
                            this.x ++;
                            System.out.println("Je me deplace");
                        }
                        else  {
                            this.x--;
                            System.out.println("Je me deplace");
                        }

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

}
