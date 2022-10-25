public class Main {
    static MaFenetre mafenetre;
    
    
   
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!"); // Le survivant
        

        /*Thread myThread2;
		myThread2 = new Thread(new Pigeon(2));
		myThread2.start();*/

        /*Pigeon pig = new Pigeon(2);
        pig.start();*/

        Thread myThread2;
		myThread2 = new Thread(new Generateur());
		myThread2.start();

        //new Pigeon(2).start();
        Nourriture.Nourrituretab[9] = new Nourriture(9);
        Nourriture.Nourrituretab[9].start();

        mafenetre = new MaFenetre();
        mafenetre.UpdatePigeon();
        

    }


    static class Generateur extends Thread {

        public void run() {
            while(Thread.currentThread().isAlive()) {
                try {

                
                int alea1 = 5000 + (int)(Math.random() * ((3000 - 500) + 1));
                int alea2 = 0 + (int)(Math.random() * ((9 - 0) + 1));

                sleep(alea1);
               
                new Pigeon(alea2).start();
                mafenetre.UpdatePigeon();
                }catch(Exception e) {

                }
            }
        }
    }
    
}
