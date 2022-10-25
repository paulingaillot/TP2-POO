import javax.swing.*;
import java.io.*;
import java.awt.Color;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

public class MaFenetre {
    private JFrame f; 

    public MaFenetre() {
        f = new JFrame("Pigeon");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // comportement modifiable
        f.setSize(800, 700);
        // on place ici la definition de l'arbre de composants
        // frame.getContentPane().add(new MonDessin()); // forme exacte
        // ...
        // on termine generalement ainsi

        try {
            JPanel panel = new JPanel();
            panel.setBounds(0, 0, 600, 550);
            BufferedImage img = ImageIO.read(new File("./Exo1/src/fenetre.png"));
            JLabel pic = new JLabel(new ImageIcon(img));
            panel.add(pic);
            f.add(panel);
        } catch (Exception e) {
            e.printStackTrace();
        }
        
                   
        f.setLayout(null);
        f.setVisible(true);
        // pour l'exemple

        f.validate();

        System.out.println(Thread.currentThread() + " en fin de MaFenetre()");
    }

    public void addBackGround() {
        try {
            JPanel panel = new JPanel();
            panel.setBounds(0, 0, 600, 550);
            BufferedImage img = ImageIO.read(new File("./Exo1/src/fenetre.png"));
            JLabel pic = new JLabel(new ImageIcon(img));
            panel.add(pic);
            f.add(panel);
            f.validate();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void addPigeon() {
        f.getComponent(0).repaint();
        for(int i=0; i<10; i++) {
            if(App.Pigeontab[i] != null) {

                try {
                    //f.removeAll();
                    //this.addBackGround();
                    JPanel panel = new JPanel();
                    panel.setForeground(new Color(100, 255, 255));
                    panel.setBounds(100+(i+1)*30, 415, 30,30);
                    BufferedImage img = ImageIO.read(new File("./Exo1/src/pigeon.png"));
                    JLabel pic = new JLabel(new ImageIcon(img));
                    panel.add(pic);
                    f.add(panel).setForeground((new Color(255, 255, 255)));
                    
                } catch (Exception e) {
                    e.printStackTrace();
                }
                f.validate();

            }
        }
      
    }
}