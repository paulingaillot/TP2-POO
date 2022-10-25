import javax.swing.*;
import java.io.*;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

public class MaFenetre implements ActionListener {
    private JFrame f;
    private JButton[] bouton = new JButton[10];

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
            f.addComponentListener(null);
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Bouton 

        for(int i=0; i<10; i++) {
            bouton[i] = new JButton();
            bouton[i].setForeground(new Color(100, 255, 255));
            bouton[i].setBounds(100+(i+1)*35, 460, 30,30);
            bouton[i].setVisible(true);
            bouton[i].setActionCommand(""+i);
            bouton[i].addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    int j = Integer.parseInt(e.getActionCommand());
                    App.Nourrituretab[j] = new App.Nourriture(j);
                    App.Nourrituretab[j].start();
                    System.out.println("Appui sur bouton");
                    UpdatePigeon();
                }
            });

            f.add(bouton[i]);
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

    public void UpdateFood() {
        for(int i=0; i<10; i++) {
            if(App.Nourrituretab[i] != null) {

                try {
                    //f.removeAll();
                    //this.addBackGround();

                    bouton[i].setForeground(new Color(100, 255, 255));
                    bouton[i].setBounds(100+(i+1)*35, 460, 30,30);
                    Icon icon = new ImageIcon("./Exo1/src/graines.png");

                    bouton[i].setIcon(icon);
                    bouton[i].setVisible(true);
                    f.add(bouton[i]).setForeground((new Color(255, 255, 255)));
                    
                } catch (Exception e) {
                    e.printStackTrace();
                }
                f.validate();

            } else {
                bouton[i].setIcon(null);
            }
        }
    }

    public void UpdatePigeon() {
        f.getComponent(0).repaint();
        UpdateFood();
        for(int i=0; i<10; i++) {
            if(App.Pigeontab[i] != null) {

                try {
                    //f.removeAll();
                    //this.addBackGround();
                    JPanel panel = new JPanel();
                    panel.setForeground(new Color(100, 255, 255));
                    panel.setBounds(100+(i+1)*35, 415, 30,30);
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

    @Override
    public void actionPerformed(ActionEvent e) {
        // TODO Auto-generated method stub
        
    }
}